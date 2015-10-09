#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import sublime
import sublime_plugin
import LiveReload

sys.path.append(os.path.join(sublime.packages_path(), 'LiveReload'))
LiveReload = __import__('LiveReload')
sys.path.remove(os.path.join(sublime.packages_path(), 'LiveReload'))


def plugin_loaded():
    sublime.set_timeout(lambda : sublime.run_command("simple_reload_delay"), 10000)


class SimpleReloadDelayCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        index = 5
        LiveReload.Plugin.togglePlugin(index)
