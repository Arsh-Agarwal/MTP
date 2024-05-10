class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] == x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] <= self.rank[y_root]:
            self.parent[x_root] = y_root
            self.rank[y_root] += self.rank[x_root]
        else: 
            self.parent[y_root] = x_root
            self.rank[x_root] += self.rank[y_root]

        return True

# # Example usage:
# n = 5  # Number of elements
# dsu = DisjointSetUnion(n)

# # Union operations
# dsu.union(0, 1)
# dsu.union(2, 3)
# dsu.union(0, 2)

# # Find operations
# print("Parent of 1:", dsu.find(1))  # Should print 0
# print("Parent of 3:", dsu.find(3))  # Should print 0
# print("Parent of 4:", dsu.find(4))  # Should print 4, as it's not part of any union operation
