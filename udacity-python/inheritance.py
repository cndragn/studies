class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, no_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.no_toys = no_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of toys - "+str(self.no_toys))

billy_cyrus = Parent("Cyrus","blue")
#print(billy_cyrus.last_name)
#billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "blue", 5)
#print(miley_cyrus.last_name)
#print(miley_cyrus.no_toys)
miley_cyrus.show_info()


