class Territories:
    
    def __init__(self, occupier, territory_name, amount_of_troops, adjacent_territories, vulnerability_index, attack_potential_index):
        # Name of territry
        self.occupier = occupier
        self.territory_name = territory_name
        self.amount_of_troops = amount_of_troops
        self.adjacent_territories = adjacent_territories

    def get_name(self):
        return self.territory_name

    def change_troops(self, amount):
        self.amount = amount
        self.amount_of_troops += self.amount

    def change_team(self, new_occupier):
        self.new_occupier = new_occupier
        self.occupier = self.new_occupier

