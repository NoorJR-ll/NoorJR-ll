class Flyweight:
    def __init__(self, shared_data):
        self.shared_data = shared_data

    def operation(self, unique_data):
        print(f"Shared data: {self.shared_data}, Unique data: {unique_data}")


class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_data):
        if shared_data not in self.flyweights:
            self.flyweights[shared_data] = Flyweight(shared_data)
        return self.flyweights[shared_data]


# Client code
factory = FlyweightFactory()

flyweight1 = factory.get_flyweight("shared_data_1")
flyweight1.operation("data_1")

flyweight2 = factory.get_flyweight("shared_data_2")
flyweight2.operation("data_2")

flyweight3 = factory.get_flyweight("shared_data_1")
flyweight3.operation("data_3")
