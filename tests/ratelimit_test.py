import unittest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


class TestRateLimit(unittest.TestCase):
    def test_rate_limit(self):
        for _ in range(5):
            response = client.post("/api/v2/analyze", json={"text": "I am glad this happened", "language": "en"})
            self.assertEqual(response.status_code, 200)
        
        # Sixth request should be rate limited
        response = client.post("/api/v2/analyze", json={"text": "I am glad this happened", "language": "en"})
        self.assertEqual(response.status_code, 429)  # HTTP status code for Too Many Requests


def main():
    unittest.main()


if __name__ == "__main__":
    main()
