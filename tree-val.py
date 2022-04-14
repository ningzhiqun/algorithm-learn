# 平衡二叉树

print(type(True))

class VALTreeNode(object):

    def __init__(self, deep, value, leftNode, rightNode):
        self.deep = deep
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

    def getValue(self):
        return self.value

class VALTree(object):

    baseNode = None

    def __init__(self):
        self.baseNode = None

    def add(self, value):
        pass

    def remove(self, value):
        pass

    def isBalance(self) -> bool:
        node = self.baseNode
        if None is node:
            return True
        


base = VALTreeNode(0, 123, None, None)
print(base.value)


# 判断二叉树是否平衡
def isBalance(tree: VALTree):
    if None is tree:
        return True

    leftDeep = 0
    if tree.leftNode is not None:
        leftDeep = tree.leftNode.deep

    rightDeep = 0
    if tree.rightNode is not None:
        rightDeep = tree.rightNode.deep

    if abs(leftDeep - rightDeep) > 1:
        return False

    return True
