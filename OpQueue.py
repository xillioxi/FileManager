class OpQueue:
    def __init__(self):
        self.__queue = deque()

    def append(self,func):
        self.__queue.append(func)
    
    def clear(self):
        self.__queue.clear()

    def copy(self):
        """Shallow copy of the queue"""
        return self.__queue.copy()
     
    def insert(self,i,element):
        self.__queue.insert(i,element)

    def remove(self,element):
        self.__queue.remove(element)