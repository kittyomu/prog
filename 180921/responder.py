import random

class Responder:

    def __init__(self, name):
        self.name = name

    def response(self, input):

        return ""
    def get_name(self):
        return self.name

class RepeatResponder(Responder):

    def response(self, input):
        return "{}ってなに？".format(input)

class RandomResponder(Responder):
    def __init__(self, name):
        super().__init__(name)
        self.responses = []

        rfile = open("random.txt", "r", encoding="utf_8")
        r_lines = rfile.readlines()
        rfile.close()

        for line in r_lines:
            str = line.rstrip("\n")
            if (str!=""):
                self.responses.append(str)


    def response(self, input):
        return (random.choice(self.responses))

