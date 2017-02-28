from BST import *
from LL import *
import random

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
    G: Undirected Graph as Adjacency List

    Returns
    =======
    Adjacency List
    '''
    F = {}
    Q = []
    visited = []

    for v in G.keys():
        # add all v's to Q.
        Q.append(v)
        F[v] = []

    start = Q[0]
    visited.append(start)

    edge = None
    vert = None
    while len(Q) > 0:
        for v in visited:
            for e in G[v]:
                if not edge or e[1] < edge[1]:
                    if e[0] not in visited:
                        edge = e
                        to_vert = e[0]
                        from_vert = v
        if not edge:
            break
        F[from_vert].append(edge)
        F[to_vert].append((from_vert, edge[1]))
        visited.append(to_vert)
        Q.remove(to_vert)
        edge = None
        to_vert = None
        from_vert = None
    return F



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
print question3({
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 5), ('D', 3)],
    'C': [('B', 5), ('E', 6)],
    'D': [('B', 3), ('E', 1)],
    'E': [('D', 1), ('C', 6)]
})
'''
{
    'A': [('B', 2)],
    'C': [('B', 5)],
    'B': [('A', 2), ('D', 3), ('C', 5)],
    'E': [('D', 1)],
    'D': [('B', 3), ('E', 1)]
}
'''
print question3({
    'A': [('B', 1), ('C', 1), ('E', 2)],
    'B': [('A', 1), ('C', 1), ('D', 3)],
    'C': [('A', 1), ('B', 1), ('D', 4)],
    'D': [('B', 3), ('C', 4), ('E', 6), ('F', 7)],
    'E': [('A', 2), ('D', 6)],
    'F': [('D', 7)]
    })
'''
{
    'A': [('B', 1), ('C', 1), ('E', 2)],
    'C': [('A', 1)],
    'B': [('A', 1), ('D', 3)],
    'E': [('A', 2)],
    'D': [('B', 3), ('F', 7)],
    'F': [('D', 7)]
}
'''

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
