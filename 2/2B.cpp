#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    string line;
    int total = 0;
    while(getline(cin, line)) {
        istringstream iss(line);
        int curr_num;
        vector<int> vec;
        while(iss >> curr_num) {
            vec.push_back(curr_num);
        }
        for(int i = 0; i<vec.size(); ++i) {
            for(int j = 0; j<vec.size(); ++j) {
                if(i == j) continue;
                if(vec[i] % vec[j] == 0) {
                    total += vec[i] / vec[j];
                    // oh no O(n^2)
                    // luckily the input is really small
                }
            }
        }
    }
    cout << total << endl;
}
