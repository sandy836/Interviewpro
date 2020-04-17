class MaxStack:
  def __init__(self):
      self.stack = []

  def push(self, val):
    if not self.stack:
        self.stack.append((val, val))
    else:
        self.stack.append((val, max(val, self.stack[-1][1])))

  def pop(self):
      self.stack.pop()

  def max(self):
      return self.stack[-1][1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
s.push(5)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
2