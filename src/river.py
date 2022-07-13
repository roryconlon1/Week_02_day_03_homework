from src.fish import Fish 

class River:
    def __init__(self, name, fishes):
        self.name = name
        self.fishes =[fishes]
        
    def add_fish(self, fish):
        self.fishes.append(fish)

    def lose_fish(self, fish):
        self.fishes.remove(fish)