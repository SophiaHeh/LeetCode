import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        '''
        Initialize some test cases
        '''
    #Queue(3) 的意思是初始化一個 Queue 物件，並將參數 capacity_queue 設為 3，其餘參數使用預設值； 設定為 3，表示這個隊列的邏輯容量（即最多可以容納 3 個元素）。 
        self.queue = Queue(3)

    def test_init(self):
        '''
        Testing the ocnstructor
        '''
        self.assertEquals(self.queue.capacity_queue, 3,"The attributes size is not innitial")
    
    def test_enqueue(self):
        '''
        Test the enqueue method
        '''
        self.queue.enqueue(4)

        self.assertEqual(self.queue.end - self.queue.start, 1, "Number")
        self.assertEqual(self.queue.start, 0, "")
        self.assertEqual(self.queue.end, 1, "")
        self.queue.enqueue(2)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.end - self.queue.start, 3, "Number")

    def test_dequeue(self):
        '''
        Test dequeue method
        '''
        self.queue.dequeue()
        self.queue.enqueue(6)
        self.queue.enqueue(3)
        self.queue.enqueue(1)
        self.queue.enqueue(2)  # full noot able to add
        val_dequeue = self.queue.dequeue()  # dequeue後，有一個空位可以加
        self.assertEqual(self.queue.start, 1, "Bug in start attribute")
        self.assertEqual(val_dequeue, 6, "Incorrect")
        self.queue.enqueue(2) #可以成功加入

unittest.main()

# start 是指當前node的位置？ans: 是的
# end 是指當前的下一個node的位置？ ans:是的

# dequeue 會是在test method中最先run的(按字母), 所以要小心dequeue會是空的情況

#self.queue = Queue(3)的解釋：https://chatgpt.com/share/6753da3c-96ac-8001-8b57-e890f9deaf2f 
