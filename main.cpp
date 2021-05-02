#include<iostream>
#include<string>
#include<map>
using namespace std;

void display(string s[], int size){
    for(int i = 1; i<size; i++){
        if(i<size-1){
            cout<<s[i]<<", ";
        }
        if(i == size-1){
            cout<<s[i];
        }
    }
    cout<<endl;
}

string mapping(string s[],int size){

    string toString[size];
    map<char,string> m;
    m['0'] = "Zero"; m['1'] = "One";
    m['2'] = "Two"; m['3'] = "Three";
    m['4'] = "Four"; m['5'] = "Five";
    m['6'] = "Six"; m['7'] = "Seven";
    m['8'] = "Eight"; m['9'] = "Nine";
   
    for(int i =0; i<size; i++){
        string final = "";
        for(int j = 0; j<s[i].length(); j++){
            char d = s[i][j];
            final += m[d];
        }
        toString[i] = final;
    }
    display(toString,size);
}

int main(int argc, char* argv[]){
    // int a[] = {10, 300, 5};
    int size = argc;
    string s[size];
    for(int i = 1; i<size; i++){
        s[i] = argv[i];
    }
    mapping(s,size);
    
}