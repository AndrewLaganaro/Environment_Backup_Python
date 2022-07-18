<img src="Images/Environment_Backup_Python.png" min-width="400px" max-width="400px" width="400px" align="center" alt="Environment_Backup_Python">

---

# Python Environment Backup

##### Leia-me em português <p align="left">  ▶<kbd><a href="https://github.com/AndrewLaganaro/Environment_Backup_Python/" alt="Brazilian">  <img title="Brazilian" alt="Brazilian" src="Images/br.jpg" width="20"></a></kbd>◀ </p>

##### Readme in English <p align="left"> ▶<kbd><a href="https://github.com/AndrewLaganaro/Environment_Backup_Python/blob/main/Readme.en.md" alt="American"> <img title="American" alt="American" src="Images/usa.png" width="20"></a></kbd>◀ </p>

#### [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)

##### Autor: Andrew Laganaro

---

## 📜 Sobre el proyecto

#### Un script simple genera una copia de seguridad de un entorno de Python dado

> Siempre es bueno mantener sus paquetes de Python correctamente listados y bien protegidos en caso de que tenga problemas con su computadora o con la instalación en el sistema.

#### 🚀 Construido con
- 🐍Python
- 🪐Jupyter Notebook
- 🖼Drawio

### 🛠 Proyectos

  [![Store Sales Analysis](https://img.shields.io/badge/Projects-Store%20Sales%20Analysis-orange)](https://github.com/AndrewLaganaro/Store_Sales_Analysis)
  
  [![Data Science Framework](https://img.shields.io/badge/Projects-Data%20Science%20Framework-blue)](https://github.com/AndrewLaganaro/Data_Science_Framework)
  
  [![Data Science Classes](https://img.shields.io/badge/Projects-Data%20Science%20Classes-red)](https://github.com/AndrewLaganaro/Data_Science_Classes)

#### ⬇️ Echa un vistazo a mi Portafolio ⬇️
  
  [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)
  
#### 🎯 Estado general del proyecto

![](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)
  
#### 📝 Cómo usar este proyecto

Este sencillo script hace precisamente eso al generar dos archivos en una carpeta conocida:

* Environment.yml
* Packages.txt 

Ambos archivos se pueden usar para restaurar una instalación completa de Python a través de Anaconda en Windows y Linux.

##### 💻 Requisitos previos

Antes de empezar, asegúrate de cumplir con los siguientes requisitos:

- Ha instalado la última versión de Python, pandas, numpy, matplotlib, seaborn y Jupyter Notebook.
    - Se requiere al menos Python 3.6

##### 🚀 Instalación del entorno de copia de seguridad de Python

Para instalar Environment Backup Python, siga estos pasos:

- 📁 Seleccione una carpeta donde desea que esté su script de respaldo.
```
...
📁 Data Science ⬅️ 💻 Inicia aquí tu terminal 💻
    📁 Diamond_Analysis
    📁 Python_Studies
    📁 Iris_Analysis
    ...
```
    
- 💻 Por ahora el script no se puede instalar directamente, pero puedes descargarlo directamente clonando este repositorio:

```
git clone https://github.com/AndrewLaganaro/Environment_Backup_Python
```

```
...
📁 Data Science
    📁 Diamond_Analysis
    📁 Python_Studies
    📁 Iris_Analysis
    📁 Environment_Backup_Python
    ...
```

#### ☕ Uso de Environment Backup Python

En general, es posible que el archivo .yml no funcione con Anaconda debido a los metadatos de algunos paquetes que pueden haber sido incorrectos en su archivo de texto, mientras que el archivo packages.txt siempre funciona, pero tendrá que recordar su versión de Python como lo hace este archivo no proporciona esta información por defecto.

Puede encontrar más información sobre cómo solucionar el problema del archivo de texto en el caso de .yml con algunas funciones de expresiones regulares en el siguiente enlace, y luego el archivo .yml funcionará perfectamente:

- [Resolver el archivo Env.yml que no funciona](https://github.com/conda/conda/issues/9624#issuecomment-801623523)

Además, puede programar la ejecución de secuencias de comandos en Windows y Linux para guardar versiones coherentes de su configuración de Python en un determinado intervalo de tiempo, por ejemplo, días, semanas o meses.

- [Programar secuencia de comandos de copia de seguridad en Windows](https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279)

- [Programar secuencia de comandos de copia de seguridad en Linux](https://betterprogramming.pub/scheduling-python-scripts-on-linux-fa0d28a8f915)

Aunque te aconsejo que hagas esto con precaución ya que, de nuevo, algunas versiones de la configuración pueden ser tomadas en un mal momento de tu sistema, por ejemplo cuando descargaste un paquete que rompía la compatibilidad con otros paquetes previamente instalados, por ejemplo: un nuevo paquete que depende de una **versión anterior de pandas** y cuando es obligatorio degradarlo termina causando incompatibilidad con scikit-learn y todos los demás paquetes que dependían de la versión actualizada anterior de pandas.

Es por eso que siempre es una buena idea mantener una versión "maestra" de su entorno de vez en cuando para evitar que ocurran estos problemas.

##### ⭐️ Funciones por agregar

- [ ] La secuencia de comandos también se puede modificar para cambiar los nombres de los archivos periódicamente, por ejemplo, "Env_01/02/2021", "Env_01/03/2021" para ayudar con el mantenimiento

- [ ] Agregue un archivo de salida que contenga solo la versión de Python, en caso de que el archivo .yml no funcione y tampoco pueda solucionarlo, puede usar Packages.txt y el nuevo Versions.txt para restaurar completamente su configuración manualmente vía conda

- [ ] Agregar un segundo script para ejecutar la instalación de respaldo considerando la posibilidad de que se utilicen los tres archivos generados

---

#### ⬇️ Echa un vistazo a mi Portafolio ⬇️
  
  [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)
  