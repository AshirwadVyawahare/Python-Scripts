def isPalindrom(str1,str2):
    if(str1.lower() == str2.lower()):
        return True
    else:
        return False

strPalindrom = input("Enter the string to verify: ")
bool = isPalindrom(strPalindrom,strPalindrom[::-1])

if(bool):
    print("Palindrom string")
else:
    print("NOT Palindrom string")