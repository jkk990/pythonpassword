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