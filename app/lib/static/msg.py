# coding=utf-8
import os
import platform
import time
import traceback

BIUMSG_METHODS = {
    "default": 0, "highlight": 1, "underline": 4, "flash": 5, "anti": 7, "disable": 8
}

BIUMSG_COLORS = {
    "black": (30, 40),
    "red": (31, 41),
    "green": (32, 42),
    "yellow": (33, 43),
    "blue": (34, 44),
    "purple-red": (35, 45),
    "cyan-blue": (36, 46),
    "white": (37, 47),
    "default": (38, 38)
}

BIUMSG_isColor = True
if os.name == "nt":
    os.system("color")
    if "10" not in platform.platform():
        BIUMSG_isColor = False

from altfe.interface.root import interRoot


@interRoot.bind("localMsger", "LIB_STATIC")
class static_local_msger(object):
    @classmethod
    def msg(cls, text, header=None, out=True):
        r = cls.mformat(text, "default", header=header)
        if not out:
            return r
        print(r)

    @classmethod
    def sign(cls, text, header=None, out=True):
        r = cls.mformat(text, "white", "black", "highlight", header=header)
        if not out:
            return r
        print(r)

    @classmethod
    def error(cls, text, header=None, out=True):
        r = cls.mformat(text, "red", header=header)
        if not out:
            return r
        print("!Error at %s:" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(r)

    @classmethod
    def green(cls, text, header=None, out=True):
        r = cls.mformat(text, "green", header=header)
        if not out:
            return r
        print(r)

    @classmethod
    def red(cls, text, header=None, out=True):
        r = cls.mformat(text, "red", header=header)
        if not out:
            return r
        print(r)

    @classmethod
    def arr(cls, *text):
        for x in text:
            if type(x) == str:
                print(cls.mformat(x, "default"))
            elif type(x) == tuple:
                print(cls.mformat("%s: %s" % x, "default"))

    @classmethod
    def mformat(cls, text, front, back=None, method="default", header=None):
        if isinstance(text, Exception):
            text = traceback.format_exc()
        else:
            text = str(text)
        if header is None:
            finalText = text
        else:
            finalText = "[%s] %s" % (header, text)
        if BIUMSG_isColor is False:
            return finalText
        if back is None:
            r = f"\033[{BIUMSG_COLORS[front][0]}m{finalText}\033[0m"
        else:
            r = f"\033[{BIUMSG_METHODS[method]};{BIUMSG_COLORS[front][0]};{BIUMSG_COLORS[back][1]}m{finalText}\033[0m"
        return r
