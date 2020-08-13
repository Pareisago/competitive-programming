#include<iostream>
#include<cmath>
#include <iomanip>

using namespace std;

int main() {
    long double answer = 0;
    long double current = 1;

    int n;
    cin >> n;
    for(int i = 1; i <= n+1; i++) {
        answer += 1 / current;
        current *= i;
    }

    cout << fixed;
    cout.precision(16);
    cout << answer << endl;
}