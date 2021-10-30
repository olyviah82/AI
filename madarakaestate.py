import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
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
plt.axis('off')
plt.show()
