import sys
import heapq


if __name__ == "__main__":
    n = int(input())
    Mheap, mheap = [], []
    Mlen, mlen = 0, 0

    for i in range(n):
        num = int(sys.stdin.readline())
        if mlen < Mlen:
            mlen += 1
            heapq.heappush(mheap, (num, num))
        else:
            Mlen += 1
            heapq.heappush(Mheap, (-num, num))

        if Mlen > 0 and mlen > 0 and Mheap[0][1] > mheap[0][1]:
            M = heapq.heappop(Mheap)[1]
            m = heapq.heappop(mheap)[1]
            heapq.heappush(Mheap, (-m, m))
            heapq.heappush(mheap, (M, M))
        print(Mheap[0][1])