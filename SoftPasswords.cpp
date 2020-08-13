#include <iostream>
#include <sstream>

using namespace std;

bool identical(string S, string P){
    if(S.compare(P) == 0){
        return true;
    }
    else{
        return false;
    }
}

bool prepend(string S, string P){
    for(int i = 0; i<10; i++){
        string newstring = std::to_string(i)+P;
        if(newstring.compare(S) == 0){
            return true;
        }
        else{
            continue;
        }
    }
    return false;
}

bool append(string S, string P){
    for(int i = 0; i<10; i++){
        string newstring = P+std::to_string(i);
        if(newstring.compare(S) == 0){
            return true;
        }
        else{
            continue;
        }
    }
    return false;
}

bool reverse(string S, string P){
    for(int i=0; P[i]; i++){
		if (islower(P[i])){
            P[i] = toupper(P[i]);
            }
		else{P[i] = tolower(P[i]);}
    }
    if(P.compare(S) == 0){
        return true;
    }
    else{return false;}
}

int main(){
    string S;
    string P;
    cin >> S >> P;
    if(identical(S,P)){
        cout << "Yes" << endl;
        return 0;
    }
    if(prepend(S,P)){
        cout << "Yes" << endl;
        return 0;
    }
    if(append(S,P)){
        cout << "Yes" << endl;
        return 0;
    }
    if(reverse(S,P)){
        cout << "Yes" << endl;
        return 0;
    }
    cout << "No" << endl;
    return 0;
}