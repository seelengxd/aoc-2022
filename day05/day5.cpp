#include "/Users/seelengxd/stdc++.h"

void skipline() {
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

void move(int count, stack<char>* c1, stack<char>* c2) {
    for (int i = 0; i < count; ++i) {
        char toMove = c1->top();
        c2->push(toMove);
        c1->pop(); 
    }
}

void solve() {
    string line;
    int part1 = 0, part2 = 0;
    int a, b, c;  
    string arr[8];

    // parsing picture
    for (int i = 0; i < 8; ++i) getline(cin, arr[i]);
    skipline();
    skipline();

    stack<char> part1stacks[10];
    stack<char> part2stacks[10];
    for (int i = 7; i > -1; --i) {
        for (int j = 1; j < 10; j++) {
            int index = 1 + (j - 1) * 4;
            if (index < arr[i].size()) {
                char c = arr[i][index];
                if (c != ' ') {
                    part1stacks[j].push(c);
                    part2stacks[j].push(c);
                }
            }
        }
    }

    // parsing moves
    while (scanf("move %d from %d to %d\n", &a, &b, &c) == 3) {
        move(a, &part1stacks[b], &part1stacks[c]);
        move(a, &part2stacks[b], &part2stacks[0]);
        move(a, &part2stacks[0], &part2stacks[c]);
    }

    cout << "Part 1: ";
    for (int i = 1; i < 10; ++i) {
        cout << part1stacks[i].top();
    }
    cout << endl;

    cout << "Part 2: ";
    for (int i = 1; i < 10; ++i) {
        cout << part2stacks[i].top();
    }
    cout << endl;
}

int main() {
    solve();
}