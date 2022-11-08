import re
 
def validateEmail(email: str) -> bool:
    """
    Gets an email address (as a string) and determines if the email address is valid
    >>> validateEmail("not_@valid.com")
    False
    >>> validateEmail("this_is@valid.com")
    True
    
    """
    regex = r'[[a-zA-Z0-9]*[-._]?[a-zA-Z0-9]+]*@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}'
    return re.fullmatch(regex, email) != None

def validateEmailsInFile(file: str) -> tuple:
    """
    Gets a file name (as a string) and returns two lists: (1. valid email addresses, 2. invalid email addresses)
    """
    regex = r'.*@.*'
    valid = list()
    invalid = list()
    with open(file) as f:
        for line in f:
            for word in line.split():
                if re.fullmatch(regex, word):
                    if validateEmail(word):
                        valid.append(word)
                    else:
                        invalid.append(word)
    
    return valid, invalid
                    


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(validateEmail("not"))
    print(validateEmail("yes@yeso.com"))
    valid, invalid = validateEmailsInFile('emails.txt')
    print('valids')
    for index, email in enumerate(valid):
        print(index, ".", email)

    print('invalids')
    for index, email in enumerate(invalid):
        print(index, ".", email)


