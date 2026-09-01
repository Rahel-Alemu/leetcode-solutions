from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m,n=len(classroom),len(classroom[0])
        L=[]; s=None
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S': s=(i,j)
                elif classroom[i][j]=='L': L.append((i,j))

        d={p:i for i,p in enumerate(L)}
        full=(1<<len(L))-1
        q=deque([(s[0],s[1],energy,0,0)])
        best={(s[0],s[1],0):energy}
        D=((1,0),(-1,0),(0,1),(0,-1))

        while q:
            r,c,e,mask,dist=q.popleft()
            if mask==full:
                return dist

            for dr,dc in D:
                x,y=r+dr,c+dc

                if not(0<=x<m and 0<=y<n) or classroom[x][y]=='X' or e==0:
                    continue

                ne=e-1
                nm=mask

                if classroom[x][y]=='L':
                    nm|=1<<d[x,y]
                elif classroom[x][y]=='R':
                    ne=energy

                k=(x,y,nm)

                if ne>best.get(k,-1):
                    best[k]=ne
                    q.append((x,y,ne,nm,dist+1))

        return -1