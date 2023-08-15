import js
p5 = js.window

class Stone:  
  def __init__(self, x, y, exist=True):
    self.img = p5.loadImage('data/Stone.png')
    self.x = x
    self.y = y
    self.exist = exist

  def draw(self):
    if not self.exist:
      return
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, self.img.width*2, self.img.height*2)
    p5.pop()

  def getGrid(self):
    return (self.x//64, self.y//64)

    