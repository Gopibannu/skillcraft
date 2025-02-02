
def encr(text,shift):
    res =  []
    for i in text:
        if i.isalpha():
            if i.isupper():
                
                    c = chr((ord(i)-ord('A')+shift)%26+ord('A'))
                    res.append(c)  
            else:
                
                    c = chr((ord(i)-ord('a')+shift)%26+ord('a'))
                    res.append(c)
    return ''.join(res)
def dccr(text,shift):
    res =  []
    for i in text:
        if i.isalpha():
            if i.isupper():
                
                    c = chr((ord(i)-ord('A')-shift)%26+ord('A'))
                    res.append(c)  
            else:
                
                    c = chr((ord(i)-ord('a')-shift)%26+ord('a'))
                    res.append(c)
    return ''.join(res)
def main():
    option = input("Enter Your choice e or d : ")
    text= input("Enter text to Encrypt or decrypt: ")
    try:
        shift= int(input("Enter shift range: "))
    except:
        print("Invalid shift value(Enter an integer: ) : ")

    if option == "e":  
        print("Encrypted Text :  "+encr(text,shift))
    elif option == "d":
        print("Decrypted Text :  "+dccr(text,shift))
    else:
        print("incorrect please enter e or d: ")

if __name__== "__main__":
    main()

    
    

    
    
    


             
         
    

