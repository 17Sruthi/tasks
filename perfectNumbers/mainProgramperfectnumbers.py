# PROGRAM TO FIND ALL THE PERFECT NUMBERS UPTO THE RANGE GIVEN

def perfectnumbers(numb):
    while(numb):
        while(True):
            try:
                n=int(input("\nENTER THE NUMBER UPTO WHICH YOU WANT THE PERFECT NUMBERS TO BE DISPLAYED:"))
                if(n>6):
                    break 
                elif(n<6 and n>0):
                    print("\nNO PERFECT NUMBER EXISTS IN THIS RANGE")
                else:
                    print("\nNUMBER MUST BE A POSITIVE INTEGER")
            except:
                print("\nINVALID NUMBER")
        print("\nPERFECT NUMBERS UPTO",n)
        for i in range(1,n+1):
            sum=0
            for j in range(1,i):
                if(i%j==0):
                    sum=sum+j
            if(sum==i):
                print(sum)
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


perfectnumbers(numb)
