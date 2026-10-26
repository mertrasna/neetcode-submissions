class MinStack:

    def __init__(self):
        self.dynamic_array = []
        self.min_stack = []        

    def push(self, val: int) -> None:
        self.dynamic_array.append(val)
        if not self.min_stack:
            self.min_stack.append(val) 
        elif self.min_stack[-1] >= val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.dynamic_array.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.dynamic_array[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

