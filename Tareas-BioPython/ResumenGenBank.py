'''
## NAME

	ResumenGenBank.py

## VERSION

	[1.0]

## AUTHOR

	Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

	[19/09/2021]

## DESCRIPTION

	 Este programa obtiene, medianto el uso de una funcion, los datos del organismo, version de la secuencia, fuente de
	 aisaldo y pais de un archivo GenBank, así como los primeros 15 nucleotidos de DNA, RNA y los primeros 15
	 aminoacidos de cada gen dado.

## CATEGORY

	Analysis

## FUNCTIONS

	resumen(path, genes):
    	[Imprime el organismo, version de la secuencia,
    	fuente de aisaldo, pais, así como primeros 15
    	nucleotidos de DNA, RNA y primeros 15 aminoacidos por gen]

## EXAMPLES

	Input:
	    path = "/Downloads/virus.gb"
        genes = ['L', 'N', 'P']

    Output:
        Organismo:  Isfahan virus
        Version de la secuencia:  1
        Aislado:  ['Phlebotomus papatasi']
        Pais:  ['Iran:Isfahan province']

## GITHUB LINK

	https://github.com/zara-ms/python_class/tree/master/Tareas-BioPython

'''


# Librerias a usar
from Bio.Seq import Seq
from Bio import SeqIO

# Crear la funcion
def resumen(path, genes):
    for gb_record in SeqIO.parse(path, "genbank"):

        # Acceder a la informacion de los metadatos utilizando "annotations"
        print("Organismo: ", gb_record.annotations['organism'])
        print("Version de la secuencia: ", gb_record.annotations['sequence_version'])

        # Acceder a la informacion de features utilizando "features[]"
        print("Aislado: ", gb_record.features[0].qualifiers['isolation_source'])
        print("Pais: ", gb_record.features[0].qualifiers['country'])

        # Acceder a los genes
        for i in genes:

            # Si se encuentra el gen obtener su informacion
            if (gb_record.features[1].qualifiers['gene'] == i):
                print("Gen :", gb_record.features[1].qualifiers['gene'])
                inicio = gb_record.features[1].location.nofuzzy_start
                fin = inicio + 14
                dna = gb_record.seq[inicio:fin]
                print("DNA: ", dna)
                print("RNA: ", dna.transcribe())
                fin2 = inicio + 44
                proteina = gb_record.seq[inicio:fin2]
                print("Proteina: ", proteina.translate())


path = "/Downloads/virus.gb"
genes = ['L', 'N', 'P']

# Llamar a la funcion
resumen(path, genes)

