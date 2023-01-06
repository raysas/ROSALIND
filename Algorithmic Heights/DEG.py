'''
degree array
'''

def getEdges(file):
    '''takes a rosalind file and transforms it to an edges list'''
    f=open(file,'r')
    # a=f.readline()#1st line has vertices and edges count
    b=f.readlines()
    b=[e.split(' ') for e in b]
    return b


def getDegrees(E):
    '''
    takes an array of edges and returns an array of the degree of each element in the array
    '''
    deg=[0]*(int(E[0][0])) #number of vertices
    for e in range(1,len(E)):
        edge=E[e]
        #print(edge[0],edge[1])
        deg[int(edge[0])-1]+=1;deg[int(edge[1].strip())-1]+=1
    for i in range( len(deg)):
        print(deg[i],end=' ')

getDegrees(getEdges('e.txt'))