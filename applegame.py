import math

ready=[0]*100000
value=[0]*100000
def solve(arr,su):
    if (su==0):
        return 0
    elif(ready[su] == 1):
        return value[su]
    else:
        best=math.inf
        for i in arr:
            if(i<=su):
                best=min(best, (solve(arr,(su-i))+1))
        value[su]=best
        ready[su]=1
        return best


if __name__ == '__main__':
    t=int(input())
    while(t>0):
        arr=list(map(int,input().split()))
        su=int(input())
        ans=solve(arr,su)
        print(ans)
        t-=1
