# test_socketio.py
"""
Tests for SocketIo module.
"""

import unittest
from socketio import SocketIo

class TestSocketIo(unittest.TestCase):
    """Test cases for SocketIo class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SocketIo()
        self.assertIsInstance(instance, SocketIo)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SocketIo()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
