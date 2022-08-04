from typing import Tuple


def mag_number(str, int):
    """
    Returns the number of magazines a soldier needs given a
    tuple containing the name of a soldier's weapon and
    the number of streets the soldier has to patrol.

     mag_number(("PT92", 6))
    2
     mag_number(("M4A1", 6))
    1
    """
    pass


print(mag_number("PT92", 6), 2)
print(mag_number("M4A1", 8), 1)
print(mag_number("M16A2", 19), 2)
print(mag_number("PSG1", 31), 19)
print(mag_number("PT92", 19), 4)
