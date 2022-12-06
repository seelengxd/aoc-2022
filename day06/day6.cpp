#include "/Users/seelengxd/stdc++.h"
 
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int char_to_index(char c) {
    return c - 'a';
}

int detect_start_marker(string line, int window_size) {
    int arr[26];
    int unique = 0, n = line.size();;
    memset(arr, 0, sizeof(arr));
    for (int i = 0; i < window_size; i++) { 
        if (!arr[char_to_index(line[i])]) unique++;
        arr[char_to_index(line[i])]++;
    }
    if (unique == window_size) {
        return 4;
    }
    for (int i = window_size; i < n; i++) {
        arr[char_to_index(line[i - window_size])]--;
        if (!arr[char_to_index(line[i - window_size])]) unique--;
        if (!arr[char_to_index(line[i])]) unique++;
        arr[char_to_index(line[i])]++;
        if (unique == window_size) {
            return i + 1;
        }
    }
}

void solve() {
    string line;
    int part1 = 0, part2 = 0;
    int window_size = 14;
    getline(cin, line);
    
    cout << "Part 1: " << detect_start_marker(line, 4) << endl;
    cout << "Part 2: " << detect_start_marker(line, 14) << endl;
}

int main() {
    solve();
}