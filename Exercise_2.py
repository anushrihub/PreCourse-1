
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.top = None

    # push is working 
    def push(self, data):
        new_node = Node(data)
        # new node is an object and it contains the data

        if self.top:
        # if there is something in the stack new_node's pointer will point to that top
            new_node.next = self.top
        # if there is nothing already then new node become top
        self.top = new_node

    # pop is working   
    def pop(self):
        if self.top:
            popped = self.top
            self.top = popped.next
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
