import networkx as nx
import matplotlib.pyplot as plt

G = nx.fast_gnp_random_graph(10,0.45)
# adding nodes' labels
mapping = {0: 'a', 1: 'b', 2:'c', 3:'d', 4:'e', 5:'f',6:'g',7:'h',8:'i',9:'j'} # 0->'a' and 1->'b'
G = nx.relabel_nodes(G, mapping)
plt.plot()
nx.draw_networkx(G, with_labels=True)
plt.show()
