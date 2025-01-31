"""
Goal:            Practice Python OOP
Description:     Tamagotchi pet object
Author:          Émilie Roy
Date:            13-01-2025
"""

from datetime import date


#-- Decorators

def pet_status_decorator(func):
    #Decorator to check if tamagotchi pet is alive before performing any actions with pet
    def wrapper(self, *args):
        petStats = [self.energy, self.hunger, self.happiness]
        for stat in petStats:
            if stat < 1 : 
                print(f"{self.name}'s life stats are 0, they have died :c")
                print(self)
                return
            else:
                return func(self, *args)
    return wrapper



class Tamagotchi:

    #-- Constructor and attributes

    def __init__(self, name):
        #Creating the tamagotchi pet. The user can pick its pet's name. Other attributes have default starting values
        self.__name = name
        self.__hunger = 30
        self.__energy = 70
        self.__happiness = 50
        self.__dob = date.today()
    # Accepted range for hunger, energy and happiness : min is 0, max is 100.
    # These values will be limited to the accepted range with the clamp_decorator

   
    
    #-- Getters

    @property
    def name(self):
        return self.__name
    
    @property
    def hunger(self):
        return self.__hunger
    
    @property
    def energy(self):
        return self.__energy
    
    @property
    def happiness(self):
        return self.__happiness
    
    @property
    def dob(self):
        return self.__dob
    
    def getAge(self):
        #Calculates the difference in days between when the function is called and when Tamagotchi class was created
        age = date.today() - self.__dob
        print(f"{self.__name} is {age.days} old today!")
        return age.days
    

    #-- Setters

    @name.setter
    #Allows the user to change their pet's name
    def name(self, name):
        if str.isspace(name) or not name: #make sure the string is not whitespaces or empty
            "Tamagotchi pet's name must be valid"
        else:
            self.__name = name
            print(f"Tamagotchi pet's name changed succesfully to {name}")
            

    @pet_status_decorator
    def eat(self) :
        # Eating action. Option of 4 different foods. Modifies hunger, happiness and energy. 

        foodChoices = ["poutine", "apple", "coffee", "lasagna"]
        validChoice = False

        if self.__hunger < 100 :
            while validChoice == False:
                choice = input(f"What should {self.__name} eat:{"/".join(foodChoices)}? ")
                choice = choice.lower()
                if choice in foodChoices :
                    validChoice = True
            
            if choice == "poutine":
                self.__hunger = self.clamp(self.__hunger + 30)
                self.__happiness = self.clamp(self.__happiness + 10)
                self.__energy = self.clamp(self.__energy - 5)
            
            elif choice == "apple":
                self.__hunger = self.clamp(self.__hunger + 5)
                self.__happiness = self.clamp(self.__happiness + 5)
                self.__energy = self.clamp(self.__energy + 5)
                
            elif choice == "coffee":
                self.__happiness = self.clamp(self.__happiness + 5)
                self.__energy = self.clamp(self.__energy + 10)
                
            elif choice == "lasagna":
                self.__hunger = self.clamp(self.__hunger + 1)
                self.__happiness = self.clamp(self.__happiness + 10)
                self.__energy = self.clamp(self.__energy - 10)
            
            print(f"{self.__name} ate some {choice}.")

        else:
            print(f"{self.__name} is not hungry now!")
        
        print(self)
        
   
    @pet_status_decorator
    def rest(self) :
        #Resting action. 2 different options. Modifies energy and hunger. 

        restChoices = ["nap", "sleep"]
        validChoice = False

        if self.__energy < 100:
            while validChoice == False:
                choice = input(f"How long should {self.__name} rest? {"/".join(restChoices)} ")
                choice = choice.lower()
                if choice in restChoices:
                    validChoice = True
            
            if choice == "nap":
                print(f"{self.__name} is napping.")
                self.__energy = self.clamp(self.__energy + 15)
            
            elif choice == "sleep" :
                print(f"{self.__name} is sleeping.")
                self.__energy = 100
                self.__hunger = self.clamp(self.__hunger - 20)
            
        else:
            print(f"{self.__name} is not tired!")
        
        print(self)

    
    @pet_status_decorator
    def play(self) :
        "to do: game selection, implement games, adjust energy/happiness/hunger meters"
        "games ideas: rock-paper-scissors, guess number, simons says"


    @pet_status_decorator
    def pet(self) :
        #Petting action. No options. Modifies happiness.

        if self.__happiness < 100 :
            self.__happiness = self.clamp(self.__happiness + 10)
            print(f"{self.__name} loves pets!")
        else:
            print(f"{self.__name} is already very happy!")
        
        print(self)



    #-- Overrides

    def __str__(self):
        return f"{self.__name} has: \n{self.__hunger}/100 hunger \n{self.__energy}/100 energy \n{self.__happiness}/100 happiness"


    #-- Helpers

    def clamp(self, value):
        # Prevents pet's stats from being outside accepted values (min=0, max=100)
        minValue = 0
        maxValue = 100
        return max(minValue, min(maxValue, value))