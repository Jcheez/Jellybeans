class binaryNode:
    
    def __init__(self, item) -> None:
        self.leftNode = None
        self.rightNode = None
        self.parent = None
        self.item = item
        self.size = 1
        self.height = 0

    def updateSize(self) -> None:
        if self.leftNode == None and self.rightNode == None:
            self.size = 1
        elif self.leftNode == None:
            self.size = 1 + self.right.size
        elif self.rightNode == None:
            self.size = 1 + self.left.size
        else:
            self.size = 1 + self.left.size + self.right.size

    def updateHeight(self) -> None:
        if self.leftNode == None and self.rightNode == None:
            self.height = 0
        elif self.leftNode == None:
            self.height = 1 + self.right.height
        elif self.rightNode == None:
            self.height = 1 + self.left.height
        else:
            self.height = 1 + max(self.left.height, self.right.height)