import numpy as np

class circle:
    x0 = 520
    y0 = 100
    x1 = 1400
    y1 = 980
    r = 440
    a = 960
    b = 540

    def get_ord(self, x, sign):
        root = np.sqrt(np.power(self.r, 2) - np.power(x - self.a, 2))
        return self.b + (root if sign else -root)

    def circum(self):
        return 2 * np.pi * self.r