from ursina import *

class MainMenu(Entity):
    def __init__(self, start_function, **kwargs):
        super().__init__(parent=camera.ui, **kwargs)
        if True:
            self.start_function = start_function
            self.main_menu = Entity(parent=self, enabled=True)
            self.options_menu = Entity(parent=self, enabled=False)
            self.help_menu = Entity(parent=self, enabled=False)

            # Add a background. You can change 'shore' to a different texture of you'd like.
            self.background = Sprite('shore', z=1, parent=self)

            # [MAIN MENU] WINDOW START
            # Title of our menu
            Text("MAIN MENU", parent=self.main_menu, y=0.4, x=0, origin=(0, 0))

            # Reference of our action function for quit button
            def quit_game():
                application.quit()

            # Reference of our action function for options button
            def options_menu_btn():
                self.options_menu.enable()
                self.main_menu.disable()

            # Reference of our action function for help button
            def help_menu_btn():
                self.help_menu.enable()
                self.main_menu.disable()

            # Reference of our action function for options button
            def start_menu_btn():
                self.scene_data = 'game'
                self.disable()

            # Button list
            ButtonList(button_dict={
                "Start": Func(self.start_function),
                "Options": Func(options_menu_btn),
                "Help": Func(help_menu_btn),
                "Exit": Func(quit_game)
            }, y=0, parent=self.main_menu)
            # [MAIN MENU] WINDOW END

            # [OPTIONS MENU] WINDOW START
            # Title of our menu
            Text("OPTIONS MENU", parent=self.options_menu, y=0.4, x=0, origin=(0, 0))

            # Reference of our action function for back button
            def options_back_btn_action():
                self.main_menu.enable()
                self.options_menu.disable()

            # Button
            Button("Back", parent=self.options_menu, y=-0.3, scale=(0.1, 0.05), color=rgb(50, 50, 50),
                   on_click=options_back_btn_action)

            # [OPTIONS MENU] WINDOW END

            # [HELP MENU] WINDOW START
            # Title of our menu
            Text("HELP MENU", parent=self.help_menu, y=0.4, x=0, origin=(0, 0))

            # Reference of our action function for back button
            def help_back_btn_action():
                self.main_menu.enable()
                self.help_menu.disable()

            # Button list
            ButtonList(button_dict={
                "Gameplay": Func(print_on_screen, "You clicked on Gameplay help button!", position=(0, .1), origin=(0, 0)),
                "Battle": Func(print_on_screen, "You clicked on Battle help button!", position=(0, .1), origin=(0, 0)),
                "Control": Func(print_on_screen, "You clicked on Control help button!", position=(0, .1), origin=(0, 0)),
                "Back": Func(help_back_btn_action)
            }, y=0, parent=self.help_menu)
            # [HELP MENU] WINDOW END

            # Here we can change attributes of this class when call this class
            for key, value in kwargs.items():
                setattr(self, key, value)

class SelectionMenu(Entity):
    def __init__(self, game_parent, demo_parent, **kwargs):
        super().__init__(**kwargs)

        self.game_function = game_parent
        self.demo_function = demo_parent

        if self.enabled == True:
            self.background = Sprite('shore', parent=self, z=1, scale=2)
            self.game = Button(scale=(8, 4), position=(0, 2.5), parent=self, text='Game', on_click=Func(self.game_function))
            self.demo = Button(scale=(8, 4), position=(0, -2.5), parent=self, text='Demo', on_click=Func(self.demo_function))
