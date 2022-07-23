login_info = {
    "samplename": "samplepassword"
}
username = str(input("Please enter your username: "))

if username in login_info.keys():
    password = str(input("Please enter your password: "))
    if password in login_info[username] == password:
        print("Login success!")
        isLogin = True
    else:
        print("The password is wrong!")
else:
    print("No such user found! Please try again later!")
menu = ''' 
1: Change password
2: Change username 
3: Delete this account 
q: Exit
'''
while isLogin:
    print(menu)
    selection = str(input("Please select the operation you want to do from the menu: "))
    print('*' * 50)
    if selection == '1':
        newPassword = str(input("Please enter your new password: "))
        login_info[username] = newPassword
        print(f"Your new password is {newPassword}")
    elif selection == '2':
        newUsername = str(input("Please enter your new username: "))
        login_info[newUsername] = login_info[username]
        del login_info[username]
        username = newUsername
        print(f"Your new username is {username}")
    elif selection == '3':
        del login_info[username]
        print("Your account deleted successfully!")
    elif selection == 'q':
        print("Goodbye!")
        break
    else:
        print("You did a mistake during selection. Please make sure your selection is on the menu!")
