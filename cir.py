class Circle:
    id=0
    raidus=0

    def __init__(self,i,r):
        self.id=i
        self.raidus=r
    
    def circumfrence(self):
        return self.raidus * 2 * 3.14
