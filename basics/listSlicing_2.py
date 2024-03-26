amazon_cart = [
  'notebook',
  'sunglasses',
  'toys',
  'grapes'
]

amazon_cart[0]='laptop'
new_cart=amazon_cart
new_cart[0]="aeroplane"  #both new cart and amazon cart will be chnaged
print(amazon_cart)
print(new_cart)

###################
amazon_cart[0]='laptop'
new_cart=amazon_cart[:] #now different ## now orirginal amazon cart remains same
new_cart[0]="aeroplane" 
print(amazon_cart)
print(new_cart)