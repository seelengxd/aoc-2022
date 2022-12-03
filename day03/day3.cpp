#include "/Users/seelengxd/stdc++.h"
 
typedef long long ll;
typedef pair<ll, ll> pll;
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
#define forkn(i,k,n) for(int i = k; i < int(n); ++i)
#define sz(a) int(a.size())
#define deb(x) cout << #x << " " << x << endl;
 
template<typename... T>
void read(T&... args){
    ((cin >> args), ...);
}
 
template<typename... T>
void write(T&&... args){
    ((cout << args << " "), ...);
}
 
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

void skipline() {
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}
 
int priority(char c) {
    if ('a' <= c) {
        return c - 'a' + 1;
    } else {
        return c - 'A' + 27;
    }
}
void part1() {
    string line;
    int part1 = 0;
    bool arr[53];
    while (getline(cin, line)) {
        memset(arr, false, sizeof(arr));      
        int n = line.size();
        forn(i, n / 2) {
            char c = line[i];
            int p = priority(c); 
            arr[p] = true;
        }
        forkn(i, n / 2, n) {
            char c = line[i];
            int p = priority(c); 
            if (arr[p]) {
                part1 += priority(c);
                break;
            }
        }       
    }
    cout << "Part 1: " << part1 << endl;
}
 
void part2() {
    string line, line1, line2;
    int part2 = 0;
    while (getline(cin, line) && getline(cin, line1) && getline(cin, line2)) {
        sort(line.begin(), line.end());
        sort(line1.begin(), line1.end());
        sort(line2.begin(), line2.end());
        vector<char> first_intersection;
        vector<char> second_intersection;
        set_intersection(line.begin(), line.end(), line1.begin(), line1.end(), back_inserter(first_intersection));
        set_intersection(line2.begin(), line2.end(), first_intersection.begin(), first_intersection.end(), back_inserter(second_intersection));
        part2 += priority(*second_intersection.begin());
    }
    cout << "Part 2: " << part2 << endl;
}

int main() {
    ios::sync_with_stdio(false);
    part2(); 
}