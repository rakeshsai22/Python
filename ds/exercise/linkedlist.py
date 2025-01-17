class Node:
    def __init__(self, data = None, next =None):
        self.data = data
        self.next = next 

class linkedlist:
    def __init__(self):
        self.head=None # points to the head

    def insert_at_beg(self, data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        # print the linked list
        itr = self.head
        llstr = ''
        while itr:
            llstr +=str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None) # as insertion is at the end the next is None
            return
        itr = self.head
        while itr.next:
            itr=itr.next

        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    #  length of linked list
    def getlen(self):
        count =0
        itr = self.head
        while itr.next:
            count+=1
            itr=itr.next
        print(f"len of linked list:{count}")
        return count
    def remove_at(self, index):
        if index<0 or index>=self.getlen():
            # print("invalid Index")
            raise Exception("Invalid Index")
        
        if index ==0:
            self.head = self.head.next
            return
        
        count =0
        itr =self.head
        while itr:
            if count == index -1:
                itr.next=itr.next.next
                break
            itr = itr.next
            count+=1

    def insert_at(self, index,data):
        if index<0 or index > self.getlen():
            raise Exception("Invalid Index")
        if index ==0:
            self.insert_at_beg(data)
            return
        count =0
        itr=self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr=itr.next
            count+=1



if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_at_beg(5)
    ll.insert_at_beg(12)
    ll.insert_at_end(7)
    ll.insert_at_end(88)
    ll.insert_values(["Hello", "world","!!"])
    ll.getlen()
    # remove an element from the given location
    ll.remove_at(1)
    # ll.remove_at(-2)
    # insert at index
    ll.getlen()
    ll.print()
    ll.insert_at(1,"World")
    ll.print()