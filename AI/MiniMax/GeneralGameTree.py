import math

# Define the game tree as a list of nodes (example tree)
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

# Minimax function for game tree
def minimax_tree(node, is_max):
    # Base case: if the node is a leaf node (no children), return its value
    if not node.children:
        return node.value

    if is_max:
        best = -math.inf
        for child in node.children:
            best = max(best, minimax_tree(child, False))  # Minimize for the opponent
        return best
    else:
        best = math.inf
        for child in node.children:
            best = min(best, minimax_tree(child, True))  # Maximize for the player
        return best

# Example game tree
leaf1 = Node(3)
leaf2 = Node(5)
leaf3 = Node(2)
leaf4 = Node(9)

node1 = Node(0, [leaf1, leaf2])
node2 = Node(0, [leaf3, leaf4])

root = Node(0, [node1, node2])

# Get the optimal strategy
result = minimax_tree(root, True)  # True indicates that it's the maximizer's turn (Player A)
print(f"Optimal strategy value: {result}")
