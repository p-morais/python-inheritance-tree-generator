def generate_classtree(subtree):
	if subtree == []:
		return []

	else:
		return [[cls.__name__] + generate_classtree(cls.__subclasses__()) for cls in subtree]


def pprint(tree, level=0):
	if len(tree) == 0:
		return "\n"

	pp = "\t" * level + tree[0] + "\n"

	for node in tree[1:]:
		pp += pprint(node, level+1)

	return pp
	
# USAGE:
# tree = generate_classtree(YourBaseClass)
# print(pprint(tree[0]))
