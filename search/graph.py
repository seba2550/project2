import networkx as nx

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
        visited_nodes = [] # List to keep track of the nodes we have visited already
        queue = [] # List to use as a queue object for reading in nodes and their respective neighbors
        backtrace = [] # List to keep track of our path
        G = self.graph # Initialize the graph object

        queue.append(start) # Add the start node to our queue object 
        visited_nodes.append(start) # Add the start node to our list of nodes we have visited

        while queue: # This loop continues until the queue is empty
            current_node = queue.pop(0) # Remove the leftmost element from the queue, and establish it as the node we are currently looking at

            if current_node == end:
                return backtrace # There is an end node and a path from start node to end node. Return the path between them

            for neighbor in G[current_node]: # Iterate over the neighboring nodes of the node we are currently visiting
                if neighbor not in visited_nodes: # If the neighboring node has not been visited, add it to our list of visited nodes. Also enqueue it and keep track of it in our path
                    visited_nodes.append(neighbor)
                    queue.append(neighbor)
                    backtrace[neighbor] = current_node # Record the parent node for backtracing through the traversed path

        if end is None: # There is no end node. Return the order of traversal
            return backtrace 

        return None # There is an end node, but no path between the start and end. Return None

        





