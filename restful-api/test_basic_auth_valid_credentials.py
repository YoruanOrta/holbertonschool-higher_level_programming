import unittest
import requests
from requests.auth import HTTPBasicAuth

class TestBasicAuth(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000"

    def test_basic_auth_valid_credentials(self):
        """Test /basic-protected with valid credentials."""
        url = f"{self.BASE_URL}/basic-protected"
        response = requests.get(url, auth=HTTPBasicAuth("user1", "password"))
        
        self.assertEqual(response.status_code, 200)  # Expect 200 OK
        self.assertEqual(response.json(), {"message": "Basic Auth: Access Granted"})

if __name__ == "__main__":
    unittest.main()