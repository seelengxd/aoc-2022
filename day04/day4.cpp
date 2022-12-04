#include "/Users/seelengxd/stdc++.h"
 
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void solve() {
    string line;
    int part1 = 0, part2 = 0;
    int a, b, c, d;  
    while (scanf("%d-%d,%d-%d\n", &a, &b, &c, &d) == 4) {
        if (a <= c && d <= b || c <= a && b <= d) part1++;
        if (a > c) {
            swap(&a, &c);
            swap(&b, &d);
        }
        if (c <= b) part2++;
    }

    cout << "Part 1: " << part1 << endl;
    cout << "Part 2: " << part2 << endl;
}

int main() {
    solve();
}