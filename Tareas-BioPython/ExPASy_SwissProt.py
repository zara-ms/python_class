"""
## NAME

	ExPASy_SwissProt.py

## VERSION

	[1.0]

## AUTHOR

	Daniela Goretti Castillo Leon
	Jose Rodelmar Ocampo Luna
	Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

	[25/10/2021]

## DESCRIPTION

	Este programa cuenta con una funcion la cual extrae los archivos SwissProt de un ID particular y busca varios terminos GO
	en el mismo, en caso de no encontrar algun GO se le notifica al usuario, en caso contrario obtiene el ID y nombre de la
	proteina donde se encontro, el termino GO encontrado con su definicion, el organismo al que pertenece y localización subcelular.

## CATEGORY

	Analysis

## FUNCTIONS

	get_swissprot(lista de GOs a buscar,  lista de IDs a usar):
		
		[Abre el archivo donde se escribira el resultado, por cada ID extrae el archivo Swissprot, busca algun termino GO de la lista,
		en caso de encontrarlo se escribe el ID, nombre de proteina, nombre y definicion del GO, organismo donde se encontro, localizacion
		subcelular en caso de tener] 
	

## EXAMPLES

	Input:
		GO_Terms = ["GO:0046755", "GO:0046761",
              "GO:0046760", "GO:0039702",
              "GO:0046765", "GO:0046762"]
		uniprot_IDs = ["A0A0K2RVI7_9BETC", "A8R4D4_9BETC",
                 "POLG_YEFV1", "POLG_DEN1W",
                 "Q6W352_CVEN9", "D9SV67_CLOC7",
                 "A9KSF7_LACP7", "B8I7R6_RUMCH"]

	Output:

## GITHUB LINK

	https://github.com/zara-ms/python_class/tree/master/Tareas-BioPython
"""


# Librerias a usar
from Bio import ExPASy, SwissProt
from Bio.ExPASy import Prosite, Prodoc, ScanProsite
from Bio import Entrez

# Poner nuestros correos electrónicos para sacar abstracts de Entrez
# Entrez.email = "dgoretti@lcg.unam.mx"

# Crear una función que tome una lista de terminos GO y una lista de IDs de UniProt
def get_swissprot(go, ids):
    # Abrir archivo donde se guardara la informacion
    file = open("GO_in_ID.txt", "w")
    file.write("")
    file.close()

    # Extraer archivos SwissProt de cada ID
    for ID in ids:
        handle = ExPASy.get_sprot_raw(ID)
        record = SwissProt.read(handle)

        # Buscar si algun termino GO aparece en el archivo
        for GO in go:
            # En caso de encontrarlo
            if record.cross_references[2][1] == GO:
                # Obtener la informacion
                file = open("GO_in_ID.txt", "a")
                file.write('El ID es: ' + ID + '\n')
                file.write('Nombre de proteina: ' + record.description.split(';')[0] + '\n')
                file.write('Nombre y definicion del GO: ' + GO + record.cross_references[2][2] + '\n')
                file.write('Organismo: ' + record.organism + '\n')
                file.close()
            # En caso de no encontrarlo, se indica en el archivo
            else:
                file = open("GO_in_ID.txt", "a")
                file.write('No existe el ' + GO + 'en el ID' + ID + '\n')
                file.close()
                
                # Imprimir localización subcelular:
                for comment in record.comments:
                    type_c = comment.split(':')
                    if type_c[0] == 'SUBCELLULAR LOCATION':
                        print('Localización subcelular: ', comment, '\n')

                # Abstract de fuente - Sacar ID de Pubmed
                # print('Abstract de una de las fuentes: ')
                # fetch_handle = Entrez.efetch(db="pubmed", id= id_pubmed, rettype="abstract", retmode="text")
                # data = fetch_handle.read()
                # fetch_handle.close()
                # print(data)

                # Imprimir PROSITE
                for reference in record.cross_references:
                    if 'PROSITE' in reference:
                        print(reference[1])

                        # handle = ExPASy.get_prosite_raw(reference[1])
                        # record = Prosite.read(handle)
                        # print(record.name)  # Imprime PAN

                        # handle = ExPASy.get_prosite_raw(record.pdoc)
                        # record = Prodoc.read(handle)
                        # print(record.text)


GO_Terms = ["GO:0046755", "GO:0046761",
              "GO:0046760", "GO:0039702",
              "GO:0046765", "GO:0046762"]
uniprot_IDs = ["A0A0K2RVI7_9BETC", "A8R4D4_9BETC",
                 "POLG_YEFV1", "POLG_DEN1W",
                 "Q6W352_CVEN9", "D9SV67_CLOC7",
                 "A9KSF7_LACP7", "B8I7R6_RUMCH"]

get_swissprot(GO_Terms, uniprot_IDs)
