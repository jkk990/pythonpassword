import unittest
from password import User

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
        self.new_user = User("jk@b.com", "allow")

    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_user.email,"jk@b.com")
            self.assertEqual(self.new_user.password,"allow")

    def test_save_user(self):
            '''
            test_save_user test case to test if the user object is saved into the contact list
            '''
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []


    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User('jk@b.com','allow')

    def test_delete_user(self):
           '''
           test_delete_user to test if we can remove a user from our user list
           '''
           self.test_user = User("jk@b.com","allow",)
           self.test_user.save_user()
           self.test_user.delete_user()
           self.assertEqual(len(User.user_list),0)

    def test_user_exists(self):
           '''
           test to check if we can return a Boolean  if we cannot find the contact.
           '''
           self.test_user = User("jk@b.com", "allow")          
           self.test_user.save_user()
           user_exists = User.user_exist("jk@b.com")
           self.assertTrue(user_exists)

if __name__ == "__main__":
    unittest.main()
