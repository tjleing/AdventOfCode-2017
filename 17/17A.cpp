#include <iostream>
#include <vector>

using namespace std;

int main() {
    int stepsize; cin >> stepsize;
    vector<int> buffer;
    int position = 0;
    for(int i = 0; i<=2017; ++i) {
        if(buffer.size() == 0) {buffer.push_back(0);}
        else {
            position = (position + stepsize) % buffer.size();
            buffer.insert(buffer.begin()+position+1, i);
            position++;
        }
    }
    cout << buffer[position+1] << endl;
}
