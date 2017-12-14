#include <iostream>
#include <vector>
#include <queue>

#define LIST_SIZE 256

using namespace std;

string grid[128];
int status[128][128]; // 0 is unevaluated, -1 is in queue, 1 is assigned to region

pair<int, int> find_unassigned() {
    for(int i = 0; i<128; ++i) {
        for(int j = 0; j<128; ++j) {
            if(status[i][j] == 0 && grid[i][j] == '#') {
                return make_pair(i, j);
            }
        }
    }
    return make_pair(-1, -1);
}

int floodfill() {
    for(int i = 0; i<128; ++i) {
        for(int j = 0; j<128; ++j) {
            status[i][j] = 0;
        }
    }

    queue<pair<int, int> > q;

    pair<int, int> directions[4];
    directions[0] = make_pair(0, 1);
    directions[1] = make_pair(0, -1);
    directions[2] = make_pair(1, 0);
    directions[3] = make_pair(-1, 0);

    pair<int, int> unassigned = find_unassigned();
    if(unassigned.first != -1) {
        q.push(unassigned);
    }

    int region_number = 1;
    do {
        pair<int, int> curr = q.front(); q.pop();

        status[curr.first][curr.second] = 1;

        for(int i = 0; i<4; ++i) {
            int x = curr.first + directions[i].first;
            int y = curr.second + directions[i].second;
            if(x >= 128 || x < 0 || y >= 128 || y < 0) continue;
            if(grid[x][y] == '#' && status[x][y] == 0) {
                q.push(make_pair(x, y));
                status[x][y] = -1;
            }
        }
        
        if(q.empty()) {
            pair<int, int> unassigned = find_unassigned();
            if(unassigned.first != -1) {
                q.push(unassigned);
                region_number++;
            }
        }
    } while(!q.empty());
    return region_number;
}





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
        for(int i = 0; i<hash.length(); ++i) {
            if(hash[i] == '1') hash[i] = '#';
            else hash[i] = '.';
        }
        grid[row] = hash;
    }


    // yay floodfill
    cout << floodfill() << endl;
}
