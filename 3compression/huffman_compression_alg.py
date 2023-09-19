from abc import ABC, abstractmethod
from heapq import heappush, heappop


class HuffBaseNode(ABC):
    @abstractmethod
    def isLeaf(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass


# Define a Leaf node class
class HuffLeafNode(HuffBaseNode):
    def __init__(self, element, weight):
        self.element = element
        self.node_weight = weight

    def value(self):
        return self.element
    
    def get_weight(self):
        return self.node_weight
    
    def isLeaf(self):
        return True
    

# Define an Internal node class
class HuffInternalNode(HuffBaseNode):
    def __init__(self, left, right, weight):
        self.left_child = left
        self.right_child = right
        self.node_weight = weight

    def left(self):
        return self.left_child
    
    def right(self):
        return self.right_child
    
    def get_weight(self):
        return self.node_weight
    
    def isLeaf(self):
        return False
    

# class HuffTree:
#     def __init__(self, element=None, weight=None, left=None, right=None):
#         if element is not None and weight is not None:
#             self.root = HuffLeafNode(element, weight)
#         elif left is not None and right is not None and weight is not None:
#             self.root = HuffInternalNode(left, right, weight)

#     def root(self):
#         return self.root

#     def weight(self):
#         return self.root.weight()

#     def __lt__(self, other):
#         if self.weight() < other.weight():
#             return True
#         elif self.weight() == other.weight():
#             return False
#         else:
#             return False


# Define a Huffman Tree building function
def buildTree(weights):
     # Create leaf nodes for each element with their corresponding weights
    nodes = [HuffLeafNode(element, weight) for element, weight in weights.items()]

    # Create a min-heap using the nodes
    heap = []
    for node in nodes:
        heappush(heap, (node.get_weight(), id(node), node))

    # Build the Huffman tree
    while len(heap) > 1:
        weight1, _, node1 = heappop(heap)
        weight2, _, node2 = heappop(heap)
        internal_node = HuffInternalNode(node1, node2, weight1 + weight2)
        heappush(heap, (weight1 + weight2, id(internal_node), internal_node))

    return heap[0][2]  # Return the final tree


# Sample weights for each element
weights = {'A': 10, 'B': 15, 'C': 12, 'D': 3, 'E': 4, 'F': 13}

# Build the Huffman tree using the weights
huffman_tree = buildTree(weights)
print(huffman_tree)

# You can now use the huffman_tree object to navigate the tree and get the Huffman codes
# For demonstration, let's print the weights of the root and its children
print("Root weight:", huffman_tree.get_weight())
if isinstance(huffman_tree, HuffInternalNode):
    print("Left child weight:", huffman_tree.left().get_weight())
    print("Right child weight:", huffman_tree.right().get_weight())