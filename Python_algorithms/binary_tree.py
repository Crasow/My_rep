class Node:
    def __init__(self, value, right=None, left=None, link=None):
        self.right = right
        self.left = left
        self.value = value
        self.link = link


class Tree:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.head.link = 'head'
        else:
            now_node = self.head
            while True:
                if now_node.value >= node.value:
                    if now_node.left is None:
                        now_node.left = node
                        node.link = f'left to {now_node.value}'
                        # now_node.left = [node, f'left to {now_node.value}']
                        break
                    now_node = now_node.left
                else:
                    if now_node.right is None:
                        now_node.right = node
                        node.link = f'right to {now_node.value}'
                        # now_node.right = node[node, f'right to {now_node.value}']
                        break
                    now_node = now_node.right


def print_tree(node, path=True):
    print(node.value, node.link)
    if node.left:
        if node.value > node.left.value:
            path = print_tree(node.left, path)
        else:
            return False
    if node.right:
        if node.value < node.right.value:
            path = print_tree(node.right, path)
        else:
            return False
    return path


root = Tree()
n_list = [
    Node(15),
    Node(13),
    Node(14),
    Node(11),
    Node(7),
    Node(20),
    Node(16),
    Node(25),
    Node(18)
]

for el in range(len(n_list)):
    # print(n_list[el].value)
    root.add_node(n_list[el])

print_tree(root.head)
