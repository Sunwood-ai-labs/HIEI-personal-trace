"""General utility functions."""

import os
import platform
import psutil
from datetime import datetime
from typing import Dict, Any
from .logging import get_logger

logger = get_logger(__name__)

def get_system_info() -> Dict[str, Any]:
    """Get system information."""
    try:
        return {
            'platform': platform.system(),
            'platform_release': platform.release(),
            'platform_version': platform.version(),
            'architecture': platform.machine(),
            'processor': platform.processor(),
            'memory': dict(psutil.virtual_memory()._asdict()),
            'disk': dict(psutil.disk_usage('/')._asdict()),
        }
    except Exception as e:
        logger.error(f"Error getting system info: {e}")
        return {}

def format_timestamp(dt: datetime = None) -> str:
    """Format timestamp for logging."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def ensure_dir(directory: str):
    """Ensure directory exists."""
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        logger.error(f"Error creating directory {directory}: {e}")
        raise
