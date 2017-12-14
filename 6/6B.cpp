#include <iostream>
#include <vector>
#include <set>

#define NUMBANKS 16

using namespace std;

vector<int> banks(NUMBANKS);

int indexOfMax() {
    int maxBlocks = -1, maxIndex = -1;
    for(int i = 0; i<NUMBANKS; ++i) {
        if(banks[i] > maxBlocks) {
            maxBlocks = banks[i];
            maxIndex = i;
        }
    }
    return maxIndex;
}

void redistribute(int index) {
    int toRedistribute = banks[index];
    banks[index] = 0;
    while(toRedistribute--) {
        index = (index+1) % NUMBANKS;
        banks[index]++;
    }
}

int main() {
    for(int i = 0; i<NUMBANKS; ++i) {
        cin >> banks[i];
    }

    bool keepGoing = true;
    set<vector<int> > alreadySeen;
    while(keepGoing) {
        int maxIndex = indexOfMax();
        redistribute(maxIndex);
        if(alreadySeen.find(banks) != alreadySeen.end()) {
            keepGoing = false;
        }
        alreadySeen.insert(banks);
    }

    keepGoing = true;
    int cycles = 0;
    vector<int> tempbanks(NUMBANKS);
    tempbanks = banks;
    do {
        int maxIndex = indexOfMax();
        redistribute(maxIndex);
        bool isSame = true;
        for(int i = 0; i<NUMBANKS; ++i) {
            if(banks[i] != tempbanks[i]) {
                isSame = false;
            }
        }
        if(isSame) {
            keepGoing = false;
            cout << cycles+1 << endl;
        }
        cycles++;
    } while(keepGoing);
}
