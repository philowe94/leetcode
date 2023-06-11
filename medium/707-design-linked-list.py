import pdb;

class MyLinkedList:

    def __init__(self):
        self.val = None
        self.next = None

    def get(self, index: int) -> int:

        if index < 0:
            return -1

        current = self
        
        for x in range(0, index):
            if current.next:
                current = current.next
            else:
                return -1
        
        if current.val is None:
            return -1
        else:
            return current.val
        

    def addAtHead(self, val: int) -> None:
        current = MyLinkedList()
        current.next = self.next
        current.val = self.val
        self.val = val

        if current.val is None:
            self.next = None
        else:
                        self.next = current


    def addAtTail(self, val: int) -> None:

        if self.val is None:
            self.val = val
            return

        #traverse to the end of the lst
        current = self
        while current.next:
            current = current.next
              
        current.next = MyLinkedList()
        current.next.val = val
        current.next.next = None


    def addAtIndex(self, index: int, val: int) -> None:
        #illegal index
        if index < 0:
            return

        #add at head
        if index == 0:
            self.addAtHead(val)
            return

        current = self

        #traverse to the index
        while current and index > 1:
            current = current.next
            index -= 1

        if current is None:
            return
        
        if current.next is None:
            current.next = MyLinkedList()
            current.next.val = val
            current.next.next = None
        else:
            new_node = MyLinkedList()
            new_node.val = val
            new_node.next = current.next
            current.next = new_node


    def deleteAtIndex(self, index: int) -> None:

        if index == 0:
            if self.next:
                self.val = self.next.val
                self.next = self.next.next
            else:
                self.val = None
            return
        
        if index == 1:
            if self.next:
                self.next = self.next.next
                return
            else:
                return

        current = self


        while current and index > 1:
            current = current.next
            index -= 1
        
        if current is None:
            return

        if current.next is None:
            return
        else:
            current.next = current.next.next

    
    def print(self):
        current = self
        stringarr = []
        while current:
            stringarr.append(str(current.val))
            current = current.next

        print("->".join(stringarr))

    def test(self, functions, params):
        for i in range(0, len(functions)):
            print("function: ", functions[i])
            print("params: ", params[i])
            if functions[i] == "addAtHead":
                self.addAtHead(params[i][0])
            elif functions[i] == "addAtTail":
                self.addAtTail(params[i][0])
            elif functions[i] == "addAtIndex":
                self.addAtIndex(params[i][0], params[i][1])
            elif functions[i] == "deleteAtIndex":
                self.deleteAtIndex(params[i][0])
            elif functions[i] == "get":
                print("get: ", self.get(params[i][0]))
            self.print()
            print("-----")


# funs = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
# params = [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]

funs = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
params = [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]

obj = MyLinkedList()
obj.test(funs, params)