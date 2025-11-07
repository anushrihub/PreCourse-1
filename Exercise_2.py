
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.current_node = None
        self.previous_node = None

    def push(self, data):
        if self.current_node:
            self.previous_node = self.current_node
        
        self.current_node = Node(data)

        if self.previous_node:
            self.previous_node.next = self.current_node

        
    def pop(self):
        if self.current_node:
            popped = self.current_node
            print(self.previous_node.data)
            if self.previous_node:
                self.current_node = self.previous_node
                self.previous_node = None
            else:
                self.current_node = None
            return popped.data
        return None

        
a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
