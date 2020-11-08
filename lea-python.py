#Creating Binary Tree using the binary tree module
from binarytree import Node
root = Node(5)
root.left = Node(4)
root.left.left = Node(2)
root.left.right = Node(3)
root.right = Node(6)
root.right.right = Node(7)


print('Binary Tree : ', root)



def findPath(root, path, k):

	if root is None: 
		return False

	path.append(root.value)

	if root.value == k: 
		return True

	if(root.left != None and findPath(root.left, path, k)): 
		return True

	if(root.right != None and findPath(root.right, path, k)): 
		return True

	path.pop()
	return False

def findLCA(root, n1,n2): 

		path1 = []
		path2 = []

		if( findPath(root, path1, n1) == False  or findPath(root, path2, n2) == False): return -1

		i = 0
		while(i<len(path1) and i<len(path2)):
			if path1[i] != path2[i]: break
			i = i + 1

		return path1[i-1]




print("LCA of 3 and 7 is %d" %(findLCA(root,3,7)))
print("LCA of 2 and 4 is %d" %(findLCA(root,2,4)))
print("LCA of 6 and 3 is %d" %(findLCA(root,6,3)))
print("LCA of 2 and 3 is %d" %(findLCA(root,2,3)))
print("LCA of 5 and 6 is %d" %(findLCA(root,5,6)))
print("LCA of 7 and 7 is %d" %(findLCA(root,7,7)))

		