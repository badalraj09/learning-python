basket = [1,2,3,4,5]

#adding
basket.insert(5,100)
new_list = basket
print(basket)
print(new_list)

basket.extend([100,101,102,103])
print(basket)

#removing
new_list=basket.pop(0)  # removes item given index
print (new_list)  # returns the calue which is removed
print(basket)

basket.remove(3)   # removes the specific value item  ex - 3, 103
basket.remove(103)   # 
print(basket)

basket.clear() # removes everything
print(basket)