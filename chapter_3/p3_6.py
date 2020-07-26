from chapter_3.datastructs import Queue


class Animal:
    def __init__(self, name: str):
        self.arrival_time = None
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}"


class Dog(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Cat(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AnimalShelter:
    def __init__(self):
        self.dog_q = Queue()
        self.cat_q = Queue()
        self.order_seq = 0

    def enqueue(self, animal: Animal):
        self.order_seq += 1
        animal.arrival_time = self.order_seq

        if isinstance(animal, Dog):
            self.dog_q.push(animal)
        elif isinstance(animal, Cat):
            self.cat_q.push(animal)

    def dequeueAny(self):
        if self.dog_q.isEmpty() and self.cat_q.isEmpty():
            raise Exception("No animal to adopt")
        elif self.dog_q.isEmpty():
            return self.cat_q.pop()
        elif self.cat_q.isEmpty():
            return self.dog_q.pop()

        earliest_cat = self.cat_q.peek().arrival_time
        earliest_dog = self.dog_q.peek().arrival_time

        if earliest_cat > earliest_dog:
            return self.dog_q.pop()
        else:
            return self.cat_q.pop()

    def dequeueDog(self):
        return self.dog_q.pop()

    def dequeueCat(self):
        return self.cat_q.pop()


if __name__ == "__main__":
    animals = [Dog("Dave"), Cat("Catto"), Dog("Dave2"), Cat("Catto2")]
    shelter = AnimalShelter()
    for a in animals:
        shelter.enqueue(a)

    print(f"A dog is {shelter.dequeueDog()}")
    print(f"Earliest is {shelter.dequeueAny()}")
    print(f"A cat is {shelter.dequeueCat()}")
