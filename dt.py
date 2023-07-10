import datetime


def dt() -> str:
    """ formatted datetime string for tagging output """
    return '[' + str(datetime.datetime.now()) + ']'


def dt_filename() -> str:
    """ formatted datetime string for tagging output """
    return '_' + str(datetime.datetime.now()).replace(':', '.').replace(' ', '_') + '_'