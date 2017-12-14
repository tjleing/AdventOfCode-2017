#include <iostream>

using namespace std;

int main() {
    string in; cin >> in;
    bool negated = false, in_garbage = false;
    int depth = 0, total = 0;
    for(int i = 0; i<in.length(); ++i) {
        if(negated) {
            negated = false;
            continue;
        }
        if(in[i] == '!') {
            negated = true;
            continue;
        }
        if(in_garbage) {
            if(in[i] == '>') {
                in_garbage = false;
                continue;
            }
        }
        else {
            if(in[i] == '<') {
                in_garbage = true;
                continue;
            }
            else {
                if(in[i] == '{') {
                    depth++;
                    total += depth;
                }
                if(in[i] == '}') {
                    depth--;
                }
            }
        }
    }
    cout << total << endl;
}
