class TrieNode :
    def __init__(self):
        self.children = {}
        self.is_end = True

class AutoCompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        node = self.root
        for word in words:
            if word not in node.children:
                node.children[word] = TrieNode()

            node = node.children[word]
            print(node.children)

        node.is_end = True


    def search(self, prefix):
        node = self.root
        res = []
        for char in prefix:
            if char not in node.children:
                return []
            
            node = node.children[char]

        def _dfs(node , currPrefix):
            if node.is_end:
                print("at node end:", currPrefix)
                res.append(currPrefix)

            for char , children in node.children.items():
                _dfs(children, currPrefix+char)

        _dfs(node, prefix)
        return res

tries = AutoCompleteTrie()
tries.insert('hello')
tries.insert('apple')
tries.insert('applet')
tries.insert('appricon')
print(tries)
print(f'suggesion for app {tries.search("app")}')