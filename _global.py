from dragonfly import MappingRule, Function, AppContext, get_engine, Dictation, Grammar, Window, Key, Text
from pynput.keyboard import Controller
import logging
import os

keyboard = Controller()

class GlobalRule(MappingRule):
    mapping = {
        "open (chrome|browser)": Key("a-m") + Text("chrome") + Key("enter"),
        "open code": Key("a-m") + Text("code") + Key("enter"),
        "open (term|terminal)": Key("a-m") + Text("iterm") + Key("enter"),
        "open figma": Key("a-m") + Text("figma") + Key("enter"),
        "open tea greek": Key("a-m") + Text("telegram") + Key("enter"),
        "clip cut": Key("w-x"),
        "clip copy": Key("w-c"),
        "clip paste": Key("w-v"),
        "(window|wine) next": Key("w-`"),
        "(window|wine) previous": Key("sw-`"),
        "change (lang|language)": Key("c-z"),
    }
