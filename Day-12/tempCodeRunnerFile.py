# Example
class Outer:
    def __init__(self):
        # Creating an inner class Object
        self.inner = self.Inner()

    def show(self):
        print("This is an Outer Class")

    class Inner:
        def __init__(self):
            # Creating an inner class of Inner class Object
            self.innerclassofinner = self.Innerclassofinner

        def show(self):
            print("This is the Inner class.")

        # Creating an inner class of inner
        class Innerclassofinner:
            def show():
                print("This is an Inner class of Inner class.")


# Creating an Outer class Object i.e, 'Outer' class object
outer = Outer()
outer.show()
print()

# Creating an inner class Object
obj1 = outer.inner
obj1.show()
print()

# Creating an inner class of inner class object
obj2 = outer.inner.innerclassofinner
obj2.show()
