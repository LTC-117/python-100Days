from prettytable import PrettyTable

name_list = ["Pikachu", "Squirtle", "Charmander"]
type_list = ["Electric", "Water", "Fire"]

table = PrettyTable()

table.add_column("Pokemon Name", name_list)
table.add_column("Type", type_list)

table.align["Pokemon Name"] = "c"
table.align["Type"] = "c"

print(table)
print(table.align)
