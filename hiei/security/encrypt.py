"""Data encryption utilities."""

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
from ..utils.logging import get_logger

logger = get_logger(__name__)

class Encryptor:
    def __init__(self, key: str = None):
        """Initialize encryptor with a key or generate a new one."""
        if key is None:
            self.key = self._generate_key()
        else:
            self.key = self._derive_key(key)
        self.fernet = Fernet(self.key)

    def _generate_key(self) -> bytes:
        """Generate a new encryption key."""
        return base64.urlsafe_b64encode(os.urandom(32))

    def _derive_key(self, password: str) -> bytes:
        """Derive encryption key from password."""
        salt = b'hiei_salt'  # In production, use a proper salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def encrypt(self, data: str) -> str:
        """Encrypt string data."""
        try:
            return self.fernet.encrypt(data.encode()).decode()
        except Exception as e:
            logger.error(f"Encryption error: {e}")
            return ""

    def decrypt(self, encrypted_data: str) -> str:
        """Decrypt encrypted string data."""
        try:
            return self.fernet.decrypt(encrypted_data.encode()).decode()
        except Exception as e:
            logger.error(f"Decryption error: {e}")
            return ""
