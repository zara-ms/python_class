"""
## NAME

	ExPASy_SwissProt.py

## VERSION

	[1.0]

## AUTHOR

	Daniela Goretti Castillo Leon
	Jose Rodelmar Ocampo Luna <joserodelmar@gmail.com>
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
		<GO_in_ID.txt>
		El ID es: A0A0K2RVI7_9BETC
	Nombre de proteina: RecName: Full=Envelope small membrane protein {ECO:0000256|HAMAP-Rule:MF_04204}
	Nombre y definicion del GO: GO:0046760C:host cell Golgi membrane
	Organismo: Equine coronavirus.
	Localizacion subcelular
	Localización subcelular: SUBCELLULAR LOCATION: Host Golgi apparatus membrane {ECO:0000256|HAMAP- Rule:MF_04204}; Single-pass type III membrane protein {ECO:0000256|HAMAP-Rule:MF_04204}. Note=The cytoplasmic tail functions as a Golgi complex-targeting signal. {ECO:0000256|HAMAP-Rule:MF_04204}.
	El ID es: A8R4D4_9BETC
	Nombre de proteina: RecName: Full=Envelope small membrane protein {ECO:0000256|HAMAP-Rule:MF_04204}
	Nombre y definicion del GO: GO:0046760BAS18868.1
	Organismo: Equine coronavirus.
	Localizacion subcelular
	Localización subcelular: SUBCELLULAR LOCATION: Host Golgi apparatus membrane {ECO:0000256|HAMAP- Rule:MF_04204}; Single-pass type III membrane protein {ECO:0000256|HAMAP-Rule:MF_04204}. Note=The cytoplasmic tail functions as a Golgi complex-targeting signal. {ECO:0000256|HAMAP-Rule:MF_04204}.
	El ID es: POLG_YEFV1
	Nombre de proteina: RecName: Full=Genome polyprotein
	Nombre y definicion del GO: GO:0046762AAC54267.1
	Organismo: Yellow fever virus (strain 17D vaccine) (YFV).
	Localizacion subcelular
	Localización subcelular: SUBCELLULAR LOCATION: [Capsid protein C]: Virion {ECO:0000250|UniProtKB:P17763}. Host nucleus {ECO:0000250|UniProtKB:P17763}. Host cytoplasm, host perinuclear region {ECO:0000250|UniProtKB:P17763}. Host cytoplasm {ECO:0000250|UniProtKB:P17763}.
	Localización subcelular: SUBCELLULAR LOCATION: [Peptide pr]: Secreted {ECO:0000250|UniProtKB:P17763}.
	Localización subcelular: SUBCELLULAR LOCATION: [Small envelope protein M]: Virion membrane {ECO:0000269|PubMed:15507646}; Multi-pass membrane protein {ECO:0000269|PubMed:15507646}. Host endoplasmic reticulum membrane {ECO:0000269|PubMed:15507646}; Multi-pass membrane protein {ECO:0000255}. Note=ER membrane retention is mediated by the transmembrane domains. {ECO:0000269|PubMed:15507646}.
	Localización subcelular: SUBCELLULAR LOCATION: [Envelope protein E]: Virion membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000269|PubMed:15507646}. Host endoplasmic reticulum membrane {ECO:0000269|PubMed:3008425}; Multi-pass membrane protein {ECO:0000255}. Note=ER membrane retention is mediated by the transmembrane domains. {ECO:0000269|PubMed:15507646}.
	Localización subcelular: SUBCELLULAR LOCATION: [Non-structural protein 1]: Secreted {ECO:0000250|UniProtKB:P17763}. Host endoplasmic reticulum membrane; Peripheral membrane protein; Lumenal side {ECO:0000250|UniProtKB:P17763}. Note=Located in RE-derived vesicles hosting the replication complex. {ECO:0000250|UniProtKB:Q9Q6P4}.
	Localización subcelular: SUBCELLULAR LOCATION: [Non-structural protein 2A]: Host endoplasmic reticulum membrane {ECO:0000250|UniProtKB:P17763}; Multi-pass membrane protein {ECO:0000250|UniProtKB:P17763}.
	Localización subcelular: SUBCELLULAR LOCATION: [Serine protease subunit NS2B]: Host endoplasmic reticulum membrane; Multi-pass membrane protein {ECO:0000250|UniProtKB:P17763}.
	Localización subcelular: SUBCELLULAR LOCATION: [Serine protease NS3]: Host endoplasmic reticulum membrane {ECO:0000255|PROSITE-ProRule:PRU00860}; Peripheral membrane protein {ECO:0000255|PROSITE-ProRule:PRU00860}; Cytoplasmic side {ECO:0000255|PROSITE-ProRule:PRU00860}. Note=Remains non-covalently associated to serine protease subunit NS2B. {ECO:0000255|PROSITE- ProRule:PRU00860}.
	Localización subcelular: SUBCELLULAR LOCATION: [Non-structural protein 4A]: Host endoplasmic reticulum membrane {ECO:0000250|UniProtKB:P17763}; Multi-pass membrane protein {ECO:0000250|UniProtKB:P17763}. Note=Located in RE-associated vesicles hosting the replication complex. {ECO:0000250|UniProtKB:P17763}.
	Localización subcelular: SUBCELLULAR LOCATION: [Non-structural protein 4B]: Host endoplasmic reticulum membrane {ECO:0000250|UniProtKB:P17763}; Multi-pass membrane protein {ECO:0000250|UniProtKB:P17763}. Note=Located in RE-derived vesicles hosting the replication complex. {ECO:0000250|UniProtKB:Q9Q6P4}.
	Localización subcelular: SUBCELLULAR LOCATION: [RNA-directed RNA polymerase NS5]: Host endoplasmic reticulum membrane; Peripheral membrane protein; Cytoplasmic side. Host nucleus {ECO:0000250|UniProtKB:P17763}. Note=Located in RE-associated vesicles hosting the replication complex. NS5 protein is mainly localized in the nucleus rather than in ER vesicles. {ECO:0000250|UniProtKB:P17763}.
	Referencia en PROSITE ('PROSITE', 'PS51527', 'FLAVIVIRUS_NS2B', '1')
	Referencia en PROSITE ('PROSITE', 'PS51528', 'FLAVIVIRUS_NS3PRO', '1')
	Referencia en PROSITE ('PROSITE', 'PS51192', 'HELICASE_ATP_BIND_1', '1')
	Referencia en PROSITE ('PROSITE', 'PS51194', 'HELICASE_CTER', '1')
	Referencia en PROSITE ('PROSITE', 'PS50507', 'RDRP_SSRNA_POS', '1')
	Referencia en PROSITE ('PROSITE', 'PS51591', 'RNA_CAP01_NS5_MT', '1')
	El ID es: POLG_DEN1W
	Nombre de proteina: RecName: Full=Genome polyprotein
	Nombre y definicion del GO: GO:0046762AAA42940.1
	Organismo: Dengue virus type 1 (strain Nauru/West Pac/1974) (DENV-1).
	Localizacion subcelular
	Localización subcelular: SUBCELLULAR LOCATION: [Capsid protein C]: Virion. Host nucleus {ECO:0000269|PubMed:18420804}. Host cytoplasm {ECO:0000269|PubMed:19889084}. Host cytoplasm, host perinuclear region {ECO:0000269|PubMed:19889084}.
	Localización subcelular: SUBCELLULAR LOCATION: [Peptide pr]: Secreted {ECO:0000269|PubMed:19759134}.
	Localización subcelular: SUBCELLULAR LOCATION: [Small envelope protein M]: Virion membrane {ECO:0000269|PubMed:9971841}; Multi-pass membrane protein {ECO:0000255}. Host endoplasmic reticulum membrane {ECO:0000269|PubMed:9971841}; Multi-pass membrane protein {ECO:0000255}.
	Localización subcelular: SUBCELLULAR LOCATION: [Envelope protein E]: Virion membrane {ECO:0000269|PubMed:20181718}; Multi-pass membrane protein {ECO:0000255}. Host endoplasmic reticulum membrane {ECO:0000269|PubMed:20181718}; Multi-pass membrane protein {ECO:0000255}.
	Localización subcelular: SUBCELLULAR LOCATION: [Non-structural protein 1]: Secreted {ECO:0000269|PubMed:10364366, ECO:0000269|PubMed:26655246}. Host endoplasmic reticulum membrane; Peripheral membrane protein; Lumenal side {ECO:0000305}. Note=Located in RE-derived vesicles hosting the replication complex. {ECO:0000250|UniProtKB:Q9Q6P4}.
	Localización subcelular: SUBCELLULAR LOCATION: [Non-structural protein 2A]: Host endoplasmic reticulum membrane {ECO:0000269|PubMed:23408612}; Multi-pass membrane protein {ECO:0000269|PubMed:23408612}.
	Localización subcelular: SUBCELLULAR LOCATION: [Serine protease subunit NS2B]: Host endoplasmic reticulum membrane; Multi-pass membrane protein {ECO:0000269|PubMed:26072288}.
	Localización subcelular: SUBCELLULAR LOCATION: [Serine protease NS3]: Host endoplasmic reticulum membrane {ECO:0000255|PROSITE-ProRule:PRU00860}; Peripheral membrane protein {ECO:0000255|PROSITE-ProRule:PRU00860}; Cytoplasmic side {ECO:0000255|PROSITE-ProRule:PRU00860}. Note=Remains non-covalently associated to serine protease subunit NS2B. {ECO:0000255|PROSITE- ProRule:PRU00860}.
	Localización subcelular: SUBCELLULAR LOCATION: [Non-structural protein 4A]: Host endoplasmic reticulum membrane {ECO:0000269|PubMed:17276984}; Multi-pass membrane protein {ECO:0000269|PubMed:17276984}. Host mitochondrion {ECO:0000269|PubMed:27252539}. Note=Located in RE-associated vesicles hosting the replication complex. Interacts with host MAVS in the mitochondrion-associated endoplasmic reticulum membranes. {ECO:0000269|PubMed:17276984, ECO:0000269|PubMed:27252539}.
	Localización subcelular: SUBCELLULAR LOCATION: [Non-structural protein 4B]: Host endoplasmic reticulum membrane {ECO:0000269|PubMed:16436383}; Multi-pass membrane protein {ECO:0000269|PubMed:16436383}. Note=Located in RE-derived vesicles hosting the replication complex. {ECO:0000250|UniProtKB:Q9Q6P4}.
	Localización subcelular: SUBCELLULAR LOCATION: [RNA-directed RNA polymerase NS5]: Host endoplasmic reticulum membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}; Cytoplasmic side {ECO:0000305}. Host nucleus {ECO:0000269|PubMed:16699025}. Note=Located in RE-associated vesicles hosting the replication complex. NS5 protein is mainly localized in the nucleus rather than in ER vesicles, especially in the DENV 2, 3, 4 serotypes. {ECO:0000303|PubMed:28441781}.
	Referencia en PROSITE ('PROSITE', 'PS51527', 'FLAVIVIRUS_NS2B', '1')
	Referencia en PROSITE ('PROSITE', 'PS51528', 'FLAVIVIRUS_NS3PRO', '1')
	Referencia en PROSITE ('PROSITE', 'PS51192', 'HELICASE_ATP_BIND_1', '1')
	Referencia en PROSITE ('PROSITE', 'PS51194', 'HELICASE_CTER', '1')
	Referencia en PROSITE ('PROSITE', 'PS50507', 'RDRP_SSRNA_POS', '1')
	Referencia en PROSITE ('PROSITE', 'PS51591', 'RNA_CAP01_NS5_MT', '1')
	El ID es: Q6W352_CVEN9
	Nombre de proteina: RecName: Full=Envelope small membrane protein {ECO:0000256|HAMAP-Rule:MF_04204}
	Nombre y definicion del GO: GO:0046760C:integral component of membrane
	Organismo: Equine coronavirus (isolate NC99) (ECoV).
	Localizacion subcelular
	Localización subcelular: SUBCELLULAR LOCATION: Host Golgi apparatus membrane {ECO:0000256|HAMAP- Rule:MF_04204}; Single-pass type III membrane protein {ECO:0000256|HAMAP-Rule:MF_04204}. Note=The cytoplasmic tail functions as a Golgi complex-targeting signal. {ECO:0000256|HAMAP-Rule:MF_04204}.



## GITHUB LINK

	https://github.com/zara-ms/python_class/tree/master/Tareas-BioPython
"""


# Librerias a usar
from Bio import ExPASy, SwissProt

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
                for GOs in record.cross_references[1:]:
                	if GOs[1] == GO:
                		# Obtener la informacion
                		file = open("GO_in_ID.txt", "a")
                		file.write('El ID es: ' + ID + '\n')
                		file.write('Nombre de proteina: ' + record.description.split(';')[0] + '\n')
                		file.write('Nombre y definicion del GO: ' + GO + record.cross_references[2][2] + '\n')
                		file.write('Organismo: ' + record.organism + '\n')
				for comment in record.comments:
                    			type_c = comment.split(':')
                    			if type_c[0] == 'SUBCELLULAR LOCATION':
                        			file.write('Localización subcelular: '+ comment + '\n')
				for reference in record.cross_references:
                    			if 'PROSITE' in reference:
                        			file.write('Referencia en PROSITE ' + reference[1] + '\n')
                		file.close()

GO_Terms = ["GO:0046755", "GO:0046761",
              "GO:0046760", "GO:0039702",
              "GO:0046765", "GO:0046762"]
uniprot_IDs = ["A0A0K2RVI7_9BETC", "A8R4D4_9BETC",
                 "POLG_YEFV1", "POLG_DEN1W",
                 "Q6W352_CVEN9", "D9SV67_CLOC7",
                 "A9KSF7_LACP7", "B8I7R6_RUMCH"]

get_swissprot(GO_Terms, uniprot_IDs)
