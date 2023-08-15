import js
p5 = js.window

class Bullet:
  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.fill(255, 0, 127)
    p5.rect(0, 0, 4, 4)
    p5.pop()

  def update(self):
    self.x += self.vx
    self.y += self.vy
    
  def getGrid(self):
    return (self.x//64, self.y//64)
    