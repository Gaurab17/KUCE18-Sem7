def check_comment(string):
    split = list(string)
    if split[0] == "/":
        if split[1] == '/':
            print('It is a single line comment')
        elif split[1] == '*':
            print('It is Multi line comment')
        else:
            print('It is not comment line')
    else:
        print('It is not comment line')
        

str = input('Enter The given String: ')
# FUNCTION CALL
check_comment(str)

    