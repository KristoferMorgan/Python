from random  impotr randint

def get_tempereture():
    return randint(-20,0) if sensor else randint(0,20)


def get_preassure():
    return randint(750,700)

def get_wind_speed():
    return 30       