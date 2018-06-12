#!/usr/bin/env python3.6
import sys
import random
import pyperclip
from password import User
from credential import Credential
import string

def create_user(email,password):
    '''
    Function to create a new user
    '''
    new_user = User(email,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()  
 
def display_user():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_user()

def create_credential(account_name,account_email,account_password):
    '''
    function to create a new credential
    '''
    new_credential = Credential(account_name,account_email,account_password)      
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(account_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credential.find_by_account_name(account_name)

def check_existing_credential(account_name):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credential.credential_exist(account_name)

def display_credential():
    '''
    Function that returns all the saved contacts
    '''
    return Credential.display_credential()

def copy_account_password(cls,account_password):
    '''
    function to copy a password to pyperclip
    '''
    pyperclip.copy(credential_found.account_password)


def generate_password(self, size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    '''
    Function to generate an 8 character password for a credential
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def main():
    print("Hello Welcome to your password locker. What is your email adress?")
            email = input()

            print(f"Hello {email}. what are looking to do?")
            print('\n')

            while True:
                print("Use these short codes : cu - create a new user, du - display a user, ex -exit the user list ")
             
                short_code = input().lower()
             
                if short_code == 'cu':
                    print("New User")
                    print("-"*10)

                    print("email...")
                    email = input()

                    print ('\nPassword Request Program v.01\n')
                    password = id("allow")
                    user_input = input("Please Enter Password: ")
	
                    if user_input != password:
                         sys.exit("Incorrect Password, terminating... \n")
		
                    print ("User is logged in!\n")


                    save_user(create_user(email, password))

                    print ('\n')
                    print(f"New User {email} {password} created")
                    print('\n')
            
            elif short_code == 'du':
                    if display_user():
                        print("Here is a list of all users")
                        print('\n')
                        for user in display_user():
                            print(f"{user.email} {user.password}")
                        print('\n')
           
                else:
                        print('\n')
                        print("You dont seem to have any user saved yet")
                        print('\n')
            
            elif short_code == "ex":
                 print("bye....")
                 break
            else:
                 print("please use the short codes")

    print("Hello, please enter your acount_name")
        account_name = input()

        print(f"For {account_name}. lets choose what to do!")

        print('\n')

         while True:
                    print("Use these short codes : cc - create a new credential, dc - display credential, fc -find credential, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("account_name ....")
                            account_name = input()

                            print("account_email ...")
                            account_email = input()

                            print("account_password ...")
                            account_password = input()

                            save_contacts(create_credential(account_name,account_email,account_password))
                            
                            print ('\n')
                            print(f"New Credential {account_name} {account_email} created")
                            print ('\n')
                    
                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')
                                    for credential in display_credential():
                                         print(f"{credential.account_name} {credential.account_email} {credential.account_password}")
                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')
                             elif short_code == 'fc':

                            print("Enter the account_name you want to search for")

                            search_account_name = input()

                            if check_existing_credential(search_account_name):
                                    search_credential = find_credential(search_account_name)
                                    print(f"{search_credential.account_name} {search_credential.account_email}")
                                    print('-' * 20)

                                    print(f"account_name.......{search_credential.account_name}")
                                    print(f"account_email.......{search_credential.account_email}")
                                    print(f"account_password.......{search_credential.account_password}")
                            else:
                                    print("That credential does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("Please use the short codes")

            



            