from classes import Territories

England = Territories("Red", "England", 3, ["Denmark", "United_States", "France"], 0, 0)
Denmark = Territories("Red", "Denmark", 2, ["England", "United_States", "Brazil"], 0, 0)
Brazil = Territories("Red", "Brazil", 1, ["Denmark"], 0, 0)
United_States = Territories("Red", "United_States", 4, ["Denmark", "England", "France", "Germany"], 0, 0)
France = Territories("Blue", "France", 5, ["England", "United_States", "Germany"], 0, 0)
Germany = Territories("Blue", "Germany", 3, ["France", "United_States", "Austria"], 0, 0)
Austria = Territories("Blue", "Austria", 2, ["Germany"], 0, 0)

existing_territories = [England, Denmark, Brazil, France, Austria, United_States, Germany]