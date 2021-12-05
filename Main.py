from ursina import *
from menu import *
from player import CarController
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

app = Ursina()

main_menu = Entity(parent=camera.ui)
main_game = Entity()

states = Animator({
    'main_menu' : main_menu,
    'game' : main_game,
    }
)

#start menu content
def OnPlayPressed():
    states.state = 'game'
    print(states.state)
    car.on_enable()
MainMenu(OnPlayPressed, world_parent=main_menu)

#game content
test_road = Entity(model='plane', scale=100,collider = 'box', parent=main_game, world_parent=scene)
test_road.texture = 'white_cube'
test_road.texture_scale = (100,100)
#editor_camera_test_car = Entity(model = 'Car.fbx',scale = 0.01,shader = lit_with_shadows_shader, parent=main_game)
#EditorCamera(parent=main_game)
car = CarController(model = 'Car.fbx',scale = 0.005,color = color.white,shader = lit_with_shadows_shader, world_parent=main_game)
DirectionalLight(rotation=(45,45,45), parent=main_game)

app.run()
