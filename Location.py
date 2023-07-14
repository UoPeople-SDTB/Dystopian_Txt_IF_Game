from GameAsset import GameAsset 

class Location(GameAsset): 
    #Defining the dunder init method: 
    def __init__(self, name, description): 
        super.__init__(name, description)
