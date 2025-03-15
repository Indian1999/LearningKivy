import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        self.cols = 1
        
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        
        self.top_grid.add_widget(Label(text="Name"))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        self.top_grid.add_widget(Label(text="Age"))
        self.age = TextInput(multiline=False)
        self.top_grid.add_widget(self.age)
        self.top_grid.add_widget(Label(text="Email"))
        self.email = TextInput(multiline=False)
        self.top_grid.add_widget(self.email)
        
        self.add_widget(self.top_grid)
        
        self.submit = Button(text="Submit")
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)
        
        self.output_label = Label()
        self.add_widget(self.output_label)
    
    def press(self, instance):
        output = "Thank you! We have saved your information.\n"
        output += "Name: " + self.name.text + "\n"
        output += "Age: " + self.age.text + "\n"
        output += "E-mail: " + self.email.text
        
        self.output_label.text = output
        self.age.text = ""
        self.name.text = ""
        self.email.text = ""
        
    


class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()