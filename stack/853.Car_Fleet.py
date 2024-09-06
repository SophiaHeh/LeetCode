class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #(solution2)-Without using zip function
        cars = []
        for i in range(len(position)): #create a pair value without using zip()
            cars.append([position[i], speed[i]])
        #sort cars by position in descending order
        cars.sort(key= lambda x: x[0], reverse= True)
        stack = []
        for p, s in cars:
            stack.append((target - p) / s)
        #use if, instead of using while  
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                 
                stack.pop()
        return len(stack)    
