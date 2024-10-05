import sys
sys.stdin = open('C:\\Users\\DELL\\OneDrive\\Desktop\\PBL\\with_matrix\\user_input.txt','r')
sys.stdout = open('C:\\Users\\DELL\\OneDrive\\Desktop\\PBL\\with_matrix\\output.txt','w')
import networkx as nx
import matplotlib.pyplot as plt
#***********************************************************************************************************
def initial_graph() :
    n=int (input("\nenter number of nodes: "))
    e=int(input("\nenter number of edges: "))
    w=[[0 for j in range(0,n)] for i in range(0,n)] # #2d array for storing weighed adjecency matrix
    for j in range(0,e):
        b=int((input("\nenter the first node of edge: ")))
        c=int((input("\nenter the second node of edge: ")))
        d=int((input("\nenter the edge weights: ")))
        w[b][c]=d
        w[c][b]=d
    #print(w)
    A={}
    for i in range(n):
        G.add_node(i)
        A[i]={}
    for i in range(n):
        for j in range(n):
            if w[i][j]!=0:
                if j not in A[i]:
                    A[i][j]=w[i][j]
                    G.add_edge(i,j,weight=w[i][j])
                else:
                    A[i][j]+=w[i][j]
                    G.add_edge(i,j,weight=w[i][j])
    print('\n',A)
    print(w)
    return A
#************************************************************************************************************
G=nx.Graph()
path = {}
adj_node = {}
queue = []

graph = initial_graph()
pos = nx.circular_layout(G)
nx.draw_circular(G, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
offset = 0.08
for edge, weight in edge_labels.items():
    x = (pos[edge[0]][0] + pos[edge[1]][0]) / 2  # Average x-coordinate
    y = (pos[edge[0]][1] + pos[edge[1]][1]) / 2 + offset  # Average y-coordinate with offset
    plt.text(x, y, weight, ha='center', va='center')
# Show the plot
plt.axis('off')
#plt.show()
#**************************************************************************************************************
initial = int(input("enter the source node: "))
for node in graph:
    path[node] = float("inf")
    adj_node[node] = None
    queue.append(node)
path[initial] = 0
while queue:
    # find min distance which wasn't marked as current
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
        if path[queue[n]] < min_val:
            key_min = queue[n]  
            min_val = path[key_min]
    cur = key_min
    queue.remove(cur)
    print(cur)
    #print("here",graph[cur])
    for i in graph[cur]:
        alternate = graph[cur][i] + path[cur]
        if path[i] > alternate:
            path[i] = alternate
            adj_node[i] = cur
x = int(input("enter the destination node: "))
#************************************************************************************************************
print('\nThe path between source and destination node is: ')
print(x, end = '<-')
a=[]
a.append(x)
while True:
    x = adj_node[x]
    a.append(x)
    if x is None:
        print("")
        break
    print(x, end='<-')
#************************************************************************************************************
a.pop()
my_list=[]
for i in range(len(a)-1):
    my_tuple=(a[i], a[i+1])
    my_list.append(my_tuple)
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
offset = 0.08
for edge, weight in edge_labels.items():
    x = (pos[edge[0]][0] + pos[edge[1]][0]) / 2  # Average x-coordinate
    y = (pos[edge[0]][1] + pos[edge[1]][1]) / 2 + offset  # Average y-coordinate with offset
    plt.text(x, y, weight, ha='center', va='center')
plt.axis('off')
plt.pause(2)
for i in range(len(my_list)):
    show_graph=nx.draw_networkx_edges(G, pos=pos, edgelist=[my_list[i]], edge_color='red', width=2.0)
    plt.pause(1)
'''plt.subplot(1,1,1)
plt.G()
mng=plt.get_current_fig_manager()
mng.full_screen_toggle()'''
plt.show()