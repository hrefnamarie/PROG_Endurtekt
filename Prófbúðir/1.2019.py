# Constant for format
ISBN_FORMAT = 'X-XXX-XXXXX-X'
ISBN_LEN = len(ISBN_FORMAT)
QUIT = 'q'

def validation_check(isbn):
    # Fyrir hvert inntak tékka formatið X-XXX-XXXXX-X
    # Þar sem X er int
    if len(isbn) != ISBN_LEN:
        # If length does not match return False
        return False
    for i in range(ISBN_LEN):
        # Looping through every char in isbn str
        if ISBN_FORMAT[i] == 'X':
            # If index in isbn is not digit return False
            if isbn[i].isdigit() is False:
                return False
        else:
            # If both are not -
            if ISBN_FORMAT[i] != isbn[i]:
                return False
    # Everything valid return True
    return True



# user_isbn will be the isbn input from user
user_isbn = input('Enter an ISBN: ')

while user_isbn != QUIT:
    valid = validation_check(user_isbn)
    # if input is valid print 'Valid format!'
    # else print 'Invalid format!
    if valid is True:
        print('Valid format!')
    else:
        print('Invalid format!')

    user_isbn = input('Enter an ISBN: ')



# Þurfum að taka inn ISBn streng frá notanda
# Á meðan inntak strengs er ekki 'q'

# Ef inntakið er gilt, print 'Valid Format'
# Annars ætlum við að prenta 'Invalid Format'


