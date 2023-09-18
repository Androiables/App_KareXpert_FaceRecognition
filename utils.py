from os import listdir
from os.path import isdir

from constants import *

def getList(path):
    """
    :param path: Path to the dir
    :return: List of all files available
    """
    if isdir(path):
        ret = [f'{path}/{x}' for x in listdir(path)]
        return ret
    return None

def isDir(path: str):
    return isdir(path)

def isFaceDetected(status):
    if status == FACE_NO_DETECTED:
        return False
    return True