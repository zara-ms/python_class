"""
## NAME

	BasesDatos.py

## VERSION

	[1.0]

## AUTHOR

	Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

	[03/10/2021]

## DESCRIPTION

	 Este programa cuenta con dos partes: la primera parte utiliza la base de datos "Protein" para buscar la descripcion
	  del FieldList "ECNO" y el LinkList "protein_protein_small_genome", en la segunda parte el usuario ingresa el
	  nombre de un autor y dos palabras que puedan encontrarse en el titulo de un articulo para despues buscar la
	  informacion en la base de datos Pubmed y crear un archivo con la informacion

## CATEGORY

	Analysis

## EXAMPLES

	Input:
        Primera parte:
            FieldList "ECNO"
            LinkList "protein_protein_small_genome"

        Segunda parte:
            Autora: Valeria Mateo-Estrada
            Primera plabra: Genomic
            Segunda palabra: Genes

    Output:
        Primera parte:
            ECNO EC number for enzyme or CAS registry number
            protein_protein_small_genome All proteins from this genome

        Segunda parte:
            ['34282943', '32611704']

## GITHUB LINK

	https://github.com/zara-ms/python_class/tree/master/Tareas-BioPython

"""


from Bio import Entrez

# Primera parte

# Anexar el correo
Entrez.email = "zarams@lcg.unam.mx"

# Definir la base de datos
handle = Entrez.einfo(db="protein")
record = Entrez.read(handle)

# Buscar la informacion que se pide en Protein
for field in record["DbInfo"]["FieldList"]:
    if field["Name"] == "ECNO":
        print(field["Name"], field["Description"])

for field in record["DbInfo"]["LinkList"]:
    if field["Name"] == "protein_protein_small_genome":
        print(field["Name"], field["Description"])

handle.close()


# Segunda parte

#Abrir archivo a usar
archivo = open(".../docs/archivo_IDs.txt", "w")

# Solicitar informacion a buscar
print("Ingrese el nombre de autorx que desea buscar")
autora = input()

print("Ingrese una palabra que desee pueda estar en el titulo")
pal1 = input()

print("Ingrese otra palabra que pueda estar en el titulo")
pal2 = input()

termino = "(" + autora + "[AUTH] AND (" + pal1 + "[Title] OR " + pal2 + "[Title])"

# Buscar la informacion que se pide en PubMed
handle = Entrez.esearch(db="pubmed", term=termino)
result = Entrez.read(handle)
archivo.write(result["IdList"])

handle.close()
