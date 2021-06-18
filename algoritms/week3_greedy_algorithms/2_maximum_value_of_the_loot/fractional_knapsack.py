# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    for i in range(len(weights)):
        if capacity == 0:
            return value
        a = min(weights[i],capacity)
        value = value + a*values[i]/weights[i]
        weights[i] = weights[i]-a
        capacity = capacity - a
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    ans=[]
    w=[]
    v=[]
    for i in range(n):
        data = list(map(int, input().split()))
        ans.append((data[0], data[1]))
    ans.sort(key= lambda x: x[0]/x[1], reverse=True)
    for i in range(n):
        v.append(ans[i][0])
        w.append(ans[i][1])
    print(round(get_optimal_value(capacity, w, v), 4))
