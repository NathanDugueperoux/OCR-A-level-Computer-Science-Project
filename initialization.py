from classes import Territories

England = Territories("Red", "England", 3, ["Denmark", "United_States", "France"])
Denmark = Territories("Red", "Denmark", 2, ["England", "United_States", "Brazil"])
Brazil = Territories("Red", "Brazil", 1, ["Denmark"])
United_States = Territories("Red", "United_States", 4, ["Denmark", "England", "France", "Germany"])
France = Territories("Blue", "France", 5, ["England", "United_States", "Germany"])
Germany = Territories("Blue", "Germany", 3, ["France", "United_States", "Austria"])
Austria = Territories("Blue", "Austria", 2, ["Germany"])

existing_territories = [England, Denmark, Brazil, France, Austria, United_States, Germany]
