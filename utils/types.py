import ctypes


def string_to_char(data: str) -> ctypes.c_char_p:
    return ctypes.c_char_p(data.encode("utf-8"))


def char_to_string(data: ctypes.c_char_p) -> str:
    return data.decode("utf-8")
