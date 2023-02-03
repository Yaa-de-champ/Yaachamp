#a project 1
international_shipping = True
total = 150
shipping_cost = 0
if international_shipping:
	shipping_cost += 15
	print("International base cost applied")

if total <= 50:     # at most is the same as using the operator <= and at least is the same as the operator >=
   shipping_cost += 20
elif total <= 100:
	shipping_cost += 15
else:
	shipping_cost += 5

print(f"shipping_cost: {shipping_cost}") 
# dont understand!


# project 2
# creating a list to hold the sizes of lakes
sizes = [7320, 2117, 22300, 31700, 1679, 1014, 23000, 9910, 685]
largest = max(sizes)
print("Largest lake in sq mi:")
print(largest)

smallest = min(sizes)
print("10th largest lake in sq mi:")
print(smallest)

difference = largest - smallest
print("Difference between lakes in sq mi")
print(difference)



