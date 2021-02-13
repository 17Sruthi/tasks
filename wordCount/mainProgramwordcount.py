# PROGRAM TO FIND THE OCCURANCE OF EACH WORLD GIVEN A STRING OR A PARAGRAPH 

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
    input_string = input("\nENTER YOUR STRING/PARAGRAPH:")
    
    while(True):
        searchword  = input("\nENTER THE WORD TO FIND ITS OCCURANCE:")

        words = []
        words = input_string.lower().split()
        words_freq=[words.count(i) for i in words]

        wordcountmapped=dict(zip(words,words_freq))

        if(searchword.lower() in wordcountmapped):
            print("\nSEARCHED WORD:",searchword)
            print("\nOCCURANCE:", wordcountmapped[searchword.lower()])
        else:
            print("\nENTERED WORD IS NOT PRESENT IN THE GIVEN PARAGRAPH")

        ans=input("DO YOU WISH TO CONTINUE SEARCHING IN THE PRESENT STRING/PARAGRAPH ITSELF?(Y/N):")
        if(ans=='N' or ans=='NO' or ans=='n' or ans=='no'):
            break
         
    numb=numb-1
