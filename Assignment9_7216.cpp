#include<bits/stdc++.h>
using namespace std;


class Node {
public:
    int PRN;
    string Name;
    Node *next;
public:
    Node(int prn, string name){
        PRN=prn; Name=name; next=nullptr;
    }
    Node (int prn, string name, Node *ptr){
        PRN=prn; Name=name; next=ptr;
    }


};


Node* create (Node *head, int n){
    vector<pair<int, string>>v(n);
    // int arr[n];
    cout<<"Now enter the Data for each member of club as\n<PRN> <name>\n";
    for(int i=0; i<n; i++){
        cin>>v[i].first >>v[i].second;
    }
    int x=0;
    Node *ptr = new Node(v[x].first, v[x].second);
    head=ptr; 
    x++;
    Node *t=head;
    while(x<n){
        ptr=new Node(v[x].first, v[x].second);
        t->next=ptr;
        t=t->next;
        x++;
    }

    return head;
}

Node* insertToLL(Node* head, int pos){
    if(pos==1){
        Node* ptr= head;
        cout<<"Enter the PRN and Name";
        int prn=0;  string name;
        cin>>prn>>name;
        ptr=new Node(prn, name, nullptr );
        ptr->next= head;
        head=ptr;

    }
    else {
        Node* ptr= head;
        cout<<"Enter the PRN and Name";
        int prn=0;  string name;
        cin>>prn>>name;
        ptr=new Node(prn, name, nullptr );
        Node * t= head;
        pos-=2;
        while(pos--){
            t=t->next;

        }
        ptr->next=t->next;
        t->next=ptr;
    }
    return head;
}

Node* deleteFromLL (Node *head, int pos){
    if(head==nullptr)cout<<"Empty Linked List. Can't perform deletion operation.\n";
    if(pos==1){
        Node*ptr= head;
        head=head->next;
        delete ptr;
    }
    else{
        Node*ptr= head;
        Node*t =head;
        pos-=2;
        while (t!=nullptr && pos-- ){
            t=t->next;
        }
        if(t->next!=nullptr){
            ptr=t->next;
            t->next= ptr->next;
            delete ptr;
        } 
        else {
            cout<<"No Such Node Exist.\n";
        }
    }

    return head;
}




void count (Node *head){
    Node *t;
    t=head;
    int  x=0;
    while(t!=nullptr){
        // cout<<t->PRN<<":"<<t->Name<<" -> ";
        t=t->next;
        x++;
    }
    cout<<x<<endl;
    
}

void display (Node *head){
    Node *t;
    t=head;
    while(t!=nullptr){
        cout<<t->PRN<<":"<<t->Name<<" -> ";
        t=t->next;
    }
    cout<<endl;
    
}

void displayreverse (Node *temp){
    
    if(temp->next!=nullptr)displayreverse(temp->next);
    cout<<temp->PRN<<":"<<temp->Name<<" -> ";
        
    
}



int main(){
    Node* head;
    Node* head2;
//     Node *ptr = new Node(5);
//     head=ptr;
//     ptr=new Node(2);
//     head->next=ptr;
//     ptr=new Node(3);
//     head->next->next=ptr;
//     ptr=new Node(4);
//     head->next->next->next=ptr;

//     Node *t;
//     t=head;
//     while(t!=nullptr){
//         cout<<t->data<<"  ";
//         t=t->next;
//     }
//     cout<<"\n END \n";

    while (true)
    {
        /* code */
        cout<<"1. Create list for 'Pinnacle Club ' (input PRN, Name)\n";
        cout<<"2. Add President to the Linked List\n";
        cout<<"3. Insert Secretary to the Linked List\n";
        cout<<"4. Add member to the Linked List\n";
        cout<<"5. Delete President from the Linked List\n";
        cout<<"6. Delete Secretary from the Linked List \n";
        cout<<"7. Delete any member from the Linked List \n";
        cout<<"8. Count Number of Students in the Club\n";
        cout<<"9. Display all the members of the Club\n";
        cout<<"10. Display all the members of the Club in Reverse Order\n";
        cout<<"11. To Concat two Linked Lists\n";
        cout<<"12. To Exit...\n";
        int a=0; cin>>a;
        if(a==1){
            int n=0; cout<<"Enter the number of terms:";cin>>n;

            head = create(head, n);
        }
        else if(a==2){

            head= insertToLL(head,1);
        }
        else if(a==3){
            head = insertToLL(head,2);

        }
        else if(a==4){
            int pos; cout<<"Enter the position:"; cin>>pos;
            head= insertToLL(head, pos);

        }
        else if(a==5){
            head= deleteFromLL(head,1);
        }
        else if(a==6){
            head= deleteFromLL(head,2);
        }
        else if(a==7){
            int pos; cout<<"Enter the position:"; cin>>pos;
            head= deleteFromLL(head,pos);
        }
        else if(a==8){
            count(head);
        }
        else if(a==9){
            display(head);
        }
        else if(a==10){
            Node*temp= head;
            displayreverse(temp);
            cout<<endl;
        }
        else if(a==11){
            cout<<"PLease provide input for 2nd linked list:\n";
            int n=0; cout<<"Enter the number of terms:";cin>>n;

            head2 = create(head2, n);
            
            Node* temp= head;
            while(temp->next !=nullptr){
                temp=temp->next;
            }
            temp->next=head2;

            cout<<"The linked List after Concatenation is: \n ";
            display(head);

        }
        else if(a==12){
            cout<<"Exiting the Program";
            break;
        }

        
        // else if(a==);
        // else if(a==);
        // else if(a==);
        // else if(a==);

        else {
            cout<<"Invalid Input ... \nTry Again ";
        }

    }
}


