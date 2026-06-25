#include<bits/stdc++.h>
#define int long long
using namespace std;

int32_t main(){
    int n;cin>>n;
    vector<int>a(n);
    for(int i=0;i<n;i++){cin>>a[i];}

    sort(a.begin(), a.end());
    cout<<a[0]<<"\n"<<a[n-1];
    
}