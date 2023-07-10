import inspect

def superglobals():
    _globals = dict(inspect.getmembers(
                inspect.stack()[len(inspect.stack()) - 1][0]))["f_globals"]
    return _globals

def getglobal(key, default=None):
    """
    getglobal(key[, default]) -> value
    
    Return the value for key if key is in the global dictionary, else default.
    """
    _globals = dict(inspect.getmembers(
                inspect.stack()[len(inspect.stack()) - 1][0]))["f_globals"]
    return _globals.get(key, default)

def setglobal(key, value):
    _globals = superglobals()
    _globals[key] = value

def defaultglobal(key, value):
    """
    defaultglobal(key, value)

    Set the value of global variable `key` if it is not otherwise st
    """
    _globals = superglobals()
    if key not in _globals:
        _globals[key] = value
