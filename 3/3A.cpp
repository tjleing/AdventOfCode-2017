#include <iostream>

using namespace std;

int main() {
    /*
     * 17  16  15  14  13
     * 18   5   4   3  12
     * 19   6   1   2  11
     * 20   7   8   9  10
     * 21  22  23---> ...
    */
    int x = 0, y = 0;

    int dx = 1, dy = 0;
    int squaresize = 0;

    int maxi; cin >> maxi;

    for(int i = 1; i<maxi; ++i) {
        if(i == (2*squaresize+1)*(2*squaresize+1)) {
            squaresize++;
            // grow the square every time we reach the bottom-left corner
        }

        if(dx != 0 && abs(x) == squaresize) {
            switch(dx) {
                case -1:
                    dx = 0; dy = -1; break;
                case 1:
                    dx = 0; dy = 1; break;
            }
        }
        else if(dy != 0 && abs(y) == squaresize) {
            switch(dy) {
                case -1:
                    dx = 1; dy = 0; break;
                case 1:
                    dx = -1; dy = 0; break;
            }
        }

        x += dx;
        y += dy;
    }

    cout << abs(x) + abs(y) << endl;
}
