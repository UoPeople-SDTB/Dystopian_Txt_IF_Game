from Being import Being # importing the being class from the being module

class Animal(Being):
    def __init__(self, name, description, state):
        super().__init__(name, description, state)
