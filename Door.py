import js
p5 = js.window

class Door:  
  def __init__(self):
    self.img = p5.loadImage('data/Door.png')
    self.x = 480
    self.y = 480

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, self.img.width*1.3, self.img.height*1.3)
    p5.pop()