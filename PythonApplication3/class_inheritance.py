class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        # self.sides =  no_of_sides # you can even do this
        self.sides = [0 for i in range(no_of_sides)]
        print('Inside __init__(): ',self.sides)

    def input_sides(self):
        print('Befor input of value: ',self.sides)
        self.sides =[float(input('Enter side ' +str(i+1)+ ' : ')) for i in range(self.n)]
        print('After input of value: ',self.sides)
        self.disp_sides()
    
    def disp_sides(self):
        for i in range(self.n):
            print('Side ', i+1,'is', self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        #Polygon(3)
        Polygon.__init__(self, 3)

        self.find_area()

    def find_area(self):
        self.input_sides()
        a, b, c = self.sides


        s = (a+b+c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('Area of Triangle is ', area)

t= Triangle()
#print(t.sides)
print(help(Developer)) 
