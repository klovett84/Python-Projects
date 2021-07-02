#Create Pet class
class Pet:
    name = ""
    sex = ""
    age = 0
    def care(self):
        careRoutine = "Perform basic care routines"
        return(careRoutine)
        

#Create new Dog class inherited from Pet class
class Dog(Pet):
    breed = ""
    size = ""
    def care(self):
        careRoutine = "Take on a walk and give a treat"
        return(careRoutine)        

#Create new Fish class inherited from Pet class
class Fish(Pet):
    species = ""
    water = ""
    def care(self):
        careRoutine = "Feed and clean tank filter"
        return(careRoutine)

#Initialize objects and use methods
if __name__ == "__main__":
    snail = Pet()
    print(snail.care())

    jimmy = Dog()
    print(jimmy.care())

    bob = Fish()
    print(bob.care())
