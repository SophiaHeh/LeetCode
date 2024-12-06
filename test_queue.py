import unittest
from queue import Queue:
    class TestQueue(unittest.TestCase):
        def setUp(self):
            '''
            Initialize some test cases
            '''
            self.queue = Queue(3)

        def test_init(self):
            '''
            Testing the ocnstructor
            '''

            self.assertEquals(self.queue.capacity_queue, 5,
                              "The attributes size is not innitial")
            self.assertEqual(self.queue.start, )

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


# start 是指當前node的位置？
# end 是指當前的下一個node的位置？

# dequeue 會先run, 所以要小心dequeue會是空的情況
