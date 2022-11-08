import re
 
def validateEmail(email: str) -> bool:
    """
    Gets an email address (as a string) and determines if the email address is valid
    >>> validateEmail("not_@valid.com")
    False
    >>> validateEmail("this_is@valid.com")
    True
    
    
    """
    regex = r'\b[[a-zA-Z0-9]*[-._]?[a-zA-Z0-9]+]*@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email) != None

def validateEmailsInFile(file: str) -> tuple:
    regex = r'\b.*@.*\b'
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
    for i in valid:
        print(i)
    print('invalids')
    for i in invalid:
        print(i)
