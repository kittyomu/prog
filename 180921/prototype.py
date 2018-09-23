from ptna import *

class Ptna:
    #本体のクラス
    def __init__(self, name):
        #Ptnaのname
        #responderオブジェクトを生成して、responderに格納
        #@param name Pynaオブジェクトの名前
        self.name = name
        self.responder = Responder("What")

    def dialogue(self, input):
        return self.responder.response(input)

    def get_responder_name(self):
        return self.responder.name

    def get_name(self):
        return self.name

class Responder:

    def __init__(self, name):
        self.name = name

    def response(self, input):
        return "{}ってなに？".format(input)

#実行ブロック#

def prompt(obj):

    return obj.get_name() + ":" + obj.get_responder_name() + "> "

print("Ptna System prototype : ptna")
ptna = Ptna("pyna")

while True:
    inputs = input(" > ")
    if not inputs:
        print("バイバイ")
        break
    response = ptna.dialogue(inputs)
    print(prompt(ptna), response)
