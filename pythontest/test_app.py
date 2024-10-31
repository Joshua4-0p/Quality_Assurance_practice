# test_app.py
import unittest
from flask import Flask

app = Flask(__name__)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Hello level 400 FET, Quality Assurance!"}

class AppTestCase(unittest.TestCase):
    
    # Set up the testing client
    def setUp(self):
        # Set up a test client for the Flask application
        self.app = app.test_client()
        self.app.testing = True

    # Test the home route
    def test_home(self):
        # Send a GET request to the home route
        response = self.app.get('/')
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the JSON response matches the expected message
        self.assertEqual(response.json, {"message": "Hello level 400 FET, Quality Assurance!"})

# Run the tests
if __name__ == '__main__':
    unittest.main()
