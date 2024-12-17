class Queue:
    '''
    Design a queue
    '''
    
    #capacity_queue 是邏輯容量；large_size是內部儲存空間的大小
    def __init__(self, capacity_queue: int, start: int = 0, end: int = 0, large_size: int = 100):
        '''
        Constructor of Queue

        Args:
            size: int representing the capacity of the queue
            start: int representing the index of the start of the queue
            end: int representing the index of the end of the queue
        '''
        self.capacity_queue = capacity_queue  # 代表capacity
        self.start = start
        self.end = end
        self.elements = [None] * large_size

    def enqueue(self, elem):
        '''
        Enqueue elements to the queue
        Arg:
            elem: element to be added to the queue
        '''
        #self.end - self.start 代表目前隊列中實際的元素個數。
        if self.end - self.start == self.capacity_queue: 
            "Queue is full, cannot add more elements"
            return
        self.elements[self.end] = elem
        self.end += 1

    def dequeue(self):
        '''
        Dequeue method
        '''
        # You can also see it as self.end - self.start == 0(queue is empty)
        if self.start == self.end:
            print("Queue is empty, cannot dequeue any element")
            return
        self.start += 1
        return self.elements[self.start - 1]
    #是返回被丟棄的元素, 這裡沒有設置為None，只是利用start的移動去模擬dequeue，實際上被dequeue的元素仍存在queue中
       


# 當start == end 的時候就不可以dequeue了！就算是初始化的時候也會遵守，例如start =0 和end =0的時候，
# 由於queue中沒有任何元素，所以也不能使用deque!

#capacity_queue和 large_size:分別在哪裡？
#https://chatgpt.com/share/6753da3c-96ac-8001-8b57-e890f9deaf2f