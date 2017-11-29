#what is OOP and what does it stand for?
    #we can think of it as class oriented programming
#objects are key value pairs. a class is like a fancier object.It gives a way of organizing that object so we can hhave more functions at our disposal. 

#so lets talk about classes, what they are, and how to create them. 
#to create a class we need a keyword, just like in function we needed the keyword "def", here we use the keyword "class"

class Human(object): #we ask ourselves if the class inherit any properties from another class? here the answer is no, so we will just pass the keyword object into the param
    #now we can pass properties, aka attributes, aka keys to this class. we can think of properties
    def __init__(self, name, height, weight, speed): #every function that we write as a part of any class will take in the self arguement. Self means "this particular human". Now we can pass any number of arguements we want to attach to our human.
        print "creating a human"
        self.name = name
        self.height = height
        self.weight = weight
        self.speed = speed
        self.strength = 50
        self.health = 100
        
    #square bracket notation like myobj['key'], but now we use dot notation like myobj.key. Basically we're just using dot notation to add keys to our "self" aka this object that is represented by "self". We can make these attributes dynamic, we can pass in those to our constructor so that every time we create a human, the values for those keys become whatever i pass in when i create a human.

    def sayMyName(self):
        print "my name is {}".format(self.name)

    def attack(self, monster):
        print type(monster) 
        if type(monster) is Monster:
            monster.health = monster.health -25
            print "{} attacked {} for 25 health".format(self.name, monster.name)
            print "{}'s health was reduced to {}".format(monster.name, monster.health)
        else:
            print "humans and warriors have to get along with humans and warriors!" 
        return self



#lets create a class that inherits from the Human class
class Warrior(Human): #because warrior came from a Human, it will get access to the attributes and function from human class. But before i can make all this work, i gotta say "hey, go up to my parent class, run the init function, and do all of the things you said you will do inside of your function definition. To do that we need a special function called "super"
    def __init__(self, name, height, weight, speed): #we have to pass in the traits we want to instantiate the warrior with here too because this is where it initially accepts them, then we pass it off to the parent, then handing those four arguements off to the parent class b/c the parent class function is the one that actually assigns them
        super(Warrior, self).__init__(name, height, weight, speed)
        self.strength = 500 #here we adjusted the strength number for warrior b/c we want the warrior to be stronger than the parent class human 
        self.health = 150

    def sayMyName(self):
        #we usually wont overwrite the function from the parent class if we're inheriting, but we can if we wanted to. Generally, we can also have the method do something extra
        super(Warrior, self).sayMyName()
        print 'oh by the way I am a warrior!!!'

class Monster(Human):
    def __init__(self, name, height, weight, speed):
        super(Monster, self).__init__(name, height, weight, speed)



# Superman = Human('Superman', 70, 10, 100)
# Batman = Human('Batman', 75, 200, 8 )


warrior = Warrior("thrall", 80, 300, 5)
warrior2= Warrior('rob', 100, 100, 100)
monster = Monster('warewolf', 90, 325, 8)

#how do i invoke the attack function on the warrior 

#warrior.attack(monster)
#warrior2.attack(warrior)

#x = warrior.attack(monster)
#print x #x is essentially that same warrior, so it allows me to chain methods together

#print warrior.strength
#warrior.sayMyName()


#i could even write a for loop to do something several times or i could chain them:

for i in range(3):
    warrior.attack(monster)


#OOP can be confusing, but be okay with the confusion


