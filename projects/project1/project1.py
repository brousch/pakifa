#!/usr/bin/env python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Project1(BoxLayout):
    pass


class Project1App(App):
    def build(self):
        return Project1()

    def on_pause(self):
        return True

    def on_resume(self):
        pass
