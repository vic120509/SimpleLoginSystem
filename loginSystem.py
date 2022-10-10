from datetime import datetime

from DataBaseHandler import register,update_first_name,update_last_name,update_username,update_password,delete_AccountData,login,get_AccountData,search_account,ShowData

from colorama import Fore,Back,Style,init
init(convert=True)
from termcolor import colored
import maskpass
import base64





def loginRights(username, password):
    if login(username, password):
        while True:
            AccountData = get_AccountData(username,password)
            print("please select action required?")
            print()
            print("1. Change First Name")
            print("2. Change last Name")
            print("3. Change Username")
            print("4. Show Data")
            print("5. logout")
            user_input = input('>>>')
            if user_input == '1':
                while True:
                    username = input("Enter username:")
                    pw = maskpass.askpass(prompt = "Password:",mask =" ")
                    data = pw
                    data_bytes = data.encode('ascii')
                    base64_bytes = base64.b64encode(data_bytes)
                    base64_string = base64_bytes.decode('ascii')

                    base64_string
                    encpass = base64_string
                    new_first = input("Enter new first name:")
                    sure = input("Are you sure? (Y/N ")
                    if sure.lower()=='y':
                        
                        if get_AccountData(username, password):
                           update_first_name(username, encpass, new_first)
                           print(colored('_'*50,'green'))
                           print()
                           print(colored("First Name updated",'green'))
                           print
                           print(colored('_'*50,'green'))
                        else:
                           print()
                           print(colored('_'*50,'red'))
                           print(colored("username or password incorret",'red'))
                           print(colored('_'*50,'red'))
                           print()
                           continue
                    elif sure.lower=='n':
                        break
            elif user_input == '2':
                  while True:
                    username = input("Enter username:")
                    pw = maskpass.askpass(prompt = "Password:",mask =" ")
                    data = pw
                    data_bytes = data.encode('ascii')
                    base64_bytes = base64.b64encode(data_bytes)
                    base64_string = base64_bytes.decode('ascii')

                    base64_string
                    encpass = base64_string
                    new_last = input("Enter new last name:")
                    sure = input("Are you sure ?(Y/N ")
                    if sure.lower()=='y':
                        
                        if get_AccountData(username, password):
                           update_last_name(username, encpass,new_last)
                           print()
                           print(colored('_'*50,'green'))
                           print()
                           print(colored("Last Name updated",'green'))
                           print
                           print(colored('_'*50,'green'))
                        else:
                           print()
                           print(colored('_'*50,'red'))
                           print(colored("username or password incorret",'red'))
                           print(colored('_'*50,'red'))
                           print()
                           continue
                    elif sure.lower()=='n':
                        break
            elif user_input == '3':
                  while True:
                    username = input("Enter username:")
                    pw = maskpass.askpass(prompt = "Password:",mask =" ")
                    data = pw
                    data_bytes = data.encode('ascii')
                    base64_bytes = base64.b64encode(data_bytes)
                    base64_string = base64_bytes.decode('ascii')

                    base64_string
                    encpass = base64_string
                    new_user = input("Enter new  username:")
                    sure = input("Are you sure? Y/N")
                    if get_AccountData(username, password):
                       update_username(username, encpass, new_user)
                       print(colored('_'*50,'green'))
                       print()
                       print(colored("username updated",'green'))
                       print
                       print(colored('_'*50,'green'))
                    else:
                       print()
                       print(colored('_'*50,'red'))
                       print(colored("username or password incorret",'red'))
                       print(colored('_'*50,'red'))
                       continue

            elif user_input == '4':
                
                acctInfo = get_AccountData(username, password)
                print()
                print(colored('_'*20,'green'))
                print()
                print(colored(f"{'Your Data':20}",'green'))
                print(colored('_'*20,'green'))
                print()
                print(f"First Name :       {acctInfo[0]}")
                print(f"Last Name  :       {acctInfo[1]}")
                print(f"Username   :       {acctInfo[2]}")
                print(f"Password   :       {acctInfo[3]}")
                print(f"Date Registered :  {acctInfo[4]}")
                print()
                print()
                print()
            elif user_input == '5':
                print("Logging Out")
                print()
                print()
                print(colored("$"*25,'yellow'))
                print(colored("logged out THANK YOU!!!",'green'))
                print(colored("$"*25,'yellow'))
                print()
                print()
def main():
    while True:
        print("Welcome to Login System!")
        print("1.Register")
        print("2.Login")
        print("3.delete")
        print("4.change password")
        print("5.Exit")
        user_input = input(">>>")

        if user_input == "1":
            while True:
                
                first = input("First Name:")
                last = input("Last Name:")
                un = input("username:")
                pw = maskpass.askpass(prompt = "Password:",mask =" ")
                data = pw
                data_bytes = data.encode('ascii')
                base64_bytes = base64.b64encode(data_bytes)
                base64_string = base64_bytes.decode('ascii')

                base64_string
               
                encpass = base64_string
                date = datetime.strftime(datetime.now(),'%m/%d/%Y %I:%M:%p')

                sure = input("Are you sure? (Y/N ")
                
                if sure.lower() == 'y':
                   
                    register(first,last,un,encpass,date)
                    
                   
                    print(colored("_"*25,'green'))
                    print()
                    print(colored("New Account Registered!",'green'))
                    print(colored("_"*25,'green'))
                    print()
                    print()
                    break
                elif sure.lower()== 'n':
                    continue

        elif user_input == "2":
            while True:
                username = input("Enter username : ")
                password= maskpass.askpass("Enter password :" ,mask = " ")
                data = password
                data_bytes = data.encode('ascii')
                base64_bytes = base64.b64encode(data_bytes)
                base64_string = base64_bytes.decode('ascii')
                base64_string
                
                
                sure =input("Are you sure (Y/N) ")
                if sure.lower()=='y':
                            
                       if   get_AccountData( username, base64_string):
                            login(username, password)
                            
                            print(colored('_'*50,'green'))
                            print()
                            print(colored("You are successfully logged in!",'green'))
                            print(colored('_'*50,'green'))
                            print()
                            loginRights(username, base64_string)
                       else:
                            print(colored('_'*50,'red'))
                            print()
                            print(colored("Account not exist",'red'))
                            print()
                            print(colored('_'*50,'red'))
                            break
                elif sure.lower()=='n':
                    loginRights(username, password)
                    
                
                    
        elif user_input == "3":
            while True:
              
                username = input("Enter username : ")
                password= maskpass.askpass("Enter password :" ,mask = " ")
                data = password
                data_bytes = data.encode('ascii')
                base64_bytes = base64.b64encode(data_bytes)
                base64_string = base64_bytes.decode('ascii')
                base64_string
                sure =input("Are you sure ? (Y/N) ")
                if sure.lower()== 'y':
                    if  get_AccountData(username, base64_string):
                        delete_AccountData(username,password)
                        print(colored('-'*50,'green'))
                        print()
                        print(colored("Account Deleted",'green'))
                        print()
                        print(colored('-'*50,'green'))
                    else:
                        print(colored('-'*50,'red'))
                        print(colored("username or password incorrect",'red'))
                        print(colored("login not exists! please try again",'red'))
                        print(colored('-'*50,'red'))
                        break
                elif sure.lower()== 'n':
                        continue

        elif user_input == '4':
            while True:
                print()
                username = input("Enter username: ")
                password= maskpass.askpass("Enter old password :" ,mask = " ")
                data = password
                data_bytes = data.encode('ascii')
                base64_bytes = base64.b64encode(data_bytes)
                base64_string = base64_bytes.decode('ascii')
                base64_string
                encpass = base64_string
               
                password= maskpass.askpass("Enter new password :" ,mask = " ")
                data = password
                data_bytes = data.encode('ascii')
                base64_bytes = base64.b64encode(data_bytes)
                base64_string = base64_bytes.decode('ascii')
                base64_string
                
                sure =input("Are you sure ?(Y/N) ")
                if sure.lower()=='y':
                    
                
                    if get_AccountData(username,encpass):
                       update_password(username,encpass,base64_string)
                       print(colored("-"*50,'green'))
                       print(colored("Password has been changed",'green'))
                       print(colored("-"*50,'green'))
                       print()
                       break
                    else:
                        print(colored("-"*50,'red'))
                        print(colored("username or old password not exist",'red'))
                        print(colored("-"*50,'red'))
                        print()
                        print()
                        print()
                        break
                elif sure.lower()=='n':
                   break
        elif user_input == '5':
            print("Exiting....")
            print()
            print()
            print(Fore.GREEN+"<***>"*12)
            print()
            print(Fore.YELLOW+"THANK YOU !!! FOR USING THIS PROGRAM")
            print()
            print(Fore.GREEN+"<***>"*12)
            break
main()
               
                   




