class Stack:
    '''
    Design of a stack
    '''

    def __init__(self, size: int, end: int = 0): #不需要start
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
        if self.end == self.size:
            print('Stack is full, cannot push more elements')
            return
        self.elements[self.end] = elem
        self.end += 1
        
    def pop(self):
        '''
        Pop method

        Return:
            popped element from the stack
        '''
        if self.end == 0:
            print('Stack is empty, cannot pop any element')
            return
        
        self.end -= 1
        popped_elem = self.elements[self.end] #why not self.elements[self.end + 1], ans: 因為end 本身是指向下一個空位的指針，減1剛好是指到當前的元素
        self.elements[self.end] = None
        return popped_elem
    
    def len_stack(self):
        '''
        Compute number of elements in the stack (Different than size/capacity of the stack)
        '''
        return self.end #注意不用減1，length從1開始數，index是從0開始數
        
        
# end是指向下一個空位的指針？ ans: yes
# test stack的時候，test順序是：
# set up -> test_init -> set up -> test_pop -> set up -> test_push (按字母順序)
# 每一次函數完整測試結束後會得到一個“句號.”
