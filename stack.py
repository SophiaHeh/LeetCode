class Stack:
    '''
    Design of a stack
    '''

    def __init__(self, size: int, end: int = 0):
        '''
        Constructor of Stack

        Args:
            size: int representing the capacity of the stack
            end: int representing the index of the end of the stack
        '''
        self.size = size
        self.end = end
        self.elements = [None]*size  # 這裡的elements是指什麼呢？

    def push(self, elem):
        '''
        Push method

        Arg:
            elem: variable to be added to the stack
        '''

# end是指向下一個空位的指針？
# test stack的時候，test順序是：
# set up -> test_init -> set up -> test_pop -> set up -> test_push (按字母順序)
# 每一次函數完整測試結束後會得到一個“句號.”
