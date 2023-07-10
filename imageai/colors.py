col = {'person': (0, 255, 0)}
_thickness = 2
_anno_space_h = 28
_anno_space_w = 10


def label_color(_name=None):
    # print(f'NAME: {_name}')
    color = (0, 255, 0)
    if '%' in _name:
        idx_name = _name.rfind(' ')
        _name = _name[:idx_name]
        # print(f'NAME Formatted: {_name}')
    if _name is not None:
        if col.get(_name):
            color = col.get(_name)
    # print('COLOR:', color)
    return color


def thickness(_value=_thickness):
    return _value


def anno_space_h(_value=_anno_space_h):
    return _value


def anno_space_w(_value=_anno_space_w):
    return _value
