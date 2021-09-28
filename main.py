from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import SlideTransition

from source import app_layout

kv = Builder.load_file('./qtransfer.kv')

class QTransfer(App):
    def build(self):
        return kv

if __name__ == '__main__':
    QTransfer().run()
