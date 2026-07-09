// g++ prim/main.cpp

#include<bits/stdc++.h>
#define int long long
using namespace std;

int32_t main(){
    int n;//cin>>n;
    n=1e4;

    vector<bool>isp(n, true);
    isp[0]=false;
    isp[1]=false;

    for(int p=2;p*p<=n;p++){
        if(isp[p]){
            for(int m=p*p;m<n;m+=p){
                isp[m]=false;
            }
        }
    }

    int cnt=0;

    for(int i=0;i<(int)isp.size();i++){
        if(isp[i]){
            cout<<i<<"\n";
            cnt++;
        }
    }

    cout<<"\n"<<cnt<<" prims.";

}