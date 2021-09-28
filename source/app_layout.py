from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen

class QManager(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class PhotoScreen(Screen):
    pass

class ProcessScreen(Screen):
    pass

class AppLayoutGrid(GridLayout):
    
    label_text = StringProperty('ON')
    counter = 1
    count_text = StringProperty(str(counter))
    
    toggle_text = StringProperty('OFF')
    
    def enable_count(self, activator):
        if activator.state == 'down':
            self.toggle_text = 'ON'
        elif activator.state == 'normal':
            self.toggle_text = 'OFF'
            
    def increment(self, toggle=None):
        if toggle.state == 'down':
            self.counter += 1
            self.count_text = str(self.counter)
        
    def on_off(self):
        if self.label_text == 'ON':
            self.label_text = 'OFF'
        elif self.label_text == 'OFF':
            self.label_text = 'ON'
        

class AppLayoutBox(BoxLayout):
    pass