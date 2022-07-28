import modul_mult as modul
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    modul.init(value_a,value_b)
    result = modul.mult()
    view.view_data(result)