def question1(s, t):
    '''
    Given two strings s and t, determines whether some anagram of t is a
    substring of s. For example: if s = "udacity" and t = "ad", then the
    function returns True.

    Input
    =====
    s: string
    t: string

    Returns
    =======
    Boolean
    '''
    letterPos = []

    if len(t) > len(s):
        return False
    
    tempT = t
    for letter in s:
        if letter in tempT:
            tempT = tempT.replace(letter, "")
            if len(tempT) == 0: return True
        else:
            tempT = t

    return False


def question2(a):
    '''
    Given a string a, finds the longest palindromic substring contained in a.

    Input
    =====
    a: string

    Returns
    =======
    String
    '''
    result = ""
    for x in xrange(len(a)):
        testFront = a[:len(a) - x]
        testBack = a[x:]
        if testFront == testFront[::-1] and len(testFront) > len(result) and len(testFront) > 1:
            result = testFront
        if testBack == testBack[::-1] and len(testBack) > len(result) and len(testBack) > 1:
            result = testBack

    if result == "":
        return None
    else:
        return result


def question3(G):
    '''
    Given an undirected graph G, finds the minimum spanning tree within G.
    A minimum spanning tree connects all vertices in a graph with the smallest
    possible total weight of edges.

    Input
    =====
    G: Undirected Graph

    Returns
    =======
    Adjaceny List
    '''
    pass

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



def question4(T, r, n1, n2):
    '''
    Finds the least common ancestor between two nodes on a binary search tree.
    The least common ancestor being the farthest node from the root that is an
    ancestor of both nodes.

    Input
    =====
    T: The tree represented as a matrix, where the index of the list is equal
       to the integer stored in that node and a 1 represents a child node.

    r: A non-negative integer representing the root.

    n1, n2: non-negative integers representing the two nodes in no particular order.

    Returns
    =======
    Integer representing the least common ancestor.
    '''
    tree = BST(r, T)
    n1Ancesstors = tree.ancesstor_list(n1)
    n2Ancesstors = tree.ancesstor_list(n2)
    i = 0
    while i < len(n1Ancesstors) and i < len(n2Ancesstors):
        if n1Ancesstors[i] in n2Ancesstors:
            return n1Ancesstors[i]
        if n2Ancesstors[i] in n1Ancesstors:
            return n2Ancesstors[i]
        i += 1
    return None





class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


def question5(ll, m):
    '''
    Find the element in a singly linked list that's m elements from the end.
    For example, if a linked list has 5 elements, the 3rd element from the
    end is the 3rd element.

    Input
    =====
    ll: The first node of a linked list.
    m: The "mth number from the end".

    Returns
    =======
    The value of the node that's m elements from the end.
    '''
    if ll and m:
        temp = ll # Initialise temp
        listLen = 0 # Initialise count

        # Loop while end of linked list is not reached
        while (temp):
            listLen += 1
            temp = temp.next

        if m > listLen:
            return None

        nodeToReturn = listLen - m

        temp = ll
        while nodeToReturn > 0:
            temp = temp.next
            nodeToReturn -= 1
        return temp.data
    else:
        return None
        

################
## UNIT TESTS ##
################
print "Question 1 Test Cases:"
print question1("udacity", "ad")  # True
print question1("udacity", "tcd")  # False
print question1("udacity", "ycit")  # True
print question1("udacity", "udacitygreat")  # False


print "Question 2 Test Cases:"
print question2("abcba")  # "abcba"
print question2("aedbdeayou")  # "aedbdea"
print question2("iciiceci")  # "iceci"
print question2("hi")  # None


print "Question 3 Test Cases:"

print "Question 4 Test Cases:"
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4) # 3
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 5) # None
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0]],
                 4,
                 0,
                 3) # 2
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0]],
                 4,
                 2,
                 5) # 4

print "Question 5 Test Cases:"
N1 = Node("data1")
N2 = Node("data2")
N3 = Node("data3")
N4 = Node("data4")
N5 = Node("data5")
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
print question5(N1, 3)  # data3
print question5(N1, 6)  # None
print question5(N1, 5)  # data1
print question5(None, None)  # None
