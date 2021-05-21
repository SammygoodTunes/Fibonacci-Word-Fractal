'''
Title: Fibonacci Word Fractal
Author: SammygoodTunes
Version: 1.1.20210521
'''

import math,pygame,random,pyautogui


pygame.init()


class Window:

	def __init__(self):
		self.w,self.h = pyautogui.size()
		self.clock = pygame.time.Clock()

		
	def get_window_size(self):
		return self.w, self.h


class Location:

	def __init__(self):
		self.x, self.y = window.w / 2, window.h
		self.x2, self.y2 = 2, -10


class Line:

	def __init__(self):
		self.turn_id = 0
		self.size = 1


class Lists:

	def __init__(self):
		self.num_list = []
		self.fibonacci_list = []
		self.binary_list = []


class Simulation:

	def __init__(self):
		self.iterations = 0
		self.max_iterations = 5000
		self.draw = True
		self.end = False


	def start(self, lists, simulation):
		for i in range(1,s imulation.max_iterations):
			lists.fibonacci_list.append(simulation.phi(i))
		simulation.append(lists)
		simulation.compare(lists)

	
	def phi(self, n):
		return int(n * (1 + math.sqrt(5)) / 2)

	
	def append(self, lists):
		for i in range(1, self.max_iterations):
			lists.num_list.append(i)

	
	def compare(self, lists):
		for i in range(len(lists.fibonacci_list)):
			if lists.num_list[i] in lists.fibonacci_list:
				lists.binary_list.append(1)
			else:
				lists.binary_list.append(0)

	
	def check_turn_id(self, line, location):
		if line.turn_id == 0:
			location.x2, location.y2 = 2, -line.size
			location.y -= line.size
		elif line.turn_id == 1:
			location.x2, location.y2 = line.size, 2
			location.x += line.size
		elif line.turn_id == 2:
			location.x2, location.y2 = 2, line.size
			location.y += line.size
		else:
			location.x2, location.y2 = -line.size, 2
			location.x -= line.size


window = Window()
screen = pygame.display.set_mode([window.get_window_size()[0], window.get_window_size()[1]])
pygame.display.set_caption("Fibonacci Word Fractal Simulation")


def main():

	location = Location()
	simulation = Simulation()
	line = Line()
	lists = Lists()

	simulation.start(lists, simulation)

	while not simulation.end:

		#print(line.size)

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				simulation.end = True

			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_UP:
					line.size += 1

				if e.key == pygame.K_DOWN:
					line.size -= 1

				if e.key == pygame.K_SPACE:
					location = Location()
					simulation = Simulation()
					line = Line()
					lists = Lists()
					screen.fill((0, 0, 0), (0, 0, window.get_window_size()[0], window.get_window_size()[1]))
					simulation.start(lists,simulation)

				if e.key == pygame.K_ESCAPE:
					simulation.end = True

		if simulation.draw:

			simulation.check_turn_id(line, location)

			if lists.binary_list[simulation.iterations] == 1:
				if simulation.iterations % 2 == 0:
					if line.turn_id < 3:
						line.turn_id += 1
					else:
						line.turn_id = 0
				else:
					if line.turn_id > 0:
						line.turn_id -= 1
					else:
						line.turn_id = 3

			simulation.check_turn_id(line, location)


			pygame.draw.rect(screen, (255, 255, 255), (location.x, location.y, location.x2, location.y2))


		if simulation.iterations < len(lists.binary_list) - 1:
			simulation.iterations += 1
		else:
			simulation.draw = False

		pygame.display.flip()
		window.clock.tick(60)
	pygame.quit()

	
if __name__ == '__main__':
	main()
