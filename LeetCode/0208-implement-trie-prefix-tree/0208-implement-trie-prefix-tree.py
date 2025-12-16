class Trie:

    def __init__(self):
        self.s = set()
        self.subs = set()

    def insert(self, word: str) -> None:
        self.s.add(word)

        for i in range(1, len(word) + 1):
            self.subs.add(word[:i])

    def search(self, word: str) -> bool:
        if word in self.s:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.subs:
            return True
        else:
            return False