##########################################################################
######################### Doaa Maher's PHONEBOOK #########################
##########################################################################
import os
import re      # For using regular expressions

# Initially no Phone book created
phoneBook = None
# Creating the Dict
contact = {}

# Function for Displaying Contact
def display_contact () :
  if contact == {} :
    print("Empty")
  
  else :
    for a in contact.items() :
      print('########################')
      print("Contact is : " ,a)
      print('########################')

def AddContact ():
  print("########## ADD CONTACT : ###########")
  # Entering DATA
  name       = input("Enter the Name (First Char is Upper Cased) : ")
  gender     = input("Enter the Gender (First Char is Upper Cased) : ")
  phone_num  = input("Enter the Phone number : ")
  email      = input("Enter the Email : ")
  
  # Checking the Egyptian Number's Validity , Email Address , Name & Gender [REGEX]
  correct_phone_num   = re.search(r'[0][1][0 1 2]\d{8}',phone_num)
  correct_email_add   = re.search(r'[a-z\d.-]+@+[\w.]+',email)
  correct_name        = re.search(r'[A-z]+',name)
  correct_gender      = re.search(r'[F,M]+\w+',gender)

  if correct_phone_num == None or correct_email_add == None or correct_name == None or correct_gender == None:
    print("Wrong Entry!, Please Enter a Valid one!")
 
  
  else :
    if phone_num not in contact :
      contact[phone_num] = {'Gender :':gender,'Name :':name,'Email :':email}
      print('Added Successfully')
      
    else :
      print('Contact already exists!')

def EditContact ():
  print("########## EDIT CONTACT : ###########")
  phone_num = input("Enter the contact's number to be edited : ")
  
  if phone_num in contact :          
    for i in contact.keys():
      if i == phone_num :
        name = input("Enter new name : ")
        gender = input("Enter new Gender : ")
        email = input("Enter new email : ")
        
        # Checking the Egyptian Number's Validity , Email Address , Name & Gender [REGEX]
        correct_phone_num = re.search(r'[0][1][0 1 2]\d{8}',phone_num)
        correct_email_add = re.search(r'[a-z\d.-]+@+[\w.]+',email)
        correct_name      = re.search(r'[A-z]+',name)
        correct_gender      = re.search(r'[F,M]+\w+',gender)
        
        if correct_phone_num == None or correct_email_add == None or correct_name == None or correct_gender == None:
          print("Wrong Entry!, Please Enter a Valid one!")
  
        else : 
          contact[phone_num] = {'Gender :':gender,'Name :':name,'Email :':email}
          print("Contact Updated !")
          
    #print("Your Modified Contact : ")
    #print (contact)

    #display_contact()
    
  else :
    print("Contact is not found in Phone Book")

def SearchContact():
  search_num = input("Enter his/her Contact Number : ")
  if search_num in contact :
    print ("FOUND") 
  else :
    print("Contact is not Found!")
    
    
def DeleteContact():
  delete_contact = input("Enter his/her Contact Number : ")
        
  if delete_contact in contact :
    confirmation = input("Are you sure you want to delete this contact? - 'y/n' \n")
    
    if confirmation == 'y' or confirmation == 'Y':
      del contact [delete_contact]
      print ("Contact Deleted!")
      
    else : 
      print("Contact not deleted")
      
  else :
    print("Contact not found!")
    
##############################################################################
##############################################################################
          
def main():
  # Initially no Phone book/contact created
  phoneBook = None
  contact = {}

  while True :
    choice = int(input(" 1. Create Phone book \n 2. Add Contact \n 3. Modify Contact \n 4. Show Contact \n 5. Search Contact \n 6. Delete Contact \n 7. Delete Phone Book \n 8. Exit \n Enter Your Choice : "))
##############################################################################
##############################################################################

   # Creating a new phone book
    if choice  == 1 :
      if phoneBook == None :
        phoneBook ={}
        print("You've Created the Phonebook")
      else :
          print("Already Created!")    
##############################################################################
##############################################################################

    # Adding a new Contact
    elif choice == 2 :
      if phoneBook == None :
        print("NO PHONEBOOK!")
      else :
        AddContact()
           
##############################################################################
##############################################################################

    # Editing a Contact [Modification]
    elif choice == 3 :
      if phoneBook == None :
        print("NO PHONEBOOK!")
      
      else :
        EditContact()

##############################################################################
##############################################################################

    # Displaying a Contact
    elif choice == 4 :
      if phoneBook == None :
        print("NO PHONEBOOK!")
          
      else :
          display_contact()
        
##############################################################################
############################################################################## 

    # Searching for a contact
    elif choice == 5 :
      if phoneBook == None :
         print("NO PHONEBOOK!")
         
      else :
        SearchContact()
          
##############################################################################
############################################################################## 

    # Deleting a contact
    elif choice == 6 :
      if phoneBook == None :
        print("Contact is not Found!")
        
      else :
        DeleteContact()
            
##############################################################################
##############################################################################
    
    # Deleting the phone book
    elif choice == 7:
      if phoneBook == None :
        print("NO PHONEBOOK TO DELETE!") 
      else :
        del phoneBook
        print("PHONEBOOK DELETED")
        
##############################################################################
##############################################################################
    
    # Exit
    elif choice == 8:
      break
  
  else :
    print("Not Valid Entry, Try Again")
##########################################################################
##############################################################################
    
if __name__=='__main__':
  main()