from ursina import *
from player import CarController
from menu import *
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

app = Ursina()

main_menu = Entity(parent=camera.ui, enabled=True)
main_game = Entity(enabled=False)
example_skill_test_map = Entity(enabled=False)
selection_menu = Entity(enabled=False, parent=camera.ui)
not_ready = Entity(enabled=False)

states = Animator({
    'main_menu' : main_menu,
    'game' : main_game,
    'selection' : selection_menu,
    'learn' : example_skill_test_map,
    'not ready' : not_ready,
    }
)

#Main Menu
def OnPlayPressed():
    states.state = 'selection'
    print(states.state)
MainMenu(OnPlayPressed, world_parent=main_menu)

#Selection_Menu
def OnGamePressed(): states.state = 'game'; print(states.state)
def OnDemoPressed(): print('Not Yet Implemented'); application.quit()
SelectionMenu(OnGamePressed, OnDemoPressed, world_parent=selection_menu)

#Main Game
Sky()
test_road = Entity(model='plane', scale=100,collider = 'box', parent=main_game, world_parent=scene)
test_road.texture = 'grass'
test_road.texture_scale = (100,100)
#editor_camera_test_car = Entity(model = 'Car.fbx',scale = 0.01,shader = lit_with_shadows_shader, parent=main_game)
#EditorCamera(parent=main_game)
car = CarController(model = 'cube',scale = 0.005,color = color.white, world_parent=main_game)
DirectionalLight(rotation=(45,45,45), parent=main_game)

def update():
    if car.y <= -5:
        car.position = Vec3(0, 0, 0)
        car.speed = car.default_speed

app.run()
