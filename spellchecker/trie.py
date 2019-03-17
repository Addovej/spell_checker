class Node(object):

    def __init__(self, value=None):
        self.children = {}
        self.value = value
        self.word = None


class Trie(object):

    def __init__(self):
        self.node = Node()

    def __contains__(self, item) -> bool:
        curr_node = self.node
        for i in item:
            if i not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[i]
        return True

    def append(self, item: str):
        cur_node = self.node
        for i in item:
            if i in cur_node.children:
                cur_node = cur_node.children[i]
            else:
                new_node = Node(i)
                cur_node.children[i] = new_node
                cur_node = new_node
        cur_node.word = item
