class Michael:
    count = 0
    max = 5

    def teach(self):
        if self.__class__.count < self.__class__.max:
            print("強く")
        else:
            print("ok")
        self.__class__.count += 1

oni1 = Michael()
for i in range(4):
    print("スマッシュ")
    oni1.teach()

oni2 = Michael()

for i in range(2):
    print("バックストローク")
    oni2.teach()
