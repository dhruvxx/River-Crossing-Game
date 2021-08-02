import pygame
from config import *
pygame.init()

#setting the screen size

(width, height) = (800,600)
FPS = 60
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Assignment3-game')

time = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

#background image
bg = pygame.image.load("Water.jpg")
bg = pygame.transform.scale(bg, (width, height))
#pygame.mixer.music.load("")

turn = 1
level = 0
points = []
#image's initial position
x = 375
y = 580
width1 = 40
height1 = 40
velocity = 5


#class for both the players
class Player(pygame.sprite.Sprite):
  def __init__(self, pos, *groups):
    super().__init__(*groups)
    self.image = pygame.image.load('mermaid.png')
    self.image1 = pygame.transform.smoothscale(screen, (50,50))
    self.rect = self.image.get_rect(center=pos)

#for fixed obstacles
class Enemy(pygame.sprite.Sprite):
 def __init__(self, pos, *groups):
   super().__init__(*groups)
   self.image = pygame.image.load('submarine.png')
   self.image1 = pygame.transform.smoothscale(screen, (45,45))
   self.rect = self.image.get_rect(center=pos)

#for moving obstacles
class Enemy_move(pygame.sprite.Sprite):
 def __init__(self, pos, *groups):
   super().__init__(*groups)
   self.image = pygame.image.load('shark.png')
   self.image1 = pygame.transform.smoothscale(screen, (45,45))
   self.rect = self.image.get_rect(center=pos)

#adding the changes to our screen
all_sprites = pygame.sprite.Group()


#to make the partitions 
class Tile1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width,40))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.y = 80

class Tile2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width,40))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.y = 180

class Tile3(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width,40))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.y = 280

class Tile4(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width,40))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.y = 380

class Tile5(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width,40))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.y = 480

class Tile6(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width,40))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.y = 559

class Tile7(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width,40))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.y = 0


all_sprites.add(Tile1())
all_sprites.add(Tile2())
all_sprites.add(Tile3())
all_sprites.add(Tile4())
all_sprites.add(Tile5())
all_sprites.add(Tile6())
all_sprites.add(Tile7())

enemy_move = pygame.sprite.Group()
enemy_group = pygame.sprite.Group(Enemy((100, 500)), Enemy((600, 500)), Enemy((200, 100)), Enemy((350, 100)), Enemy((600, 100)), Enemy((100, 200)), Enemy((500, 200)), Enemy((400, 300)), Enemy((350, 400)), Enemy((600, 400)))



#initial positions of the moving obstacles
xlist = [0, 300, 500, 200, 400, 700, 400, 550, 700, 300, 600, 800]
ylist = [250, 250, 250, 350, 350, 350, 450, 450, 450, 150, 150, 150]
move_list = []
for i in range (12):
	move_list.append(Enemy_move((xlist[i],ylist[i]), enemy_move))
all_sprites.add(enemy_group)
all_sprites.add(enemy_move)
player = Player((x, y), all_sprites)
#deciding the winner on the basis of scores
def winner():
	global seconds
	score1 = points[0] + points[2] + points[4]
	score2 = points[1] + points[3] + points[5]
	if (score1 > score2):
		text3 = text.render("WINNER: Player1, congrats!", False, WHITE)
	elif (score2 > score1):
		text3 = text.render("WINNER: Player2, congrats!", False, WHITE)
	else:
		text3 = text.render("WINNER: It is a draw", False, WHITE)
	screen.fill((0, 0, 0))
	screen.blit(text3, (400,300))
	pygame.display.update()


def bye():
	text1 = text4.render(" YOU HAVE LOST THE GAME", True, WHITE)
	screen.fill(BLACK)
	screen.blit(text1, (100, 300))
	pygame.display.update()

def welcome(s):
	global start_ticks
	seconds = (pygame.time.get_ticks() - start_ticks)//1000
	temp1 = s - seconds
	text1 = text4.render("YOU HAVE WON THIS ROUND WITH A SCORE OF: " + str(temp1), True, WHITE)
	screen.fill(BLACK)
	screen.blit(text1, (50, 300))
	pygame.display.update()

#where does the scoreboard appear
def score(s):
	global start_ticks
	seconds = (pygame.time.get_ticks() - start_ticks)//1000
	text1 = text.render("Score: " + str(s - seconds), False, WHITE)
	screen.blit(text1, (700, 10))

############################################################################################################################################33
#changing the player and eventually the level
def next_turn (v, t, l):
	global start_ticks, x, y, screen, all_sprites, enemy_move, enemy_group, player, xlist, ylist, velocity, turn, level, width, height
	screen = pygame.display.set_mode((width, height))
	start_ticks = pygame.time.get_ticks()
	screen.fill(BLACK)
	x = 400
	if ( t == 1):
		y = 580
	else:
		y = 10
	if l == 1:
		velocity = 5
	elif l == 2:
		velocity = 10
	else:
		velocity = 15
	all_sprites = pygame.sprite.Group()
	enemy_move = pygame.sprite.Group()
	enemy_group = pygame.sprite.Group(Enemy((100, 500)), Enemy((600, 500)), Enemy((200, 100)), Enemy((350, 100)), Enemy((600, 100)), Enemy((100, 200)), Enemy((500, 200)), Enemy((400, 300)), Enemy((350, 400)), Enemy((600, 400)))
	all_sprites.add(Tile1())
	all_sprites.add(Tile2())
	all_sprites.add(Tile3())
	all_sprites.add(Tile4())
	all_sprites.add(Tile5())
	all_sprites.add(Tile6())
	all_sprites.add(Tile7())

#initial positions of the moving obstacles
	xlist = [0, 300, 500, 200, 400, 700, 400, 550, 700, 300, 600, 800]
	ylist = [250, 250, 250, 350, 350, 350, 450, 450, 450, 150, 150, 150]
	move_list = []
	for i in range (12):
		move_list.append(Enemy_move((xlist[i],ylist[i]), enemy_move))
	for i in range(12):
		if xlist[i]>800:
			xlist[i] = 0
		else:
			xlist[i] = xlist[i]+velocity
		move_list[i].rect.center = (xlist[i],ylist[i])
	all_sprites.update()

	all_sprites.add(enemy_group)
	all_sprites.add(enemy_move)
	player = Player((x, y), all_sprites)
	all_sprites.update()
	all_sprites.draw(screen)
	pygame.display.update()
##############################################################################################################




#to quit the game when cross on the upper right corner is pressed
process = True
while process:
	pygame.time.delay(100)
	time.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			process = False
			pygame.quit()
			quit()

#using keys to move
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x > velocity:	
		x -= velocity

	if keys[pygame.K_RIGHT] and x < width - width1 - velocity:
		x += velocity

	if keys[pygame.K_UP] and y > velocity:
		y -= velocity

	if keys[pygame.K_DOWN] and y < height - height1 - velocity:
		y += velocity


	screen.fill((0, 0, 0))
	screen.blit(bg, (0, 0))	

	for i in range(12):
		if xlist[i]>800:
			xlist[i] = 0
		else:
			xlist[i] = xlist[i]+velocity
		move_list[i].rect.center = (xlist[i],ylist[i])
	all_sprites.update()


#calculating the score
	s = 0
	if turn == 1:
		temp = y + 32 
		if y <= 480:
			s = s + 10
		if y <= 380:
			s = s + 10
		if y <= 280:
			s = s + 5
		if y <= 180:
			s = s + 10
		if y <= 80:
			s = s + 15
		if y <= 140:
			s = s + 30
		if y <= 240:
			s = s + 30
		if y <= 340:
			s = s + 30
		if y <= 440:
			s = s + 30
	#if y == 0:
	#	s = s - seconds
	else:
		if y >= 480 + 32:
			s = s + 10
		if y >= 380 + 32:
			s = s + 10
		if y >= 280 + 32:
			s = s + 5
		if y >= 180 + 32:
			s = s + 10
		if y >= 80 + 32:
			s = s + 15
		if y >= 140 + 32:
			s = s + 30
		if y >= 240 + 32:
			s = s + 30
		if y >= 340 + 32:
			s = s + 30
		if y >= 440 + 32:
			s = s + 30
	
	player.rect.center = (x, y)
	
	all_sprites.update()

	#start and end for different players is defined differently
	if turn == 1:
		text1 = text.render("START", False, WHITE)
		screen.blit(text1, (400,10))
		text2 = text.render("END", False, WHITE)
		screen.blit(text2, (400, 580))
	else:
		text1 = text.render("START", False, WHITE)
		screen.blit(text1, (400,580))
		text2 = text.render("END", False, WHITE)
		screen.blit(text2, (400,10))
#on collisin with the obstacles
	hit_fixed = pygame.sprite.spritecollide(player, enemy_group, False)
	hit_move = pygame.sprite.spritecollide(player, enemy_move, False)

	all_sprites.draw(screen)

	score(s)

	seconds = (pygame.time.get_ticks() - start_ticks)//1000
	text1 = text.render("Timer: " + str(seconds), False, WHITE)
	screen.blit(text1, (10, 580))
#displaying the scores of the players
	#draw_text(screen,"Player1: " + str(score1),18,400,10)
	#draw_text(screen,"Player2: " + str(score2),18,400,580)

	showcase = text.render("Player1: " + str(s), False, WHITE)
	showcase = text.render("Player2: " + str(s), False, WHITE)


	for enemy in hit_fixed:
		pygame.time.delay(2000)
		points.append(s)
		bye()
		pygame.time.delay(2000)
		turn = (turn + 1) % 2
		level += 1
		if level > 5:
			winner()
			pygame.quit()
		else:
			next_turn(velocity, turn, level)

	for enemy in hit_move:
		pygame.time.delay(800)
		points.append(s)
		bye()
		pygame.time.delay(2000)
		turn = (turn + 1) % 2
		level += 1
		if level > 5:
			winner()
			pygame.quit()
		else:
			next_turn(velocity, turn, level)

#when player 1 plays what's the initial position
	if turn == 1:
		if y<=10:
			pygame.time.delay(800)
			points.append(s)
			welcome(s)
			pygame.time.delay(2000)
			turn = (turn + 1) % 2
			level += 1
			if level > 5:
				winner()
				pygame.quit()
			else:
				next_turn(velocity, turn, level)

#initial position for player 2
	else:
		if y>=569:
			pygame.time.delay(800)
			points.append(s)
			welcome(s)
			pygame.time.delay(2000)
			turn = (turn + 1) % 2
			level += 1
			if level > 5:
				winner()
				pygame.quit()
			else:
				next_turn(velocity, turn, level)
	pygame.display.update()
	time.tick(60)
pygame.quit()
quit()
