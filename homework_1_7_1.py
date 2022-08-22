class Stack:
	def __init__(self):
		self.stack = []
		self.brackets_dict = {'}': '{', ')': '(', ']': '['}

	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		else:
			return False

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		removed_item = self.stack.pop()
		return removed_item

	def peek(self):
		if len(self.stack) == 0:
			return 'Stack is empty'
		else:
			return self.stack[-1]

	def size(self):
		return len(self.stack)


def stack_is_balanced(brackets_list):
	stack_example = Stack()
	brackets_list = brackets_list
	for bracket in brackets_list:
		if bracket in ['(', '{', '[']:
			stack_example.push(bracket)
		if bracket in [')', '}', ']']:
			if stack_example.peek() == stack_example.brackets_dict[bracket]:
				stack_example.pop()
			else:
				return 'Несбалансированно'
	return 'Сбалансированно'


print(stack_is_balanced('(((([{}]))))'))
print(stack_is_balanced('[([])((([[[]]])))]{()}'))
print(stack_is_balanced('{{[()]}}'))
print(stack_is_balanced('}{}'))
print(stack_is_balanced('{{[(])]}}'))
print(stack_is_balanced('[[{())}]'))
