#!/usr/bin/env python3.6
import sys
from password import User
from credential import Credential

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

def main():
        print ('\nPassword Request Program v.01\n')
        password = id("allow")
        user_input = input("Please Enter Password: ")
	
        if user_input != password:
            sys.exit("Incorrect Password, terminating... \n")
		
            print ("User is logged in!\n")

def create_credential(account_name,account_email,account_password):
    '''
    function to create a new credential
    '''
    new_credential = Credential(account_name,account_email,account_password)      
    return new_credential

def save_credential(credential):
    '''
    Function to save contact
    '''
    credential.save_credential()
