class GoodDog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        print('Python is getting a behaviour')
        return f'{self._name} says arf!'

    def name(self):
        print('Python is getting a behaviour')
        return self._name

    def set_name(self, new_name):
        print('Python is setting a behaviour')
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        self._name = new_name

    def age(self):
        print('Python is getting a behaviour')
        return self._age

    def set_age(self, new_age):
        print('Python is setting a behaviour')
        if not isinstance(new_age, int):
            raise TypeError('Age must be an integer')
        if new_age < 0:
            raise ValueError("Age can't be negative")
        self._age = new_age

sparky = GoodDog('Sparky', 5)
# print(sparky.name())          # Sparky
# print(sparky.age())           # 5
# sparky.set_name('Fireplug')
# print(sparky.name())          # Fireplug
# sparky.set_age(6)
# print(sparky.age())           # 6

# sparky.set_name(42)
# # TypeError: Name must be a string

# sparky.set_age(-1)
# # ValueError: Age can't be negative

# 🎉 Huge shoutout to the amazing Xi 🎉

# You did it! After all those late nights, endless coffee cups, and relentless hard work, you’ve conquered one of the toughest exams here! Your determination and grit have paid off, and I couldn’t be prouder of you.

# This is more than just passing a test—it's a testament to your perseverance, intelligence, and sheer willpower. You've shown everyone what true dedication looks like, and you’ve set the bar launch school high!

# Now it’s time to celebrate this incredible achievement. You deserve all the accolades, and I can't wait to see where this success takes you next. Keep shining Xi, there are no limit! 🚀✨

# Maybe I should start drinking coffee too :D
