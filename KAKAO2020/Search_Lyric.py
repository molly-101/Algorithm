from collections import deque


class Node(object):
    def __init__(self, key, count = 0):
        self.key = key
        self.child = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        if "*" not in cur.child:
            cur.child['*'] = 1
        else:
            cur.child['*'] += 1

    def search(self, word):
        cur = self.head
        Q = deque()
        Q.append(cur)
        cnt = 0
        for ch in word:
            for i in range(len(Q)):
                tmp = Q.popleft()
                if ch == "?":
                    for i in tmp.child:
                        if i != "*":
                            Q.append(tmp.child[i])
                else:
                    if ch in tmp.child:
                        Q.append(tmp.child[ch])

        for i in Q:
            if '*' in i.child:
                cnt += i.child['*']
        return cnt


def solution(words, queries):
    dictionary1 = Trie()
    dictionary2 = Trie()
    for i in words:
        dictionary1.insert(i)
        dictionary2.insert(i[::-1])
    result = []
    for querie in queries:
        if querie[0] != "?":
            dictionary1.search(querie)
        else:
            dictionary2.search(querie[::-1])
    return result


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))