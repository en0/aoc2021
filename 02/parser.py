from aocfw.typing import IParser


class SubmarineInstructionParser(IParser):
    def parse(self, data):
        for val in data:
            a, b = val.split(" ")
            yield a, int(b)

