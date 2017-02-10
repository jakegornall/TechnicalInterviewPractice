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
	pass


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
	pass

Q1passing = "Failed"
q1TestCases = [
	("udacity", "ad", True),
	("udacity", "tcd", False),
	("udacity", "ycit", True),
	("udacity", "udacitygreat", False)]
for case in q1TestCases:
	if question1(case[0], case[1]) == case[2]:
		Q1passing = "Success!"
	else:
		Q1passing = "Failed"
print "Q1 Test Cases: " + Q1passing


Q2passing = "Failed"
q2TestCases = [
	("abcba", "abcba"),
	("aedbdeayou", "aedbdea"),
	("iciiceci", "iceci"),
	("hi", "")]
for case in q2TestCases:
	if question2(case[0]) == case[1]:
		Q2passing = "Success!"
	else:
		Q2passing = "Failed"
print "Q2 Test Cases: " + Q1passing


print "Question 3 Test Cases:"

print "Question 4 Test Cases:"

print "Question 5 Test Cases:"