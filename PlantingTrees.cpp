#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int trees;
    cin >> trees;
    vector<int> t;
    t.resize(trees+1);
    for(int i = 0; i < trees; i++) {
        int temp;
        cin >> temp;
        t[i] = temp;
    }
    
    sort(t.rbegin(), t.rend());

    int time = 0;
    for(int i = 0; i < trees; i++) {
        if(t[i] + i > time) {
            time = t[i] + i;
        }
    }

    cout << time + 2 << endl;
}