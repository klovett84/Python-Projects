from abc import ABC, abstractmethod
class recipe(ABC):
    def description(self, food):
        print("This recipe is for: ",food)
#This function is telling us to pass in an argument, but we won't tell you how
# or what kind of data it will be.
    @abstractmethod
    def prep(self, food):
        pass

class Rye(recipe):
#Here is defined how to implement the payment function from its parent prep class.
    def prep(self, food):
        print("To make this {}, carry out the following steps...".format(food))

obj = Rye()
obj.description("rye bread")
obj.prep("rye bread")


