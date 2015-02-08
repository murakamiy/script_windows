KEYCODE = (
    ("j",  ord("j"),  70,   200),
    ("k",  ord("k"),  70,   270),
    ("l",  ord("l"),  30,   230),
    ("h",  ord("h"),  110,  230),
    ("c",  ord("c"),  110,  170),

    ("0",  ord("0"),  50,   300),

    ("1",  ord("1"),  30,   270),
    ("2",  ord("2"),  70,   270),
    ("3",  ord("3"),  110,  270),

    ("4",  ord("4"),  30,   240),
    ("5",  ord("5"),  70,  240),
    ("6",  ord("6"),  110,  240),

    ("7",  ord("7"),  30,   200),
    ("8",  ord("8"),  70,   200),
    ("9",  ord("9"),  110,  200),
)

KEYCODE_ARROW = (
    ("up",     0x48,  70,   200),
    ("down",   0x50,  70,   270),
    ("left",   0x4B,  30,   230),
    ("right",  0x4D,  110,  230),
)

KEYCODE_CONTROL = {
    "control+h":ord("h") - 0x60,
    "control+s":ord("s") - 0x60,
    "control+q":ord("q") - 0x60,
}


# for k in KEYCODE_ARROW:
#     print k
