# python
import unittest
from unittest.mock import patch, MagicMock
import logging
import main

class TestStartupShutdown(unittest.TestCase):

    @patch('main.connect')
    @patch('main.area_data.initialize_indexes')
    @patch('main.logging.config.dictConfig')
    def test_startup_success(self, mock_dictConfig, mock_initialize_indexes, mock_connect):
        # Mock the logger
        mock_logger = MagicMock()
        with patch('main.logging.getLogger', return_value=mock_logger):
            main.startup()
            # Verify that logging configuration was set up
            mock_dictConfig.assert_called_once_with(main.config.LOGGING_CONFIG)
            # Verify that connect and initialize_indexes were called
            mock_connect.assert_called_once()
            mock_initialize_indexes.assert_called_once()
            # Verify that the logger recorded the startup steps
            mock_logger.info.assert_any_call("Starting up application resources.")
            mock_logger.info.assert_any_call("Database connection established.")
            mock_logger.info.assert_any_call("Database indexes created successfully.")

    @patch('main.close')
    def test_shutdown(self, mock_close):
        # Mock the logger
        mock_logger = MagicMock()
        with patch('main.logging.getLogger', return_value=mock_logger):
            main.shutdown()
            # Verify that close was called
            mock_close.assert_called_once()
            # Verify that the logger recorded the shutdown steps
            mock_logger.info.assert_any_call("Shutting down. Cleaning up resources.")

if __name__ == '__main__':
    unittest.main()