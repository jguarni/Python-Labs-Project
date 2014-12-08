def main():
    userinput()
    
def userinput():
    utext = input('Please Enter the first letter of your word: ')
    while utext.isdigit():
        print('That is not a letter')
        utext = input('Please enter another letter: ')
    return utext

main()
