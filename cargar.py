import ply.lex as lex

ruta=input("Ingrese la ruta del archivo :")
file=open(ruta,"r")
trok=file.read()
print (trok)

lex.input(trok)
while True:
    tok = lex.token()
    if not tok:
        break
    print(tok)