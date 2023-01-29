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
        "open notion": Key("a-m") + Text("notion") + Key("enter"),
        "clip cut": Key("w-x"),
        "clip copy": Key("w-c"),
        "clip paste": Key("w-v"),
        "undo action": Key("w-z"),
        "(window|wine) next": Key("w-`"),
        "(window|wine) previous": Key("sw-`"),
        "change (lang|language)": Key("c-z"),
        "insert (emoji|emotion)": Key("cw-space"),
        "(make|create|new) screenshot window": Key("sw-2"),
        "(make|create|new) screenshot full": Key("sw-3"),
        "(make|create|new) screenshot crop": Key("sw-4"),
        "(make|create|new) screenshot video": Key("sw-5"),
    }
