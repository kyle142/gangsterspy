#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  game.py
#  
#  Copyright 2012 Kyle Clothier <kyle@kyle-desktop>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

import pygame,sys,npc_civillian,collidable_objects
from pygame.locals import *



def main():
	#House Keeping
	cursor_image="images/simple/cursor.png"
	background_image="images/simple/stonewall.jpg"
	screen=pygame.display.set_mode((450,348),0,32)
	background=pygame.image.load(background_image).convert()
	cursor=pygame.image.load(cursor_image).convert_alpha()
	civilian_image = "images/complex/civillian_up.png"
	npc_civillian.__init__(self, centerPoint, civilian_image)
	
	#Quit
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		#Initialize Background,Mouse		
		screen.blit(background,(0,0))
		x,y = pygame.mouse.get_pos()
		x -= cursor.get_width()/2
		y -= cursor.get_height()/2
		screen.blit(cursor,(x,y))
		pygame.display.update()
	

	

if __name__ == '__main__':
	pygame.init()
	main()
