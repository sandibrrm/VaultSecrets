# test_vaultsecrets.py
"""
Tests for VaultSecrets module.
"""

import unittest
from vaultsecrets import VaultSecrets

class TestVaultSecrets(unittest.TestCase):
    """Test cases for VaultSecrets class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultSecrets()
        self.assertIsInstance(instance, VaultSecrets)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultSecrets()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
