'''
print a cube with any side length to console 
'''
class Cube:
  def __init__(this, side = 8):
    this.side = side
  def printCube(this):
    for i in range(this.side):
      for j in range(this.side - i - 1): print(' ', end='')
      for j in range(this.side): print(' #', end='')
      for k in range(i): i >= 1 and print(' ', end='')
        
      if i > 0: print('#', end='')
      print()
    for i in range(this.side - 1):
      for j in range(this.side): print(' #', end='')
      for j in range(this.side - 2, i, -1): print(' ', end='')
      i != this.side - 2 and print('#', end='')
      print()

cube = Cube(12)
cube.printCube()
      