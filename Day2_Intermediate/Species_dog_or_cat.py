class animal:
    def __init__(self, species):
        self.species= species
        print(f"I am {species}")
    

class dog(animal):
    def speak(self):
        print("Woof!!")
    def run(self):
        print("Dog is running!!")

class cat(animal):
    def speak(self):
        print("Meow!!")

species = input("Enter the species :")

if species.lower()=="dog":
    b = dog("Dog")
    b.speak()
    b.run()

elif species.lower()=="cat":
    b = cat("Cat")
    b.speak()
else:
    print("species extinct.")
    

    


        
            
        
