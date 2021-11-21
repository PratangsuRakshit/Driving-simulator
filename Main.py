from ursina import *
app = Ursina()

class Car(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'cube'
        self.scale = Vec3(1, 1, 2)
        self.speed = 5
        self.can_turn = False

    def update(self):
        if held_keys['w']:
            self.position += self.forward * time.dt * self.speed
            self.speed += 0.01
            self.can_turn = True
        else:
            self.can_turn = False
        if held_keys['a'] and self.can_turn:
            self.rotation_y -= self.speed * 10 * time.dt
        if held_keys['d'] and self.can_turn:
            self.rotation_y += self.speed * 10 * time.dt

test_road = Entity(model='plane', scale=100, texture='white_cube')
Car().y += 0.5

EditorCamera()

app.run()
