from ursina import *
from player import CarController
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

app = Ursina()

test_road = Entity(model='plane', scale=100, texture='white_cube' ,color = color.white,collider = 'box',shader = lit_with_shadows_shader)

#editor_camera_test_car = Entity(model = 'Car.fbx',scale = 0.01,shader = lit_with_shadows_shader)
#EditorCamera()

car = CarController(model = 'Car.fbx',scale = 0.005,color = color.white,shader = lit_with_shadows_shader)
camera.z = -550

DirectionalLight(rotation=(45,45,45))

app.run()
