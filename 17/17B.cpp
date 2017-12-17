#include <iostream>
#include <vector>

using namespace std;

int main() {
    int stepsize; cin >> stepsize;
    int position = 0;
    int zeroposition = 0;
    int ans = 0;
    for(int i = 1; i<=50000000; ++i) {
        position = (position + stepsize) % i;
        if(position < zeroposition) {
            zeroposition++;
        }
        if(position == zeroposition) {
            ans = i;
        }
        position++;
    }
    cout << ans << endl;
}
