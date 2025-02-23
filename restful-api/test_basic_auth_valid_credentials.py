import unittest
import json
import base64
from task_05_basic_security import app  # Ensure your main script is named "app.py" or adjust the import accordingly

class TestSecurityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def get_basic_auth_headers(self, username, password):
        # Create a Basic Auth header (username:password encoded in base64)
        creds = f"{username}:{password}"
        b64_creds = base64.b64encode(creds.encode()).decode()
        return {"Authorization": f"Basic {b64_creds}"}

    def get_jwt_token(self, username, password):
        # Login to retrieve a JWT access token
        response = self.app.post("/login", json={"username": username, "password": password})
        data = json.loads(response.data.decode())
        return data.get("access_token")

    def test_basic_protected_valid(self):
        # Test /basic-protected with valid Basic Auth credentials
        headers = self.get_basic_auth_headers("user1", "password")
        response = self.app.get("/basic-protected", headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data.get("message"), "Basic Auth: Access Granted")

    def test_basic_protected_invalid(self):
        # Test /basic-protected with invalid credentials
        headers = self.get_basic_auth_headers("user1", "wrongpassword")
        response = self.app.get("/basic-protected", headers=headers)
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data.decode())
        self.assertIn("error", data)

    def test_login_valid(self):
        # Test valid login returns a JWT token
        response = self.app.post("/login", json={"username": "user1", "password": "password"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn("access_token", data)

    def test_login_invalid(self):
        # Test login with invalid credentials returns an error
        response = self.app.post("/login", json={"username": "user1", "password": "wrongpassword"})
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data.decode())
        self.assertIn("error", data)

    def test_jwt_protected_valid(self):
        # Test /jwt-protected endpoint with a valid JWT token
        token = self.get_jwt_token("user1", "password")
        headers = {"Authorization": f"Bearer {token}"}
        response = self.app.get("/jwt-protected", headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data.get("message"), "JWT Auth: Access Granted")

    def test_jwt_protected_missing_token(self):
        # Test accessing /jwt-protected without a token
        response = self.app.get("/jwt-protected")
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data.decode())
        self.assertIn("error", data)
        self.assertEqual(data.get("error"), "Missing or invalid token")

    def test_admin_only_valid(self):
        # Test /admin-only endpoint with an admin token
        token = self.get_jwt_token("admin1", "password")
        headers = {"Authorization": f"Bearer {token}"}
        response = self.app.get("/admin-only", headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data.get("message"), "Admin Access: Granted")

    def test_admin_only_non_admin(self):
        # Test /admin-only endpoint with a non-admin token
        token = self.get_jwt_token("user1", "password")
        headers = {"Authorization": f"Bearer {token}"}
        response = self.app.get("/admin-only", headers=headers)
        self.assertEqual(response.status_code, 403)
        data = json.loads(response.data.decode())
        self.assertEqual(data.get("error"), "Admin access required")

    def test_admin_only_missing_token(self):
        # Test accessing /admin-only without any JWT token
        response = self.app.get("/admin-only")
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data.decode())
        self.assertIn("error", data)
        self.assertEqual(data.get("error"), "Missing or invalid token")

if __name__ == '__main__':
    unittest.main()