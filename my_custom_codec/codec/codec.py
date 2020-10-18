from encodings import utf_8
from keyword import iskeyword


def decode(string, _="strict"):
    string = bytes(string).decode(errors=_)
    lines = []
    for line in string.splitlines(True):
        if not iskeyword(line.strip()):
            lines.append(line)
    return "".join(lines), len(string)


def handler(string):
    lines = []
    for line in string.splitlines(True):
        if not iskeyword(line.decode().strip()):
            lines.append(line)
    return b"".join(lines)


class IncrementalDecoder(utf_8.IncrementalDecoder):
    def decode(self, string, final=False):
        self.buffer += string
        if final:
            buffer = self.buffer
            self.buffer = b""
            return super().decode(handler(buffer))
        return ""
