#include <iostream>

#define HALFGRID 250

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

    int maxval; cin >> maxval;

    int grid[2*HALFGRID][2*HALFGRID];
    for(int i = 0; i<2*HALFGRID; ++i) {
        for (int j = 0; j<2*HALFGRID; j++) {
            grid[i][j] = 0;
        }
    }
    
    grid[HALFGRID][HALFGRID] = 1;

    for(int i = 1; i</*4*HALFGRID*HALFGRID*/100; ++i) { // rough upper bound
        int total = 0;
        for(int i = -1; i<=1; ++i) {
            for(int j = -1; j<=1; ++j) {
                total += grid[x+HALFGRID+i][y+HALFGRID+j];
            }
        }
        grid[x+HALFGRID][y+HALFGRID] = total;
        cout << x << " " << y << " " << i << " " << squaresize << " " << total << endl;
        if(total > maxval) {
            cout << total << endl;
            break;
        }

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
}
