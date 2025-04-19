
from collections import deque, defaultdict
import heapq
import math

# === Helper Functions ===
def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return -1, -1

def get_successors(state):
    successors = []
    x, y = find_empty(state)
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    for dx, dy, move in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            successors.append((move, new_state))
    return successors

# === Uninformed Search Algorithms ===

# 1. Depth-First Search
def depth_first_search(initial, goal):
    stack = [(initial, [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        visited.add(tuple(map(tuple, state)))
        for move, new_state in get_successors(state):
            if tuple(map(tuple, new_state)) not in visited:
                stack.append((new_state, path + [move]))
    return None

# 2. Breadth-First Search
def breadth_first_search(initial, goal):
    queue = deque([(initial, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        visited.add(tuple(map(tuple, state)))
        for move, new_state in get_successors(state):
            if tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, path + [move]))
    return None

# 3. Uniform Cost Search
def uniform_cost_search(initial, goal, move_cost=1):
    pq = [(0, initial, [])]
    visited = set()
    while pq:
        cost, state, path = heapq.heappop(pq)
        if state == goal:
            return path, cost
        visited.add(tuple(map(tuple, state)))
        for move, new_state in get_successors(state):
            if tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(pq, (cost + move_cost, new_state, path + [move]))
    return None, float('inf')

# 4. Bidirectional Search
def bidirectional_search(initial, goal):
    def tuple_state(state): return tuple(map(tuple, state))
    front, back = {tuple_state(initial): []}, {tuple_state(goal): []}
    qf, qb = deque([(initial, [])]), deque([(goal, [])])
    while qf and qb:
        state_f, path_f = qf.popleft()
        for move, new_state in get_successors(state_f):
            t = tuple_state(new_state)
            if t not in front:
                front[t] = path_f + [move]
                qf.append((new_state, path_f + [move]))
            if t in back:
                return front[t] + back[t][::-1]

        state_b, path_b = qb.popleft()
        for move, new_state in get_successors(state_b):
            t = tuple_state(new_state)
            if t not in back:
                back[t] = path_b + [move]
                qb.append((new_state, path_b + [move]))
            if t in front:
                return front[t] + back[t][::-1]
    return None

# 5. Depth Limited Search
def depth_limited_search(initial, goal, limit):
    def recursive_dls(state, path, depth):
        if state == goal:
            return path
        if depth == 0:
            return None
        for move, new_state in get_successors(state):
            result = recursive_dls(new_state, path + [move], depth - 1)
            if result:
                return result
        return None
    return recursive_dls(initial, [], limit)

# === Informed Search Algorithms ===

# 6. Greedy Best First Search
def greedy_best_first_search(graph, heuristics, start, goal):
    pq = [(heuristics[start], start, [start])]
    visited = set()
    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))
    return None

# 7. A* Search (Misplaced Tiles Heuristic for 8-Puzzle)
def a_star_search_8_puzzle(initial, goal):
    def h(state):
        return sum(1 for i in range(3) for j in range(3) if state[i][j] != 0 and state[i][j] != goal[i][j])
    pq = [(h(initial), 0, initial, [])]
    visited = set()
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal:
            return path
        visited.add(tuple(map(tuple, state)))
        for move, new_state in get_successors(state):
            if tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(pq, (g + 1 + h(new_state), g + 1, new_state, path + [move]))
    return None

# 8. A* Search on Graph
def a_star_graph(graph, heuristics, start, goal):
    pq = [(heuristics[start], 0, start, [start])]
    visited = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                heapq.heappush(pq, (g + cost + heuristics[neighbor], g + cost, neighbor, path + [neighbor]))
    return None, float('inf')

# 9. AO* Algorithm for AND-OR Trees
class AONode:
    def __init__(self, name, is_and=False):
        self.name = name
        self.children = []
        self.is_and = is_and
        self.heuristic = 0

    def add_children(self, groups):
        self.children = groups

def ao_star(node):
    if not node.children:
        return node.heuristic
    costs = []
    for group in node.children:
        cost = sum(ao_star(child) + 1 for child in group)
        costs.append(cost)
    node.heuristic = min(costs)
    return node.heuristic

# 10. Hill Climbing for Block World

def hill_climbing(initial, goal):
    def heuristic(state):
        return sum(1 if i < len(goal) and state[i] == goal[i] else -1 for i in range(len(state)))

    current = initial[:]
    current_score = heuristic(current)
    for _ in range(100):
        neighbors = []
        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                new_state = current[:]
                new_state[i], new_state[j] = new_state[j], new_state[i]
                neighbors.append((heuristic(new_state), new_state))
        neighbors.sort(reverse=True)
        if neighbors and neighbors[0][0] > current_score:
            current_score, current = neighbors[0]
        else:
            break
    return current

# === Sample Function Calls ===
# Call the respective function with required parameters
# Example:
# path = depth_first_search(initial_state, goal_state)
# path = breadth_first_search(initial_state, goal_state)
# path, cost = uniform_cost_search(initial_state, goal_state)
# path = bidirectional_search(initial_state, goal_state)
# path = depth_limited_search(initial_state, goal_state, limit=10)
# path = greedy_best_first_search(graph, heuristics, 'A', 'G')
# path = a_star_search_8_puzzle(initial_state, goal_state)
# path, cost = a_star_graph(graph, heuristics, 'A', 'G')
# optimal_cost = ao_star(root_node)
# final_state = hill_climbing(initial_config, goal_config)