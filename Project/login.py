print('Login Page\n')

username = input('Enter User Name : ')

if username == 'Aditya':
    password = input('Enter Password : ')
    if password == '12345':
        print('\nWelcome '+username+' to our Program')
    else:
        print('Password Incorrect')
else:
    print('\nUser Name does not exist')