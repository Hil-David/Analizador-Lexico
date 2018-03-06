import ply.lex as lex

# resuSltado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'TRAE',
    'MUESTRA',
    'QUEESLOQUEES',
    'CADENA',
    'RETORNA',
    'ENTERO'
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNAR',
    
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'MODULO',

   'MENOSMENOS',
   'MASMAS',

    #Condiones
   'SI',
    'SINO',
    #Ciclos
   'MIENTRAS',
   'PARA',
    #logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DIFERENTE',
    # Symbolos
    'NUMERAL',

    'PARENTESISIZQ',
    'PARENTESISDER',
    'CORCHETEIZQ',
    'CORCHETEDER',
    'LLAVEIZQ',
    'LLAVEDER',
    
    # Otros
    'PUNTOYCOMA',
    'COMILLA',
    'COMILLADOBLE',
    'MAYORDER', #>>
    'MAYORIZQ', #<<
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNAR = r'='
# Expresiones Logicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOYCOMA = ';'
t_COMILLA = r','
t_PARENTESISIZQ = r'\('
t_PARENTESISDER = r'\)'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'
t_LLAVEIZQ = r'{'
t_LLAVEDER = r'}'
t_COMILLADOBLE = r'\"'



def t_TRAE(t): #import
    r'trae'
    return t

def t_MUESTRA(t): #print
    r'muestra'
    return t

def t_QUEESLOQUEES(t): #input
    r'queesloques'
    return t

def t_SINO(t):
    r'sino'
    return t

def t_SI(t):
    r'si'
    return t

def t_RETORNA(t): #return
   r'retorna'
   return t

def t_MIENTRAS(t):
    r'mientras'
    return t

def t_PARA(t):
    r'para'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_MASMAS(t):
    r'\+\+'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_DIFERENTE(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/"""(.|\n)*?\"""'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\#(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)