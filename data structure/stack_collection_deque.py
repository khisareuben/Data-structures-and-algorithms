# deque is the same as stack_list but its much faster

from collections import deque

stack = deque()
stack.append("welcome")
stack.append("to")
stack.append("dsa")
print(stack)
print(stack.pop()) # to delete a element in the stack
print(stack)
