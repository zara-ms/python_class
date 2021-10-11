"""
## NAME

	BusquedaAbstracts.py

## VERSION

	[1.0]

## AUTHOR

	Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

	[10/10/2021]

## DESCRIPTION

	 Este programa hace uso de Entrez para buscar y guardar los IDs de los articulos de unx autorx que cuenten con
	 ciertas palabras en el titulo, para despues obtener los abstracts de los primeros tres articulos encontrados.

## CATEGORY

	Analysis

## EXAMPLES
	Input:
            Autorx = "Ardem Patapoutian"
            Primera palabra = "piezo2"
            Segunda palabra = "pathway"
    Output:
       IDs = ['33057202', '30305457', '28002412', '26551544', '25471886', '24717433', '23487782', '22921401',
                '21041958', '20813920']
       Abstracts:
1. Nature. 2020 Dec;588(7837):290-295. doi: 10.1038/s41586-020-2830-7. Epub 2020 Oct 14.

PIEZO2 in sensory neurons and urothelial cells coordinates urination.

Marshall KL(1), Saade D(2), Ghitani N(3), Coombs AM(1), Szczot M(3), Keller
J(4)(5), Ogata T(2), Daou I(1), Stowers LT(4), Bönnemann CG(2), Chesler AT(6)(7),
Patapoutian A(8).

Author information:
(1)Howard Hughes Medical Institute, Department of Neuroscience, Dorris
Neuroscience Center, The Scripps Research Institute, La Jolla, CA, USA.
(2)National Institute of Neurological Disorders and Stroke, National Institutes
of Health, Bethesda, MD, USA.
(3)National Center for Complementary and Integrative Health, National Institutes
of Health, Bethesda, MD, USA.
(4)Department of Neuroscience, Dorris Neuroscience Center, The Scripps Research
Institute, La Jolla, CA, USA.
(5)Howard Hughes Medical Institute, Janelia Research Campus, Ashburn, VA, USA.
(6)National Institute of Neurological Disorders and Stroke, National Institutes
of Health, Bethesda, MD, USA. alexander.chesler@nih.gov.
(7)National Center for Complementary and Integrative Health, National Institutes
of Health, Bethesda, MD, USA. alexander.chesler@nih.gov.
(8)Howard Hughes Medical Institute, Department of Neuroscience, Dorris
Neuroscience Center, The Scripps Research Institute, La Jolla, CA, USA.
ardem@scripps.edu.

Comment in
    Kidney Int. 2021 Jul;100(1):9-11.
    Eur Urol. 2021 Aug;80(2):255-256.

Henry Miller stated that "to relieve a full bladder is one of the great human
joys". Urination is critically important in health and ailments of the lower
urinary tract cause high pathological burden. Although there have been advances
in understanding the central circuitry in the brain that facilitates
urination1-3, there is a lack of in-depth mechanistic insight into the process.
In addition to central control, micturition reflexes that govern urination are
all initiated by peripheral mechanical stimuli such as bladder stretch and
urethral flow4. The mechanotransduction molecules and cell types that function as
the primary stretch and pressure detectors in the urinary tract mostly remain
unknown. Here we identify expression of the mechanosensitive ion channel PIEZO2
in lower urinary tract tissues, where it is required for low-threshold
bladder-stretch sensing and urethral micturition reflexes. We show that PIEZO2
acts as a sensor in both the bladder urothelium and innervating sensory neurons.
Humans and mice lacking functional PIEZO2 have impaired bladder control, and
humans lacking functional PIEZO2 report deficient bladder-filling sensation. This
study identifies PIEZO2 as a key mechanosensor in urinary function. These
findings set the foundation for future work to identify the interactions between
urothelial cells and sensory neurons that control urination.

DOI: 10.1038/s41586-020-2830-7
PMCID: PMC7725878
PMID: 33057202  [Indexed for MEDLINE]

2. Sci Transl Med. 2018 Oct 10;10(462). pii: eaat9897. doi:
10.1126/scitranslmed.aat9897.

The mechanosensitive ion channel Piezo2 mediates sensitivity to mechanical pain
in mice.

Murthy SE(1), Loud MC(1), Daou I(1), Marshall KL(1), Schwaller F(2), Kühnemund
J(2), Francisco AG(1), Keenan WT(1), Dubin AE(1), Lewin GR(2)(3), Patapoutian
A(4).

Author information:
(1)Howard Hughes Medical Institute, Department of Neuroscience, The Scripps
Research Institute, La Jolla, CA 92037, USA.
(2)Department of Neuroscience, Max Delbrück Center for Molecular Medicine,
Robert-Rössle Straße 10, Berlin 13125, Germany.
(3)Excellence Cluster Neurocure, Charité Universitätsmedizin, Berlin 13125,
Germany.
(4)Howard Hughes Medical Institute, Department of Neuroscience, The Scripps
Research Institute, La Jolla, CA 92037, USA. ardem@scripps.edu.

The brush of a feather and a pinprick are perceived as distinct sensations
because they are detected by discrete cutaneous sensory neurons. Inflammation or
nerve injury can disrupt this sensory coding and result in maladaptive pain
states, including mechanical allodynia, the development of pain in response to
innocuous touch. However, the molecular mechanisms underlying the alteration of
mechanical sensitization are poorly understood. In mice and humans, loss of
mechanically activated PIEZO2 channels results in the inability to sense
discriminative touch. However, the role of Piezo2 in acute and sensitized
mechanical pain is not well defined. Here, we showed that optogenetic activation
of Piezo2-expressing sensory neurons induced nociception in mice. Mice lacking
Piezo2 in caudal sensory neurons had impaired nocifensive responses to mechanical
stimuli. Consistently, ex vivo recordings in skin-nerve preparations from these
mice showed diminished Aδ-nociceptor and C-fiber firing in response to mechanical
stimulation. Punctate and dynamic allodynia in response to capsaicin-induced
inflammation and spared nerve injury was absent in Piezo2-deficient mice. These
results indicate that Piezo2 mediates inflammation- and nerve injury-induced
sensitized mechanical pain, and suggest that targeting PIEZO2 might be an
effective strategy for treating mechanical allodynia.

Copyright © 2018 The Authors, some rights reserved; exclusive licensee American
Association for the Advancement of Science. No claim to original U.S. Government
Works.

DOI: 10.1126/scitranslmed.aat9897
PMCID: PMC6709986
PMID: 30305457  [Indexed for MEDLINE]

3. Nature. 2017 Jan 12;541(7636):176-181. doi: 10.1038/nature20793. Epub 2016 Dec
21.

Piezo2 senses airway stretch and mediates lung inflation-induced apnoea.

Nonomura K(1), Woo SH(1), Chang RB(2), Gillich A(3), Qiu Z(1)(4), Francisco
AG(1), Ranade SS(1), Liberles SD(2), Patapoutian A(1).

Author information:
(1)Howard Hughes Medical Institute, Molecular and Cellular Neuroscience, Dorris
Neuroscience Center, The Scripps Research Institute, La Jolla, California 92037,
USA.
(2)Department of Cell Biology, Harvard Medical School, Boston, Massachusetts
02115, USA.
(3)Howard Hughes Medical Institute, Department of Biochemistry, Stanford
University School of Medicine, Stanford, California 94305, USA.
(4)Genomics Institute of the Novartis Research Foundation, San Diego, California
92121, USA.

Comment in
    Nature. 2017 Jan 12;541(7636):165-166.

Respiratory dysfunction is a notorious cause of perinatal mortality in infants
and sleep apnoea in adults, but the mechanisms of respiratory control are not
clearly understood. Mechanical signals transduced by airway-innervating sensory
neurons control respiration; however, the physiological significance and
molecular mechanisms of these signals remain obscured. Here we show that global
and sensory neuron-specific ablation of the mechanically activated ion channel
Piezo2 causes respiratory distress and death in newborn mice. Optogenetic
activation of Piezo2+ vagal sensory neurons causes apnoea in adult mice.
Moreover, induced ablation of Piezo2 in sensory neurons of adult mice causes
decreased neuronal responses to lung inflation, an impaired Hering-Breuer
mechanoreflex, and increased tidal volume under normal conditions. These
phenotypes are reproduced in mice lacking Piezo2 in the nodose ganglion. Our data
suggest that Piezo2 is an airway stretch sensor and that Piezo2-mediated
mechanotransduction within various airway-innervating sensory neurons is critical
for establishing efficient respiration at birth and maintaining normal breathing
in adults.

DOI: 10.1038/nature20793
PMCID: PMC5267560
PMID: 28002412  [Indexed for MEDLINE]

## GITHUB LINK

	https://github.com/zara-ms/python_class/tree/master/Tareas-BioPython
"""

# Libreria a usar
from Bio import Entrez

# Anexar el correo
Entrez.email = "zarams@lcg.unam.mx"

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

# Abrir archivo con informacion
archivo = open("archivo_IDs.txt", "r")
info = str(archivo.readlines())
archivo.close()

# Abrir archivo donde se escribira el resultado
doc = open(".../docs/archivo_Abstracts.txt", "w")

# Obtener 3 abstracts utilizando un contador
i = 1
for ID in info:
    if i <= 3:
        handle = Entrez.efetch(db="pubmed", id=ID, rettype="abstract", retmode="text")
        abstract = handle.read()
        # Escribir la informacion obtenida
        doc.write(abstract)
        i += 1

handle.close()
doc.close()
