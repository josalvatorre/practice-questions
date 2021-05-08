import operator


# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def pop(self):
        top_i = len(self.stack) - 1

        for stack in (self.min_stack, self.max_stack):
            if self.stack[stack[-1]] == self.stack[top_i]:
                stack.pop()

        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def push(self, number):
        self.stack.append(number)
        number_i = len(self.stack) - 1

        for stack, insert_yes in (
            (self.min_stack, operator.le),
            (self.max_stack, operator.ge),
        ):
            if len(stack) == 0 or insert_yes(number, self.stack[stack[-1]]):
                stack.append(number_i)
        pass

    def get_min(self):
        if len(self.stack) > 0:
            return self.stack[self.min_stack[-1]]
        return None

    def get_max(self):
        if len(self.stack) > 0:
            return self.stack[self.max_stack[-1]]
        return None
