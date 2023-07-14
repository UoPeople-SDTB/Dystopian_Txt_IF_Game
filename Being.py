import GameAsset
class Being(GameAsset):
    def __init__(self, name, description, state):
        self._name = name
        self._description = description
        self._state = state

    def look(self):
        print(self._description)
        #insert logic for possible state change
    
    def speak(self):
        print("What do you want to say to ", self.name)
        #insert logic for dialogue
        #insert logic for possible state change

    def some_command(self):
        pass

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
