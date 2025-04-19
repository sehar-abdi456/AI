import math

# Define the game tree node class
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

# Alpha-Beta Pruning with Minimax
def minimax_with_alpha_beta(node, depth, alpha, beta, is_max, path="Root"):
    # If the node has no children, it is a leaf node, return its value
    if not node.children:
        print(f"Evaluating leaf node at {path} with value {node.value}")
        return node.value

    if is_max:
        best = -math.inf
        for i, child in enumerate(node.children):
            # Recursive call for child nodes with updated alpha and beta
            print(f"Exploring max node at {path} - Child {i}")
            best = max(best, minimax_with_alpha_beta(child, depth + 1, alpha, beta, False, f"{path}->{i}"))
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruning at {path}->{i} (Alpha: {alpha}, Beta: {beta})")
                break  # Prune the branch
        return best
    else:
        best = math.inf
        for i, child in enumerate(node.children):
            # Recursive call for child nodes with updated alpha and beta
            print(f"Exploring min node at {path} - Child {i}")
            best = min(best, minimax_with_alpha_beta(child, depth + 1, alpha, beta, True, f"{path}->{i}"))
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruning at {path}->{i} (Alpha: {alpha}, Beta: {beta})")
                break  # Prune the branch
        return best

# Example game tree with leaf nodes having payoff values
leaf1 = Node(3)
leaf2 = Node(5)
leaf3 = Node(2)
leaf4 = Node(9)

node1 = Node(0, [leaf1, leaf2])
node2 = Node(0, [leaf3, leaf4])

root = Node(0, [node1, node2])

# Start the Alpha-Beta Pruning Minimax algorithm
print("Starting Alpha-Beta Pruning Minimax Algorithm:")
result = minimax_with_alpha_beta(root, 0, -math.inf, math.inf, True)
print(f"Optimal strategy value with Alpha-Beta Pruning: {result}")
