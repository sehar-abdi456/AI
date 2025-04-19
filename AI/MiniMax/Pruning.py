import math

# Define the game tree as a list of nodes (example tree)
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

# Minimax with Alpha-Beta Pruning function
def minimax_with_alpha_beta(node, alpha, beta, is_max):
    # Base case: if the node is a leaf node (no children), return its value
    if not node.children:
        return node.value

    if is_max:
        best = -math.inf
        for child in node.children:
            best = max(best, minimax_with_alpha_beta(child, alpha, beta, False))  # Minimize for the opponent
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Prune the branch
        return best
    else:
        best = math.inf
        for child in node.children:
            best = min(best, minimax_with_alpha_beta(child, alpha, beta, True))  # Maximize for the player
            beta = min(beta, best)
            if beta <= alpha:
                break  # Prune the branch
        return best

# Example game tree
leaf1 = Node(3)
leaf2 = Node(5)
leaf3 = Node(2)
leaf4 = Node(9)

node1 = Node(0, [leaf1, leaf2])
node2 = Node(0, [leaf3, leaf4])

root = Node(0, [node1, node2])

# Get the optimal strategy with Alpha-Beta pruning
result = minimax_with_alpha_beta(root, -math.inf, math.inf, True)
print(f"Optimal strategy value with alpha-beta pruning: {result}")
