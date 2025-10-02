import heapq
def main():
    import sys
    read = sys.stdin.readline
 
    n_words = int(read().strip())
    dict_words = [read().strip() for i in range(n_words)]

    adj = {ch: set() for ch in "abcdefghijklmnopqrstuvwxyz"}
    indeg = {ch: 0 for ch in "abcdefghijklmnopqrstuvwxyz"}
    present = set()  

    for w in dict_words:
        for ch in w:
            present.add(ch)

    for i in range(n_words - 1):
        first, second = dict_words[i], dict_words[i + 1]
        limit = min(len(first), len(second))
        mismatch = False
        for j in range(limit):
            if first[j] != second[j]:
                if second[j] not in adj[first[j]]:
                    adj[first[j]].add(second[j])
                    indeg[second[j]] += 1
                mismatch = True
                break
        if not mismatch and len(first) > len(second):
            print(-1)
            return

    min_heap = []
    for ch in present:
        if indeg[ch] == 0:
            heapq.heappush(min_heap, ch)

    ordering = []
    while min_heap:
        curr = heapq.heappop(min_heap)
        ordering.append(curr)
        for nxt in sorted(adj[curr]): 
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                heapq.heappush(min_heap, nxt)

    if len(ordering) != len(present):
        print(-1)
    else:
        print("".join(ordering))
main()