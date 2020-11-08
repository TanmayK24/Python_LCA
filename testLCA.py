import unittest
import lcaPython #changed the main file name from LEA-Python to lcaPython because of some formatting issues. You may need to do it if you download the repository. 
from binarytree import Node


class TestLCA(unittest.TestCase):

	

	def test_LCA(self):
		root = Node(5)
		root.left = Node(4)
		root.left.left = Node(2)
		root.left.right = Node(3)
		root.right = Node(6)
		root.right.left = Node(11)
		root.right.right = Node(7)
		root.right.right.left = Node(8)
		print(root)
		self.assertEqual(lcaPython.findLCA(root,3,7),5)
		self.assertEqual(lcaPython.findLCA(root,2,4),4)
		self.assertEqual(lcaPython.findLCA(root,6,3),5)
		self.assertEqual(lcaPython.findLCA(root,2,3),4)
		self.assertEqual(lcaPython.findLCA(root,5,6),5)
		self.assertEqual(lcaPython.findLCA(root,5,5),5)
		self.assertEqual(lcaPython.findLCA(root,7,7),7)
		self.assertEqual(lcaPython.findLCA(root,7,11),6)
		self.assertEqual(lcaPython.findLCA(root,7,20),-1)



