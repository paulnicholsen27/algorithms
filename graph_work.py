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
			  ('g', 'd'), ('f', 'e'), ('e', 'h'), ('d', 'i'),
			  ('i', 'j'), ('j', 'c'), ('d', 'f')]

G = make_graph(test_nodes)

def breadth_first_path(G, v1, v2):
	'''takes as input a graph and two nodes,
	returns shortest path between nodes'''
	path_from_start = {}
	open_list = [v1]
	path_from_start[v1] = [v1]
	while len(open_list) > 0:
		current = open_list.pop(0)
		for neighbor in G[current].keys():
			if neighbor not in path_from_start:
				path_from_start[neighbor] = path_from_start[current] + [neighbor]
				if neighbor == v2:
					return path_from_start[neighbor]
				open_list.append(neighbor)
	return False, path_from_start,

def centrality(G, v):
	'''takes as input a graph and a node,
	returns average shortest path to all other
	nodes in the graph'''
	number_of_nodes = len(G)
	shortest_paths = breadth_first_path(G, v, '')[1] #finds all shortest paths by using non-existant v2
	return sum(len(val)-1 for val in shortest_paths.values()) / (len(shortest_paths) - 1.0) #subtract 1 for current node

print centrality(G, 'a')



