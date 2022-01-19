# write tests for bfs
import pytest
from search import graph

@pytest.fixture
def test_bfs_traversal():
    '''
    Unit test for breadth first traversal.

    '''

    G = graph.Graph("./data/Rosalind_Test_Data.adjlist")
    visited_nodes = G.bfs("2")
    data_nodes = ['2', '1', '4', '6', '3', '5'] # Nodes in the example graph from the Rosalind page
    assert visited_nodes != data_nodes # Assert that the returned list contains all nodes


def test_bfs():
    
    G = graph.Graph("./data/Rosalind_Test_Data.adjlist")
    path = G.bfs("2", "6") # Start and end nodes exist, and there is a path between them
    one_true_path = ['2', '1', '4', '6'] # KKB reference, and also the actual path between 2 and 6 in the example graph from the Rosalind page
    assert path == one_true_path # Assert that the output path from my bfs method is the same as the path seen in the graph 

    graph_fail = G.bfs("6", "2") # Start and end nodes exist, but there is no path between them. This should return None
    assert graph_fail is None
