from BST import *
from LL import *
import random
import unittest

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
    F = {}  # stores final adjacency list.
    visited = []

    for v in G.keys():
        # initialize F with all keys, v, being set to empty lists.
        F[v] = []

    # pick an arbitary node to start the process.
    visited.append(random.choice(G.keys()))

    edge = None
    vert = None
    while len(visited) < len(G):
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
class UnitTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(question1("udacity", "ad"))
        self.assertFalse(question1("udacity", "tcd"))
        self.assertTrue(question1("udacity", "ycit"))
        self.assertFalse(question1("udacity", "udacitygreat"))


    def test2(self):
        self.assertEqual(question2("abcba"), "abcba")
        self.assertEqual(question2("aedbdeayou"), "aedbdea")
        self.assertEqual(question2("iciiceci"), "iceci")
        self.assertEqual(question2("hi"), None)


    def test3(self):
        self.assertEqual(
            question3({
                'A': [('B', 2)],
                'B': [('A', 2), ('C', 5), ('D', 3)],
                'C': [('B', 5), ('E', 6)],
                'D': [('B', 3), ('E', 1)],
                'E': [('D', 1), ('C', 6)]
            }),
            {
                'A': [('B', 2)],
                'C': [('B', 5)],
                'B': [('A', 2), ('D', 3), ('C', 5)],
                'E': [('D', 1)],
                'D': [('B', 3), ('E', 1)]
            }
        )
        self.assertEqual(
            question3({
                'A': [('B', 1), ('C', 1), ('E', 2)],
                'B': [('A', 1), ('C', 1), ('D', 3)],
                'C': [('A', 1), ('B', 1), ('D', 4)],
                'D': [('B', 3), ('C', 4), ('E', 6), ('F', 7)],
                'E': [('A', 2), ('D', 6)],
                'F': [('D', 7)]
            }),
            {
                'A': [('B', 1), ('C', 1), ('E', 2)],
                'C': [('A', 1)],
                'B': [('A', 1), ('D', 3)],
                'E': [('A', 2)],
                'D': [('B', 3), ('F', 7)],
                'F': [('D', 7)]
            }
        )

    def test4(self):
        self.assertEqual(
            question4([
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4
            ),
                3
        )
        self.assertEqual(
            question4([
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                5
            ),
                None
        )
        self.assertEqual(
            question4([
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0]],
                4,
                0,
                3
            ),
                2
        )
        self.assertEqual(
            question4([
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0]],
                4,
                2,
                5
            ),
                4
        )


    N1 = Node("data1")
    N2 = Node("data2")
    N3 = Node("data3")
    N4 = Node("data4")
    N5 = Node("data5")
    N1.next = N2
    N2.next = N3
    N3.next = N4
    N4.next = N5


    def test5(self):
        self.assertEqual(question5(N1, 3), "data3")
        self.assertEqual(question5(N1, 6), None)
        self.assertEqual(question5(N1, 5), "data1")
        self.assertEqual(question5(None, None), None)


if __name__ == '__main__':
    unittest.main()
