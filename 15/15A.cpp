#include <iostream>

#define AMULT 16807
#define BMULT 48271
#define MOD 2147483647

using namespace std;

int main() {
    long long A, B; cin >> A >> B;
    int total = 0;
    for(long long i = 0; i<40000000; ++i) {
        A = A*AMULT % MOD;
        B = B*BMULT % MOD;
        if(A % 65536 == B % 65536) {
            total++;
        }
    }
    cout << total << endl;
}
