#include<bits/stdc++.h>
using  namespace std;
void BFS (vector<int>adj[],int node,vector<int>&vis)
{
	queue<int>q;
	q.push(node);
	vis[node]=1;
	while(!q.empty())
	{
		int top=q.front();
		cout<<top<<" ";
		q.pop();
		for(auto it:adj[top])
		{
			if(!vis[it])
			{
				q.push(it);
				vis[it]=1;
			}
		}
	}
}
int main()
{
	int n,e;
	cin>>n>>e;
	vector<int>adj[n+1];
	for(int i=0;i<e;i++) // Corrected 'o' to '0' here
	{
		int u,v;
		cin>>u>>v;
		adj[u].push_back(v);
		adj[v].push_back(u);
		
	}
	vector<int>vis(n+1,0);
	BFS(adj,1,vis);
	
}

