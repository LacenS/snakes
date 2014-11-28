import random
from snake import *

# Barva glave in repa
COLOR_HEAD = 'deep pink'
COLOR_TAIL = 'teal'

class CornSnake(Snake):
    def __init__(self, field, x, y, dx, dy):
        # Poklicemo konstruktor nadrazreda
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = 1, dy = 1)
        # V konstruktor lahko dodate se kaksne atribute

    
    def turn(self):
        
        
        self.turn_right()
        
        
        
    
        
        """Igrica poklice metodo turn vsakic, preden premakne kaco. Kaca naj se tu odloci, ali se
           bo obrnila v levo, v desno, ali pa bo nadaljevala pot v isti smeri.

           * v levo se obrne s self.turn_left()
           * v desno se obrne s self.turn_right()
           * koordinate glave so self.coords[0]
           * smer, v katero potuje je (self.dx, self.dy)
           * spisek koordinat vseh misk je self.field.mice.keys()
           * spisek vseh kac je self.field.snakes
        """
##           
##        if random.randint(0,50) < 20:
##            if random.randint(0,1) == 1:
##                self.turn_left()
##            else:
##                self.turn_right()
        
