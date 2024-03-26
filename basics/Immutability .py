selfish='0123456789'

selfish="badal"
#string cannot be mutate
#selfish[0]="f"
print(selfish)


selfish2=selfish.replace("b","E") #here we are overriding but not chaning bcoz strings are immutable  --->here new string is being created
print (selfish)
print (selfish2)