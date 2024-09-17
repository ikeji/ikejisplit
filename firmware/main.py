print("Starting")

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.mouse_keys import MouseKeys

import board
import analogio
from kmk.modules import Module
from kmk.kmktime import PeriodicTimer
from supervisor import ticks_ms
from kmk.keys import AX
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()

#split = Split()
split = Split(use_pio=True)
keyboard.modules.append(split)

combos = Combos()
keyboard.modules.append(combos)

keyid_layer = []

for i in range(48):
    c, r = divmod(i, 100)
    d, u = divmod(r, 10)
    keyid_layer.append(
        simple_key_sequence(
            (
                getattr(KC, 'N' + str(c)),
                getattr(KC, 'N' + str(d)),
                getattr(KC, 'N' + str(u)),
                KC.ENT,
            )
        )
    )

import re

def ex(str):
    keys = re.sub('[ \n]+', ' ', str).strip().split(' ')
    return [KC[k] for k in keys]

keyboard.keymap = [
    keyid_layer,
]

if __name__ == '__main__':
    print("start")
    keyboard.go()
