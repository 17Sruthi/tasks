# PROGRAM TO FIND FREQUENCY OF EACH DIGIT IN A GIVEN NUMBER

def frequencyofdigits(numb):
    while(numb):
        while(True):
            try:
                noOfdigits=0
                inputnumber=input("\nENTER A NUMBER:")
                inputnumber=inputnumber.strip('-')
                number=float(inputnumber)
                if(inputnumber.isnumeric()==True):
                    break
                elif(type(number)==float):
                    inputnumber=str(number)
                    break
            except:
                print("\nINVALID INPUT ENTER A NUMERIC VALUE")
        res=[]
        res[:]=inputnumber
        numb_freq=[res.count(i) for i in res]
        numbcountmapped=dict(zip(res,numb_freq))
        for i in numbcountmapped:
            if(i!='.'):
                print("DIGIT:",i," OCCURANCE:",numbcountmapped[i])             
        numb=numb-1
        

while(True):
    try:
        numb=int(input("\nENTER THE NUMBER OF TIMES YOU WANT TO RUN THE PROGRAM:"))
        if(numb>0):
            break
        else:
            print("\nNUMBER MUST BE A POSITIVE INTEGER")
    except:
        print("\nINVALID NUMBER")

frequencyofdigits(numb)

