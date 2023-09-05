# Liskov Substitution Principle 



class Bird:
    def fly(self):
        return "I can fly"

def bird_flying_ability(bird):
    return bird.fly()


bird = Bird()
print(bird_flying_ability(bird))




















class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying low"
    

class Eagle(Bird):
    def fly(self):
        return "Eagle flying high"



sparrow = Sparrow()
eagle = Eagle()


print(bird_flying_ability(sparrow))
print(bird_flying_ability(eagle))