"""
## NAME

	Arrays.py

## VERSION

	[1.0]

## AUTHOR

	Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

	[25/10/2021]

## GITHUB LINK

	https://github.com/zara-ms/python_class/tree/master/Tareas-BioPython

"""


import numpy as np

# Crear arrays estructurados especificando los tipos de datos
produccion = np.array([('Gen1', 30, 5), ('Gen2', 30, 11), ('Gen3', 30, 4), ('Gen4', 30, 2),
                       ('Gen1', 35, 3), ('Gen2', 35, 7), ('Gen3', 35, 9), ('Gen4', 35, 6)],
                      dtype=[('gen', (np.str_, 5)), ('temperatura', np.int32), ('produccion', np.int32)])

inductor = np.array([('Gen1', 3.5), ('Gen2', 5), ('Gem3', 7), ('Gen4', 4.3)],
                    dtype=[('gen', np.str_, 5), ('costo', np.float64)])

costo = np.array([('Gen1', 30, 0.7), ('Gen2', 30, 0.45454545), ('Gen3', 30, 1.75), ('Gen4', 30, 2.15),
                    ('Gen1', 35, 1.16666667), ('Gen2', 35, 0.71428571), ('Gen3', 35, 0.77777778),
                  ('Gen4', 35, 0.71666667)],
                      dtype=[('gen', (np.str_, 5)), ('temperatura', np.int32), ('costo por 1g/L', np.float64)])

