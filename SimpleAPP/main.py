from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter

class simpleApp(App):
    def build(self):
        lb1 = Label(text="Hello!", font_size=96)
        sct = Scatter()
        sct.add_widget(lb1)

        return sct

if __name__ == "__main__":
    simpleApp().run()