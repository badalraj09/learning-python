username = input('Enter Your Username :')
password = input('Enter your PASSWORD :')

pas_len=len(password)
hidden_password= '*' * pas_len    # ye * ko jitna paswd ka length hai utna baar print kr dega :  ex length=3  so , ***
if pas_len>8:
  print(f'hey {username} your password {hidden_password} length is {pas_len} ')
  print('reduce it to 6 digit')

# print(password)
# print(pas_len)
