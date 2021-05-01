from email.utils import formatdate

def isBinaryData(data):
    return hasattr(data, '__len__') and (not isinstance(data, str))

def HttpDateTime():
    return formatdate(timeval=None, localtime=False, usegmt=True)