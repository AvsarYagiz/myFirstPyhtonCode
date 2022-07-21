loginInfo = {"nickname": "password"}
username = str(input("Please enter your username or nickname: "))
isLogin = False

if username in loginInfo.keys():
    password = str(input("Please enter your password: "))
    if loginInfo[username] == password:
        print("You logged in successfully")
        isLogin = True
    else:
        print("The password is wrong!")
else:
    print("That username you entered does not exist!")
menu = '''
1: Change password
2: Change username
3: Delete account
q: Exit
'''
while isLogin:
    print(menu)
    selected = input("Please make a selection on the menu: ")
    print("*" * 70)
    if selected == '1':
        newPassword = input("\nPlease enter your new password: ")
        if len(newPassword) >= 8:
            loginInfo[username] = newPassword
            print(f"\nYour password updated as {newPassword}")
        else:
            print("Your password must be 8 characters at least!")
    elif selected == '2':
        newUsername = input("\nPlease enter your new username: ")
        loginInfo[newUsername] = loginInfo[username]
        del loginInfo[username]
        username = newUsername
        print(f"\nYour username updated as {newUsername}")
    elif selected == "3":
        del loginInfo[username]
        print("Your account deleted successfully")
    elif selected == "q":
        print("Goodbye!!!")
        break
    else:
        print("You entered wrong key! Please check the select options on the menu then try again!")

