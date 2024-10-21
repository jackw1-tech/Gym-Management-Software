from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from GestionePalestra.view.gym import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.graphics import SmoothRoundedRectangle, Color



class StylishButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.background_down = ''
        self.font_size = '18sp'
        self.bold = True
        self.color = get_color_from_hex('#FFFFFF')
        self.size_hint = (0.8, None)
        self.height = 60
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*get_color_from_hex('#007AFF'))
            SmoothRoundedRectangle(pos=self.pos, size=self.size, radius=[15])

class MainScreen(Screen):
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
            "Gestione Personale",
            "Gestione Clienti",
            "Gestione Contabilità",
            "Gestione Palestra"
        ]

        for button_text in buttons:
            button = StylishButton(text=button_text)
            button.bind(on_press=self.button_pressed)
            layout.add_widget(button)

        self.add_widget(layout)


    def button_pressed(self, instance):
        if instance.text == "Gestione Palestra":
            self.manager.current = 'gestione_palestra'
        else:
            print(f"{instance.text} button pressed")

class GymManagementApp(App):
    def build(self):
        Window.size = (400, 600)
        Window.clearcolor = get_color_from_hex('#F2F2F7')

        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GymManagementScreen(name='gestione_palestra'))
        return sm

if __name__ == '__main__':
    GymManagementApp().run()
