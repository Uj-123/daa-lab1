#bubble sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr=[64,34,25,12,22,11,90]
bubbleSort(arr)
print("sorted array:",arr)

#selection sort
def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
arr=[64,25,12,22,11]
selectionsort(arr)
print("sorted array:",arr)

#sequential search
def sequentialsearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
        return-1
arr=[10,20,30,40,50]
key=30

result=sequentialsearch(arr,key)
if result !=-1:
    print("Element found at index:",result)
else:
    print("Element not found")

# Rabin karp
def rabinkarp(text,pattern):
    d=256
    q=101
    m=len(pattern)
    n=len(text)
    p=0
    t=0
    h=1

    for i in range(m-1):
        h=(h*d)%q

    for i in range(m):
        p=(d*p+ord(pattern[i]))%q
        t=(d*t+ord(text[i]))%q

    for i in range(n-m+1):
        if p==t:
            if text[i:i+m]==pattern:
                print("Pattern found at index:",i)

    if i<n-m:
        t=(d*(t-ord(text[i])*h)+ord(text[i+m]))%q
        if t<0:
            t+=q

text="GEEKS FOR GEEKS"
pattern="GEEK"
rabinkarp(text,pattern)

#Travelling sales man problem
import itertools
import sys


def travelling_salesman(graph,start):
    n = len(graph)
    vertices=[i for i in range(n) if i != start]
    min_cost=sys.maxsize

    for perm in itertools.permutations(vertices):
        cost=graph[start][perm[0]]
        for i in range(len(perm)-1):
            cost+=graph[perm[i]][perm[i+1]]
        cost+=graph[perm[-1]][start]
        min_cost=min(min_cost,cost)

    return min_cost

graph=[
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

print("Minimum cost:",travelling_salesman(graph,0))


#Knap-sack problem
def knapsack(W,wt,val,n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w]=0
            elif wt[i-1]<=w:
                dp[i][w]=max(val[i-1],dp[i-1][w-wt[i-1]],
                             dp[i-1][w]
                             )
            else:
                dp[i][w]=dp[i-1][w]
            return dp[n][W]
val=[60,100,120]
wt=[10,20,30]
W=50
n=len(val)

print("Maximum value:",knapsack(W,wt,val,n))
