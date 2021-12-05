try:
    from app import app, Contact, contact_schema
    import unittest
    from unittest.mock import patch
    import requests

except Exception as e:
    print("Module missing {}".format(e))

class TestRequests(unittest.TestCase):
    """ Make sure app.py server is running """

    # GET REQUESTS
    # Check for the response 200
    def test_contacts_statuscode_200(self):
        test_object = app.test_client(self)
        response = test_object.get("/api/contacts")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check for data return type
    def test_contacts_content(self):
        test_object = app.test_client(self)
        response = test_object.get("/api/contacts")
        self.assertEqual(response.content_type, "application/json")
    
    # Check for returned data
    def test_contacts_data_return(self):
        test_object = app.test_client(self)
        response = test_object.get("/api/contacts")
        self.assertTrue(b'id' in response.data)
        self.assertTrue(b'first_name' in response.data)
        self.assertTrue(b'last_name' in response.data)
        self.assertTrue(b'email' in response.data)
        self.assertTrue(b'phone_number' in response.data)

    # POST REQUEST
    @patch('requests.post')
    def test_post(self, mock_post):
        """
        Method assert_called_with checks if the patched method was called 
        exactly with the parameters specified in its invocation. In this 
        case it is True.
        """
        test_contact = Contact(id=99999, first_name="Test FName", last_name="Test LName", email="test@email.com", phone_number="07555555555")
        requests.post("/api/contacts/add", data=contact_schema.dump(test_contact), headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with("/api/contacts/add", data=contact_schema.dump(test_contact), headers={'Content-Type': 'application/json'})


if __name__ == "__main__":
    unittest.main()
