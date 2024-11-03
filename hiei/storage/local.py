"""Local file storage operations."""

import json
import os
from pathlib import Path
from typing import Dict, Any
from ..utils.logging import get_logger

logger = get_logger(__name__)

class LocalStorage:
    def __init__(self, base_path: str = None):
        if base_path is None:
            base_path = os.path.expanduser("~/.hiei")
        self.base_path = Path(base_path)
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        """Ensure storage directory exists."""
        os.makedirs(self.base_path, exist_ok=True)

    def save_json(self, filename: str, data: Dict[str, Any]):
        """Save data as JSON file."""
        try:
            file_path = self.base_path / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving JSON file {filename}: {e}")

    def load_json(self, filename: str) -> Dict[str, Any]:
        """Load data from JSON file."""
        try:
            file_path = self.base_path / filename
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except Exception as e:
            logger.error(f"Error loading JSON file {filename}: {e}")
            return {}
