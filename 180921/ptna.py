from responder import *

class Ptna:
    #本体
    def __init__(self, name):

        self.name = name
        self.res_random = RandomResponder("Random")
        self.res_what = RepeatResponder("Repeat")
        self.responder = self.res_what


    def dialogue(self, input):
        x = random.randint(0, 1)
        if x == 0:
            self.responder = self.res_random
        else:
            self.responder = self.res_what

        return self.responder.response(input)

    def get_responder_name(self):
        return self.responder.name

    def get_name(self):
        return self.name

