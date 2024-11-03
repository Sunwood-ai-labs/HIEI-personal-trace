"""Clipboard monitoring functionality."""

import pyperclip
from time import sleep
from threading import Thread
from ..security.filter import SensitiveDataFilter
from ..storage.database import ActivityDatabase

class ClipboardMonitor:
    def __init__(self):
        self.previous = ""
        self.running = False
        self.filter = SensitiveDataFilter()
        self.db = ActivityDatabase()
        self.monitor_thread = None

    def start(self):
        """Start monitoring clipboard changes."""
        self.running = True
        self.monitor_thread = Thread(target=self._monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def stop(self):
        """Stop monitoring clipboard changes."""
        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join()

    def _monitor_loop(self):
        """Main monitoring loop."""
        while self.running:
            try:
                current = pyperclip.paste()
                if current != self.previous:
                    self._handle_clipboard_change(current)
                    self.previous = current
            except Exception as e:
                # TODO: Implement proper error handling
                print(f"Error monitoring clipboard: {e}")
            sleep(0.5)  # Reduce CPU usage

    def _handle_clipboard_change(self, content):
        """Handle clipboard content changes."""
        if not self.filter.contains_sensitive_data(content):
            # TODO: Implement storage logic
            pass
