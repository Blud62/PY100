vehicles = {
        'car': {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003
    },
    'truck': {
        'type': 'pickup', 
        'color': 'red', 
        'year': 1998
    }
}
print(vehicles.keys())
print(vehicles.values())
for k, v in vehicles.items():
    print(k, v)