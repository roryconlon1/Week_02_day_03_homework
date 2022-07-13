from src.fish import Fish

class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []

    def can_eat(self, fish):
        return self.stomach.append(fish)
        

    def food_count(self):
        return len(self.can_eat)

    # def food_from_river(self, river_fish):
    #     return self.stomach.append(river_fish)