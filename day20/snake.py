import turtle 

turtle.colormode(255)
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 #("209, 226, 45)
COLORS1 = ['(40, 125, 125)', '(37, 126, 124)', '(35, 127, 122)', '(34, 128, 120)', '(33, 130, 118)', '(34, 131, 115)', '(35, 131, 113)', '(37, 132, 110)', '(40, 133, 107)', '(43, 134, 103)', '(47, 135, 100)', '(51, 136, 96)', '(56, 136, 92)', '(61, 137, 89)', '(65, 137, 84)', '(70, 138, 80)', '(75, 138, 76)', '(81, 138, 72)', '(86, 139, 67)', '(91, 139, 63)', '(97, 139, 58)', '(102, 139, 54)', '(108, 139, 49)', '(113, 138, 45)', '(119, 138, 40)', '(125, 137, 36)', '(131, 137, 31)', '(137, 136, 26)', '(143, 135, 22)', '(149, 134, 18)', '(155, 133, 13)', '(161, 132, 10)', '(161, 132, 10)', '(155, 133, 13)', '(149, 134, 18)', '(143, 135, 22)', '(137, 136, 26)', '(131, 137, 31)', '(125, 137, 36)', '(119, 138, 40)', '(113, 138, 45)', '(108, 139, 49)', '(102, 139, 54)', '(97, 139, 58)', '(91, 139, 63)', '(86, 139, 67)', '(81, 138, 72)', '(75, 138, 76)', '(70, 138, 80)', '(65, 137, 84)', '(61, 137, 89)', '(56, 136, 92)', '(51, 136, 96)', '(47, 135, 100)', '(43, 134, 103)', '(40, 133, 107)', '(37, 132, 110)', '(35, 131, 113)', '(34, 131, 115)', '(33, 130, 118)', '(34, 128, 120)', '(35, 127, 122)', '(37, 126, 124)', '(40, 125, 125)']
COUNT = 0

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.count_i = 0
        self.init_snake()
        self.head = self.segments[0]
        self.is_pressed = False
        
        
    def init_snake(self):
        """Initiliazes snake"""    
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.segments[0].shape("circle")
        self.segments[0].shapesize(stretch_len=1.25,stretch_wid= 1.05)

    def move_snake(self):
        """moves snakes head and its segments"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            snake_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(snake_position)
        self.head.forward(MOVE_DISTANCE)
        
    def add_segment(self, position):
        """appends new segment to snake at the tail"""
        new_segment = turtle.Turtle(shape="square")
        new_segment.penup()
        new_segment.speed(1)
        new_segment.color(eval(COLORS1[self.count_i]))
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.count_i = (self.count_i + 1) % (len(COLORS1) -1)
        
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        """resets everything after death"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.count_i = 0
        self.init_snake()
        self.head = self.segments[0]

    
    # movement logic
    
    def heading(self, direction):
        if self.is_pressed == False:
            self.head.setheading(direction)
            self.is_pressed = True
                
    def up(self):
        if self.head.heading() != DOWN and self.is_pressed == False:
            return self.heading(UP)

    def down(self):
        if self.head.heading() != UP and self.is_pressed == False:
            return self.heading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT and self.is_pressed == False:
            return self.heading(LEFT)

    def right(self):
        if self.head.heading() != LEFT and self.is_pressed == False:
            return self.heading(RIGHT)