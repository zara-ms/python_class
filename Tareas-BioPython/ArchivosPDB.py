"""
## NAME

	ArchivosPDB.py

## VERSION

	[1.0]

## AUTHOR

	Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

	[26/09/2021]

## DESCRIPTION

	 Este programa utiliza una funcion para obtener una lista con todos los ID de residuos del aminoacido que se
	 especifique obtenido de cierta cadena tambien especificada por el usuario.

## CATEGORY

	Analysis

## FUNCTIONS

	def residuos_aa(cadena, residuo, model, struc):
    	[Obtiene una lista con todos los ID de residuos especificados
    	de cierta cadena y la imprime]

## EXAMPLES

	Input:
        path = Downloads\clasePDB\1fat.pdb
        residuo = lys
        cadena = A

    Output:
        100
        102
        129
        149
        184
        196
        215
        231

## GITHUB LINK

	https://github.com/zara-ms/python_class/tree/master/Tareas-BioPython

"""


# Importar libreria a usar
from Bio import PDB


# Funcion para obtener todos los residuos especificados de una cadena en concreto
def residuos_aa(cadena, residuo, path):
    parser = PDB.PDBParser(QUIET=True)
    # Metodo para obtener los datos
    struc = parser.get_structure('prot', path)
    lista_residuos = []
    for model in struc:
        for chain in model:
            if chain == model[cadena]:
                for residue in chain:
                    if residue.get_resname() == residuo:
                        lista_residuos.append(residue.get_id()[1])
    for aa in lista_residuos:
        print(aa)


print("Ingrese el path del archivo a usar")
path = input()

print("Ingrese el residuo que desea buscar con su codigo de tres letras")
residuo = input()
# Asegurarse que el codigo de tres letras esta en mayuscula
residuo = residuo.upper()

print("Ingrese la cadena en la que desea buscar el resiudo")
cadena = input()

# Llamar a la funcion
residuos_aa(cadena, residuo, path)