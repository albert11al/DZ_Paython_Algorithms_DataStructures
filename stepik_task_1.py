#Условие здесь: https://stepik.org/media/attachments/lesson/41233/statements.pdf
#Сдавать здесь: https://stepik.org/course/1547/syllabus раздел 2.3 вторая задача

import queue
import sys

proc_kolv = sys.stdin.readline().split(' ')
ochered = sys.stdin.readline().split(' ')
proc = int(proc_kolv[0])
kolv = int(proc_kolv[1])
derevo = queue.PriorityQueue()
for z in range(proc):
    derevo.put([0,proc,z])
for x in ochered:
    x = int(x)
    verh = derevo.get()
    if x < 1:
        print(verh[2], verh[0])
        derevo.put(verh)
    else:
        print(verh[2], verh[0])
        verh[0] += x
        derevo.put(verh)