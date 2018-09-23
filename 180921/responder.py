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
        self.responses = ["いい天気だね", "君はパーリーピーポー", "10円拾った"]

    def response(self, input):
        return (random.choice(self.responses))

