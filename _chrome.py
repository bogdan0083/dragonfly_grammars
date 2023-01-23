from dragonfly import MappingRule, Function, AppContext, get_engine, Dictation, Grammar
from pynput.keyboard import Key, Controller
import logging
import os

keyboard = Controller()

def tab_left():
    with keyboard.pressed(Key.shift, Key.cmd_l):
        keyboard.press("[")

def tab_right():
    with keyboard.pressed(Key.shift, Key.cmd_l):
        keyboard.press("]")

def tab_new():
    with keyboard.pressed(Key.cmd_l):
        keyboard.press("t")

def tab_close():
    with keyboard.pressed(Key.cmd_l):
        keyboard.press("w")

def toggle_developer_tools():
    with keyboard.pressed(Key.cmd, Key.alt):
        keyboard.press("i")

def toggle_history():
    with keyboard.pressed(Key.cmd):
        keyboard.press("y")

def search():
    with keyboard.pressed(Key.cmd):
        keyboard.press("l")

def select_element():
    with keyboard.pressed(Key.shift, Key.cmd):
        keyboard.press("c")


chrome_context = AppContext(executable="google chrome")

class ChromeRule(MappingRule):
    mapping = {
        "tab left": Function(lambda: tab_left()),
        "tab right": Function(lambda: tab_right()),
        "tab new": Function(lambda: tab_new()),
        "tab close": Function(lambda: tab_close()),
        "(open|toggle) developer tools": Function(lambda: toggle_developer_tools()),
        "(open|toggle) history": Function(lambda: toggle_history()),
        "search <text>": Function(lambda: search()),
        "select [an] element": Function(lambda: select_element()),
    }

    extras = [Dictation("text")]
    context = chrome_context
