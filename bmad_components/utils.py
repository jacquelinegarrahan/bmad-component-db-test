import numpy as np

device_marker_map = {
    "mirror": "<",
    "multipole": ">",
    "marker": "^",
    "instrument": "D",
    "lcavity": "H",
    "solenoid": "P",
    "wiggler": "o",
    "sbend":  "v",
    "rbend":   "8",
    "vkicker":  "1",
    "hkicker": "s",
    "drift": "X",
    "monitor": "4", 
    "quadrupole": "|",
    "ecollimator": "5",
    "rcollimator": "6",
}


def get_marker(device):
    return device_marker_map[device.element_type]
