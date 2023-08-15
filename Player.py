import js
p5 = js.window

# class definition for the Spaceship object:
class Player():  
  def __init__(self):
    self.img = p5.loadImage('data/Player.png')
    self.x = 32
    self.y = 32
    self.life = 5
  
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0)
    p5.pop()

  def move(self, distance_x, distance_y):
    self.x += distance_x
    self.y += distance_y

  def changeLife(self, change):
    self.life += change

  def getGrid(self):
    return (self.x//64, self.y//64)
  
  def restart(self):
    self.x = 32
    self.y = 32
    self.life = 5
    


    
    