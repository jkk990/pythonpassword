import sys

class User:
    """
    Class that generates new instances of user data
    """
    user_list = []

    def __init__(self,email,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            email : New user_data email.
            password : New user_data password.
        '''
        self.email = email
        self.password = password
    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def main(self):
        print ('\nPassword Request Program v.01\n')
        password = id("")
        user_input = raw_input("Please Enter Password: ")
	
        if user_input != password:
            sys.exit("Incorrect Password, terminating... \n")
		
            print ("User is logged in!\n")
	

    def delete_user(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''
        
        User.user_list.remove(self)

    @classmethod
    def user_exist(cls,email):
        '''
        Method that checks if a user exists from the user list.
        Args:
            email: email to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.email == email:
                    return True

        return False