#PROGRAM TO CHECK WHETHER ENTERED CHARACTER IS AN ALPHABET OR NOT 
        
while(True):
    try:
        numb=int(input("\nENTER THE NUMBER OF TIMES YOU WANT TO RUN THE PROGRAM:"))
        if(numb>0):            
            break               
        else:
            print("\nNUMBER MUST BE A POSITIVE INTEGER")
    except:
        print("\nINVALID NUMBER")

while(numb):
    char=input("\nENTER A CHARACTER OF YOUR CHOICE:")
    if(len(char)>1):
        print("\nNOTE")
        print("THIS PROGRAM CHECKS ONLY WHETHER THE FIRST CHARACTER ENTERED IS ALPHABET OR NOT!!!")
    if(char[0].isalpha()==True):
        print("\nENTERED CHARACTER IS AN ALPHABET")
    else:
        print("\nENTERED CHARACTER IS NOT AN ALPHABET")
    numb=numb-1

