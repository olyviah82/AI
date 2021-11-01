import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
from collections import deque
import sys
from typing import List, Set
G = nx.Graph()
G.add_node("sports_complex")
G.add_node("siwaka")
G.add_node("ph.1A")
G.add_node("mada")
G.add_node("parkinglot")
G.add_node("ph.1b")
G.add_node("stc")
G.add_node("phase2")
G.add_node("j1")
G.add_node("phase3")
G.nodes()

G.add_edge("sports_complex","siwaka",weight=450)
#siwaka
G.add_edge("siwaka","ph.1A",weight=10)
G.add_edge("siwaka","ph.1b",weight=230)
#ph.1A
G.add_edge("ph.1A","ph.1b",weight=100)
G.add_edge("ph.1A","mada",weight=850)
#ph.1b
G.add_edge("ph.1b","phase2",weight=112)
G.add_edge("ph.1b","stc",weight=50)
#stc
G.add_edge("stc","phase2",weight=50)
G.add_edge("stc","parkinglot",weight=250)
#phase2
G.add_edge("phase2","j1",weight=600)
G.add_edge("phase2","phase3",weight=500)
#phase3
G.add_edge("phase3","parkinglot",weight=350)
#j1
G.add_edge("j1","mada",weight=200)
#mada
G.add_edge("mada","parkinglot",weight=700)

#positions 
G.nodes['sports_complex']['pos']=(-3,1)
G.nodes['siwaka']['pos']=(-1,1)
G.nodes['ph.1A']['pos']=(0,1)
G.nodes['ph.1b']['pos']=(0,0)
G.nodes['phase2']['pos']=(1,0)
G.nodes['j1']['pos']=(2,0)
G.nodes['mada']['pos']=(3,0)
G.nodes['stc']['pos']=(0,-1)
G.nodes['phase3']['pos']=(2,-1)
G.nodes['parkinglot']['pos']=(2,-2)
#store all the positions 
node_pos = nx.get_node_attributes(G,'pos')
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"sports_complex","parkinglot")
print(route_bfs.visited)
route_list = route_bfs.visited
 #color the nodes in the route_bfs
node_col=['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges=list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)

def bfs(
    G: nx.Graph, destination: str, start: str = "sports_complex"
) -> (List[str], Set[str]):
    """
    Searches for a path from *destination* from *start* in the
    graph *G*. A path is a list of nodes from start you need to
    pass to reach destination. Returns the path and a set of
    nodes visited during the search
    """
    if start == destination:
        return []
    frontier = deque([start])
    explored = set()
    solution = []
    visited = set()
    while True:
        if not frontier:
            return []
        node = frontier.popleft()
        explored.add(node)
        solution.append(node)
        for adj in G.neighbors(node):
            visited.add(adj)
            if adj not in explored and adj not in frontier:
                if adj == destination:
                    return solution, visited
                frontier.appendleft(adj)


def ucs(
    G: nx.Graph, destination: str, start: str = "sports_complex"
) -> (List[str], Set[str]):
    """
    Searches for a path from *destination* from *start* in the
    graph *G* using Uniform Cost Search. A path is a list of nodes from start
    you need to pass to reach destination. Returns the path and a set of
    nodes visited during the search
    """

    distances = {
        "SportsComplex": 730,
        "Siwaka": 405,
        "Ph.1A": 380,
        "Ph.1B": 280,
        "STC": 213,
        "Phase2": 210,
        "J1": 500,
        "Phase3": 160,
        "Mada": 630,
        "Parking Lot": 0,
    }
    if start == destination:
        return []
    frontier = deque([start])
    explored = set()
    solution = []
    visited = set()
    while True:
        if not frontier:
            return []
        node = frontier.popleft()
        explored.add(node)
        solution.append(node)
        if node == destination:
            visited.add(node)
            return solution, visited
        neighbors_dist = {}
        for n in G.neighbors(node):
            visited.add(node)
            neighbors_dist[n] = distances[n]
        shortest_neighbour = min(neighbors_dist, key=lambda n: distances[n])
        frontier.appendleft(shortest_neighbour)
        neighbors_dist.clear()


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "bfs":
        path, visited = bfs(G, "STC")
    elif sys.argv[1] == "ucs":
        path, visited = ucs(G, "Parking Lot")
    else:
        path, visited = bfs(G, "STC")
    color_map = []
    # color nodes that have been visited red
    for node in G:
        if node in visited:
            color_map.append("#bb2205")
        else:
            color_map.append("#0e918c")
    nx.draw_networkx(
        G,
        node_pos,
        node_size=2000,
        node_color=color_map,
        edgelist=straight_edges,
    )
    edge_labels = []
    nx.draw_networkx_edge_labels(G, node_pos, path_names)

plt.axis('off')
plt.show()
