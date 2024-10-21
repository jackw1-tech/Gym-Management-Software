from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from main import StylishButton
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from gym import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle


class GymManagementScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        title = Label(
            text='Gym Management',
            font_size='32sp',
            bold=True,
            color=get_color_from_hex('#1C1C1E'),
            size_hint_y=None,
            height=100
        )
        layout.add_widget(title)

        buttons = [
            "Equipment Inventory",
            "Class Schedule",
            "Facility Maintenance",
            "Staff Management",
            "Back to Main Menu"
        ]

        for button_text in buttons:
            button = StylishButton(text=button_text)
            button.bind(on_press=self.button_pressed)
            layout.add_widget(button)

        self.add_widget(layout)


    def button_pressed(self, instance):
        if instance.text == "Back to Main Menu":
            self.manager.current = 'main'
        else:
            print(f"{instance.text} button pressed")
