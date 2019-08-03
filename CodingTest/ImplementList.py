# 리스트를 구현하시오.

# 노드 구현
class Node_:
	# 생성자
	def __init__(self, data):
		self.data = data
		self.next = None

# 리스트 구현	
class List_:
	# 생성자
	def __init__(self):
		HeadNode = Node_("헤드")
		self.head = HeadNode
		self.tail = HeadNode
		self.NumOfData = 0
	
	# 노드 삽입	
	def insert(self, data):
		newNode = Node_(data)
		self.tail.next = newNode
		self.tail = newNode
		self.NumOfData += 1
		
	# 노드 삭제
	def delete(self, data):
		pass
	
