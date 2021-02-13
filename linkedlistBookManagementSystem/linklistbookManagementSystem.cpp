// CPP PROGRAM USING LINKLIST FOR BOOK MANAGEMENT SYSTEM
#include <iostream>
using namespace std;
#include <string>

typedef struct bookmanagementsystem{
	string bname;
	string bnameAuthor;
	struct bookmanagementsystem *next;
}NODE;

int i;


void create(NODE *head){
	NODE *newnode,*last;
	int n;
	string name, nameAuthor;
	cout<<"\nEnter The Number Of Book Records To Be Created Initially:";
	cin>>n;
	last=head;
	for(i=1;i<=n;i++){
		newnode=(NODE *)malloc(sizeof(NODE));
		newnode->next=NULL;
		cout<<"\nEnter The Name Of The Book:";
		cin>>name;
		newnode->bname=name;
		cout<<"\nEnter The Name Of The Author:";
		cin>>nameAuthor;
		newnode->bnameAuthor=nameAuthor;
		last->next=newnode;
		last=newnode;
	}
}


void insert(NODE *head, int pos, string name, string nameAuthor){
	NODE *newnode,*temp;
	for(temp=head,i=1;(temp!=NULL)&&(i<=pos-1);i++){
		temp=temp->next;
	}		
	if(temp==NULL){
		cout<<"\nInvalid Position:";
	}
	else{
		newnode=(NODE *)malloc(sizeof(NODE));	
		newnode->bname=name;
		newnode->bnameAuthor=nameAuthor;
		newnode->next=NULL;
		newnode->next=temp->next;
		temp->next=newnode;
	}
}


void deletebk(NODE *head, int pos){
	NODE *temp1,*temp2;
	for(temp1=head,i=1;(temp1!=NULL) && (i<=pos-1);i++){
		temp1=temp1->next;
	}
	if(temp1->next==NULL){
		cout<<"\nInvalid Position";
		return;
	}
	else{
		temp2=temp1->next;
		temp1->next=temp2->next;
		free(temp2);
	}
}


void search(NODE *head, string name){
	NODE *temp;
	int count=0;
	for(temp=head->next;temp!=NULL;temp=temp->next){
		if(temp->bname==name){
			cout<<"\n\nBOOK FOUND"<<endl;
			cout<<"\tBOOKS\t\tAUTHORS"<<endl;
			cout<<"\t"<<temp->bname;
			cout<<"\t\t"<<temp->bnameAuthor<<endl;
			count=0;
			break;
		}
		else{
			count=1;
		}
	}
	if(count==1){
		cout<<"\nBOOK NOT FOUND";	
	}
}




void display(NODE *head){
	NODE *temp1,*temp2;
	temp2=head->next;
	if(temp2==NULL){
		cout<<"\nNo Books To Display";
	}
	else{
		cout<<"\nThe Records Of The Books Are:\n"<<endl;
		cout<<"\tBOOKS\t\tAUTHORS"<<endl;
		for(temp1=temp2;temp1!=NULL;temp1=temp1->next){
			cout<<"\t"<<temp1->bname;
			cout<<"\t\t"<<temp1->bnameAuthor<<endl;	
		}
	}
}


int main(){
	NODE *head;
	string name, nameAuthor;
	string choice;
	int ch,pos;
	head=(NODE *)malloc(sizeof(NODE));
	head->next=NULL;
	do{
		cout<<"\n\nMENU";
		cout<<"\n1.CREATE LIST INITIALLY\n2.INSERT\n3.DELETE\n4.SEARCH\n5.DISPLAY\n6.QUIT";
		
//         cout<<"\nUNIT-TESTING CASE 1: NEGATIVE INPUT";
//         choice= "-2";
//         cout<<"\nUNIT-TESTING CASE 2: 0 AS INPUT";
//         choice="0";
//         cout<<"\nUNIT-TESTING CASE 3: 17>6 UNAVAILABE CHOICE AS INPUT";
//         choice="17";
//         cout<<"\nUNIT-TESTING CASE 4: CHARACTER INPUT";
//         choice="#";
        
        cout<<"\nUNIT-TESTING CASE 5: VALID INPUT(USER CHOICE)";
		cout<<"\nEnter Your Choice:";
	    cin>>choice;
		if(isdigit(choice[0])==true){
			ch=stoi(choice);
			switch(ch){
				case 1: create(head);
					display(head);
					break;
				
				case 2:	cout<<"\nEnter The Position AT Which You Want To Insert The Book:";
					cin>>pos;
					cout<<"\nEnter The Name Of The Book:";
					cin>>name;
					cout<<"\nEnter The Name Of The Author:";
					cin>>nameAuthor;
					insert(head,pos,name,nameAuthor);
					display(head);
					break;
				
				case 3: cout<<"\nEnter The Position AT Which You Want To Insert The Book:";
					cin>>pos;
					deletebk(head,pos);
					display(head);
					break;
					
				case 4:	cout<<"\nEnter The Name Of The Book You Want To Search:";
					cin>>name;
					search(head,name);
					break;
					
				case 5: display(head);
					break;
					
				case 6: exit(1);
				
				default:cout<<"\n\nENTER A VALID CHOICE";
			}
		}
		else{
		    cout<<"\nINVALID INPUT";
		}
	}while(1);
	return 0;
}
