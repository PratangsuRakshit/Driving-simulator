from ursina import *

class CarController(Entity):
    def __init__(self, **kwargs):
        self.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45, world_parent=self)
        super().__init__(parent=scene)

        self.default_speed = 10
        self.speed = self.default_speed
        self.height = 1
        self.camera_pivot = Entity(parent=self, y=self.height)

        camera.parent = self.camera_pivot
        camera.position = (0,0,-5)
        camera.rotation = (0,0,0)
        camera.fov = 90
        mouse.locked = False
        self.mouse_sensitivity = Vec2(40, 40)

        self.gravity = 1
        self.grounded = False
        self.jump_height = 2
        self.jump_duration = .5
        self.jumping = False
        self.air_time = 0
        self.can_turn = False

        self.speed_display = Text(world_parent=self, y=3.4, x=2, color=color.red)

        for key, value in kwargs.items():
            setattr(self, key ,value)


    def update(self):
        if self.enabled == True:
            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
            self.camera_pivot.rotation_x= clamp(self.camera_pivot.rotation_x, -90, 90)

            self.speed_display.text = f'Speed:{int(self.speed)}'

            if held_keys['w']:
                self.position += self.forward * time.dt * self.speed * 20
                if self.speed < 75:
                    self.speed += 0.01
                self.can_turn = True
            else:
                if self.speed > (self.default_speed + 1):
                    self.speed -= 0.05
                self.can_turn = False

            if held_keys['a'] and self.can_turn and self.grounded:
                self.speed_display.text = f'Speed:{int(self.speed)}'
                self.rotation_y -= self.speed * 4 * time.dt
            elif held_keys['d'] and self.can_turn and self.grounded:
                self.speed_display.text = f'Speed:{int(self.speed)}'
                self.rotation_y += self.speed * 4 * time.dt

            if self.gravity:
                # gravity
                ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
                # ray = boxcast(self.world_position+(0,2,0), self.down, ignore=(self,))

                if ray.distance <= self.height+.1:
                    if not self.grounded:
                        self.land()
                    self.grounded = True
                    # make sure it's not a wall and that the point is not too far up
                    if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
                        self.y = ray.world_point[1]
                    return
                else:
                    self.grounded = False

                # if not on ground and not on way up in jump, fall
                self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
                self.air_time += time.dt * .25 * self.gravity


    def input(self, key):
        if key == 'space':
            self.jump()


    def jump(self):
        if not self.grounded:
            return
        self.grounded = False
        self.animate_y(self.y+self.jump_height, self.jump_duration, resolution=int(1//time.dt), curve=curve.out_expo)
        invoke(self.start_fall, delay=self.jump_duration)


    def start_fall(self):
        self.y_animator.pause()
        self.jumping = False

    def land(self):
        # print('land')
        self.air_time = 0
        self.grounded = True


    def on_enable(self):
        mouse.locked = True
        self.cursor.enabled = True


    def on_disable(self):
        mouse.locked = False
        self.cursor.enabled = False
