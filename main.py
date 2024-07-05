class Territories:
    
    def __init__(self, occupier, territory_name, amount_of_troops, adjacent_territories):
        self.occupier = occupier
        self.territory_name = territory_name
        self.amount_of_troops = amount_of_troops
        self.adjacent_territories = adjacent_territories

    def get_info(self):
        return [self.occupier, self.territory_name, self.amount_of_troops, self.adjacent_territories]

    def change_troops(self, amount):
        self.amount = amount
        self.amount_of_troops += self.amount
    


