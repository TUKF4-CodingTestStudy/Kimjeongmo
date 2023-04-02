## 트럭 ##

n,w,l = map(int,input().split())

weight = list(map(int,input().split()))
bridge = [0] * w
time = 0
 
while bridge:
    time += 1
    bridge.pop(0)
    if weight:
        if sum(bridge) + weight[0] <= l:
            bridge.append(weight.pop(0))
        else:
            bridge.append(0)
print(time)