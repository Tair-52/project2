n = input ("Ввод - ")
# with open ("file.txt", "w") as f:
#     f.write (f"\n{n}")

with open ("file.txt", "a", encoding = 'utf-8',newline= '\n') as f:
    append=f.write( 'curcle\n')
    print(append)   