from math import pi

class lingkaran:
        #
    def __init__(self, r):
        self.r = r
        #
    def show_r(self):
        print(self.r)
        #
    def area(self):
        print(3.14 * self.r * self.r)
        #

   #RUNING Fungsi Dalam Class
circle = lingkaran(18)
circle.__init__
print("jari-jari : ")
circle.show_r()
print("luas : ")
circle.area()     


