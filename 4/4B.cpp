#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    string line;
    int total = 0;
    while(getline(cin, line)) {
        istringstream iss(line);
        string curr_word;
        unordered_set<string> word_set;
        bool is_valid = true;
        while(iss >> curr_word) {
            vector<char> word_vec;
            for(int i = 0; i<curr_word.length(); ++i) {
                word_vec.push_back(curr_word[i]);
            }
            sort(word_vec.begin(), word_vec.end());
            for(int i = 0; i<curr_word.length(); ++i) {
                curr_word[i] = word_vec[i];
            }

            if(word_set.find(curr_word) != word_set.end()) {
                is_valid = false;
                break;
            }

            word_set.insert(curr_word);
        }
        total += (is_valid ? 1 : 0);
    }
    cout << total << endl;
}
