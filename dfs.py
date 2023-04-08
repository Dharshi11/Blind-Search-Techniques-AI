def create_graph():# function to create data structure explained clearly in bfs.py
    n=int(input("Enter the number of nodes in the graph : "))
    graph={}
    for i in range(n):
        a=input("Enter the parent node "+str(i+1)+" ")
        s=int(input("Enter the num of child nodes for the parent node "+a+" "))
        path_cost=[]
        for j in range(s):
            path_cost1=[]
            d1=input("Enter child node "+str(j+1)+" ")
            cost=int(input("Enter the corresponding path cost for node  "+d1+" "))
            path_cost1.append(d1)
            path_cost1.append(cost)
            path_cost.append(tuple(path_cost1))
        graph[a]=path_cost
    return graph

def tot_pathcost_calculation(path):# function to calculate path cost
    path_cost=0
    for(edge,cost) in path:
        path_cost+=cost
    return path_cost
def dfs(stack,visited,graph,src,des,cost): # depth first search function 
    stack.append((src,cost)) #using stack data structure
    visited.append(src) #appending visited nodes
    if src==des: #goal
        path_cost=tot_pathcost_calculation(stack)
        print("Path found : ",stack)
        print("corresponding path cost for the obtained path : ",path_cost)
    adjacent_nodes=graph.get(src,[]) # if goal not reached traversing to neighboring nodes
    for (i,j) in adjacent_nodes:
                if i not in visited:
                    dfs(stack,visited,graph,i,des,j)#src node and cost is updated
#Driver code
input_graph=create_graph()
print("Depth First search\n")
stack=[]
visited=[]
cost=0
source=input("Enter the start node : ")
goal=input("Enter the goal node : ")
dfs(stack,visited,input_graph,source,goal,cost)
