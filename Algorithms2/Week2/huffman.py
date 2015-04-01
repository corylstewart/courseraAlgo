import heapq

def make_freq(txt):
    char_count = dict()
    for ch in txt:
        if ch not in char_count:
            char_count[ch] = 0
        char_count[ch] += 1
    return char_count

def huffman(char_count):
    heap = list()
    for ch, count in char_count.items():
        heap.append([count, [ch, '']])
    heapq.heapify(heap)
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        for ch_bit in first[1:]:
            ch_bit[1] = '0' + ch_bit[1]
        for ch_bit in second[1:]:
            ch_bit[1] = '1' + ch_bit[1]
        new_weight = [first[0]+second[0]] + first[1:] + second[1:]
        heapq.heappush(heap, new_weight)
    encodings = dict()
    for ch_bit in heap[0][1:]:
        encodings[ch_bit[0]] = ch_bit[1]
    return encodings

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print huffman(make_freq(txt))