from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#-------------------------------------------------------------------------------

def update():
    global type_block, tay

    if held_keys['left mouse'] or held_keys['right mouse']:
        tay.active()
    else:
        tay.passive()

    if held_keys['1']: 
        type_block = 1
        destroy(tay)
        tay = Tay(texture = 'white_cube')

    if held_keys['2']: 
        type_block = 2
        destroy(tay)
        tay = Tay(texture = 'white_cube', color = color.red)

    if held_keys['3']: 
        type_block = 3
        destroy(tay)
        tay = Tay(texture = 'white_cube', color = color.blue)

    if held_keys['4']: 
        type_block = 4
        destroy(tay)
        tay = Tay(texture = 'brick')
        
    if held_keys['5']: 
        type_block = 5
        destroy(tay)
        tay = Tay(texture = 'white_cube', color = color.black)

#-------------------------------------------------------------------------------

class Block(Button):
    def __init__(self, position = (0, 0, 0), texture = 'white_cube', color = color.white):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = texture,
            color = color,
            position = position
        )      
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if type_block == 1: Block(position = self.position + mouse.normal, texture = 'white_cube')
                if type_block == 2: Block(position = self.position + mouse.normal, texture = 'white_cube', color = color.red)
                if type_block == 3: Block(position = self.position + mouse.normal, texture = 'white_cube', color = color.blue)
                if type_block == 4: Block(position = self.position + mouse.normal, texture = 'brick')
                if type_block == 5: Block(position = self.position + mouse.normal, texture = 'white_cube', color = color.black)
            if key == 'left mouse down':
                destroy(self)
#-------------------------------------------------------------------------------

class Tay(Entity):
    def __init__(self, texture = 'white_cube', color = color.white):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            scale = 0.4,
            rotation = Vec3(165, -15, 0),
            position = Vec2(0.4, -0.4),
            texture = texture,
            color = color
        )

    def active(self):
        self.position = Vec2(0.3, -0.3)
        self.rotation = Vec3(180, -15, 0)

    def passive(self):
        self.position = Vec2(0.4, -0.4)
        self.rotation = Vec3(165, -15, 0)
#-------------------------------------------------------------------------------

app = Ursina()
type_block = 1

for x in range (7):
    for z in range (7):
        block = Block(position = (x, 0, z))

Sky(texture = 'sky_sunset')
player = FirstPersonController()
tay = Tay()

app.run()