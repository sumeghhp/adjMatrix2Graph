import pandas
import networkx
import matplotlib.pyplot as plt
import csv
input_data = pandas.read_csv('test.csv', index_col=0)
G1 = networkx.DiGraph(input_data.values)
networkx.write_edgelist(G1, "test.edgelist")
fh=open("test.edgelist", 'rb')
G1=networkx.read_edgelist(fh,create_using=networkx.DiGraph(), nodetype=int)
pos = networkx.spring_layout(G1,scale=2)
networkx.draw(G1, pos, with_labels=True,arrow=True,node_shape="o")
node_labels = networkx.get_node_attributes(G1,'weight')
networkx.draw_networkx_labels(G1, pos, labels = node_labels)
edge_labels = networkx.get_edge_attributes(G1,'weight')
networkx.draw_networkx_edge_labels(G1, pos, labels = edge_labels, font_size=6)
plt.show()
