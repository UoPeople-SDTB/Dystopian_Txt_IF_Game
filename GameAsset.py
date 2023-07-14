class GameAsset:
    def __init__(self, name, auditory_description, gustatory_description, olfactory_description, tactile_description, visual_description):
        self._name = name
        self._auditory_description = auditory_description
        self._gustatory_description = gustatory_description
        self._olfactory_description = olfactory_description
        self._tactile_description = tactile_description
        self._visual_description = visual_description

    def command_aliases(self, command):
        if command.lower() in ["listen", "hear"]:
            self.listen()
        elif command.lower() in ["look", "examine"]:
            self.look()
        elif command.lower() in ["smell"]:
            self.smell()
        elif command.lower() in ["talk", "speak"]:
            self.speak()
        elif command.lower() in ["taste"]:
            self.taste()
        elif command.lower() in ["feel", "touch"]:
            self.touch()
        elif command.lower() in ["command", "alias"]:
            self.some_command()
        else:
            print("Invalid command")

    def listen(self):
        print(self._auditory_description)

    def look(self):
        print(self._visual_description)

    def smell(self):
        print(self._olfactory_description)

    def taste(self):
        print(self._gustatory_description)

    def touch(self):
        print(self._tactile_description)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
