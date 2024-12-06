class Queue:
    '''
    Design a queue
    '''

    def __init__(self, capacity_queue: int, start: int = 0, end: int = 0, large_size: int = 100):
        '''
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
        if self.end - self.start == self.capacity_queue:
            "Queue is full, cannot add more elements"
            return
        self.elements[self.end] = elem
        self.end += 1

    def dequeue(self, elem):
        '''
        Dequeue method
        '''
        # You can also see it as self.end - self.start == 0(queue is empty)
        if self.start == self.end:
            print("Queue is empty, cannot dequeue any element")
            return
        self.start += 1
        return self.elements[self.start - 1]  # 不確定，是返回被丟棄的元素嗎？ 為何不用設置為None?


# 當start == end 的時候就不可以dequeue了！就算是初始化的時候也會遵守，例如start =0 和end =0的時候，
# 由於queue中沒有任何元素，所以也不能使用deque!
