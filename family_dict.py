my_family = {
    'sister too': {
        'name': 'Ravin',
        'age': 20
    },
    'mother': {
        'name': 'Vickie',
        'age': 52
    },
    'brother': {
    	'name': 'Sage',
    	'age': 22
    },
    'sister': {
        'name': 'Willow',
        'age': 14
    }
}

family_string = {str(v['name'])+' is my '+str(k)+' and is '+str(v['age'])+' years old.' for (k,v) in my_family.items()}

print(family_string)