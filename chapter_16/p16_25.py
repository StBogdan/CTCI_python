class LRUCache:
    def __init__(self, max_size):
        super().__init__()
        self.latest = None
        self.oldest = None
        self.max_size = max_size
        self._dict = {}

    def add(self, key, val) -> None:
        if key in self._dict:
            self._dict[key].val = val
            self._bump_node(self._dict[key])
        elif len(self._dict) == self.max_size:
            self.evict_lru()

        new_node = CacheNode(key,val)
        if self.latest:
            self.latest.right = new_node
        else:
            self.oldest = new_node
        
        new_node.left = self.latest
        self._dict[key] = new_node
        self.latest = new_node

        # print(f"Self.latest now is {self.latest}, to it's left {self.latest.left}")

    def get(self,key):
        if key not in self._dict:
            raise Exception(f"Key {key} not in cache")

        val =  self._dict[key].val
        self._bump_node(self._dict[key])
        return val

    def evict_lru(self):
        if not self.oldest:
            raise Exception("Cannot evict, cache should be empty")

        oldest_nodes = self.oldest
        # print(f"[Evicting] oldest, which is {oldest_nodes}, on it's right {oldest_nodes.right}")

        if oldest_nodes.right:
            # print(f"[Evicting] On right is {oldest_nodes.right}")
            self.oldest = oldest_nodes.right
            oldest_nodes.right.left = None
        else:
            self.oldest = None
            self.latest = None
        
        del self._dict[oldest_nodes.key]
        
    def _bump_node(self, node):
        # print(f"Bumping node {node}, w/ LEFT: {node.left} and RIGHT {node.right}")
        # print(f"Bumping node in dict: {self._dict[node.left.key] if node.left else 'Nevermind'}")


        if node != self.latest:
            if node.left:
                node.left.right = node.right
            else: # You are the oldest
                self.oldest = node.right
            
            # Add to the latest nodes, become latest
            self.latest.right = node
            node.left = self.latest
            self.latest = node


    def __str__(self):
        return f"LRUCache w/ items: {list(self._dict.items())}, oldest: {self.oldest} , newest: {self.latest}"
        
class CacheNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None
    
    def __str__(self):
        return f"CN(k:{self.key}, v:{self.val})"

    
    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    lrc = LRUCache(4)
    for i in range(10):
        lrc.add(i,i)
        assert lrc.get(i) == i
        print(lrc)

    print("-"*50)
    lrc.get(6)
    lrc.get(8)
    print(lrc)
    print("-"*50)

    for i in range(10,16):
        lrc.add(i,i)
        print(lrc)