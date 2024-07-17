# 최소 힙

class MyHeap:
    def __init__(self):
        self.arr = [None]

    def insert(self, value):
        self.arr.append(value)
        cur_idx = len(self.arr)-1
        parent = cur_idx // 2

        while parent > 0:
            # parent = cur_idx // 2
            if self.arr[cur_idx] < self.arr[parent]: # 현재 노드와 부모 노드를 비교해서 부모노드가 더 크면
                self.arr[cur_idx], self.arr[parent] = self.arr[parent], self.arr[cur_idx] # 두 개의 자리 교체
                cur_idx = parent # 현재 노드를 부모 노드로 수정
                parent = cur_idx // 2 # 부모 노드 업데이트
            else:
                return #self.arr


    def remove(self):

        if len(self.arr)<2:
            return 0

        # 가장 마지막 노드와 첫 번째 노드를 바꾸고 마지막 노드 추출
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        root = self.arr.pop()

        now_idx = 1 # 햔재 노드 (첫 번째부터 시작)
        l = len(self.arr) - 1

        while now_idx <= l//2:
            left = now_idx * 2 # 왼쪽 자식 노드
            right = now_idx * 2 + 1 # 오른쪽 자식 노드
            compare_idx = now_idx # 비교할 노드

            # 자식 노드가 없는 경우
            if left > l:
                break
            # 왼쪽 자식만 있는 경우
            if left == l:
                if self.arr[now_idx] > self.arr[left]:
                    # self.arr[left], self.arr[now_idx] = self.arr[now_idx], self.arr[left]
                    compare_idx = left
            # 둘 다 있는 경우
            else:
                if self.arr[left] <= self.arr[right]:
                    # self.arr[left], self.arr[now_idx] = self.arr[now_idx], self.arr[left]
                    compare_idx = left
                else:
                    # self.arr[right], self.arr[now_idx] = self.arr[now_idx], self.arr[right]
                    compare_idx = right

            if self.arr[now_idx] <= self.arr[compare_idx]:
                break
            else:
                self.arr[now_idx], self.arr[compare_idx] = self.arr[compare_idx], self.arr[now_idx]
                now_idx = compare_idx
        return root



h = MyHeap()
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(h.remove())
        # print(h.arr)
        continue
    h.insert(n)
    # print(h.insert(n))



