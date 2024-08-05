# 카드 합체 놀이

import sys

class Heap:
    def __init__(self):
        self.heap = []

    def heappush(self, value):
        self.heap.append(value)

        idx = len(self.heap)-1
        while idx > 0:
            parent = (idx+1)//2-1
            if self.heap[parent] <= self.heap[idx]:
                break

            elif self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent

    def heappop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        node = self.heap.pop()

        idx = 0
        while idx < len(self.heap)-1:
            left = idx*2
            right = idx*2+1

            # 자식 노드가 없는 경우
            if right>len(self.heap)-1:
                break

            # 왼쪽 자식 노드만 있는 경우
            if left == len(self.heap)-1:
                if self.heap[left] < self.heap[idx]:
                    self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left]
                    idx = left

            # 자식이 모두 있는 경우
            else:
                # 왼쪽 자식이 더 작은 경우
                if self.heap[left] <= self.heap[right] and self.heap[idx] > self.heap[left]:
                    self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                    idx = left
                # 오른쪽 자식이 더 작은 경우
                elif self.heap[right] < self.heap[left] and self.heap[idx] > self.heap[right]:
                    self.heap[idx], self.heap[right] = self.heap[right], self.heap[idx]
                    idx = right
                # 부모 노드가 제일 작은 경우
                else:
                    break

        return node


n, m = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))

my_card = Heap()
for c in card_list:
    my_card.heappush(c)

for _ in range(m):
    a = my_card.heappop()
    b = my_card.heappop()
    c = a+b
    my_card.heappush(c)
    my_card.heappush(c)

print(sum(my_card.heap))

