# Tested on https://github.com/KMKfw/kmk_firmware/tree/690286b42b231c02f66b53023a7aece1483b6aac

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
import board

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
    )
    row_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
    )
    diode_orientation = DiodeOrientation.ROW2COL
    data_pin = board.GP1

    coord_mapping = [
        0  , 1  , 2  , 3  , 4  , 5  , 24 , 25 , 26 , 27 , 28 , 29 ,
        6  , 7  , 8  , 9  , 10 , 11 , 30 , 31 , 32 , 33 , 34 , 35 ,
        12 , 13 , 14 , 15 , 16 , 17 , 36 , 37 , 38 , 39 , 40 , 41 ,
        18 , 19 , 20 , 21 , 22 , 23 , 42 , 43 , 44 , 45 , 46 , 47 ,
    ]


keyboard = KMKKeyboard()

from kmk.modules.split import Split

split = Split(use_pio=True)
keyboard.modules.append(split)

from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

from kmk.modules.macros import Macros

macros = Macros()
keyboard.modules.append(macros)

from kmk.keys import KC

keyid_layer = []
for i in range(48):
    keyid_layer.append(KC.MACRO(str(i),"\n"))

from kmk.modules.holdtap import HoldTap
keyboard.modules.append(HoldTap())

import re

def ex(str):
    keys = re.sub('[ \n]+', ' ', str).strip().split(' ')
    return [KC[k] for k in keys]

KC["FL"]   = KC.MO(1)
KC["FR"]   = KC.MO(2)
KC["FN"]   = KC.MO(3)
KC["ESCc"] = KC.HT(KC.ESC, KC.LCTRL)
KC["____"] = KC.TRNS

keyboard.keymap = [
    keyid_layer,  # <- Comment out after test
    # L0
    ex("""
TAB  Q    W    E    R    T    Y    U    I    O    P    BSPC
ESCc A    S    D    F    G    H    J    K    L    ;    '
LSFT Z    X    C    V    B    N    M    ,    .    /    ENT
FN   LALT ____ LGUI FL   SPC  SPC  FR   GUI  RALT RSFT FN
    """),
    # L1 L
    ex("""
~    !    @    #    $    %    ^    &    *    (    )    ____
____ ____ ____ ____ ____ ____ ____ _    +    {    }    |
____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
    """),
    # L2 R
    ex("""
`    1    2    3    4    5    6    7    8    9    0    ____
____ ____ ____ ____ ____ ____ ____ -    =    [    ]    \\
____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
    """),
    # L3 FN
    ex("""
____ F1   F2   F3   F4   F5   F6   F7   F8   F9   F10  DEL
____ F11  F12  ____ ____ ____ LEFT DOWN UP   RGHT PGUP HOME
____ ____ ____ ____ ____ ____ ____ BACK FORD ____ PGDN END
____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
    """),
    # L4 backup
    ex("""
____ ____ ____ ____ ____ ____ ____ ____ ____ ____
____ ____ ____ ____ ____ ____ ____ ____ ____ ____
____ ____ ____ ____ ____ ____ ____ ____ ____ ____
____ ____
    """),
]

if __name__ == '__main__':
    print("start")
    keyboard.go()
