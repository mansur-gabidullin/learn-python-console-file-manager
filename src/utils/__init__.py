"""
Вспомогательные функции-утилиты
"""


def wrap(fn, *args, **kwargs):
    """Даёт возможность вызвать функцию с заранее определёнными параметрами"""
    return lambda: fn(*args, **kwargs)