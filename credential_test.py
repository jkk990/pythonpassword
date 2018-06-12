import unittest
from credential import Credential

class TestUser(unittest.TestCase):
    '''
     Test class that defines test cases for the user class behaviours.
    
     Args: 
      unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("facebook", "jk@c.com", "allow")

    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_credential.account_name,"facebook")
            self.assertEqual(self.new_credential.account_email,"jk@c.com")
            self.assertEqual(self.new_credential.account_password,"allow")
    
    def test_save_credential(self):
            '''
            test_save_credential test case to test if the credential object is saved into the credential list
            '''
            self.new_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("facebook", "jk@c.com", "allow")

    def test_delete_credential(self):
           '''
           test_delete_credential to test if we can remove a credential from our credential list
           '''
           self.test_credential = Credential("facebook", "jk@c.com", "allow")
           self.test_credential.save_credential()
           self.test_credential.delete_credential()
           self.assertEqual(len(Credential.credential_list),0)

    def test_find_credential_by_account_name(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("facebook", "jk@c.com", "allow")# new contact
        test_credential.save_credential()

        found_credential = Credential.find_by_account_name("facebook")

        self.assertEqual(found_credential.email,test_credential.email)
if __name__ == "__main__":
    unittest.main()
