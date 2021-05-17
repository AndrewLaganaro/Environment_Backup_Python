# Backup de ambiente Python

É sempre bom manter seus pacotes de **Python** e **R** do Anaconda devidamente listados e bem guardados para caso você tenha problemas com o seu computador ou com a instalação no sistema.

Esse script simples faz exatamente isso, gerando dois arquivos em uma pasta conhecida:

* Environment.yml
* Packages.txt

Ambos os arquivos podem ser usados ​​para restaurar uma instalação Python e R completa via Anaconda no Windows e Linux.

O arquivo .yml pode não funcionar com o Anaconda por conta dos metadados de alguns pacotes que podem ter vindo incorretos em seu arquivo de texto, enquanto o arquivo packages.txt sempre funciona, mas você terá que se lembrar de sua versão Python e R já que este arquivo não fornece essas informações por padrão.

Você pode encontrar mais informações sobre como corrigir o problema do arquivo de texto no caso do .yml com algumas funções regex no link abaixo, e então o arquivo .yml vai funcionar perfeitamente:

- [Resolver arquivo Env.yml não funcionando](https://github.com/conda/conda/issues/9624#issuecomment-801623523)

Além disso, é possível agendar a execução do script no Windows e Linux para salvar versões consistentes da sua configuração Python dado um determinado intervalo de tempo, por exemplo dias, semanas ou meses.

- [Programar script de backup no Windows](https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279)

- [Programar script de backup no Linux](https://betterprogramming.pub/scheduling-python-scripts-on-linux-fa0d28a8f915)

Embora eu aconselhe a fazer isso com cautela pois, novamente, algumas versões da configuração podem ser tiradas em um mal momento do seu sistema, por exemplo quando você baixou um pacote que quebrou a compatibilidade com outros pacotes previamente instalados, por exemplo: um novo pacote que depende de uma **versão mais antiga do pandas** e ao fazer o downgrade obrigatório, acaba causando incompatiblidade com o scikit-learn e com todos os outros pacotes que dependiam da versão atualizada do pandas anterior.

Por isso é sempre bom manter uma versão "principal" do seu ambiente de vez em quando para evitar que esses problemas aconteçam.

### **Melhorias planejadas:**

1. O script também pode ser modificado para alterar os nomes dos arquivos periodicamente, por exemplo "Env_01/02/2021", "Env_01/03/2021" para ajudar na manutenção

1. Adicionar uma saída de arquivo contendo apenas a versão do Python, caso o arquivo .yml não funcione e você também não consiga consertá-lo, você pode usar o Packages.txt e o novo Versions.txt para restaurar totalmente sua configuração manualmente via conda

1. Adicionar um segundo script para executar a instalação do backup considerando a possibilidade dos três arquivos gerados serem usados

Os arquivos presentes neste repo também são meus próprios backups que fiz para mim do meu ambiente, atualmente estou usando Python 3.6, mas estou planejando mudar para Python 3.7 ou 3.8 em breve. A longa lista de pacotes, além de referir-se aos principais, também se refere a dependências e dependências de dependências. Sinta-se à vontade para usá-los como quiser.

> [American Readme](Readme.md)