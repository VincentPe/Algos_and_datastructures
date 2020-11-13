#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.max_stack) == 0:
            self.max_stack.append(a)
        elif self.max_stack[-1] < a:
            self.max_stack.append(a)
        else: 
            self.max_stack.append(self.max_stack[-1])

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        del(self.max_stack[-1])

    def Max(self):
        assert(len(self.__stack))
        return self.max_stack[-1]

## Example 1
#stacky = StackWithMax() 
#stacky.Push(2)
#stacky.Push(1)
#stacky.Max()
#stacky.Pop()
#stacky.Max()
#
#
## Example 2  
#stacky = StackWithMax() 
#stacky.Push(1)
#stacky.Push(2)
#stacky.Max()
#stacky.Pop()
#stacky.Max()
        
    





if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
