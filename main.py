class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i  
class CircularQueue:
    def init(self, k):
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = k

    def enqueue(self, value):
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return -1
        value = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def rear(self):
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1) % self.capacity]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity       

def find_max(arr):
    if not arr:
        return None
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Example usage:
input_arr = [1, 2, 3, 4, 5]
print("Maximum element:", find_max(input_arr))  # Output: 5


def reverse_string(input_string):
    if not input_string:
        return ""
    stack = []
    for char in input_string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

# Example usage:
input_string = "hello"
print("Reversed string:", reverse_string(input_string))  # Output: "olleh"