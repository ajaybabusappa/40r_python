#Synchronous
import time
import asyncio
import os
import test


def sample_function(num1):
    print(os.getpid())
    print('Hi' + str(num1))
    time.sleep(5)
    print('End' + str(num1))


# sample_function(10)
# sample_function(11)
# sample_function(13)





# import asyncio
# async def sample_function(num):
#     print('Hi' + str(num))
#     await asyncio.sleep(5)
#     print('End' + str(num))
#     return num


# async def main():
#     results = await asyncio.gather(sample_function(1), sample_function(2), sample_function(3))
#     print(results)

# asyncio.run(main())
# asyncio.run(sample_function(2))
# asyncio.run(sample_function(3))





#Multithreading
#1 process  => 


# import threading



# thd1 = threading.Thread(target=sample_function, args=(10,))
# thd1.start()

# thd2 = threading.Thread(target=sample_function, args=(11,))
# thd2.start()

# thd3 = threading.Thread(target=sample_function, args=(12,))
# thd3.start()


# print('All threads completed')

# thd1.join()
# thd2.join()
# thd3.join()




#True parallalism
import multiprocessing as mp

if __name__ == '__main__':

    p1 = mp.Process(target=sample_function, args=(10,))
    p1.start()

    p2 = mp.Process(target=sample_function, args=(11,))
    p2.start()

    p3 = mp.Process(target=sample_function, args=(12,))
    p3.start()

    p1.join()
    p2.join()
    p3.join()





