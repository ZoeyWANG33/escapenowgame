import js
p5 = js.window

from Player import *
from Mushroom import *
from Toxic import *
from MagicBottle import *
from Bullet import *
from Stone import *
from Door import *
from Key import *

sound1 = p5.loadSound('data/heal.wav')  
sound2 = p5.loadSound('data/poison.wav')  
sound3 = p5.loadSound('data/mushroom.wav')  
sound4 = p5.loadSound('data/win.wav')  
sound5 = p5.loadSound('data/getkey.wav') 
sound4_played = False
font = p5.loadFont('data/PressStart2P.otf')
heart_img = p5.loadImage('data/heart.png')
program_state = 'START'

player = Player()
hasKey = False
door = Door()

bullet_list = []
key_list = []
mushroom_list = []
toxic_list = []
magicbottle_list = []
stone_map = []
key = None


def againAll():
  global bullet_list
  global key_list
  global mushroom_list
  global toxic_list
  global magicbottle_list
  global stone_map
  global hasKey
  global key
  position_list = []
  key_list = []
  while(len(position_list) < 21):
    x = int(p5.random(1, 8))
    y = int(p5.random(1, 8))
    if(x, y) not in position_list:
      if((x, y) != (0, 0)) and ((x, y) != (7, 7)):
        position_list.append((x, y))
        
  mushroom_position_list = position_list[0: 8]
  mushroom_list = []
  for i in range(8):
    mushroom = Mushroom(mushroom_position_list[i])
    mushroom_list.append(mushroom)
  
  
  toxic_position_list = position_list[8: 16]
  toxic_list = []
  for i in range(8):
    toxic = Toxic(toxic_position_list[i])
    toxic_list.append(toxic)
  
  
  magicbottle_position_list = position_list[16: 20]
  magicbottle_list = []
  for i in range(4):
    magicbottle = MagicBottle(magicbottle_position_list[i])
    magicbottle_list.append(magicbottle)
  
  
  key_position = position_list[20]
  key = Key(key_position)
  key_list.append(key)

  stone_map = []
  for i in range(8):
    stone_row = []
    for j in range(8):
      stone_row.append(Stone(32+64*i, 32+64*j, ((i,j)!=(0,0)) and ((i,j)!=(7,7))))
    stone_map.append(stone_row)

  hasKey = False

def setup():
  p5.createCanvas(512, 600) 
  p5.rectMode(p5.CENTER)
  p5.imageMode(p5.CENTER)
  p5.textFont(font)
  p5.textSize(50)


def draw():
  global key
  global door
  global player 
  global toxic_list
  global magicbottle_list
  global mushroom_list
  global stone_map
  global bullet_list
  global key_list
  global program_state
  global sound4_played
  p5.background(0) 
  p5.fill(0)  # fill with black
  p5.noStroke()  # no stroke
  # show cursor coordinates:
  p5.text((int(p5.mouseX), int(p5.mouseY)), 10, 20)
  p5.strokeWeight(1)  # 1-pixel stroke
  if(program_state == 'START'):
    p5.fill(255)
    p5.text('Start', 135, 270)
  if(program_state == 'PLAY'):
    p5.image(heart_img, 245, 550, heart_img.width/2, heart_img.height/2)
    p5.fill(255)
    p5.textSize(20)
    p5.text(player.life, 270, 560)
    player.draw()
  
    #for i in range(8):
    for i in range(len(mushroom_list)):
      mushroom_list[i].draw()
  
    #for i in range(8):
    for i in range(len(toxic_list)):
      toxic_list[i].draw()
  
    #for i in range(4):
    for i in range(len(magicbottle_list)):
      magicbottle_list[i].draw()
  
    for i in range(len(bullet_list)):
      bullet_list[i].draw()
      bullet_list[i].update()
  
    for i in range(len(key_list)):
      key_list[i].draw()
    door.draw()
  
    for i in range(len(stone_map)):
      for j in range(len(stone_map[i])):
        stone_map[i][j].draw()
      
    collect()

  if(program_state == 'WIN'):
    p5.fill(237, 250, 0)
    p5.textSize(40)
    p5.text('You Escaped!', 30, 270)
    if (sound4_played == False):
      sound4.play()
      sound4_played = True

  if(program_state == 'LOSE'):
    p5.fill(255)
    p5.textSize(40)
    p5.text('You Died!', 50, 270)
    
  

def collect():
  global key
  global door
  global player 
  global toxic_list
  global magicbottle_list
  global mushroom_list
  global bullet_list
  global key_list
  global hasKey
  global stone_map
  global program_state
  
  for i in range(len(mushroom_list)-1, -1, -1):
    if (player.getGrid() == (mushroom_list[i].x, mushroom_list[i].y)):
      # print('remove mushroom_list item', i)
      sound3.play()
      mushroom_list.pop(i)
      # print('life = ', player.life)

  for i in range(len(toxic_list)-1, -1, -1):
    if (player.getGrid() == (toxic_list[i].x, toxic_list[i].y)):
      toxic_list.pop(i)
      sound2.play()
      player.changeLife(-2)
      # print('life = ', player.life)

  for i in range(len(magicbottle_list)-1, -1, -1):
    if (player.getGrid() == (magicbottle_list[i].x, magicbottle_list[i].y)):
      magicbottle_list.pop(i)
      sound1.play()
      player.changeLife(1)
      # print('life = ', player.life)

  if (player.getGrid() == (key.x, key.y)):
    if (key_list != []):
      hasKey = True
      key_list.pop()
      sound5.play()
    # print('hasKey =', hasKey)

  j = len(bullet_list) - 1
  while(j >= 0):
    x,y = bullet_list[j].getGrid()
    if x > 7 or x<0 or y> 7 or y<0:
      bullet_list.pop(j)
    elif stone_map[x][y].exist:
      stone_map[x][y].exist = False
      bullet_list.pop(j)
    j -= 1
  # print(player.getGrid(), hasKey, program_state)  
  
  if (player.getGrid() == (7, 7)):
    if(hasKey == True):
      program_state = 'WIN'

  if (player.life <= 0):
    program_state = 'LOSE'


def getGrid(x,y):
  return (x//64, y//64)
  

def canMove(player, dx, dy, stoneMap):
  tx, ty = getGrid(player.x+dx,player.y+dy)
  return not stoneMap[tx][ty].exist
    
  
def keyPressed(event):
  global bullet_list
  # print('key pressed.. ' + p5.key)
  if(p5.key == 'ArrowRight'):
    if canMove(player,5,0,stone_map):
      player.move(5, 0)
  if(p5.key == 'ArrowLeft'):
    if canMove(player,-5,0,stone_map):
      player.move(-5, 0)
  if(p5.key == 'ArrowUp'):
    if canMove(player,0,-5,stone_map):
      player.move(0, -5)
  if(p5.key == 'ArrowDown'):
    if canMove(player,0,5,stone_map):
      player.move(0, 5)
  
  if (bullet_list == []):
    if(p5.key == 's'):
      bullet = Bullet(player.x, player.y, 0, 5)
      bullet_list.append(bullet)
    elif(p5.key == 'w'):
      bullet = Bullet(player.x, player.y, 0, -5)
      bullet_list.append(bullet)
    elif(p5.key == 'a'):
      bullet = Bullet(player.x, player.y, -5, 0)
      bullet_list.append(bullet)
    elif(p5.key == 'd'):
      bullet = Bullet(player.x, player.y, 5, 0)
      bullet_list.append(bullet)




def keyReleased(event):
  pass

def mousePressed(event):
  global program_state
  global sound4_played
  if(program_state == 'START'):
    againAll()
    program_state = 'PLAY'
    sound4_played = False
    player.restart()

  if(program_state == 'LOSE'):
    againAll()
    program_state = 'PLAY'
    sound4_played = False
    player.restart()

  if(program_state == 'WIN'):
    againAll()
    program_state = 'PLAY'
    sound4_played = False
    player.restart()


    # print('program_state = ' + program_state)

def mouseReleased(event):
  pass