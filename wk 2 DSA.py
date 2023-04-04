# Python program for implementation of Bubble Sort


def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

# if __name__ == "__main__":
# arr = [5, 1, 4, 2, 8]
# bubbleSort(arr)
# print(arr)

# Optimized

def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if (swapped == False):
			break

# arr1 = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(arr1)

# print(arr1)

#selection sort
def selection_sort(arr):
	n = len(arr)
	for i in range(n-1):
		min = i
		for j in range(i+1,n):
			if arr[min] > arr[j]:
				min = j
		arr[i], arr[min] = arr[min], arr[i]


# arr1 = [64, 34, 25, 12, 22, 11, 90, 89]
# selection_sort(arr1)
# print(arr1)

#Insertion Sort

def insertion_sort(array):
	n = len(array)
	for i in range(1,n):
		key = array[i]
		j = i-1
		while j>=0 and key < array[j]:
			array[j+1] = array[j]
			j-=1
		array[j+1] = key
# arr1 = [64, 34, 25, 12, 22, 11, 90, 89]
# insertion_sort(arr1)
# print(arr1)
#defining merge
def merge(list1, list2):
	combined = []
	i = 0
	j = 0
	while i < len(list1) and j < len(list2):
		if list1[i] < list2[j]:
			combined.append(list1[i])
			i+=1
		else:
			combined.append(list2[j])
			j+=1
	while i < len(list1):
		combined.append(list1[i])
		i+=1
	while j < len(list2):
		combined.append(list2[j])
		j+=1
	return combined

# print(merge([1,1,1,2,7,8],[1,3,4,5,6]))

def merge_sort(my_list):
	if len(my_list) == 1:
		return  my_list
	mid_index = len(my_list)//2
	left = merge_sort(my_list[:mid_index])
	right = merge_sort(my_list[mid_index:])

	return merge(left,right)

# list = [1,2,3,4,5,67,4,232,4,2]
# print(list)
# print(merge_sort(list))
#swap
def swap(my_list,index1,index2):
	temp = my_list[index1]
	my_list[index1] = my_list[index2]
	my_list[index2] = temp

#pivot
def pivot(my_list, pivot_index, end_index):
	swap_index = pivot_index

	for i in range(pivot_index+1,end_index+1):
		if my_list[i] < my_list[pivot_index]:
			swap_index+=1
			swap(my_list,swap_index,i)
	swap(my_list, pivot_index, swap_index)
	return swap_index

def quick_sort_helper(my_list, left, right):
	if left < right:
		pivot_index = pivot(my_list, left, right)
		quick_sort_helper(my_list, left, pivot_index-1)
		quick_sort_helper(my_list, pivot_index+1, right)
	return my_list

def quick_sort(my_list):
	return quick_sort_helper(my_list, 0, len(my_list)-1)


# arr = ['a','s','d','w','e','a','f','a','w']
# print(quick_sort(arr))

#Stack
# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None
#
# class Stack:
# 	def __init__(self):
# 		self.top = None
# 		self.length = 0
#
# 	def print_stack(self):
# 		temp = self.top
# 		if temp is None:
# 			print("stack is empty")
# 		else:
# 			while temp is not None:
# 				print(temp.value)
# 				temp = temp.next
#
# 	def push(self, value):
# 		new_node = Node(value)
# 		if self.length == 0:
# 		# if self.top is None:
# 			self.top = new_node
# 		else:
# 			new_node.next = self.top
# 			self.top = new_node
# 		self.length += 1
#
# 	def pop(self):
# 		# if self.length == 0:
# 		if self.top is None:
# 			return None
# 		else:
# 			temp = self.top
# 			self.top = self.top.next
# 			temp.next  = None
# 			self.length -= 1
# 			return temp.value




# ss = Stack()
# ss.push(45)
# ss.push(56)
#
# print(ss.pop())
# ss.print_stack()

#QUEUE
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def print_queue(self):
		if self.first is None:
			print("Queue is empty")
		else:
			temp = self.first
			while temp is not None:
				print(temp.value)
				temp = temp.next

	def enqueue(self,value):
		new_node = Node(value)
		if self.first is None:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node
		self.length +=1

	def dequeue(self):
		if self.first is None:
			return None
		temp = self.first
		if self.first == self.last:
			self.first = None
			self.last = None
		else:
			self.first = self.first.next
			temp.next = None
		self.length -= 1
		return temp.value

# q1 = Queue()
# q1.enqueue(45)
# q1.enqueue(85)
# print(q1.dequeue())
# print(q1.dequeue())
# print(q1.dequeue())
#HASH TABLE


class HashTable:
	def __init__(self, size = 7):
		self.data_map = [None] * size

	def _hash(self,key):
		my_hash = 0
		for letter in key:
			my_hash = my_hash + ord(letter)
		return my_hash % len(self.data_map)

	def print_table(self):
		for i, val in enumerate(self.data_map):
			print(i, ": ", val)

# seperate chaining
	def set_item(self, key, value):
		index = self._hash(key)
		if self.data_map[index] == None:
			self.data_map[index] = []
			self.data_map[index].append([key, value])
		else:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    self.data_map[index][i][1] = value
                    return
            self.data_map[index].append([key, value])

	def remove_item(self, key):
		index = self._hash(key)
		if self.data_map[index] is not None:
			for i in range(len(self.data_map[index])):
				if self.data_map[index][i][0] == key:
					self.data_map[index].pop(i)
					return




	def get_item(self, key):
		index = self._hash(key)
		if self.data_map[index] is not None:
			for i in range(len(self.data_map[index])):
				if self.data_map[index][i][0] == key:
					return self.data_map[index][i][1]
		return None

# linear probing
	def set(self, key, value):
	    index = self._hash(key)
	    if self.data_map[index] == None:
	        self.data_map[index] = []
	        self.data_map[index].append([key, value])
	    else:
	        i = index
	        while self.data_map[i] != None and self.data_map[i][0] != key:
	            i = (i + 1) % len(self.data_map)
	        if self.data_map[i] == None:
	            self.data_map[i] = []
	        if self.data_map[i][0] == key:
	            self.data_map[i][1] = value
	        else:
	            self.data_map[i].append([key, value])

	def get(self, key):
		index = self._hash(key)
		i = index
		while self.data_map[i] != None:
			if self.data_map[i][0] == key:
				return self.data_map[i][1]
			i = (i + 1) % len(self.data_map)
			if i == index:
				break
		return None

	def keys(self):
		all_keys = []
		for i in range(len(self.data_map)):
			if self.data_map[i] is not None:
				for j in range(len(self.data_map[i])):
					all_keys.append(self.data_map[i][j][0])
		return all_keys



my_hash = HashTable()
my_hash.set_item('bolts', 198)
my_hash.set_item('nuts', 1354)
my_hash.set_item('washers', 1873)
my_hash.print_table()
print(my_hash.get_item('washers'))
print(my_hash.get_item('wash'))
print(my_hash.keys())



