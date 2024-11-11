class MyString:
  def __init__(self, s):
    self.s = s

  def __getitem__(self, k):
    return self.s[k]

  def __len__(self):
    return len(self.s)

mystr = MyString(input())

print(mystr[0])
print(mystr[7])
print(mystr[-1])

for char in mystr:
  print(char, end="")

