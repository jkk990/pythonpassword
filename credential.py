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