#!/usr/bin/env python

from ConfigParser import ConfigParser

config = ConfigParser()
config.read('config.ini')
project_name = config.get('Project', 'open_project')

def reset_project():
    config.set('Project', 'open_project', '')
    with open('config.ini', 'wb') as configfile:
        config.write(configfile)

if not project_name:
    from pakifa import MainApp
else:
    try:
        project_module = __import__('projects.'+project_name, globals(), locals(),["MainApp"])
        MainApp = project_module.MainApp
    except:
        print("WARNING: Problem importing your project's MainApp")
        from pakifa import MainApp

__version__ = '0.0.1'

if __name__ == '__main__':
   MainApp().run()
   if project_name:
    reset_project()
