selfish = 'me me me'

print(selfish[0])  #m
print(selfish[1])  #e
print(selfish[2])  #_
print(selfish[3]+'\n')  #m

selfish="0123456789"
# [start:stop:stepover]    ------ slicing
print(selfish[0:10])    
print(selfish[:3])  #  
print(selfish[3:])  #  

print(selfish[0:2])
print(selfish[-1])
print(selfish[-2])
print(selfish[-2:-3])

#reverse a string
print(selfish[::-1])