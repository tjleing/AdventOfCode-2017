#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int p) {
    for(int i = 2; i<=sqrt(p); ++i) {
        if(p % i == 0) return false;
    }
    return true;
}

int main() {
    int total = 0;
    for(int p = 108400; p<=125400; p+=17) {
        if(!isPrime(p)) {
            total++;
        }
    }
    cout << total << endl;
}
