#include <iostream>
#include <cmath>

using namespace std;

int main(){
    long long n, b; // could be significantly larger than 4 bytes
    cin >> n >> b;

    if(n <= pow(2, (b+1)) - 1){
        // bit strings are either 1 or 0, so 2^b+1 power and then subtract 1. 
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
}
