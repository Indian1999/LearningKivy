from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from random import randint

SCORE_REQ = 50
TIME_LIMIT = 60

class GameWidget(Widget):
    def __init__(self, **kwarg):
        super().__init__()
        
        self.score = 0
        self.time_passed = 0
        self.gameOn = False
        
        self.score_label = Label(text="Score: 0", 
                                 font_size="20",
                                 pos=(10, Window.height - 75),
                                 opacity=0)
        self.add_widget(self.score_label)
        
        self.time_label = Label(text="Time: 0", 
                                 font_size="20",
                                 pos=(Window.width-130, Window.height - 75),
                                 opacity=0)
        self.add_widget(self.time_label)
        
        self.game_over_label = Label(text="", 
                                 font_size="50",
                                 pos=(Window.width / 2 - 80, Window.height / 2 + 80),
                                 opacity = 0)
        self.add_widget(self.game_over_label)
        
        self.target = Button(size=(50,50), background_color=(1,1,1,1), opacity=0)
        self.target.bind(on_press = self.target_pressed)
        self.move_target()
        self.add_widget(self.target)
        
        self.start_button = Button(text = "Start",
                                   size = (200,80),
                                   font_size=30,
                                   pos=(Window.width/2-100, Window.height/2-40),
                                   background_color=(1,0,0,1))
        self.start_button.bind(on_press=self.start_pressed)
        self.add_widget(self.start_button)
        

    def start_pressed(self,instance):
        self.score = 0
        self.time_passed = 0
        self.gameOn = True
        
        self.start_button.disabled = True
        self.start_button.opacity = 0
        self.game_over_label.opacity = 0
        
        self.score_label.opacity = 1
        self.score_label.test = "Score: 0"
        self.time_label.opacity = 1
        self.time_label.text = "Time: 0"
        self.target.opacity = 1
        self.target.disabled = False
        self.timer_event = Clock.schedule_interval(self.increment_timer, 1)
        
        self.move_target()
        
    def move_target(self):
        x = randint(50, Window.width - 50)
        y = randint(50, Window.height - 50)
        self.target.pos = (x,y)
        
    def target_pressed(self, instance):
        self.score += 1
        self.score_label.text = "Score: " + str(self.score)
        self.move_target()
        
    def increment_timer(self, dt):
        if not self.gameOn:
            return
        self.time_passed += 1
        self.time_label.text = "Time: " + str(self.time_passed)
        
        if self.time_passed >= TIME_LIMIT:
            self.gameOver()
            
    def gameOver(self):
        self.timer_event.cancel()
        self.gameOn = False
        self.target.disabled = True
        self.target.opacity = 0
        if self.score >= SCORE_REQ:
            self.game_over_label.text = "You win!"
        else:
            self.game_over_label.text = "You lost!"
        self.game_over_label.opacity = 1
        self.start_button.disabled = False
        self.start_button.opacity = 1
        
class TapTheTarget(App):
    def build(self):
        return GameWidget()
    
if __name__ == "__main__":
    TapTheTarget().run()