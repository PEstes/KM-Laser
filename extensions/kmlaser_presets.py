_pcolors = {
    "#ff0000": "cut",
    "#000000": "cut",
    "#00ffff": "engrave-light",
    "#0000ff": "engrave-heavy",
}

_presets = {
    "3mm-wood": {
        "engrave-light": [10000,1000,0.15],
        "engrave-heavy": [10000,1000,0.2],
        "cut": [10000,750,0.55],
    },
    "6mm-wood": {
        "engrave-light": [10000,1000,0.15],
        "engrave-heavy": [10000,1000,0.2],
        "cut": [10000,500,0.55],
    },
    "3mm-acrylic": {
        "engrave-light": [10000,1000,0.17],
        "engrave-heavy": [10000,1000,0.25],
        "cut": [10000,600,0.55],
    },
    "6mm-acrylic": {
        "engrave-light": [10000,1500,0.2],
        "engrave-heavy": [10000,1000,0.2],
        "cut": [10000,400,0.55],
    },
    "paper": {
        "engrave-light": [1, 1000, 0.2], # Perforated
        "engrave-heavy": [10000,1500,0.15],
        "cut": [10000, 500, 0.165]
    },
    "cardboard": {
        "engrave-light": [10000,400,0.15],
        "engrave-heavy": [10000,1000,0.17],
        "cut": [10000,1000,0.5]
    }
}
