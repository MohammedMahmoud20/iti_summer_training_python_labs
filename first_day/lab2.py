unordered_list = []
for i in range(5):
    element = input(f"Enter element {i+1}: ")
    if(element.isnumeric()):
        element=int(element)
    unordered_list.append(element)
ascending_list = unordered_list.sort()
descending_list = unordered_list.sort(reverse=True)
print("Ascending order:", ascending_list)
print("Descending order:", descending_list)