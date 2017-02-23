import random, string

class Graph(object):
	def __init__(self, v={}, e={}):
		self.vertices = v
		self.edges = e

	def insert_node(self, value):
		node = self.vertices.get(value)
		if not node:
			node = graphNode(value)
			self.vertices[node.value] = node
			return node
		else:
			return ValueError("Node, " + str(value) + ", already exists.")

	def insert_edge(self, value, nodeA_val, nodeB_val):
		nodeA_found = self.vertices.get(nodeA_val)
		nodeB_found = self.vertices.get(nodeB_val)
		if not nodeA_found:
			nodeA_found = self.insert_node(nodeA_val)
		if not nodeB_found:
			nodeB_found = self.insert_node(nodeB_val)
		new_edge = graphEdge(value, nodeA_found, nodeB_found, self.key_gen())
		nodeA_found.edges.append(new_edge.key)
		nodeB_found.edges.append(new_edge.key)
		self.edges[new_edge.key] = new_edge

	def key_gen(self):
		key = ''.join(
            random.choice(
                string.ascii_uppercase + string.digits) for x in xrange(32))
		if key in self.edges:
			return key_gen()
		else:
			return key


class graphNode(object):
	def __init__(self, value, edges=[]):
		self.value = value
		self.edges = edges

class graphEdge(object):
	def __init__(self, value, nodeA, nodeB, key):
		self.key = key
		self.value = value
		self.nodeA = nodeA
		self.nodeB = nodeB