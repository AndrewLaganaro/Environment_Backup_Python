<img src="Images/Environment_Backup_Python.png" min-width="400px" max-width="400px" width="400px" align="center" alt="Environment_Backup_Python">

---

# Python Environment Backup

##### Readme in English <p align="left"> ▶<kbd><a href="https://github.com/AndrewLaganaro/Environment_Backup_Python/blob/main/README.en.md" alt="American"> <img title="American" alt="American" src="Images/usa.png" width="20"></a></kbd>◀ </p>

##### Léame en Español <p align="left"> ▶<kbd><a href="https://github.com/AndrewLaganaro/Environment_Backup_Python/blob/main/README.es.md" alt="Español"> <img title="Español" alt="Español" src="Images/es.png" width="20"></a></kbd>◀ </p>

#### [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)

##### Autor: Andrew Laganaro

---

## 📜 Sobre o projeto

#### Um script simples gera um backup de um determinado ambiente Python

> É sempre bom manter seus pacotes de **Python** devidamente listados e bem guardados para caso você tenha problemas com o seu computador ou com a instalação no sistema.

#### 🚀 Construído com
- 🐍Python
- 🪐Jupyter Notebook
- 🖼Drawio

### 🛠 Projetos

  [![Store Sales Analysis](https://img.shields.io/badge/Projects-Store%20Sales%20Analysis-orange)](https://github.com/AndrewLaganaro/Store_Sales_Analysis)
  
  [![Data Science Framework](https://img.shields.io/badge/Projects-Data%20Science%20Framework-blue)](https://github.com/AndrewLaganaro/Data_Science_Framework)
  
  [![Data Science Classes](https://img.shields.io/badge/Projects-Data%20Science%20Classes-red)](https://github.com/AndrewLaganaro/Data_Science_Classes)

####  ⬇️ Dá uma olhada no meu Portfolio ⬇️
  
  [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)

#### 🎯 Status geral do projeto

![](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)
  
#### 📝 Como usar este projeto

Este script simples faz exatamente isso gerando dois arquivos em uma pasta conhecida:

* Environment.yml
* Packages.txt 

Ambos os arquivos podem ser usados para restaurar uma instalação completa do Python via Anaconda no Windows e Linux.

##### 💻 Pré-requisitos

Antes de começar, verifique se você atende aos seguintes requisitos:

- Você instalou a versão mais recente do Python, pandas, numpy, matplotlib, seaborn e Jupyter Notebook.
    - No mínimo Python 3.6 é necessário

##### 🚀 Instalando o ambiente de backup Python

Para instalar o Environment Backup Python, siga estas etapas:

- 📁 Selecione uma pasta na qual você deseja que seu script de backup fique.
```
...
📁 Data Science ⬅️ 💻 Inicie seu terminal aqui 💻
     📁 Diamond_Analysis
     📁 Python_Estudos
     📁 Iris_Analysis
     ...
```
    
- 💻 Por enquanto o script não é instalável diretamente, mas você pode baixá-lo diretamente clonando este repositório:

```
git clone https://github.com/AndrewLaganaro/Environment_Backup_Python
```

```
...
📁 Ciência de Dados
     📁 Diamond_Analysis
     📁 Python_Estudos
     📁 Iris_Analysis
     📁 Environment_Backup_Python
     ...
```

#### ☕ Usando o Environment Backup Python

Em geral arquivo .yml pode não funcionar com o Anaconda por conta dos metadados de alguns pacotes que podem ter vindo incorretos em seu arquivo de texto, enquanto o arquivo packages.txt sempre funciona, mas você terá que se lembrar de sua versão Python e R já que este arquivo não fornece essas informações por padrão.

Você pode encontrar mais informações sobre como corrigir o problema do arquivo de texto no caso do .yml com algumas funções regex no link abaixo, e então o arquivo .yml vai funcionar perfeitamente:

- [Resolver arquivo Env.yml não funcionando](https://github.com/conda/conda/issues/9624#issuecomment-801623523)

Além disso, é possível agendar a execução do script no Windows e Linux para salvar versões consistentes da sua configuração Python dado um determinado intervalo de tempo, por exemplo dias, semanas ou meses.

- [Programar script de backup no Windows](https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279)

- [Programar script de backup no Linux](https://betterprogramming.pub/scheduling-python-scripts-on-linux-fa0d28a8f915)

Embora eu aconselhe a fazer isso com cautela pois, novamente, algumas versões da configuração podem ser tiradas em um mal momento do seu sistema, por exemplo quando você baixou um pacote que quebrou a compatibilidade com outros pacotes previamente instalados, por exemplo: um novo pacote que depende de uma **versão mais antiga do pandas** e ao fazer o downgrade obrigatório, acaba causando incompatiblidade com o scikit-learn e com todos os outros pacotes que dependiam da versão atualizada do pandas anterior.

Por isso é sempre bom manter uma versão "principal" do seu ambiente de vez em quando para evitar que esses problemas aconteçam.

##### ⭐️ Recursos a serem adicionados

- [ ] O script também pode ser modificado para alterar os nomes dos arquivos periodicamente, por exemplo "Env_01/02/2021", "Env_01/03/2021" para ajudar na manutenção

- [ ] Adicionar uma saída de arquivo contendo apenas a versão do Python, caso o arquivo .yml não funcione e você também não consiga consertá-lo, você pode usar o Packages.txt e o novo Versions.txt para restaurar totalmente sua configuração manualmente via conda

- [ ] Adicionar um segundo script para executar a instalação do backup considerando a possibilidade dos três arquivos gerados serem usados

---

####  ⬇️ Dá uma olhada no meu Portfolio ⬇️
  
  [![Portfolio](https://img.shields.io/badge/Projects-Portfolio-blue)](https://andrewcode.herokuapp.com)
  