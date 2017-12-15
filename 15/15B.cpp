#include <iostream>

#define AMULT 16807
#define BMULT 48271
#define MOD 2147483647

using namespace std;

int main() {
    long long A, B; cin >> A >> B;
    int total = 0;
    for(long long i = 0; i<5000000; ++i) {
        do {
            A = A*AMULT % MOD;
        } while(A % 4 != 0);
        do {
            B = B*BMULT % MOD;
        } while(B % 8 != 0);
        if(A % 65536 == B % 65536) {
            total++;
        }
    }
    cout << total << endl;
}
