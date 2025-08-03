itemTypes = ['Ranged Weapon', 'Melay Weapon', 'Armor', 'Heal Item', 'Ingredient', 'Currency']

itemData = [
	{'name': 'Iron Sword', 'type': itemTypes[1], 'cost': {'min': 12, 'max': 63}, 'damage': {'min': 7, 'max': 27}, 'id': 1},
	{'name': 'Flail', 'type': itemTypes[1], 'cost': {'min': 110, 'max': 257}, 'damage': {'min': 1, 'max': 51}, 'id': 2},
	{'name': 'Apple', 'type': itemTypes[3], 'worth': {'min': 5, 'max': 14}, 'healAmount': {'min': 2, 'max': 17}, 'id': 3},
	{'name': 'Iron Breastplate', 'type': itemTypes[2], 'worth': {'min': 86, 'max': 127}, 'id': 4}
]

def searchItems(itemName):
	itemName = itemName.lower()
	for i in itemData:
		if i['name'].lower() == itemName:
			return i['id']
	return 0


def item(id):
	for i in itemData:
		if i['id'] == id:
			return i
	return ''