keyboard_map = {
    "~": [35, 329],
    "`": [35, 329],
    "1": [90, 329],
    "!": [90, 329],
    "2": [144, 329],
    "@": [144, 329],
    "3": [198, 329],
    "#": [198, 329],
    "4": [253, 329],
    "$": [253, 329],
    "5": [307, 329],
    "%": [307, 329],
    "6": [361, 329],
    "^": [361, 329],
    "7": [415, 329],
    "&": [415, 329],
    "8": [469, 329],
    "*": [469, 329],
    "9": [524, 329],
    "(": [524, 329],
    "0": [579, 329],
    ")": [579, 329],
    "-": [630, 329],
    "_": [630, 329],
    "+": [685, 329],
    "=": [685, 329],
    "Q": [115, 275],
    "W": [169, 275],
    "E": [224, 275],
    "R": [278, 275],
    "T": [332, 275],
    "Y": [386, 275],
    "U": [440, 275],
    "I": [494, 275],
    "O": [548, 275],
    "P": [602, 275],
    "[": [656, 275],
    "{": [656, 275],
    "]": [710, 275],
    "}": [710, 275],
    "\\": [764, 275],
    "A": [130, 225],
    "S": [184, 225],
    "D": [238, 225],
    "F": [292, 225],
    "G": [346, 225],
    "H": [400, 225],
    "J": [454, 225],
    "K": [508, 225],
    "L": [562, 225],
    ";": [616, 225],
    ":": [616, 225],
    "'": [670, 225],
    '"': [670, 225],
    "Z": [158, 174],
    "X": [212, 174],
    "C": [266, 174],
    "V": [320, 174],
    "B": [374, 174],
    "M": [482, 174],
    "N": [428, 174],
    ",": [536, 174],
    "<": [536, 174],
    ".": [590, 174],
    ">": [590, 174],
    "/": [644, 174],
    "?": [644, 174],
}


def get_strokes(s):
    for c in s:
        if c.upper() in keyboard_map:
            yield c.upper(), keyboard_map[c.upper()]