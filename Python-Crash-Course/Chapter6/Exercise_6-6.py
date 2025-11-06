people = ['andrei','ana','lavi','radu','irina']
favorite_language = {
    'andrei':'c',
    'ana':'java',
    'irina':'python'
}

print ("------------------------- Solution 1 -----------------------")

for name in people:
    if name in favorite_language.keys():
        print (f"{name.title()} thanks for answering")
    else:
        print(f'{name.title()} please take the poll')

