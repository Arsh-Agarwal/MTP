#include <bits/stdc++.h>
using namespace std;
#define ld long double
#define ll long long

ld dmax = std::numeric_limits<long double>::max();
ll n;
vector<vector<ld>> dp;
vector<vector<ll>> back;
vector<vector<ld>> g;
ld rec(ll index, ll mask){
    if(mask == (1LL<<n)-1LL) return g[index][0];
    if(~back[index][mask]) return dp[index][mask];
    ld ans = dmax;
    ll choice = -1;

    for(ll i = 0; i < n; i++){
        if((mask>>i)&1LL) continue;
        ld temp = rec(i, mask|(1LL<<i)) + g[index][i];
        if(temp < ans) ans = temp, choice = i;
    }

    back[index][mask] = choice;
    return dp[index][mask] = ans;
}

int main(int argc, char* argv[]){
    // ifstream file("input.txt");
    ifstream file(argv[1]);
    file>>n;
    dp.resize(n, vector<ld>(1LL<<n, dmax));
    back.resize(n, vector<ll>(1LL<<n, -1));
    g.resize(n, vector<ld>(n));
    for(ll i = 0; i < n; i++) for(ll j = 0; j < n; j++) file>>g[i][j];

    ll index = 0, mask = 1LL;
    vector<ll> ans = {0};
    for(ll i = 0; i < n-1; i++){
        rec(index, mask);
        int choice = back[index][mask];
        ans.push_back(choice);
        mask |= (1LL<<choice);
        index = choice;
    }
    ans.push_back(0);
    for(auto it: ans) cout << it << ' '; cout << '\n';
    return 0;
}