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
            self.background = Sprite('shore', color=color.dark_gray, z=1, parent=self)

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

            # Input function that check if key pressed on keyboard

        def input(self, key):
            # And if you want use same keys on different windows
            # Like [Escape] or [Enter] or [Arrows]
            # Just write like that:

            # If our main menu enabled and we press [Escape]
            if self.main_menu.enabled:
                if key == "escape":
                    # Close app
                    application.quit()

            # If our options menu enabled and we press [Escape]
            if self.options_menu.enabled:
                if key == "escape":
                    # Close options window and show main menu
                    self.main_menu.enable()
                    self.options_menu.disable()

            # If our help menu enabled and we press [Escape]
            if self.help_menu.enabled:
                if key == "escape":
                    self.main_menu.enable()
                    self.help_menu.disable()
