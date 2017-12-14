#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> instructions;
    int inst;
    while(cin >> inst) {
        instructions.push_back(inst);
    }

    int position = 0;
    int counter = 0;
    while(position >= 0 && position < instructions.size()) {
        instructions[position] += 1;
        position += instructions[position]-1;
        counter++;
    }
    cout << counter << endl;
}
