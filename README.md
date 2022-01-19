![BuildStatus](https://github.com/seba2550/project2/actions/workflows/test.yml/badge.svg)


# Project 2 (Breadth-first search)

This repository contains code for my implementation of the Breadth-First search (BFS) algorithm, along with some unit tests for the implementation. Briefly, the BFS algorithm is a traversing algorithm, wherein we start at a particular node and traverse the graph by layers, moving horizontally across these layers until we reach the end of the graph. The BFS algorithm has various real-world applications, including people searching in social networks, GPS navigation, and puzzle solving. 
<br>

This implementation has three possible outcomes, depending on the inputs given. The first scenario involves a start node, an end node, and a path between the two. In this case, the method will return the shortest path between the start and end node. The second scenario involves a start node, but no end node. For this case, the method will return a list of traversed nodes, from the start node to the end of the graph after having visited all nodes. The last scenario involves a start node and end node, but no possible path between the two nodes. In this last scenario, the method returns None.
<br>

I've included two unit tests for this implementation. Both are run on an example graph from [Rosalind](https://rosalind.info/problems/bfs/). 

<br>

![Rosalind_BFS_Graph](https://user-images.githubusercontent.com/36509785/150235753-2fe9ce8e-be91-4d5a-834b-302cbd581cb5.jpg)

The first test checks that all nodes in the graph are traversed, regardless of order. The second test checks that all three of the scenarios described above are handled correctly (start + end + path; start + path; start + end + no path). Both tests were built and tested using pytest in this repository.
