"""Sensitive data filtering."""

import re
from typing import List, Pattern
from ..utils.logging import get_logger

logger = get_logger(__name__)

class SensitiveDataFilter:
    def __init__(self):
        """Initialize with default patterns for sensitive data."""
        self.patterns = {
            'credit_card': r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b',
            'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
            'password': r'(?i)password\s*[=:]\s*\S+',
            'api_key': r'(?i)(api[_-]?key|access[_-]?token)[=:]\s*\S+',
        }
        self._compile_patterns()

    def _compile_patterns(self):
        """Compile regex patterns."""
        self.compiled_patterns = {
            name: re.compile(pattern)
            for name, pattern in self.patterns.items()
        }

    def add_pattern(self, name: str, pattern: str):
        """Add a new pattern for sensitive data detection."""
        try:
            re.compile(pattern)  # Validate pattern
            self.patterns[name] = pattern
            self._compile_patterns()
        except re.error as e:
            logger.error(f"Invalid regex pattern '{pattern}': {e}")

    def contains_sensitive_data(self, text: str) -> bool:
        """Check if text contains any sensitive data."""
        return any(
            pattern.search(text)
            for pattern in self.compiled_patterns.values()
        )

    def mask_sensitive_data(self, text: str) -> str:
        """Replace sensitive data with masked version."""
        masked = text
        for name, pattern in self.compiled_patterns.items():
            masked = pattern.sub(f"[MASKED_{name.upper()}]", masked)
        return masked
