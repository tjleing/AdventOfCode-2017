#include <iostream>

#define LIST_SIZE 256

using namespace std;

int main() {
    int circular_list[LIST_SIZE];
    for(int i = 0; i<LIST_SIZE; ++i) {
        circular_list[i] = i;
    }

    // I did a quick pre-parse of the input file to replace the commas with spaces so that input was easier
    // In a contest or something, I'd probably do this question in python because that's how much I don't want to do C++ input
    
    int length, skipsize = 0, position = 0;
    while(cin >> length) {
        length--;
        // reverse sublist
        for(int i = 0; i<=length/2; ++i) {
            int temp = circular_list[(position+i)%LIST_SIZE];
            circular_list[(position+i)%LIST_SIZE] = circular_list[(position+length-i)%LIST_SIZE];
            circular_list[(position+length-i)%LIST_SIZE] = temp;
        }
        position += (length+1)+(skipsize++);
        position %= LIST_SIZE;
    }

    cout << circular_list[0] * circular_list[1] << endl;
}
