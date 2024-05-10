class DataPoint:
    def __init__(self, x=0.0, y=0.0, cluster=-1):
        self.x = x
        self.y = y
        self.cluster = cluster

    def __str__(self):
        return f"DataPoint({self.x:.4f}, {self.y:.4f}, {self.cluster})"

    def __repr__(self):
        return self.__str__()