class npc_civillian(pygame.basicSprite.Sprite):
	def __init__(self, centerPoint, civilian_image):  
		basicSprite.Sprite.__init__(self, centerPoint, image)
		self.image = image
		#Direction
		self.direction = random.randint(1,4)self.dist = 3
		self.moves = random.randint(100,200)
		self.moveCount = 0;
		
