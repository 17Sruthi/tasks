# PYTHON PROGRAM TO CONVERT NUMBERS TO FIGURES UPTO 10 TO THE POWER OF 19(20 DIGITS)

while(True):
    try:
        n=int(input("\nENTER THE NUMBER OF TIMES YOU WANT TO RUN THE PROGRAM:"))
        if(n>0):
            break               
        else:
            print("\nNUMBER MUST BE A POSITIVE INTEGER")
    except:
        print("\nINVALID NUMBER")



while(n):        
    while(True):                                                # Input From User And Check Whether It's A Valid Non-Negative Integer
        try:
            numb=input("Enter A Non-Negative Integer:")

            if(len(numb)>20):
                print("Please Enter A Number Having Maximum Number Of Digits 20")
            
            elif(len(numb)>1 and numb[0]=='0'):
                print("Please Enter A Number Without Leading Zeros")

            elif(numb[0]=='-'):
                print("Please Enter A Non-Negative Number")

            elif(type(numb)==float):
                print("Please Enter An Integer Value")
                
            elif(numb.isdigit()):
                break
        
            else:
                print("INVALID INPUT")
                
        except Error:
            print("Please Enter A Valid Non-Negative Integer")
            


    lengthOfnumb=len(numb)

    sanskritUnitSystem=['Mahashank','Mahashank',                            # List Storing Units In Figures
                        'Shank','Shank',
                        'Padma','Padma',
                        'Neel','Neel',
                        'Kharab','Kharab',
                        'Arab','Arab',
                        'Crores','Crores',
                        'Lakh','Lakh',
                        'Thousand','Thousand',
                        'Hundred','Tens','Units']

    unitsPlace=['Zero',                                                     # List Storing Unit Place Values In Figures 
                'One',
                'Two',
                'Three',
                'Four',
                'Five',
                'Six',
                'Seven',
                'Eight',
                'Nine']


    tensPlaceOne=['Ten',                                                    # List Storing Tens Place One Values In Figures
                  'Eleven',
                  'Twelve',
                  'Thirteen',
                  'Fourteen',
                  'Fifteen',
                  'Sixteen',
                  'Seventeen',
                  'Eighteen',
                  'Nineteen']

    tensPlaceOtherDigits=['Zero',                                       # List Storing Other Values In Tens Place In Figures
                          'Tens',
                          'Twenty',
                          'Thirty',
                          'Forty',
                          'Fifty',
                          'Sixty',
                          'Seventy',
                          'Eighty',
                          'Ninety']


    alphaNumericResult=[]                                           # To Store Values In Alphanumeric Format After Certain Mapping With sanskritUnitSystem List 
    alphaResult=[]                                                  # To Store Final Result In Figures



    valuesOfnumb=0                                                  # To Traverse The Input Number
    indexposition=len(sanskritUnitSystem)-len(numb)-1               # Since We Have To Map 10,000 also to Thousand and 1000 also to Thousand
    if(lengthOfnumb%2==0):                                          # To Check Whether Given Number Is Even Or Odd Depending On Which The Mapping Of LeftMost Digit Will Be Done
        varyingValue=int((numb[valuesOfnumb]))                      # For Even Numbers Mapping
        alphaNumericResult.append(varyingValue)
        valuesOfnumb=valuesOfnumb+1
        alphaNumericResult.append(sanskritUnitSystem[indexposition])


        
    while(valuesOfnumb<lengthOfnumb-3 and numb[valuesOfnumb]!='0'):     # FOr Odd Numbers Mapping
        varyingValue=int((numb[valuesOfnumb]))
        alphaNumericResult.append(varyingValue)
        valuesOfnumb=valuesOfnumb+1
        varyingValue=int((numb[valuesOfnumb]))
        alphaNumericResult.append(varyingValue)
        valuesOfnumb=valuesOfnumb+1
        indexposition=indexposition+2
        alphaNumericResult.append(sanskritUnitSystem[indexposition])


    # print(alphaNumericResult)                                 # Storing The Mapping In alphaNumericResult List



    i=0                                                         # To Traverse The alphaNumericResult List
    while(i<len(alphaNumericResult)):                           # Mapping Of Figures except Hundreds, Tens And Units Place Stored In alphaResult
        if(alphaNumericResult[i]!=0):
            if(type(alphaNumericResult[i])==str):
                alphaResult.append(alphaNumericResult[i])
            elif(type(alphaNumericResult[i+1])==str and alphaNumericResult[i-1]!=1):
                alphaResult.append(unitsPlace[alphaNumericResult[i]])
            elif(alphaNumericResult[i]>1  and type(alphaNumericResult[i+1])==int):
                alphaResult.append(tensPlaceOtherDigits[alphaNumericResult[i]])
        elif(alphaNumericResult[i-1]==1 and type(alphaNumericResult[i])==int):
                alphaResult.append(tensPlaceOne[alphaNumericResult[i]])
        i=i+1




    i=-3                                                        # For Mapping Of Digits In Hundreds, Tens And Units Place                            
    while(i<0):
        varyingValue=int(numb[i])
        if(varyingValue!=0):
            if(i==-3):
                alphaResult.append(unitsPlace[varyingValue])
                alphaResult.append('Hundred')
            elif(i==-2):
                if(varyingValue>1):
                    alphaResult.append(tensPlaceOtherDigits[varyingValue])
            elif(i==-1):
                if(numb[-2]=='1'):
                    alphaResult.append(tensPlaceOne[varyingValue])
                else:
                    alphaResult.append(unitsPlace[varyingValue])
        i=i+1
            
     
    # print(alphaResult)                                    # Final Result Stored In List

    result = ",".join(alphaResult).replace(",", " ")        # For Better Display
    print("FIGURES:",result)
    n=n-1
