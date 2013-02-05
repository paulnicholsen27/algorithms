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


test_cluster = [('a', 'g'), ('a', 'd'), ('b', 'f'), ('c', 'g'), 
			  ('g', 'd'), ('f', 'e'), ('e', 'h'), ('d', 'i'),
			  ('i', 'j'), ('j', 'c'), ('d', 'f')]

test_tree = [(1, 2), (1, 3),
            (2, 4), (2, 5),
            (3, 6), (3, 7),
            (4, 8), (4, 9),
            (6, 10), (6, 11)]



def breadth_first_path(node_list, v1, v2):
	'''takes as input a node list and two nodes,
	returns shortest path between nodes'''
	G = make_graph(node_list)
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
	return False, path_from_start

def centrality(node_list, v):
	'''takes as input a node list and a node,
	returns average shortest path to all other
	nodes in the graph'''
	G = make_graph(node_list)
	number_of_nodes = len(G)
	shortest_paths = breadth_first_path(node_list, v, '')[1] #finds all shortest paths by using non-existant v2
	return sum(len(val)-1 for val in shortest_paths.values()) / (len(shortest_paths) - 1.0) #subtract 1 for current node

def max_centrality(node_list, v):
	'''takes as input a node_list and a node,
	returns maximum shortest path length between 
	that node and all other nodes in graph'''
	G = make_graph(node_list)
	path_lengths = {}
	for node in G:
		path_lengths[node] = len(breadth_first_path(node_list, v, node)) - 1
	return max(path_lengths.values())


print max_centrality(test_tree, 11)

