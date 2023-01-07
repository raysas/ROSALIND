'''double degree array''' 

def getEdges(file):
    '''takes a rosalind file and transforms it to an edges list'''
    f=open(file,'r')
    # a=f.readline()#1st line has vertices and edges count
    b=f.readlines()
    b=[e.split(' ') for e in b]
    c=[]
    for item in b:
        c.append([int(item[0]),int(item[1].strip())])
    return c

def getGraph(E):
    '''takes array of edges and returns the adjacency list representation of this graph D=(V,E) s.t V=1...n and E[0]=[n,len(edges)] '''
    adj_list=[[] for x in range(int(E[0][0])+1)]
    for i in range(1,len(E)):
        e=E[i]
        # print(e[0],e[1])
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
        # print(adj_list[e[0]])
    adj_list=adj_list[1:]
    return adj_list

def getDoubleDegree(G):
    '''takes an adjacency list representation of a graph and returns an array D[1..n] where D[i] is the sum of the degrees of i's neighbors'''
    # print(G)
    D=[0 for x in range(len(G))]
    for i in range(len(G)):
        for j in G[i]:
            D[i]+=len(G[j-1])

    return D

def printArray(a):
    for i in a:
        print(i,end=' ')

e=getEdges("rosalind_ddeg.txt")
g=getGraph(e)
D=getDoubleDegree(g)
printArray(D)