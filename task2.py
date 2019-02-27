# 1.1 Problems 1-3 (Python - part). Problem 1.2
import math
import operator

#denote V(G) and D(v)
D = {'v1':[["v2",5],["v3",2],["v4",4],["v5",8],["v6",12],["v7",10]],
     'v2':[["v1",5],["v3",3],["v4",5],["v5",9],["v6",13],["v7",11]],
     'v3':[["v1",2],["v2",3],["v4",2],["v5",6],["v6",10],["v7",8]],
     'v4':[["v1",4],["v2",5],["v3",2],["v5",4],["v6",8],["v7",6]],
     'v5':[["v1",8],["v2",9],["v3",6],["v4",4],["v6",4],["v7",2]],
     'v6':[["v1",12],["v2",13],["v3",10],["v4",8],["v5",4],["v7",3]],
     'v7':[["v1",10],["v2",11],["v3",8],["v4",6],["v5",2],["v6",3]]}
IValue = {}
#define f(value) function
def f(value):
    return pow(math.e, -value)

for node in D:
    IValue[node] = 0   #set I-value of a node to be zero
for node in D:
        #sort DS in descending order by d-values
    DS = sorted(D[node], key=lambda d: d[1], reverse=True)
    sum = 0
    index = len(D) - 1
    prevDistance = -1
    prev_I = -1

    while index > 0 :
        if DS[index-1][1] == prevDistance :
                curr_I = prev_I
        else :
                curr_I = f(DS[index-1][1])/(1+index)-sum

        IValue[DS[index - 1][0]] += curr_I
        sum += f(DS[index-1][1])/(index*(1+index))
        prevDistance = DS[index-1][1]
        prev_I = curr_I
        index = index -1
    IValue[node] += f(0) - sum
sumI = 0
for k, v in IValue.items():
    tmp = k[1:]
    sumI += v
    print('I(node %s) = %f' % (tmp, v))

print('SUM: %f' % (sumI))


