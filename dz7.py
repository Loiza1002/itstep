class MyIterable:
  def __init__(self, data):
      self.data = data

  def __iter__(self):
     for item in self.data:
      yield item

it = MyIterable([1, 2, 3, 4, 5])

for item in it:

   print(item)