#list Slicing

amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'Grapes'
]
 #everytime we do list slicing we create a new copy of the list
print(amazon_cart[1:2])
print(amazon_cart[0::2])  # all the way till end skipping 2nd one

amazon_cart[0]='laptop' 
new_cart =(amazon_cart[0:3])  # new list is being created , and we assigned to new variable
print(amazon_cart)
print(new_cart)  
