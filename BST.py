class bstNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root, nodeList=None):
        self.root = bstNode(root)
        if nodeList:
            self.build_tree(nodeList)

    def build_tree(self, nodeList):
        self.build_tree_helper(self.root, nodeList)

    def build_tree_helper(self, node, nodeList):
        for idx, link in enumerate(nodeList[node.value]):
            if link == 1:
                if idx < node.value:
                    node.left = bstNode(idx)
                    self.build_tree_helper(node.left, nodeList)
                elif idx > node.value:
                    node.right = bstNode(idx)
                    self.build_tree_helper(node.right, nodeList)
                else:
                    raise ValueError("Invalid BST Structure For Node " + str(idx))

    def ancesstor_list(self, searchValue):
        ancesstors = []
        while True:
            temp = self.ancesstor(searchValue)
            if temp:
                ancesstors.append(temp.value)
                if temp.value == self.root.value:
                    return ancesstors
                else:
                    searchValue = temp.value
            else:
                return ancesstors
                

    def ancesstor(self, searchValue):
        return self.recursive_ancess_search(self.root, searchValue)

    def recursive_ancess_search(self, node, searchValue):
        if node:
            if node.left and searchValue == node.left.value:
                return node
            if node.right and searchValue == node.right.value:
                return node
            if searchValue < node.value:
                return self.recursive_ancess_search(node.left, searchValue)
            elif searchValue > node.value:
                return self.recursive_ancess_search(node.right, searchValue)
            else:
                raise ValueError("An Error Occurred: Invalid Tree Structure Found.")
        else:
            return None