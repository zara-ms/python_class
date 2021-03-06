"""
## NAME

        instrumentos-POO.py

## VERSION

        [1.0]

## AUTHOR

        Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

        06/09/2021

## DESCRIPTION

        Con este programa se pueden clasificar instrumentos musicales al hacer uso de metodos, atributos, clases,
        subclases, herencia, overriding y polimorfismos.

## ARGUMENTS

        No hay argumentos

## EXAMPLES

        violin = cuerda('madera', 'europeo', 'Glin glin')
        print(violin.__dict__)
        violin.emite_musica()

        Output:
        {'material': 'madera', 'origen': 'europeo', 'sonido': 'Glin glin'}
        'Glin glin'

## GITHUB LINK

        https://github.com/zara-ms/python_class

"""

class instrumento():

#   Atributos
    def __init__(self, material, origen, sonido):
        self.material = material
        self.origen = origen
        self.sonido = sonido

#   Metodos
    def emite_musica(self):
        print(self.sonido)


# Heredar la clase intsrumento

class viento(instrumento):

#   Overriding del metodo
    def emite_musica(self):
        print(self.sonido)


class cuerda(instrumento):

# Polimorifismo del netodo
    def emite_musica(self):
        print(self.sonido)


class percusion(instrumento):

#   Polimorfismo del metodo
    def emite_musica(self):
        print(self.sonido)


violin = cuerda('madera', 'europeo', 'Glin glin')
print(violin.__dict__)
violin.emite_musica()
