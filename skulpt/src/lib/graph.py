import turtle

_turtle = turtle.Turtle()
_screen = turtle.Screen()

adj = _screen.window_width() / 2
scale = 2

_turtle.ht()

def dot(x, y, color = "black", size = 3):
	_x = (x * scale) - adj
	_y = y * scale

	_turtle.up()
	_turtle.setpos(_x, _y)
	_turtle.down()
	_turtle.dot(size, color)


def grid():
	_turtle.tracer(0, 0)
	spacing = 10 * scale

	width = _screen.window_width() / 2
	height = _screen.window_height() / 2
	start_x = -width + spacing
	start_y = -height + spacing

	for x in range(start_x, width, spacing):
		for y in range(start_y, height, spacing):
			if (y != 0):
				_turtle.up()
				_turtle.setpos(x, y)
				_turtle.down()
				_turtle.dot(1)
	
	_turtle.up()
	_turtle.setpos(-width, 0)
	_turtle.down()
	_turtle.forward(_screen.window_width())

	_turtle.update()
	_turtle.tracer(1, 10)


def clear():
	_screen.reset()
	_turtle.ht()
	grid()
