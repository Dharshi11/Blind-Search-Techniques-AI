#function to get input from the user
#The function will return a dictionary with key values as nodes and values with
#list of tuples , tuples have the neighbouring nodes and their corresponding
#path cost.
def create_graph():
    n=int(input("Enter the number of nodes in the graph : "))
    graph={} #dictionary
    for i in range(n):
        a=input("Enter the parent node "+str(i+1)+" ")
        s=int(input("Enter the num of child nodes for the parent node "+a+" "))
        path_cost=[] 
        for j in range(s): #neighbouring nodes
            d1=input("Enter child node "+str(j+1)+" ")
            cost=int(input("Enter the corresponding path cost for node  "+d1+" "))
            path_cost.append((d1,cost))
        graph[a]=path_cost
    return graph

#function to calculate the total path cost of the path found by bfs traversal
#path found is given as input
#path is a list of tuples , tuples contains the nodes and their corresponding
#path cost.
def tot_pathcost_calculation(path):
    path_cost=0 #initial path cost assigned to 0
    for(edge,cost) in path: #(edge,cost) iterates through each tuple in list
        path_cost+=cost #cost is added to get total path cost
    return path_cost

# breadth first traversal function
# inputs : graph, source node and destination node
def bfs(graph,src,des):
    visited=[] #visited list
    queue=[[(src,0)]] #queue
    while queue:
        path=queue.pop(0) #pop the first element from queue andappend to path
        current_node=path[-1][0] #take the last node from path as current node
        visited.append(current_node) #append the current node to visited
        if current_node==des: #if goal reached
            path_cost=tot_pathcost_calculation(path)
            print("Path found : ",path)
            print("corresponding path cost for the obtained path : ",path_cost)
        else: #if goal not reached traverse to neighbouring nodes
            adjacent_nodes=graph.get(current_node,[])
            for (i,j) in adjacent_nodes:
                if i not in visited:
                    new_path=path.copy()
                    new_path.append((i,j))
                    queue.append(new_path)

# This how the graph structure will be that is returned by the create_graph function
##input_graph = {
##    'A': [('B',2),('C',3),('D',5)],
##    'B': [('E',4),('F',5)],
##    'C': [('G',1),('H',2)],
##    'D': [('H',5)],
##    'E': [],
##    'F': [],
##    'G': [],
##    'H': []
##}

#Driver code

#inputting a graph from user                    
input_graph=create_graph()
print("Breadth first search\n")
#getting source and destination
source=input("Enter the start node : ")
goal=input("Enter the goal node : ")
#bfs traversal
bfs(input_graph,source,goal)


