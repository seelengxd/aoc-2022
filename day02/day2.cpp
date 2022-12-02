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
 
int score(int a, int b) {
    if ((b - a + 3) % 3 == 1) {
        return 6;
    } else if (a == b) {
        return 3;
    } else {
        return 0;
    }
}

void solve() {
    string line;
    int a, b, part1 = 0, part2 = 0;
    while (getline(cin, line)) {      
        a = line[0] - 'A';
        b = line[2] - 'X';
        part1 += score(a, b) + b + 1;
        forn(i, 3) if (score(a, i) == b * 3) part2 += score(a, i) + i + 1;     
    }
    cout << "Part 1: " << part1 << endl;
    cout << "Part 2: " << part2 << endl;
}
 
int main() {
    ios::sync_with_stdio(false);
    solve(); 
}