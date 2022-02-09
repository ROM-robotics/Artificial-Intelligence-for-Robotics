p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['green','red']
z = 'red'
pHit = 0.6
pMiss = 0.2

def sense (p,z):
    q = []
    for i in range(len(p)):
        hit=(z==world[i])
        q.append(p[i]*(hit*pHit+(1-hit)*pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i]=q[i]/s
    return q
  
for k in range (len(measurements)):
    p = sense(p,measurements[k])
    print(p)
    
print(p)