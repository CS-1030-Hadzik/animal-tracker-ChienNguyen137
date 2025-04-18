from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    animal1 = Animal("Generic", "Unknown")

    # TODO: Print the Animal instance
    print(animal1)

    # TODO: Call the method to make a generic animal sound
    animal1.speak()

    # TODO: Create an instance of the Dog class
    dog1 = Dog("Buddy", "Canine", "Golden Retriever")

    # TODO: Print the Dog instance
    print(dog1)

    # TODO: Call the method to make the dog-specific sound
    dog1.speak()

    # TODO: print out all the animals
    print("All Animals:")
    for animal in Animal.all_animals:
        print(animal)
