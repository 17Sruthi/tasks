#TO CHECK WHETHER GIVEN STRING IS A PALINDROME OR NOT

while(True):
    try:
        numb=int(input("\nENTER THE NUMBER OF TIMES YOU WANT TO RUN THE PROGRAM:"))
        if(numb>0):
            break
        else:
            print("NUMBER MUST BE A POSITIVE INTEGER")
    except:
        print("INVALID INPUT")

while(numb):
    string = input("\nENTER A STRING OF YOUR CHOICE:")
    revstring=string[::-1]
    if(revstring==string):
            print("\nGIVEN STRING IS A PALINDROME")
    else:
            print("\nGIVEN STRING IS NOT A PALINDROME")
    numb=numb-1
