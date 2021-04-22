def isBinaryData(data):
    return hasattr(data, '__len__') and (not isinstance(data, str))