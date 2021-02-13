#PROGRAM TO CHECK NUMBER OF DIGITS IN A GIVEN NUMBER

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
    while(True):
        try:
            noOfdigits=0
            inputnumber=input("\nENTER A NUMBER:")
            inputnumber=inputnumber.strip('-')
            number=float(inputnumber)
            if(inputnumber.isnumeric()==True):
                inputnumber=inputnumber.strip('0')
                print("\nNUMBER OF DIGITS:",len(inputnumber))
                break
            elif(type(number)==float):
                print("\nNUMBER OF DIGITS:",len(inputnumber)-1)
                break
        except:
            print("\nINVALID INPUT ENTER A NUMERIC VALUE")
               
    numb=numb-1
    
