from responder import *

class Ptna:
    #本体
    def __init__(self, name):

        self.name = name
        self.responder = RandomResponder("Random")

    def dealogue(self, input):

        return self.responder.response(input)
   
    def get_responder_name(self):
        return self.s\responder.name

    def get_name(self):
        return self.name

