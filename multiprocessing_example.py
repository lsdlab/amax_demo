import multiprocessing
import os
import time


# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C', 'D', 'E']:
        print('Put %s to queue...(%s)' % (value, os.getpid()))
        q.put(value)
        time.sleep(3)


# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue...(%s)' % (value, os.getpid()))
            time.sleep(3)
        else:
            break


if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    q = manager.Queue()
    p = multiprocessing.Pool(4)
    p.apply_async(write, args=(q, ))
    time.sleep(3)
    # for i in range(5):
    # p.apply_async(read, args=(q,))
    p.apply_async(read, args=(q, ))
    p.close()
    p.join()
    print('所有数据都写入并且读完')
