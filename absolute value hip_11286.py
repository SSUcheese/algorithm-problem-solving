# 백준 절댓값 힙 문제이다.
# 문제 번호는 11286번

from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
queue = PriorityQueue()

for i in range(N):
    order = int(input())
    if order == 0:
        if queue.empty():
            print('0\n')
        else:
            temp = queue.get()
            print(str((temp[1])) + '\n')
    else:
        queue.put((abs(order), order))
'''
queue.Queue를 사용하는 경우: queue.empty()를 사용하는 것이 적합
list 또는 deque 기반의 큐를 사용하는 경우: if queue 방식이 더 적합

queue 클래스는 python의 __bool__ 구현이 안 되어 있어 if queue 이런식으로 불가능
'''