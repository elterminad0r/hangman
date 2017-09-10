from getpass import getpass
import random
import turtle
import time

s = turtle.Screen()
s.colormode(255)

t = turtle.Turtle()
t.hideturtle()
t.speed(10)
t.width(3)

def win():
	height, width = s.window_height() / 2, s.window_width() / 2
	t.speed(0)
	t.width(1)

	try:
		while True:
			t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			line((random.randint(-width, width), random.randint(-height, height)), (random.randint(-width, width), random.randint(-height, height)))

	except KeyboardInterrupt:
		pass

def line(xy1, xy2):
	t.penup()
	t.setpos(*xy1)
	t.pendown()
	t.setpos(*xy2)

def s0():
	line((200, -200), (-200, -200))

def s1():
	line((-100, -200), (-100, 200))
	line((0, -200), (-100, -100))

def s2():
	line((-200, 200), (200, 200))
	line((0, 200), (-100, 100))

def s3():
	line((100, 200), (100, 150))

def s4():
	t.penup()
	t.setpos(100, 150)
	t.setheading(180)
	t.pendown()
	t.circle(40, 360)

def s5():
	line((100, 70), (100, -80))

def s6():
	line((100, -80), (82.14 * 2, -78.30 * 2))
	line((100, -80), (17.86 * 2, -78.30 * 2))

def s7():
	line((100, 20), (72.94 * 2, -22.77 * 2))

def s8():
	line((100, 20), (27.06 * 2, -22.77 * 2))

def s9():
	t.penup()
	t.setpos(86, 120)
	t.dot(10)

	t.penup()
	t.setpos(114, 120)
	t.dot(10)

	t.penup()
	t.setpos(114, 86)
	t.setheading(90)
	t.pendown()
	t.circle(14, 180)

steps = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]

def custom_getpass(msg):
	while True:
		print '\x1b[0m{0}\x1b[0;30;40m'.format(msg)
		inp = raw_input()
		print '\x1b[0m{0}\x1b[0;30;40m'.format('Can you verify?')
		if raw_input() == inp:
			print '\x1b[0m'
			return inp
			break
		else:
			print '\x1b[0mThose do not match.'

def printStrikes(l):
	if len(l) == 0:
		print
	else:
		print (u'\u0336{}' * len(l) + u'\u0336').format(*l)

while True:
	word = getpass('What should the word be? ')
	
	check = getpass('Can you verify?')

	if word == check:
		break
	else:
		print 'Sorry, those did not match.'


if '_' in word or '/' in word:
	while True:
		word = getPass('No underscores or slashes, please')
		if not ('_' in word or '/' in word):
			break

word = word.lower()

guesses = ['_'] * len(word)
for i in range(len(word)):
	if word[i] == ' ':
		guesses[i] = '/'

guessed = [' ']

turns = 10

try:
	while True:
		print 'Incorrect letters you have guessed:'
		print ''.join(guessed)
		print 'This how much you have currently guessed:'
		print ' '.join(guesses)
		print 'You have {0} remaining guesses'.format(turns)
		char = raw_input('Guess a letter\n')

		if len(char) == 1:
			if char in word and not char in guessed:
				print 'You guessed correctly!'
				for i in range(len(word)):
					if word[i] == char:
						guesses[i] = char

				if not '_' in guesses:
					print 'You won! The word was \'{0}\''.format(word)
					s.bgcolor(0, 255, 0)
					win()
					break

			else:
				if char in guessed:
					print 'You already guessed that!'
				else:
					turns -= 1
					steps[9-turns]()
					if turns == 0:
						print 'You lost! :('
						s.bgcolor(255, 0, 0)
						win()
						break

					print 'That was wrong.'
					guessed.append(char)

		else:
			if char == word:
				print 'You won! The word was \'{0}\''.format(word)
				s.bgcolor(0, 255, 0)
				win()
				break

			else:
				print 'That was wrong.'
				turns -= 1
				steps[9-turns]()

				if turns == 0:
					print 'You lost! :('
					s.bgcolor(255, 0, 0)
					win()
					break

except KeyboardInterrupt:
	print 'You lose :p'
