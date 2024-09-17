import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

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
    # diode_orientation = DiodeOrientation.COL2ROW
    diode_orientation = DiodeOrientation.ROW2COL
    data_pin = board.GP1

    coord_mapping = [
        0  , 1  , 2  , 3  , 4  , 5  , 24 , 25 , 26 , 27 , 28 , 29 ,
        6  , 7  , 8  , 9  , 10 , 11 , 30 , 31 , 32 , 33 , 34 , 35 ,
        12 , 13 , 14 , 15 , 16 , 17 , 36 , 37 , 38 , 39 , 40 , 41 ,
        18 , 19 , 20 , 21 , 22 , 23 , 42 , 43 , 44 , 45 , 46 , 47 ,
    ]
