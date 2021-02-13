#PYTHON PROGRAM USING MAP FOR BOOK MANAGEMENT SYSTEM

bookdetails={}
print("List Is Created!")
while(True):
    try:
        print("\n\nMENU")
        print("\n1.APPEND")
        print("\n2.UPDATE BASED ON BOOK'S NAME")
        print("\n3.DELETE LAST INSERTED BOOK")
        print("\n4.DELETE BASED ON BOOK'S NAME")
        print("\n5.SEARCH")
        print("\n6.DISPLAY")
        print("\n7.QUIT")
        ch=int(input("\nENTER YOUR CHOICE:"))
        if(ch==1):
            while(True):
                try:
                    n=int(input("\nENTER THE NUMBER OF BOOKS TO APPEND:"))
                    if(n>0):
                        for i in range(n):
                            bname=input("\nENTER THE NAME OF THE BOOK:")
                            bAuthor=input("\nENTER THE NAME OF THE AUTHOR:")
                            bookdetails[bname]=bAuthor
                        break
                    else:
                        print("\nNUMBER MUST BE AN INTEGER VALUE BETWEEN(1-6)")
                except:
                    print("\nINVALID NUMBER")        
        
        elif(ch==2):
            if(len(bookdetails)==0):
                 print("\nNO RECORDS EXIST")
            else:
                try:
                    bnamekey=input("\nENTER THE BOOK'S NAME WHICH YOU WANT TO UPDATE/CHANGE:")
                    if(bnamekey in bookdetails):
                        bAuthorvalue=input("\nENTER THE NAME OF THE AUTHOR:")
                        bookdetails[bnamekey]=bAuthorvalue
                        print("\nBOOK DETAILS SUCCESSFULLY UPDATED")

                    else:
                        print("\nBOOK NOT FOUND TO UPDATE AUTHOR'S NAME")
                        
                except:
                    print("\nINVALID NUMBER")

        elif(ch==3):
            if(len(bookdetails)==0):
                 print("\nNO RECORDS EXIST")
            else:
                bookdetails.popitem()
                print("\nLAST INSERTED BOOK SUCCESSFULLY DELETED")

        elif(ch==4):
            if(len(bookdetails)==0):
                 print("\nNO RECORDS EXIST")
            else:
                try:
                    bnamekey=input("\nENTER THE BOOK'S NAME WHICH YOU WANT TO DELETE:")
                    if(bnamekey in bookdetails):
                        bookdetails.pop(bnamekey)
                        print("\nBOOK DETAILS SUCCESSFULLY DELETED")
                        
                    else:
                        print("\nBOOK NOT FOUND")
                        
                except:
                    print("\nINVALID NUMBER")
        
        elif(ch==5):
            if(len(bookdetails)==0):
                 print("\nNO RECORDS EXIST")
            else:
                bnamekey=input("\nENTER THE BOOK'S NAME WHICH YOU WANT TO SEARCH:")
                if(bnamekey in bookdetails):
                    print("\nBOOKS\t\tAUTHORS\n")
                    print(bnamekey,end="\t\t")
                    print(bookdetails[bnamekey])
                    
                else:
                    print("\nBOOK NOT FOUND")
                    

        elif(ch==6):
            if(len(bookdetails)==0):
                 print("\nNO RECORDS EXIST")
            else:
                print("\nBOOKS\t\tAUTHORS\n")
                for i in bookdetails:
                    print(i,end="\t\t")
                    print(bookdetails[i])
            
        elif(ch==7):
            break

        else:
            print("\nONLY CHOICES FROM 1-7 ARE ACCEPTED")

            
    except:
        print("\nINVALID INPUT")
                
         
        
        
        
