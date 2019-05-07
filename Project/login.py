print('Login Page\n')

username = input('Enter User Name : ')

if username == 'Aditya':
    password = input('Enter Password : ')
    if password == '12345':
        a = input('\nWelcome '+username+' to our Program')
    else:
        b = input('Password Incorrect')
else:
    c = input('\nUser Name does not exist')
