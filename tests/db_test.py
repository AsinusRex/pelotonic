import unittest
from unittest.mock import MagicMock, patch

import db.__init__ as db_module
import config
from pymongo import GEOSPHERE

class TestDBFunctions(unittest.TestCase):

    def setUp(self):
        # Reset the globals before each test.
        db_module._client = None
        db_module._db_client = None

    @patch('db.__init__.MongoClient')
    def test_connect_success(self, MockMongoClient):
        # Create a dummy client for the ping check.
        tmp_client = MagicMock()
        # Ensure admin.command('ping') works without error.
        tmp_client.admin.command.return_value = {"ok": 1}

        # The first call for MongoClient returns our temporary client.
        # The second call creates the main client.
        main_client = MagicMock()
        # Dummy database object returned when indexing the client with config.DB_NAME.
        dummy_db = MagicMock()
        main_client.__getitem__.return_value = dummy_db

        # Setup side effects so that the temporary and main clients are returned.
        MockMongoClient.side_effect = [tmp_client, main_client]

        result = db_module.connect()

        # Verify that ping was performed.
        tmp_client.admin.command.assert_called_once_with('ping')
        # Check that the returned database object is the dummy_db.
        self.assertEqual(result, dummy_db)
        # Check that the globals were set.
        self.assertIsNotNone(db_module._client)
        self.assertIsNotNone(db_module._db_client)

    @patch('db.__init__.MongoClient')
    def test_shutdown(self, MockMongoClient):
        # Simulate an existing client.
        client = MagicMock()
        db_module._client = client
        db_module._db_client = MagicMock()

        db_module.close()

        # Verify that close is called.
        client.close.assert_called_once()
        # Ensure globals are reset.
        self.assertIsNone(db_module._client)
        self.assertIsNone(db_module._db_client)

    @patch('db.__init__.MongoClient')
    def test_geospatial_index_creation(self, MockMongoClient):
        # Mock the database client and collection
        mock_client = MagicMock()
        mock_db = MagicMock()
        mock_collection = MagicMock()

        # Set up the mocks to return the desired objects
        mock_db.__getitem__.return_value = mock_collection

        # The key fix: set the global _db_client that initialize_indexes uses
        db_module._db_client = mock_db

        # Call the function to create the index
        db_module.initialize_indexes()

        # Assert that create_index was called with the correct parameters
        mock_collection.create_index.assert_called_once_with([("tile_polygon", GEOSPHERE)])
if __name__ == '__main__':
    unittest.main()