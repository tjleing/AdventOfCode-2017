#include <iostream>

using namespace std;

int main() {
    string in; cin >> in;
    int n = in.length();
    int total = 0;
    for(int i = 0; i<n-1; ++i) {
        if(in[i] == in[i+1]) {
            total += in[i]-'0';
        }
    }
    if(in[n-1] == in[0]) {
        total += in[0]-'0';
    }
    cout << total << endl;
}
