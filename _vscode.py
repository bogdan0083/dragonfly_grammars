from dragonfly import MappingRule, Function, AppContext, get_engine, Dictation, Grammar, Window
from pynput.keyboard import Key, Controller
import logging
import os

keyboard = Controller()


def search_everywhere():
    with keyboard.pressed(Key.shift, Key.cmd_l):
        keyboard.press("f")


def replace_everywhere():
    with keyboard.pressed(Key.shift, Key.cmd_l):
        keyboard.press("h")


def toggle_drawer():
    with keyboard.pressed(Key.shift, Key.cmd_l):
        keyboard.press("e")


def code_actions():
    with keyboard.pressed(Key.cmd):
        keyboard.press(".")


def go_to_definition():
    keyboard.press(Key.f12)


def format_document():
    with keyboard.pressed(Key.shift, Key.alt_l):
        keyboard.press("f")


def cancel():
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press("c")


def focus_terminal():
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press("`")


def focus_main_window():
    with keyboard.pressed(Key.cmd_l):
        keyboard.press("1")


def open_commands():
    with keyboard.pressed(Key.cmd_l, Key.shift):
        keyboard.press("p")


def open_symbol():
    with keyboard.pressed(Key.cmd_l):
        keyboard.press("t")

def rename_symbol():
    keyboard.press(Key.f2)

def jump_to_letter():
    with keyboard.pressed(Key.alt_l):
        keyboard.press("/")


vscode_context = AppContext(executable="electron")


class VscodeRule(MappingRule):
    mapping = {
        "search (dumb|everywhere)": Function(lambda: search_everywhere()),
        "replace (dumb|everywhere)": Function(lambda: search_everywhere()),
        "code actions": Function(lambda: code_actions()),
        "go to definition": Function(lambda: go_to_definition()),
        "format (document|file)": Function(lambda: format_document()),
        "(focus|toggle) draw": Function(lambda: toggle_drawer()),
        "cancel": Function(lambda: cancel()),
        "focus (term|terminal)": Function(lambda: focus_terminal()),
        "focus main": Function(lambda: focus_main_window()),
        "open commands": Function(lambda: open_commands()),
        "open symbol": Function(lambda: open_symbol()),
        "rename symbol": Function(lambda: rename_symbol()),
        "jump to letter": Function(lambda: jump_to_letter()),
    }

    context = vscode_context
    # def _process_recognition(self, node, third):
    #     win = Window.get_foreground()
    #     print(win.executable)
    #     print(win.title)
