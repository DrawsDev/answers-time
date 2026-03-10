from enum import Enum
from typing import Union

import pygame

STRING_TO_KEYCODE = {
    "unknown": pygame.K_UNKNOWN,
    "a": pygame.K_a,
    "b": pygame.K_b,
    "c": pygame.K_c,
    "d": pygame.K_d,
    "e": pygame.K_e,
    "f": pygame.K_f,
    "g": pygame.K_g,
    "h": pygame.K_h,
    "i": pygame.K_i,
    "j": pygame.K_j,
    "k": pygame.K_k,
    "l": pygame.K_l,
    "m": pygame.K_m,
    "n": pygame.K_n,
    "o": pygame.K_o,
    "p": pygame.K_p,
    "q": pygame.K_q,
    "r": pygame.K_r,
    "s": pygame.K_s,
    "t": pygame.K_t,
    "u": pygame.K_u,
    "v": pygame.K_v,
    "w": pygame.K_w,
    "x": pygame.K_x,
    "y": pygame.K_y,
    "z": pygame.K_z,
    "0": pygame.K_0,
    "1": pygame.K_1,
    "2": pygame.K_2,
    "3": pygame.K_3,
    "4": pygame.K_4,
    "5": pygame.K_5,
    "6": pygame.K_6,
    "7": pygame.K_7,
    "8": pygame.K_8,
    "9": pygame.K_9,
    "space": pygame.K_SPACE,
    "!": pygame.K_EXCLAIM,
    "\"": pygame.K_QUOTEDBL,
    "#": pygame.K_HASH,
    "$": pygame.K_DOLLAR,
    "&": pygame.K_AMPERSAND,
    "%": pygame.K_PERCENT,
    "'": pygame.K_QUOTE,
    "(": pygame.K_LEFTPAREN,
    ")": pygame.K_RIGHTPAREN,
    "*": pygame.K_ASTERISK,
    "+": pygame.K_PLUS,
    ",": pygame.K_COMMA,
    "-": pygame.K_MINUS,
    ".": pygame.K_PERIOD,
    "/": pygame.K_SLASH,
    ":": pygame.K_COLON,
    ";": pygame.K_SEMICOLON,
    "<": pygame.K_LESS,
    "=": pygame.K_EQUALS,
    ">": pygame.K_GREATER,
    "?": pygame.K_QUESTION,
    "@": pygame.K_AT,
    "[": pygame.K_LEFTBRACKET,
    "\\": pygame.K_BACKSLASH,
    "]": pygame.K_RIGHTBRACKET,
    "^": pygame.K_CARET,
    "_": pygame.K_UNDERSCORE,
    "`": pygame.K_BACKQUOTE,
    "kp0": pygame.K_KP0,
    "kp1": pygame.K_KP1,
    "kp2": pygame.K_KP2,
    "kp3": pygame.K_KP3,
    "kp4": pygame.K_KP4,
    "kp5": pygame.K_KP5,
    "kp6": pygame.K_KP6,
    "kp7": pygame.K_KP7,
    "kp8": pygame.K_KP8,
    "kp9": pygame.K_KP9,
    "kp.": pygame.K_KP_PERIOD,
    "kp/": pygame.K_KP_DIVIDE,
    "kp*": pygame.K_KP_MULTIPLY,
    "kp-": pygame.K_KP_MINUS,
    "kp+": pygame.K_KP_PLUS,
    "kpenter": pygame.K_KP_ENTER,
    "kp=": pygame.K_KP_EQUALS,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "right": pygame.K_RIGHT,
    "left": pygame.K_LEFT,
    "home": pygame.K_HOME,
    "end": pygame.K_END,
    "pageup": pygame.K_PAGEUP,
    "pagedown": pygame.K_PAGEDOWN,
    "insert": pygame.K_INSERT,
    "backspace": pygame.K_BACKSPACE,
    "tab": pygame.K_TAB,
    "clear": pygame.K_CLEAR,
    "return": pygame.K_RETURN,
    "delete": pygame.K_DELETE,
    "f1": pygame.K_F1,
    "f2": pygame.K_F2,
    "f3": pygame.K_F3,
    "f4": pygame.K_F4,
    "f5": pygame.K_F5,
    "f6": pygame.K_F6,
    "f7": pygame.K_F7,
    "f8": pygame.K_F8,
    "f9": pygame.K_F9,
    "f10": pygame.K_F10,
    "f11": pygame.K_F11,
    "f12": pygame.K_F12,
    "f13": pygame.K_F13,
    "f14": pygame.K_F14,
    "f15": pygame.K_F15,
    "numlock": pygame.K_NUMLOCK,
    "capslock": pygame.K_CAPSLOCK,
    "scrolllock": pygame.K_SCROLLLOCK,
    "rshift": pygame.K_RSHIFT,
    "lshift": pygame.K_LSHIFT,
    "rctrl": pygame.K_RCTRL,
    "lctrl": pygame.K_LCTRL,
    "ralt": pygame.K_RALT,
    "lalt": pygame.K_LALT,
    "rgui": pygame.K_RGUI,
    "lgui": pygame.K_LGUI,
    "rmeta": pygame.K_RMETA,
    "lmeta": pygame.K_LMETA,
    "rsuper": pygame.K_RSUPER,
    "lsuper": pygame.K_LSUPER,
    "mode": pygame.K_MODE,
    "pause": pygame.K_PAUSE,
    "escape": pygame.K_ESCAPE,
    "help": pygame.K_HELP,
    "print": pygame.K_PRINT,
    "printscreen": pygame.K_PRINTSCREEN,
    "sysreq": pygame.K_SYSREQ,
    "break": pygame.K_BREAK,
    "menu": pygame.K_MENU,
    "power": pygame.K_POWER,
    "euro": pygame.K_EURO,
    "androidback": pygame.K_AC_BACK
}

STRING_TO_MODCODE = {
    "none": pygame.KMOD_NONE,
    "lshift": pygame.KMOD_LSHIFT,
    "rshift": pygame.KMOD_RSHIFT,
    "shift": pygame.KMOD_SHIFT,
    "lctrl": pygame.KMOD_LCTRL,
    "rctrl": pygame.KMOD_RCTRL,
    "ctrl": pygame.KMOD_CTRL,
    "lalt": pygame.KMOD_LALT,
    "ralt": pygame.KMOD_RALT,
    "alt": pygame.KMOD_ALT,
    "lmeta": pygame.KMOD_LMETA,
    "rmeta": pygame.KMOD_RMETA,
    "meta": pygame.KMOD_META,
    "capslock": pygame.KMOD_CAPS,
    "numlock": pygame.KMOD_NUM,
    "mode": pygame.KMOD_MODE
}


class Key(str, Enum):
    UNKNOWN = "unknown"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    H = "h"
    I = "i"
    J = "j"
    K = "k"
    L = "l"
    M = "m"
    N = "n"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    S = "s"
    T = "t"
    U = "u"
    V = "v"
    W = "w"
    X = "x"
    Y = "y"
    Z = "z"
    NUM_0 = "0"
    NUM_1 = "1"
    NUM_2 = "2"
    NUM_3 = "3"
    NUM_4 = "4"
    NUM_5 = "5"
    NUM_6 = "6"
    NUM_7 = "7"
    NUM_8 = "8"
    NUM_9 = "9"
    SPACE = "space"
    EXCLAIM = "!"
    QUOTEDBL = "\""
    HASH = "#"
    PERCENT = "%"
    DOLLAR = "$"
    AMPERSAND = "&"
    QUOTE = "'"
    LEFTPAREN = "("
    RIGHTPAREN = ")"
    ASTERISK = "*"
    PLUS = "+"
    COMMA = ","
    MINUS = "-"
    PERIOD = "."
    SLASH = "/"
    COLON = ":"
    SEMICOLON = ";"
    LESS = "<"
    EQUALS = "="
    GREATER = ">"
    QUESTION = "?"
    AT = "@"
    LEFTBRACKET = "["
    BACKSLASH = "\\"
    RIGHTBRACKET = "]"
    CARET = "^"
    UNDERSCORE = "_"
    BACKQUOTE = "`"
    KP_0 = "kp0"
    KP_1 = "kp1"
    KP_2 = "kp2"
    KP_3 = "kp3"
    KP_4 = "kp4"
    KP_5 = "kp5"
    KP_6 = "kp6"
    KP_7 = "kp7"
    KP_8 = "kp8"
    KP_9 = "kp9"
    KP_PERIOD = "kp."
    KP_DIVIDE = "kp/"
    KP_MULTIPLY = "kp*"
    KP_MINUS = "kp-"
    KP_PLUS = "kp+"
    KP_ENTER = "kpenter"
    KP_EQUALS = "kp="
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"
    HOME = "home"
    END = "end"
    PAGEUP = "pageup"
    PAGEDOWN = "pagedown"
    INSERT = "insert"
    BACKSPACE = "backspace"
    TAB = "tab"
    CLEAR = "clear"
    RETURN = "return"
    DELETE = "delete"
    F1 = "f1"
    F2 = "f2"
    F3 = "f3"
    F4 = "f4"
    F5 = "f5"
    F6 = "f6"
    F7 = "f7"
    F8 = "f8"
    F9 = "f9"
    F10 = "f10"
    F11 = "f11"
    F12 = "f12"
    F13 = "f13"
    F14 = "f14"
    F15 = "f15"
    NUMLOCK = "numlock"
    CAPSLOCK = "capslock"
    SCROLLLOCK = "scrolllock"
    RSHIFT = "rshift"
    LSHIFT = "lshift"
    RCTRL = "rctrl"
    LCTRL = "lctrl"
    RALT = "ralt"
    LALT = "lalt"
    RGUI = "rgui"
    LGUI = "lgui"
    RMETA = "rmeta"
    LMETA = "lmeta"
    RSUPER = "rsuper"
    LSUPER = "lsuper"
    MODE = "mode"
    PAUSE = "pause"
    ESCAPE = "escape"
    HELP = "help"
    PRINT = "print"
    PRINTSCREEN = "printscreen"
    SYSREQ = "sysreq"
    BREAK = "break"
    MENU = "menu"
    POWER = "power"
    EURO = "euro"
    ANDROIDBACK = "androidback"


class Modifier(str, Enum):
    NONE = "none"
    LSHIFT = "lshift"
    RSHIFT = "rshift"
    SHIFT = "shift"
    LCTRL = "lctrl"
    RCTRL = "rctrl"
    CTRL = "ctrl"
    LALT = "lalt"
    RALT = "ralt"
    ALT = "alt"
    LMETA = "lmeta"
    RMETA = "rmeta"
    META = "meta"
    NUM = "numlock"
    CAPS = "capslock"
    MODE = "mode"


KeyLike = Union[str, Key]
ModifierLike = Union[str, Modifier]


class Keyboard:
    @staticmethod
    def _get_key_state(key: KeyLike, wrapper: pygame.key.ScancodeWrapper) -> bool:
        keycode = STRING_TO_KEYCODE.get(key, pygame.K_UNKNOWN)
        return wrapper[keycode]
    
    @staticmethod
    def is_pressed(key: KeyLike) -> bool:
        wrapper = pygame.key.get_pressed()
        return Keyboard._get_key_state(key, wrapper)

    @staticmethod
    def is_released(key: KeyLike) -> bool:
        return not Keyboard.is_pressed(key)

    @staticmethod
    def is_just_pressed(key: KeyLike) -> bool:
        wrapper = pygame.key.get_just_pressed()
        return Keyboard._get_key_state(key, wrapper)

    @staticmethod
    def is_just_released(key: KeyLike) -> bool:
        wrapper = pygame.key.get_just_released()
        return Keyboard._get_key_state(key, wrapper)

    @staticmethod
    def is_modifier_active(modifier: ModifierLike) -> bool:
        bitmask = pygame.key.get_mods()
        modcode = STRING_TO_MODCODE.get(modifier, pygame.KMOD_NONE)
        return bool(bitmask & modcode)

    @staticmethod
    def get_axis(negative_key: KeyLike, positive_key: KeyLike) -> int:
        negative_pressed = Keyboard.is_pressed(negative_key)
        positive_pressed = Keyboard.is_pressed(positive_key)
        return positive_pressed - negative_pressed
