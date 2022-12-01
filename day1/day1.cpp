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

void update(priority_queue<int, vector<int>, greater<int>>* pq, int curr) {
    pq->push(curr);
    if (pq->size() > 3) {
        pq->pop();
    }
}
 
void solve() {
    int curr = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    forn(i, 2) skipline();
    string line;
    while (getline(cin, line)) {
        if (line.empty()) {
            update(&pq, curr);
            curr = 0;
        } else {
            curr += stoi(line);
        }
    }
    update(&pq, curr);
    int third = pq.top();
    pq.pop();
    int second = pq.top();
    pq.pop();
    int first = pq.top();
    cout << "Part 1: " << first << endl;
    cout << "Part 2: " << first + second + third << endl;
    
}
 
int main() {
    ios::sync_with_stdio(false);
    solve(); 
}