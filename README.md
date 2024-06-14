# Detecção de faces para bola de ouro PIFA 2024

Este projeto tem como objetivo desenvolver um modelo de detecção de faces e emoções em imagens para a bola de ouro PIFA 2024. Para isso, será utilizado um classificador em cascata Haar Cascade.

## Como instalar e rodar o projeto

Para executar o projeto, é necessário ter o Python instalado na máquina. Com o Python instalado, basta clonar este repositório e executar o comando `pip install -r requirements.txt` para instalar as dependências do projeto. Após a instalação das dependências, basta executar o comando `python faces.py` para iniciar a detecção de faces nas imagens de exemplo.

## Perguntas técnicas

### 2.1 - O modelo escolhido

O método escolhido foi o Haar Cascade. Este, funciona através de um algoritmo de aprendizado de máquina que utiliza um classificador em cascata para detectar objetos em imagens ou vídeos. O classificador é treinado a partir de imagens positivas e negativas. As imagens positivas contêm o objeto que se deseja detectar, enquanto as imagens negativas contêm tudo o que não é o objeto. O resultado é um arquivo XML que contém as informações necessárias para detectar o objeto em questão.

### 2.2 - Classificação de modelos por detecção de faces

Na lista a seguir, os modelos estão classificados por viabilidade técninca, facilidade de implementação e versatilidade da solução para se desenvolver um modelo de detecção de faces em imagens. <br>

1. Haar Cascade - Viável, fácil de implementar e versátil, sendo que possui dados já treinados e não exige conhecimento avançado em aprendizado de máquina.
2. NN Linear - Viável, porém mais difícil de implementar e menos versátil, pois exige grandes quantidades de dados para treinamento.
3. CNN - Viável, porém complexo de implementar, sendo que requer conhecimento avançado em álgebra e convoluções, além de ser menos versátil, já que é necessário também um grande volume de dados para treinamento.
4. Filtros de correlação cruzada - Menos viável por não ser especificamente feito para detectar imagens, mais complexo de implementar, já que também exige conhecimentos complexos e é menos versátil pelo mesmo motivo.

### 2.3 - Classificação de modelos por detecção de emoções

Na lista a seguir, os modelos estão classificados por viabilidade técninca, facilidade de implementação e versatilidade da solução para se desenvolver um modelo de detecção de emoções em imagens. <br>

1. NN Linear - Viável, já que usa uma quantidade de dados maior para realizar seus treinamentos porém mais difícil de implementar e menos versátil, pois exige um conhecimento maior de máquinas de aprendizado e redes neurais.
2. CNN - Viável por necessitar de uma grande quantidade de dados específicos, porém complexo de implementar por requerer conhecimento avançado em convoluções como dito anteriormente, assim não sendo muito versátil.
3. Haar Cascade - Menos viável por não ser especificamente feito para detectar emoções, não é tão complexo de implementar, já que não exige conhecimentos avançados e é menos versátil por não possuir dados treinados para tal.
4. Filtros de correlação cruzada - Menos viável por não ser especificamente feito para detectar emoções, mais complexo de implementar, já que também exige conhecimentos complexos e é menos versátil pelo mesmo motivo.

### 2.4 - Variabilidade de um frame para outro no modelo escolhido

A solução apresentada não tem a capacidade de considerar variações de um frame para outro, pois ela é baseada em um classificador em cascata que não leva em consideração a relação entre os frames. Para que isso seja possível, seria necessário utilizar um modelo de aprendizado de máquina que levasse em consideração a relação temporal entre os frames, como uma rede neural recorrente (RNN) ou uma rede neural convolucional 3D (CNN 3D). Dessa forma, o modelo seria capaz de considerar as variações de um frame para outro e detectar emoções com base nessa informação.

### 2.5 - Vencedor da bola de ouro PIFA 2024

O vencedor da bola de ouro PIFA 2024, sem dúvida alguma será o Vinícius Junior, o rei das finais de Champions. 