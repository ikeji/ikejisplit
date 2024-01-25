# (lazy-make-configulation
#   (define target_file "lets-split.py")
#   (task "default" (target_file))
#   (task "clean" () (string-append "rm " target_file))
#   (task target_file ("gen.py")
#     (string-append "python3 gen.py > " target_file)))

import math
from pprint import pprint


# |
# |
# v y  x
#  ---->

# keyarea: 114.3 x 76.2
# header: 114x22.86
# height = 99.06

outline = [
    [[0,0], [114.3, 0]],
    [[114.3, 0],[114.3,99.06]],
    [[114.3,99.06],[0,99.06]],
    [[0,99.06],[0,0]],
]

components = {}

sw = 1
for y in range(4):
    for x in range(6):
        components["SW" + str(sw)] = {
            'location':[
                x*19.05+12.065,
                22.86+y*19.05+4.445,
            ],
            'rotation': 0,
        }
        components["D" + str(sw)] = {
            'location':[
                63+(sw-1)%6*4*2+(4 if ((sw-1)/6)%2 >= 1 else 0),
                9 + (8 if sw > 12 else 0),
            ],
            'rotation': 45,
        }
        sw+=1

# PiPico {{{

components["J1"] = {
    'location':[
        2.54,
        2.54+17.78
    ],
    'rotation': 90*1,
}
components["J2"] = {
    'location':[
        2.54*20,
        2.54,
    ],
    'rotation': 90*3,
}

# }}}

layout = {
    'origin': [30,30],
    'components': components,
    'outline':outline,
}

pprint(layout)

# vim: set fdm=marker :
