#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <deque>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
// const int N=5000;

int ncr(int n,int r){
    double ans = 1;
    for(int i=1;i<=r;i++){
        ans = ans * (n-i+1);
        ans = ans / i;
    }
    return (int)ans;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, r;
    cin>>n>>r;
    cout << ncr(n,r);
    return 0;
}