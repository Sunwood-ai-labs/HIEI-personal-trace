"""Text processing utilities."""

import re
from typing import List, Dict
from ..utils.logging import get_logger

logger = get_logger(__name__)

class TextProcessor:
    def __init__(self):
        self.patterns = {
            'url': r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s]*',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'path': r'(?:[a-zA-Z]:\\|/)(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*',
        }

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract various entities from text."""
        results = {}
        for entity_type, pattern in self.patterns.items():
            try:
                matches = re.findall(pattern, text)
                if matches:
                    results[entity_type] = matches
            except Exception as e:
                logger.error(f"Error extracting {entity_type}: {e}")
        return results

    def sanitize(self, text: str) -> str:
        """Remove sensitive information from text."""
        # TODO: Implement text sanitization
        return text

    def summarize(self, text: str, max_length: int = 100) -> str:
        """Create a summary of the text."""
        if len(text) <= max_length:
            return text
        return text[:max_length-3] + "..."
