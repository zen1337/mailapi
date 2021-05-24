from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class GridGrid(GridLayout):
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(GridGrid, self).__init__(**kwargs)
        # set columns
        self.cols = 6
        # add widgets
        self.add_widget(Label(text="Name: "))
        # add Input Box
        self.name = TextInput(text='test', multiline=True)
        #self.wtf = Button(text='wtf test', size_hint_x=1, width=100)
        self.add_widget(self.name)
        self.add_widget(Button(text='wtf test', size_hint_x=1, width=100))
        self.add_widget(Label(text="Surname: "))

class MainApp(App):
    def build(self):
        label = Label(text="testuje")
        return GridGrid()
        #label = Label(text="testuje", size_hint = (.5, .5), pos_hint = {'center_x': .5, 'center_y': .5})
        #return label
if __name__ == '__main__':
    app = MainApp()
    app.run()