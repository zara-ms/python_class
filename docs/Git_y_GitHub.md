# Git y GitHub 

*Por: Zara P. Martínez Sánchez* 

#### Comandos de Git

`git init `: Inicializar el repositorio

`git add `: Agregar y dar seguimiento a los archivos del repositorio

`git commit -m`: Formalizar y asegurar los cambios realizados

`git commit -a`: Colocar un mensaje más largo, con título.

`git commit --amend -m`

`git log`: Lista los commits realizados en orden cronológico inverso

`git log -N`: Siendo _N_ el número de commits que queremos obtener

`git diff`: Muestra las modificaciones recientes 

`git log --online`: Obtener información reducida

`git log --online | wc -l`: Obener el número de commits hechos

`git status`: Identificar el estado de mi repositorio

`git status -u`: Nos dice qué archivos dentro de las carpetas necesitan un commit.

`git status --ignored`: Ver cuales archivos no están siendo controlados. 

`git diff HEAD`: Ver cambios

`git diff HEAD~1`: Ver el penúltimo cambio

`git show HEAD~1`: Muestra el commit más detallado

`git checkout`: Recuperar versiones anteriores 

`git checkout [HEAD | IdCommit] [file]`: Restaurar una versión de un archivo particular

*Buena práctica: Realizar un commit por cada archivo o por archivos relacionados*

#### Comandos cuando se tiene un repositorio web

`git remote add origin`[link]: Conectar el repositorio local con el web

`git remote -v`: Ver con cuál link se está conectando el repositorio local

`git push origin master`: Llevar los archivos que viven en nuestro repositorio local al remoto. 

`git pull origin master`: Actualizar el repositorio local con los cambios realizados en el remoto.







