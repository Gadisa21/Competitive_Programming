#include<iostream>
// #include<bits/stdc++.h>
// #include<set>
#include<vector>
// #include<map>
#include<algorithm>
using namespace std;

#define ll long long
#define nl "\n"
#define ws " "
#define FASTIO ios_base::sync_with_stdio(false); cin.tie(NULL);
#define MOD 1000000007

bool comp (pair<int, int> l, pair <int, int> r) {
    return l.second < r.second;
}

int main () {
    int t;
    cin>>t;
    while (t--) {
        int n;
        cin>>n;
        vector <pair<int, int>> v (n);
        for (int i = 0; i < n; i++) {
            cin>>v[i].first;
            v[i].second = i;
        }
        sort (v.rbegin (), v.rend ());
        // for (auto e: v) {
        //     cout<<e.first<<ws<<e.second<<nl;
        // }
        // cout<<nl;
        for (int i = 0; i < n; i++) {
            v[i].first = i + 1;
        }
        sort (v.begin (), v.end (), comp);
        for (auto e: v) {
            cout<<e.first<<ws;
        }
        cout<<nl;
    }
    return 0;
}