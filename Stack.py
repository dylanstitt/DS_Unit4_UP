# Dylan Stitt
# Unit 4 Lab 1
# ArrayStack

class ArrayStack:

    def __init__(self):
        self.__stack = []
        self.__size = 0


    def __str__(self):
        """Display contents of stack"""
        out = ""
        for ele in self.__stack:
            out += str(ele) + ' '

        out += "<TOP"
        return out


    def __len__(self):
        """Return the length of the stack"""
        return self.__size


    def __is_empty(self):
        """Return True if the stack is empty"""
        if self.__size == 0:
            return True
        return False


    def push(self, ele):
        """Add an element to the top of the stack"""
        self.__stack.append(ele)
        self.__size += 1


    def pop(self):
        """Remove and return the top element of the stack"""
        if not self.__is_empty():
            delValue = self.__stack[-1]
            del self.__stack[-1]
            self.__size -= 1

            return delValue
        else:
            raise IndexError("Stack is empty")


    def top(self):
        """Return the top element of the stack"""
        if not self.__is_empty():
            return self.__stack[-1]
        else:
            raise IndexError("Stack is empty")

    # Lab Specific
    def displayRod(self, name):
        '''Displays the towers of the game'''
        joinStr = ''.join(self.__stack)
        joinStr += '-'*(5-self.__size)
        print(f'{" ".join(joinStr)} | {name}')
