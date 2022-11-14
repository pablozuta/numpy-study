import dis
import ast, inspect, pprint


def erase():  #definimos una funcion de salto de linea
    print('')

def diasDeLaSemana():
    dias = 7
    print('lunes a domingo')
    print('friday friday')

pprint.pprint(
    ast.dump(
        ast.parse(
            inspect.getsource(diasDeLaSemana)
        )
    )
)
erase()
erase()
erase()

def semanaRapida():
    return 7 * 86400

dis.dis(semanaRapida)
erase()   

def semanaRapidaArgumento(x):
    return x * 86400

dis.dis(semanaRapidaArgumento)
erase()    


dias = 'lunes a viernes'

#aca usamos el disassembler
dis.dis(diasDeLaSemana)
dis.dis(erase)
#podemos analisar metodos externos tambien



pprint.pprint(dias)

pprint.pprint(dis)#esto nos da informacion sobre algun objeto interno o externo
pprint.pprint(np)
pprint.pprint(erase)#la informacion que nos devuelve dependera del tipo de objeto
erase()
erase()

tree = ast.parse(inspect.getsource(diasDeLaSemana))
print(tree)
print(tree.body[0])
print(tree.body[0].body)
erase()

print(diasDeLaSemana.__code__)
print(diasDeLaSemana.__code__.co_consts)
print(f'variables: {diasDeLaSemana.__code__.co_varnames}')
print(diasDeLaSemana.__code__.co_code)
erase()

print(dis.opname[diasDeLaSemana.__code__.co_code[0]])
print(dis.opname[diasDeLaSemana.__code__.co_code[2]])
print(dis.opname[diasDeLaSemana.__code__.co_code[4]])
print(dis.opname[diasDeLaSemana.__code__.co_code[6]])
print(dis.opname[diasDeLaSemana.__code__.co_code[8]])
print(dis.opname[diasDeLaSemana.__code__.co_code[10]])