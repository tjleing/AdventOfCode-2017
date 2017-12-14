#include <iostream>
#include <vector>

#define LIST_SIZE 256

using namespace std;

string to_binary(int decimal) {
    string ret = "";
    ret = to_string(decimal % 2) + ret; decimal /= 2;
    ret = to_string(decimal % 2) + ret; decimal /= 2;
    ret = to_string(decimal % 2) + ret; decimal /= 2;
    ret = to_string(decimal % 2) + ret; decimal /= 2;
    ret = to_string(decimal % 2) + ret; decimal /= 2;
    ret = to_string(decimal % 2) + ret; decimal /= 2;
    ret = to_string(decimal % 2) + ret; decimal /= 2;
    ret = to_string(decimal % 2) + ret;
    return ret;
}

int main() {
    int num_used = 0;
    string in; cin >> in;
    for(int row = 0; row<128; ++row) {
        int circular_list[LIST_SIZE];
        for(int i = 0; i<LIST_SIZE; ++i) {
            circular_list[i] = i;
        }

        // well I had to put the commas back in :(
        
        string salted_in = in + "-" + to_string(row);
        vector<int> lengths;
        for(int i = 0; i<salted_in.length(); ++i) {
            lengths.push_back(int(salted_in[i]));
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
            hash += to_binary(total);
        }
        for(int i = 0; i<hash.size(); ++i) {
            if(hash[i] == '1') num_used++;
        }
    }


    cout << num_used << endl;
}
