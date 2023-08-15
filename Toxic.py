import js
p5 = js.window

class Toxic:  
  def __init__(self, pos):
    self.img = p5.loadImage('data/Toxic.png')
    # self.x = int(p5.random(1, 8))
    # self.y = int(p5.random(1, 8)) 
    self.x = pos[0]
    self.y = pos[1] 


  def draw(self):
    p5.push()
    p5.translate(self.x*64 + 32, self.y*64 + 32)
    p5.image(self.img, 0, 0, self.img.height*0.9, self.img.width*0.9)
    p5.pop()