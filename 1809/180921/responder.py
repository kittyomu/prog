import random
import re

class Responder:

    def __init__(self, name, dictionary):
        self.name = name
        self.dictionary = dictionary

    def response(self, input):

        return ""
    def get_name(self):
        return self.name

class RepeatResponder(Responder):

    def response(self, input):
        return "{}ってなに？".format(input)

class RandomResponder(Responder):
    def response(self, input):
        return random.choice(self.dictionary.random)

class PatternResponder(Responder):
    def response(self, input):
        for ptn, prs in zip(
            self.dictionary.pattern["pattern"],
            self.dictionary.pattern["phrases"]
            ):

            m = re.search(ptn, input)

            if m:
                resp = random.choice(prs.split("|"))
                return re.sub("%match%", m.group(), resp)
        return random.choice(self.dictionary.random)


