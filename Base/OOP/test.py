class MyClass:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def calc_method(self,x,y,z):

        return (x + y/z)

    def printing_calc_result(calc_method):

        print(calc_method) # - хочу показать результат подсчета а не показать то что это функция)



##########################################

root = MyClass(150,60,40)
root.printing_calc_result()