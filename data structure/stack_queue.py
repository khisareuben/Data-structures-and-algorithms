from queue import LifoQueue

stack = LifoQueue(maxsize = 20) 
stack.put("welcome")
stack.put("to")
stack.put("dsa")
print(stack.full())
print(stack.qsize())
print(stack.get())

