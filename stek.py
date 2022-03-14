from queue import Empty
from turtle import left


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, el):
        self._data.append(el)
        return self._data

    def top(self):
        if self.is_empty():
            raise Empty("Stack je prazan")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack je prazan")
        return self._data.pop()


def is_match(exp):
    lefty = "({["
    righty = ")}]"
    s = ArrayStack()
    for ch in exp:
        if ch in lefty:
            s.push(ch)
        elif ch in righty:
            if s.is_empty():
                return False
            if righty.index(ch) != lefty.index(s.pop()):
                return False
    return s.is_empty()


if __name__ == "__main__":
    print(is_match("(2z+y)-(3h+y))"))
