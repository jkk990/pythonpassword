import pyperclip
import random
import string

class Credential:
    """
    Class that generates new instances of user credentials
    """
    credential_list = []

    def __init__(self, account_name, account_email, account_password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: New account name.
            account_email : New account email address.
            account_password : New account password.
        '''

        self.account_name = account_name
        self.account_email = account_email
        self.account_password = account_password
    def save_credential(self):
        '''
        save_user method saves credential objects into user_list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        
        Credential.credential_list.remove(self)

    def generate_password(self, size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password for a credential
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in an account_name and returns a credential that matches that name.

        Args:
            account_name: name to search for
        Returns :
            Credential of person that matches the name.
        '''

        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential

    @classmethod 
    def credential_exist(cls,account_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            account_name:account name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                    return True

        return False
    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

    @classmethod

    def copy_account_password(cls,account_name):

        credential_found = Credential.find_by_account_name("account_name")
        
        pyperclip.copy(credential_found.account_password)
        