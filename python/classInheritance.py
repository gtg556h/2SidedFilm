import numpy as np
#import sampleLib as sl
import matplotlib.pyplot as plt
class class1:
    def __init__(self):
        print('init class 1')
        self.param1 = 1

    class class2:
        def __init__(self, c1):
            print('init class 2')
            self.param2 = c1.param1 + 1

    def initc2(self):
        self.c2 = self.class2(self)

    def initc3(self):
        self.c3 = class3()


class class3:
    def __init__(self):
        print('init class 3')
        self.param3 = 3


