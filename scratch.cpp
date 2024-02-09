#include<iostream>

#include<bits/stdc++.h> 
#include <vector>
#define ll long long

bool comp(const vector<string>& a, const `vector<string>& b){
    return a[1]<b[1];   
}

vector<vector<string>> extractErrorLogs(vector<vector<string>>& logs){
    sort(logs.begin(), logs.end(), comp);
    return logs;
}

int main(){
    int n, m;
    cin>>n>>m;
    vector<vector<string>> logs(n, vector<string>(m));
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin>>logs[i][j];
        }
    }
    
    vector<vector<string>> ans;
    ans=extractErrorLogs(logs);
    
    for(int i=0; i<3; i++){
        for(int j=0; j<4; j++){
            cout<<ans[i][j]<<" ";
        }
        
        cout<<endl;
    }
    
    
}