import hashlib
from bisect import bisect
from StorageNodes import *

class ConsistentHashing:

	def __init__(self):
		self.total_slots = 2^128
		self.storageNodes = StorageNodes()
		self.nodesToSlotMapping = {}
		self.filesToSlotMapping = {}

		self.nodeSlots = []
		self.fileSlots = []

		self.fileToNodeMapping = {}

		self.mapStorageNodesToSlot()

	def mapStorageNodesToSlot(self):
		for node in self.storageNodes.getNodes():
			slot = self.hashFn(node.nodeIp)
			self.nodesToSlotMapping[slot] = node.name
			self.nodeSlots.append((slot, node.name))

		self.nodeSlots.sort(key = lambda elem: elem[0])

	def hashFn(self, key):
		# Create a SHA256 hash object
		sha256_hash = hashlib.sha256()

		# Update the hash object with the input text encoded as bytes
		sha256_hash.update(key.encode('utf-8'))

		# Convert the hexadecimal hash to an integer
		int_hash = int(sha256_hash.hexdigest(), 16)

		return int_hash % self.total_slots

	def uploadFile(self, path):
		index = self.hashFn(path)
		self.filesToSlotMapping[index] = path
		self.fileSlots.append((index, path))

		self.assignNodeToFile(index)

		print("File {slot}:{path} assigned to StorageNode {name}".format(slot=index, path=path, name=self.nodesToSlotMapping[self.fileToNodeMapping[index]]))

	def assignNodeToFile(self, fileSlot):
		# nodeSlot = bisect(self.nodeSlots, fileSlot)
		# assignedNodeSlot = self.nodeSlots[nodeSlot % len(self.nodeSlots)] 

		assignedNodeSlot = None
		for nodeIdx, _ in self.nodeSlots:
			if nodeIdx > fileSlot:
				assignedNodeSlot = nodeIdx
				break
		else:
			assignedNodeSlot = self.nodeSlots[0][0]

		self.fileToNodeMapping[fileSlot] = assignedNodeSlot

	def removeNode(self, nodeName):
		print("\nRemoving Storage Node {name}".format(name=nodeName))

		#Find the node in the existingNodes
		pos, oldSlot = 0, 0
		for idx, nodeSlot in enumerate(self.nodeSlots):
			if nodeSlot[1] == nodeName:
				pos = (idx + 1) % len(self.nodeSlots)
				oldSlot = nodeSlot[0]
				break
		else:
			print("Storage Server {nodeName} not found".format(nodeName))
			return

		#Find the next storage node in position
		newSlot, newNode = self.nodeSlots[pos][0], self.nodeSlots[pos][1]
		print("Storage Node {nodeName} data would be assigned to node {newNode}".format(nodeName=nodeName, newNode=newNode))
		print("Assign files from storage slot {old} to {new}".format(old=oldSlot, new=newSlot))
		
		#Assign all the files from the removedNode to the next identifiedNode
		for fileSlot, nodeSlot in self.fileToNodeMapping.items():
			if nodeSlot == oldSlot:
				self.fileToNodeMapping[fileSlot] = newSlot
				print("\nFileslot {fileSlot} assigned the new node".format(fileSlot=fileSlot))

		#Remove the old slot from the StorageNodes
		del(self.nodeSlots[pos-1])
		self.storageNodes.removeNode(nodeName)

		#Print the new file to slot mapping
		print("\nUpdated assignment of files to Storage Nodes:")
		for fileSlot, fileName in self.fileSlots:
			print("File {slot}:{path} belongs to StorageNode {name}".format(slot=fileSlot, path=fileName, name=self.nodesToSlotMapping[self.fileToNodeMapping[fileSlot]]))

		print("\n Updated Storage nodes:")
		print(self.nodeSlots)


hashing = ConsistentHashing()
print("Storage Nodes position in the ring")
print(hashing.nodeSlots)
print("\n")

hashing.uploadFile('file123124.txt')
hashing.uploadFile('file123125.txt')
hashing.uploadFile('file123126.txt')
hashing.uploadFile('file123127.txt')
hashing.uploadFile('file123128.txt')
hashing.uploadFile('file123129.txt')
hashing.uploadFile('file123130.txt')
hashing.uploadFile('file123131.txt')

# 
hashing.removeNode('B')


