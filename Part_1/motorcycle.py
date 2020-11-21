motorcycles = ['honda','yamaha','suzuki', 'ducati']
print(motorcycles)

popped_motorcycle=motorcycles.pop(2)
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a "+popped_motorcycle.title()+".")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+ too_expensive.title()+ " is too expensive")