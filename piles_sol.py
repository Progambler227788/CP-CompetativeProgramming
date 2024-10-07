

# # 1,2,3 ->

# def MaxScore(a, b, c):

#     # Write your code here
#       score = 0
#       newValue =[a] + [b] +[c]
#       while (newValue[0]>0 and newValue[1]>0) or (newValue[1]>0 and newValue[2]>0) or (newValue[0]>0 and newValue[2]>0):
#           newValue = sorted(newValue)
#           print(newValue)
#           newValue[1] = newValue[1] - 1
#           newValue[2] = newValue[2] - 1 # last 2 big 
#           score+=1
#       print(score)
# a = int(input())
# b = int(input())
# c = int(input())
# MaxScore(a, b, c)




class Node:
    def __init__(self, newValue):
        self.newValue = newValue  
        self.next = None  
class MyLinkingList:
    def __init__(self):
        self.main = None  

    def adding(self, newValue):
        new_node = Node(newValue)
        if self.main is None:  
            self.main = new_node
            return
        last = self.main
        # iterate while there is node at next of main like 1-2-3 then insert at next of 3
        while last.next:  
            last = last.next
        last.next = new_node

    def insert_at_start(self, newValue):
        new_node = Node(newValue)
        new_node.next = self.main 
        self.main = new_node  

    def delete_char(self, newValue):
        current = self.main
        previous = None
        # If the main node itself holds the key to be deleted
        if current is not None:
            if current.newValue == newValue:
                self.main = current.next  # Change main
                current = None 
                return
            
        while current is not None:
            if current.newValue == newValue:
                break
            previous = current
            current = current.next

        if current == None:
            return
        previous.next = current.next
        current = None


# Create a new linked list
linked_list = MyLinkingList()

# Append characters to the linked list to represent "tea#eat"
for char in "tea#eat":
    linked_list.adding(char)

# Print the initial state of the linked list
print("Initial linked list:")
linked_list.print_list()

# Insert '%' at the beginning of the linked list
linked_list.insert_at_start('%')

# Print the linked list after insertion
print("After inserting '%':")
linked_list.print_list()

# Delete '#' from the linked list
linked_list.delete_char('#')

# Print the linked list after deletion
print("After deleting '#':")
linked_list.print_list()
