# -*- coding: utf-8 -*-
from __future__ import unicode_literals

facts = [
  ('gabriel', 'endereço', 'av rio branco, 109', True),
  ('joão', 'endereço', 'rua alice, 10', True),
  ('joão', 'endereço', 'rua bob, 88', True),
  ('joão', 'telefone', '234-5678', True),
  ('joão', 'telefone', '91234-5555', True),
  ('joão', 'telefone', '234-5678', False),
  ('gabriel', 'telefone', '98888-1111', True),
  ('gabriel', 'telefone', '56789-1010', True),
]

schema = [
	('endereço', 'cardinality', 'one'),
	('telefone', 'cardinality', 'many')
]


def search_tuple(tups, elem):
	return next((x for x in tups if x[0] == elem), None)

def is_card_one(item, schema):
	schemaSelected = search_tuple(schema, item)
	return(schemaSelected[2] == 'one')

def item_is_valid(item): 
	return(item[3] == True)

def name_in_map(item, facts_map): 
	return(item[0] in facts_map)

def item_in_map(item, index, facts_map): 
	return(item[index] in facts_map[item[0]])

def return_current_facts(schema, facts):
	facts_map = {}
	for item in facts:
		if item_is_valid(item):
			if name_in_map(item, facts_map):
				if is_card_one(item[1], schema):
					print('Substituindo por '+item[1]+' mais atual!') 
					facts_map[item[0]].update({ item[1]: item[2] })
				else:
					facts_map[item[0]].update({
							item[1]: [facts_map[item[0]][item[1]], item[2]] 
							if item_in_map(item, 1, facts_map)
							else item[2]
					})
				print('Adicionando '+item[1])
			else:
					print('Criando '+item[1])   
					facts_map[item[0]] = {item[1]: item[2]}
	return dict_to_tuples(facts_map)

def dict_to_tuples(dict_items):
	tup = []
	for k, v in dict_items.items():
		for value in v.keys():
			if is_card_one(value, schema):
				item = (k, value, v[value], True)
				tup.append(item)            
			else:
				if (isinstance(v[value], list)):
					for i in v[value]:
						item = (k, value, i, True)
						tup.append(item)
				else:
					item = (k, value, i, True)
					tup.append(item)

	return tup

teste = return_current_facts(schema, facts)
print(teste)

expected_result = [
	('gabriel', 'endereço', 'av rio branco, 109', True),
	('gabriel', 'telefone', '98888-1111', True),
	('gabriel', 'telefone', '56789-1010', True),
	('joão', 'endereço', 'rua bob, 88', True),
	('joão', 'telefone', '234-5678', True),
	('joão', 'telefone', '91234-5555', True)
]
