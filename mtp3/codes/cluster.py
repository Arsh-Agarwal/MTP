class Cluster:
    def __init__(self, num = -1, pts = []):
        self.x = -1
        self.y = -1
        self.rad = -1
        self.num = num
        self.pts = pts

    def make(self):
        pts = self.pts
        self.rad = min((max([pt.x for pt in pts]) - min([pt.x for pt in pts])), (max([pt.y for pt in pts]) - min([pt.y for pt in pts])))/2
        self.x = (max([pt.x for pt in pts]) + min([pt.x for pt in pts]))/2
        self.y = (max([pt.y for pt in pts]) + min([pt.y for pt in pts]))/2
        
