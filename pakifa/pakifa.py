#!/usr/bin/env python

from ConfigParser import ConfigParser

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Pakifa(BoxLayout):
    def run_project(self, project):
        config = ConfigParser()
        config.read('config.ini')
        config.set('Project', 'open_project', project)
        with open('config.ini', 'wb') as configfile:
            config.write(configfile)
        App.get_running_app().stop()

class PakifaApp(App):
    def build(self):
        return Pakifa()

    def on_pause(self):
        return True

    def on_resume(self):
        pass
