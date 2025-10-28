"""Task 2

Doggy age
Create a class Dog with class attribute 'age_factor' equals to 7.
Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent."""

class Dog :
    age_factor = 7
    def __init__(self, dog_name, dog_age):
        self.dog_name = dog_name
        self.dog_age = dog_age
    def human_age(self):
        total_human_age = self.age_factor * self.dog_age
        return total_human_age
dog_1 = Dog("Richy", 10)
print (f" {dog_1.dog_name} in a human age is {dog_1.human_age()} years old")