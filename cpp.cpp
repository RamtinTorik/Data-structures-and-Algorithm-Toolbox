#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    map<pair<int,int>,int>m;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        int i;
        m.clear();//不要忘记清空 
        m[{0,0}]=0;
        int x=0,y=0;
        int ans=100000000;
        int beg=-1,end=-1;
        char s[200005];
        scanf("%s",s);
        for(i=1;i<=n;i++)
        {
            char c=s[i-1];
            if(c=='L')
            {
                x-=1;
            }
            else if(c=='R')
            {
                x+=1;
             } 
             else if(c=='U')
             {
                 y+=1;
             }
             else if(c=='D')
             {         
                 y-=1;
             }
             if(m.find({x,y})!=m.end())
             {
                 if(ans>i-m[{x,y}]+1)
                 {
                     ans=i-m[{x,y}]+1;//更新答案 
                     beg=m[{x,y}]+1;
                     end=i;
                     m[{x,y}]=i;
                 }
                 else
                 {
                     m[{x,y}]=i;//ans不必更新的话只更新这个点对应的值即可 
                 }
             }
             else
             {
                 m[{x,y}]=i;//之前没发现的话直接添加进字典 ，经过第i次操作到达(x,y) 
             }
        }
        if(ans!=99999999&&beg!=-1)cout<<beg<<' '<<end<<endl;
        else cout<<-1<<endl;
    }    
    return 0;
}