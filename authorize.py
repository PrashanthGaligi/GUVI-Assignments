def validate_username(email):
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if '@' not in email or '.' not in email:
        return False
    else:
        a = email.index('@')
        dot = email.rindex('.')
        if (dot - a) < 2 or dot == (len(email) - 1):
            return False
        if email[0] not in alphabets:
            return False
    return True

def valid_password(password):
    digits = '0123456789'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(password) < 6 or len(password) > 15:
        return False
    digit_exists = False
    lower_exists = False
    upper_exists = False
    for i in password:
        if i in digits:
            digit_exists = True
        elif i in lowercase:
            lower_exists = True
        elif i in uppercase:
            upper_exists = True
        if digit_exists and lower_exists and upper_exists:
            return True
    return False

def registration():
    username = input('Username: ')
    if validate_username(username):
        f = open('userdata.csv')
        helper = True
        exists = False
        while helper:
            row = f.readline().split(',')
            if len(row) > 1:
                if row[0] == username:
                    exists = True
                    helper = False
            else:
                helper = False
        if exists:
            print('User already exists. Try another username')
            registration()
        else:
            password = input('Please enter Password for registration: ')
            if valid_password(password):
                new_user = username+','+password+'\n'
                f = open('userdata.csv', 'a')
                f.write(new_user)
                f.close()
                print('You are logged in as '+username)
            else:
                valid = False
                while not valid:
                    password = input('password format is wrong. Please try again: ')
                    if valid_password(password):
                        new_user = username+','+password+'\n'
                        f = open('userdata.csv', 'a')
                        f.write(new_user)
                        f.close()
                        print('You are logged in as '+username)
                        valid = True
    else:
        print('username format is wrong. Please try again')
        registration()

def login():
    username = input('Username: ')
    if validate_username(username):
        f = open('userdata.csv')
        helper = True
        exists = False
        while helper:
            row = f.readline().split(',')
            if len(row) > 1:
                if row[0] == username:
                    exists = True
                    helper = False
            else:
                helper = False
        if exists:
            password = input('Password: ')
            if row[1] == password+'\n':
                print('You are logged in as '+username)
            else:
                wrong = True
                while wrong:
                    print('The password you entered is wrong')
                    forgot = input('Enter 1 for retreiving password or 2 for retry: ')
                    if forgot == '1':
                        wrong = False
                        forgot_password(username)
                    elif forgot == '2':
                        password = input('Please try again: ')
                        print(row[1])
                        print(password)
                        if row[1] == password+'\n':
                            print('You are logged in as '+username)
                            wrong = False
                    else:
                        wrong = False
                        print('Incorrect option. Please retry')
        else:
            print('User not found. Please register before login')
            registration()
    else:
        print('username format is wrong. Please try again')
        login()

def forgot_password(username):
    f = open('userdata.csv')
    helper = True
    exists = False
    while helper:
        row = f.readline().split(',')
        if len(row) > 1:
            if row[0] == username:
                exists = True
                helper = False
        else:
            helper = False
    if exists:
        print('Your password is '+row[1])
    else:
        print('User does not exist. Please register')
        registration()

loop = True
while loop:
    option = input('Enter 1 for Registration or 2 for Login or 3 if forgot password: ')
    if option == '1':
        registration()
        loop = False
    elif option == '2':
        login()
        loop = False
    elif option == '3':
        username = input('Username: ')
        if validate_username(username):
            forgot_password(username)
            loop = False
        else:
            print('Username wrong format. Try again')
    else:
        print('Incorrect option. Please try again.')