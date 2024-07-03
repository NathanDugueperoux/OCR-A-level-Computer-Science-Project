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
    
England = Territories("Red", "England", 0, ["Denmark", "United_States", "France"])
Denmark = Territories("Red", "Denmark", 0, ["England", "United_States", "Brazil"])
Brazil = Territories("Red", "Brazil", 0, ["Denmark"])
United_States = Territories("Red", "United_States", 0, ["Denmark", "England", "France", "Germany"])
France = Territories("Blue", "France", 0, ["England", "United_States", "Germany"])
Germany = Territories("Blue", "Germany", 0, ["France", "United_States", "Austria"])
Austria = Territories("Blue", "Austria", 0, ["Germany"])

