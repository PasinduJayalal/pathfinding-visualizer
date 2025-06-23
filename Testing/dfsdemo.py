# https://www.datacamp.com/tutorial/depth-first-search-in-python
# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

# Recursive DFS function
def dfs_recursive(tree, node, end, visited=None):
    if visited is None:
        visited = []  
        
    visited.append(node)   
    if node == end:       
        print(f"Found: {node}")
        print(f"Visited nodes:", visited)
        return True
    
    # print(node)         
    for child in tree[node]:  
        if child not in visited:
            if dfs_recursive(tree, child, end, visited):
                return True
                     

dfs_recursive(tree, 'A', 'O')