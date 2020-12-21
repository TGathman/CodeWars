# Python 3.8, 20 March 2020.


def make_readable(seconds):

    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    seconds = (seconds - hours*3600 - minutes*60)
    fhours = "0" + str(hours) if len(str(hours)) == 1 else hours
    fminutes = "0" + str(minutes) if len(str(minutes)) == 1 else minutes
    fseconds = "0" + str(seconds) if len(str(seconds)) == 1 else seconds
    return f"{fhours}:{fminutes}:{fseconds}"
