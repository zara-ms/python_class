"""
## NAME

        traduccion_rna.py

## VERSION

        [1.0]

## AUTHOR

        Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

        16/06/2021

## DESCRIPTION

        Este programa traduce una secuencia de nucleotidos a aminoacidos y le notifica al usuario si la
        secuencia ingresada contiene caracteres no validos.

## CATEGORY

        Sequence analysis

## USAGE

        traduccion_rna.py es de uso bioinformático

## ARGUMENTS

        No hay argumentos

## FUNCTIONS

        Funcion que toma como parametro la secuencia ingresada, si se encuentran caracteres no validos marca Error,
        de lo contrario regresa la secuencia con caracteres modificados.

        def analizar_sec(seq):
            no_bases = re.findall(r"[^ATGCU]", seq)

            try:
                if no_bases:
                    raise ValueError

            except ValueError:
                print(f'La secuencia que ingresó cuenta con caracteres no válidos: {no_bases}')

            else:
                seq = seq.replace('U', 'T')
                return(seq)


## EXAMPLES

        Input:
            AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

        Output:
            El péptido formado por la secuencia ingresada es: MAMAPRTEINSTRING


## GITHUB LINK

        https://github.com/zara-ms/python_class/tree/master/src

"""

import re


def analizar_sec(seq):
#   Buscar caracteres no validos
    no_bases = re.findall(r"[^ATGCU]", seq)
    try:
        if no_bases:
            raise ValueError

    except ValueError:
        print(f'La secuencia que ingresó cuenta con caracteres no válidos: {no_bases}')
#   Modificar la secuencia para trabajar con el gencode
    else:
        seq = seq.replace('U', 'T')
        return(seq)


# Definir el codigo genetico
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

print("Ingrese la secuencia de RNA que desea traducir")
sec = input()
sec = sec.upper()

# Asegurar que la secuencia dada cuenta con caracteres validos
rna = analizar_sec(sec)
long = len(rna)
aa = []

# Dividir toda la seuencia en tripletes
for n in range(0, long, 3):
    codon = rna[n:n+3]
#   Al encontrar un codon de paro se termina la traduccion
    if gencode[codon] == "_":
        break
#   Guardar la secuencia de aminoacidos en una lista
    else:
        aa.append(gencode[codon])

# Unir la lista para formar una cadena
peptide = "".join(aa)

# Imprimir el resultado
print("El péptido formado por la secuencia ingresada es: " + peptide)
