import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        if start == end: # If the start and end node are the same, return that node
            return [start]
        visited = [start] # Initialize a list to keep track of nodes we've visited
        queue = deque([(start, [])]) # Initialize a queue object to read in nodes and their neighbors. We also add the starting node to it 

        while queue: # Keep going until the queue is empty (which is when we reach the end of the graph)
            current_node, traversed_path = queue.popleft() # Remove the leftmost element from the queue, add it to the "current_node" variable for processing and track it in our path
            visited.append(current_node) # Note that we have visited the current node
            for neighbor in self.graph[current_node]: # Iterate over the neighboring nodes for the node we are currently visiting
                if neighbor == end: # If the neighbor we are iterating over is the end node, we stop, return our path, the node we are in, and the end node
                    return traversed_path + [current_node, neighbor]
                if neighbor in visited: # If the neighbor we are iterating over has already been visited, we skip through it
                    continue
                queue.append((neighbor, traversed_path + [current_node])) # Stack the iterated node and the path used to reach it onto the queue
                visited.append(neighbor) # Add the iterated node to our list of visited nodes
        if end is None: # There is no specified end node, thus we return the traversed path from the start node to the end of the graph
            return traversed_path
        if None: # There is an end node, but there is no path between it and the start node. We return None
            return None        

        





