import enum
import pygame

class Key(enum.Enum):
    KEY_UNKNOWN = "unknown"
    KEY_A = "a"
    KEY_B = "b"
    KEY_C = "c"
    KEY_D = "d"
    KEY_E = "e"
    KEY_F = "f"
    KEY_G = "g"
    KEY_H = "h"
    KEY_I = "i"
    KEY_J = "j"
    KEY_K = "k"
    KEY_L = "l"
    KEY_M = "m"
    KEY_N = "n"
    KEY_O = "o"
    KEY_P = "p"
    KEY_Q = "q"
    KEY_R = "r"
    KEY_S = "s"
    KEY_T = "t"
    KEY_U = "u"
    KEY_V = "v"
    KEY_W = "w"
    KEY_X = "x"
    KEY_Y = "y"
    KEY_Z = "z"
    KEY_0 = "0"
    KEY_1 = "1"
    KEY_2 = "2"
    KEY_3 = "3"
    KEY_4 = "4"
    KEY_5 = "5"
    KEY_6 = "6"
    KEY_7 = "7"
    KEY_8 = "8"
    KEY_9 = "9"
    KEY_SPACE = "space"
    KEY_EXCLAIM = "!"
    KEY_QUOTEDBL = "\""
    KEY_HASH = "#"
    KEY_PERCENT = "%"
    KEY_DOLLAR = "$"
    KEY_AMPERSAND = "&"
    KEY_QUOTE = "'"
    KEY_LEFTPAREN = "("
    KEY_RIGHTPAREN = ")"
    KEY_ASTERISK = "*"
    KEY_PLUS = "+"
    KEY_COMMA = ","
    KEY_MINUS = "-"
    KEY_PERIOD = "."
    KEY_SLASH = "/"
    KEY_COLON = ":"
    KEY_SEMICOLON = ";"
    KEY_LESS = "<"
    KEY_EQUALS = "="
    KEY_GREATER = ">"
    KEY_QUESTION = "?"
    KEY_AT = "@"
    KEY_LEFTBRACKET = "["
    KEY_BACKSLASH = "\\"
    KEY_RIGHTBRACKET = "]"
    KEY_CARET = "^"
    KEY_UNDERSCORE = "_"
    KEY_BACKQUOTE = "`"
    KEY_KP_0 = "kp0"
    KEY_KP_1 = "kp1"
    KEY_KP_2 = "kp2"
    KEY_KP_3 = "kp3"
    KEY_KP_4 = "kp4"
    KEY_KP_5 = "kp5"
    KEY_KP_6 = "kp6"
    KEY_KP_7 = "kp7"
    KEY_KP_8 = "kp8"
    KEY_KP_9 = "kp9"
    KEY_KP_PERIOD = "kp."
    KEY_KP_DIVIDE = "kp/"
    KEY_KP_MULTIPLY = "kp*"
    KEY_KP_MINUS = "kp-"
    KEY_KP_PLUS = "kp+"
    KEY_KP_ENTER = "kpenter"
    KEY_KP_EQUALS = "kp="
    KEY_UP = "up"
    KEY_DOWN = "down"
    KEY_RIGHT = "right"
    KEY_LEFT = "left"
    KEY_HOME = "home"
    KEY_END = "end"
    KEY_PAGEUP = "pageup"
    KEY_PAGEDOWN = "pagedown"
    KEY_INSERT = "insert"
    KEY_BACKSPACE = "backspace"
    KEY_TAB = "tab"
    KEY_CLEAR = "clear"
    KEY_RETURN = "return"
    KEY_DELETE = "delete"
    KEY_F1 = "f1"
    KEY_F2 = "f2"
    KEY_F3 = "f3"
    KEY_F4 = "f4"
    KEY_F5 = "f5"
    KEY_F6 = "f6"
    KEY_F7 = "f7"
    KEY_F8 = "f8"
    KEY_F9 = "f9"
    KEY_F10 = "f10"
    KEY_F11 = "f11"
    KEY_F12 = "f12"
    KEY_F13 = "f13"
    KEY_F14 = "f14"
    KEY_F15 = "f15"
    KEY_NUMLOCK = "numlock"
    KEY_CAPSLOCK = "capslock"
    KEY_SCROLLLOCK = "scrolllock"
    KEY_RSHIFT = "rshift"
    KEY_LSHIFT = "lshift"
    KEY_RCTRL = "rctrl"
    KEY_LCTRL = "lctrl"
    KEY_RALT = "ralt"
    KEY_LALT = "lalt"
    KEY_RGUI = "rgui"
    KEY_LGUI = "lgui"
    KEY_RMETA = "rmeta"
    KEY_LMETA = "lmeta"
    KEY_RSUPER = "rsuper"
    KEY_LSUPER = "lsuper"
    KEY_MODE = "mode"
    KEY_PAUSE = "pause"
    KEY_ESCAPE = "escape"
    KEY_HELP = "help"
    KEY_PRINT = "print"
    KEY_PRINTSCREEN = "printscreen"
    KEY_SYSREQ = "sysreq"
    KEY_BREAK = "break"
    KEY_MENU = "menu"
    KEY_POWER = "power"
    KEY_EURO = "euro"
    KEY_ANDROIDBACK = "androidback"

class ModifierKey(enum.Enum):
    MODKEY_NONE = "none"
    MODKEY_LSHIFT = "lshift"
    MODKEY_RSHIFT = "rshift"
    MODKEY_SHIFT = "shift"
    MODKEY_LCTRL = "lctrl"
    MODKEY_RCTRL = "rctrl"
    MODKEY_CTRL = "ctrl"
    MODKEY_LALT = "lalt"
    MODKEY_RALT = "ralt"
    MODKEY_ALT = "alt"
    MODKEY_LMETA = "lmeta"
    MODKEY_RMETA = "rmeta"
    MODKEY_META = "meta"
    MODKEY_CAPS = "capslock"
    MODKEY_NUM = "numlock"
    MODKEY_MODE = "mode"

STRING_TO_SCANCODE = {
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

STRING_TO_MODKEY = {
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

class Keyboard:
    def _get_key_state(self, key: Key, wrapper: pygame.key.ScancodeWrapper) -> bool:
        scancode = STRING_TO_SCANCODE.get(key, pygame.K_UNKNOWN)
        return wrapper[scancode]
    
    def is_pressed(self, key: Key) -> bool:
        wrapper = pygame.key.get_pressed()
        return self._get_key_state(key, wrapper)

    def is_released(self, key: Key) -> bool:
        return not self.is_pressed(key)

    def is_just_pressed(self, key: Key) -> bool:
        wrapper = pygame.key.get_just_pressed()
        return self._get_key_state(key, wrapper)

    def is_just_released(self, key: Key) -> bool:
        wrapper = pygame.key.get_just_released()
        return self._get_key_state(key, wrapper)

    def is_modifier_active(self, modifier: ModifierKey) -> bool:
        bitmask = pygame.key.get_mods()
        modkey = STRING_TO_MODKEY.get(modifier, pygame.KMOD_NONE)
        return bool(bitmask & modkey)

    def get_axis(self, negative_key: Key, positive_key: Key) -> int:
        negative_pressed = self.is_pressed(negative_key)
        positive_pressed = self.is_pressed(positive_key)
        return positive_pressed - negative_pressed
