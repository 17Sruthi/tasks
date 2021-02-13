//CPP PROGRAM TO GENERATE RANDOM NUMBERS FOR A DICE(1-6)
#include <iostream>
using namespace std;
#include <string>

int main(void)
{
    string choice;
    int progcount=-1,numb,res;
    while(1){
        
        // cout<<"\nUNIT-TESTING CASE 1: NEGATIVE INPUT";
        // choice='-2';
        // cout<<"\nUNIT-TESTING CASE 2: 0 AS INPUT";
        // choice='0';
        // cout<<"\nUNIT-TESTING CASE 3: CHARACTER INPUT";
        // choice='#';
        
        cout<<"\nUNIT-TESTING CASE 4: VALID INPUT(USER CHOICE)";
        cout<<"\nENTER THE NUMBER OF TIMES YOU WANT TO RUN THE PROGRAM:";
        cin>>choice;
        if(isdigit(choice[0])==true){
			progcount=stoi(choice);
            if(progcount>0){
                break;
            }
            else{
                cout<<"\nNUMBER MUST BE A POSITIVE INTEGER";
            }
        }
        else{
            cout<<"\nINVALID INPUT";  
        }
    }
    
    while(progcount){
        
        // cout<<"\nUNIT-TESTING CASE 5: NEGATIVE INPUT";
        // choice='-2';
        // cout<<"\nUNIT-TESTING CASE 6: 0 AS INPUT";
        // choice='0';
        // cout<<"\nUNIT-TESTING CASE 7: CHARACTER INPUT";
        // choice='#';
        
        cout<<"\nUNIT-TESTING CASE 8: VALID INPUT(USER CHOICE)";
        cout<<"\nENTER THE NUMBER OF TIMES YOU WANT TO GENERATE THE RANDOM NUMBERS FOR THE DICE:";
        cin>>choice;
        if(isdigit(choice[0])==true){
			numb=stoi(choice);
            if(numb>0){
                srand(time(0));
                cout<<"\nRANDOM NUMBERS GENERATED ARE AS FOLLOWS\n";
                while(numb--){
	                res=rand()%6+1;
            	    cout<<res<<endl;
                }
            }
            else{
                cout<<"\nNUMBER MUST BE A POSITIVE INTEGER";
            }
        }
        else{
            cout<<"\nINVALID INPUT";  
        }
        progcount--;
    }
    
	return 0;
}