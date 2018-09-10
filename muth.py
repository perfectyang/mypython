import multiprocessing as mp
import threading as td


def job(a, b):
    print('aaaa')

if __name__ == '__main__':
    p1 = mp.Process(target=job, args=(1, 2))
    t1 = td.Thread(target=job, args=(1, 2))
    p1.start()
    p1.join()
    t1.start()
    t1.join()
