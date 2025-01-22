class StorageNode:
	def __init__(self, name, nodeIp):
		self.name = name
		self.nodeIp = nodeIp

	def __repr__(self):
		return "Node " + self.name + ", Ip: " + self.nodeIp

class StorageNodes:
	nodes = [
		StorageNode('A', '10.131.213.12'),
		StorageNode('B', '10.131.217.11'),
		StorageNode('C', '10.131.142.46'),
		StorageNode('D', '10.131.114.17'),
		StorageNode('E', '10.131.189.18')
	]

	def getNodes(self):
		return self.nodes

	def displayNodes(self):
		print("Storage Nodes configured are:\n")
		for node in self.nodes:
			print(node)

	def addNode(self, name, nodeIp):
		print("\nAdding node {}", name)
		self.nodes.append(StorageNode(name, nodeIp))
		self.getNodes()

	def removeNode(self, name):
		# print("\nTrying to delete node {}", name)
		for node in self.nodes:
			if node.name == name:
				self.nodes.remove(node)
				self.getNodes()
				break
		else:
			print("Node not found")

# nodes = StorageNodes()
# nodes.getNodes()

# nodes.addNode('T', '10.131.156.33')

# nodes.removeNode('B')
# nodes.removeNode('Q')

