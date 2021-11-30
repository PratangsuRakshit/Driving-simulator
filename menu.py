#Test
from ursina import *

class MenuHandler(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_menu = Entity(parent=camera.ui)
        self.main_menu_btns = ButtonList(button_dict={
            'Start':self.start
        })
    def start(self):
        destroy(self.main_menu)
        print('a')
