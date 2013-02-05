def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def make_graph(node_list):
 	G = {}
 	for node1, node2 in node_list:
 		make_link(G, node1, node2)
 	return G


test_nodes = [('a', 'g'), ('a', 'd'), ('b', 'f'), ('c', 'g'), 
			  ('g', 'd'), ('f', 'e'), ('e', 'h')]

G = make_graph(test_nodes)

def breadth_first_path(G, v1, v2):
	distance_from_start = {}
	open_list = [v1]
	distance_from_start[v1] = 0
	while len(open_list) > 0:
		current = open_list.pop(0)
		for neighbor in G[current].keys():
			if neighbor not in distance_from_start:
				distance_from_start[neighbor] = distance_from_start[current] + 1
				if neighbor == v2:
					return distance_from_start[neighbor]
				open_list.append(neighbor)
	return False

print breadth_first_path(G, 'a', 'c')