#include <iostream>
#include <vector>

#define LIST_SIZE 256

using namespace std;

string to_hex(int decimal) {
    string ret = "";
    if(decimal / 16 < 10) {
        ret += to_string(decimal/16);
    }
    else {
        ret += 'a'+(decimal/16-10);
    }
    if(decimal % 16 < 10) {
        ret += to_string(decimal%16);
    }
    else {
        ret += 'a'+(decimal%16-10);
    }
    return ret;
}

int main() {
    int circular_list[LIST_SIZE];
    for(int i = 0; i<LIST_SIZE; ++i) {
        circular_list[i] = i;
    }

    // well I had to put the commas back in :(
    
    string in; cin >> in;
    vector<int> lengths;
    for(int i = 0; i<in.length(); ++i) {
        lengths.push_back(int(in[i]));
    }
    lengths.push_back(17);
    lengths.push_back(31);
    lengths.push_back(73);
    lengths.push_back(47);
    lengths.push_back(23);
    
    int skipsize = 0, position = 0;
    for(int round = 0; round < 64; ++round) {
        for(int length_index = 0; length_index < lengths.size(); ++length_index) {
            int length = lengths[length_index];
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
    }

    string hash = "";
    for(int i = 0; i<16; ++i) {
        int total = circular_list[16*i];
        for(int j = 1; j<16; ++j) {
            total ^= circular_list[16*i+j];
        }
        hash += to_hex(total);
    }


    cout << hash << endl;
}
