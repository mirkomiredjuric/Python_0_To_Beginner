from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ['Electric', "Water", "Fire"])
table.title = "Pokemon Types"
print(table)
