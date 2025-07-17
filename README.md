<h1>Detector de invasões</h1>

<h2>Descrição 💻</h2>

Esse projeto consiste em utilizar visão computacional. O projeto vai analisar imagens utilizando Python e OpenCv, com um modelo para detectar pessoas para calcular a probabilidade de invasão.

<h2>Resumo 📝</h2>

O projeto vai realizar detecções de pessoas nas imagens. Cada detecção tem um nível de confiança que varia entre 0 e 1. Após detectar a pessoa, é chamada as classes para pegarem a hora e o status da trava do portão, e com essas métricas calculam com Markov e com Bayes a probabilidade de estar ocorrendo uma invasão.

<h2>Introdução 🧾</h2>

Com as ondas de violência aumentando e assaltos à residência se tornando mais comuns, surge a ideia de detectar invasões. Esse projeto visa utilizar visão computacional com análise de imagens utilizando Python, OpenCv e um modelo para detectar pessoas.

Após detectar a pessoa, é chamada o cálculo da probabilidade de invasão. Esse cálculo é feito utilizando outras duas variáveis, a criticidade do horário e o estado da trava do portão.

Dependendo da hora, ela pode ser crítica, ou seja, grande probabilidade de invasões ocorrerem nesse horário, que está definido no código como das dez horas da noite até às cinco da manhã; das cinco da manhã às sete, e das seis da noite até às dez, é um horário de periculosidade moderado e o resto dos horários é de baixo perigo.

O código também irá checar se a trava do portão está ativada ou desativada, o que também influencia no risco da invasão.

Como entrada para a visão computacional, será utilizado um vídeo já gravado em que há uma pessoa se aproximando e diferentes fases de confiança na detecção.

<h2>Metodologia 🛠️</h2>

O projeto segue uma metodologia de desenvolvimento que inicia com o levantamento detalhado dos requisitos, incluindo funcionalidades específicas e com pesquisa sobre os assuntos.

O trabalho foi inspirado no do Adrian Rosebrock sobre detecção de objetos com visão computacional utilizando OpenCv. Para realizar o cálculo da probabilidade de invasão foi utilizado  duas maneiras, redes bayesianas e cadeias de Markov, a seguir, será detalhado melhor o funcionamento.

<h3>PAES 📲</h3>

O agente é do tipo reativo símples. Nesse momento do projeto, ele vai tomas as decisões baseados no estado atual.

**Performance:** Faz a detecção atutomática de invasões de maneira rápida e eficiente, ganhando um tempo precioso para a segurança dos residentes. 

**Ambiente:** Um domicilio com uma cámera e verificação no portão.

**Atuadores:** Alerta de invasão

**Sensores:** Cameras, rélogio e sensor de trava do portão.

<h3>Detecção 🔎</h3>

Para a detecção de pessoas, foi utilizada a biblioteca de visão computacional OpenCV, com a rede neural treinada de um dos exemplos do Adrian Rosebrock. No código realizado ele vai realizar a detecção da pessoa e marcar ela na imagem e retornar um valor da confiança da detecção, ou seja, o quanto o modelo tem certeza de que o objeto detectado é realmente uma pessoa.

Há também uma variável responsável por filtrar detecções com confianças muito baixas. Há uma variável confidence_threshold para impedir que seja contado e marcado detecções que tenham uma confiança abaixo de 25(vinte e cinco) por cento, para realmente evitar ao máximo falsos positivos.

Normalmente a detecção na pessoa é fixada e passaria a informação da detecção com o mesmo valor de confiança várias vezes, e para impedir de bombardear a classe de cálculo com informações repetidas foi criado um bloco de controle para limitar a passagem de detecções com a mesma confiança muitas vezes seguidas.

Após realizar essa detecção, as informações são enviadas para a classe de cálculo de probabilidade, para que assim seja realizado o cálculo.

<h3>Bayes 📈</h3>

O primeiro algoritmo a ser implementado foi o de redes bayesianas, utilizando o exemplo do notebook, foi criada uma classe com os métodos para criar as redes e realizar os cálculos.

A primeira coisa sobre esse algoritmo, é que ele é bem conservador, logo, é preciso que as três variáveis estejam verdadeiras para a probabilidade aumentar significativamente. Nesse sentido isso é bem positivo, pois como é pra detectar uma invasão, algo mais sério, é interessante essa característica conservadora.

No bayes foram utilizados apenas valores booleanos, true e false. Na trava do portão isso é imediato, se o portão está aberto, significa que a trava não foi ativada, então ele manda true, se o portão está fechado, a trava retorna false.

Na hora, ela retorna a criticidade da hora, sendo elas critical, medium e low. Foi considerado critical e medium para serem true e low como sendo false.

Na detecção das pessoas, ele retorna a taxa de confiança, se a taxa for maior ou igual a 70, passa true, se não, passa false.

<h3>Markov 📉</h3>

Já Markov também se mostrou um algoritmo mais conservador. Contudo, ele tem a característica de migrar de um valor para outro mesmo que a chance seja baixa por mera estatística. Durante os testes já ocorreu dele migrar para médio e depois para alta imediatamente mesmo com as chances sendo baixíssimas.

No Markov é passado os valores diretamente e as probabilidades são alteradas com base em condicionalismos. É importante frisar que os condicionalismos sempre aumentam a chance de migrar para o estado adjacente, para garantir uma melhor transição.

No caso da trava não está ativada, a confiança da detecção ser maior que 70(setenta) por cento e a horá for crítica, aumenta muito o próximo estado  de alerta, ou seja, se está baixo, aumenta a chance de transitar para médio, e se está médio, aumenta a chance de transitar para alto.

No caso da trava não está ativada, a confiança da detecção entar entre 70(setenta) e 55(cinquenta e cinco) por cento, e a horá for crítica, aumenta consideravelmente a probabilidade de transitar de baixo para médio, e se está médio, aumenta a chance de transitar para alto.

No caso da trava não está ativada, a confiança da detecção ser maior que 70(setenta) por cento e a horá for de risco médio, aumenta pouco a chance de transição de baixo para médio, e se está médio, aumenta a chance de transitar para alto.

Caso contrário, aumenta consideravelmente a chance de transição de ir de alto para médio ou de médio para baixo.

<h2> Resultados e discussões 📊</h2>

Com isso, torna-se interessante ter os dois algoritmos para comparação, visto que markov tem sempre a possibilidade de transitar sem haver mudanças, ter o bayes para comparar acaba sendo um porto seguro para evitar falsos positivos.

O sistema se mostrou interessante visto que os algoritmos tendem a ser mais conservadores, principalmente as redes bayesianas, fazendo com que as detecções realmente altas de invasão só ocorram com múltiplos fatores de risco bem estabelecidos, e evitando que a probabilidade de invasão tenha grande alteração quando levado em conta a união dos dois algoritmos.

O desempenho para visão computacional pesa muito porque esse recurso é caro computacionalmente falando. Tendo isso em vista, foram feitas operações de otimização que tiveram um bom efeito, como colocar um threshold para não contar detecções com confiança abaixo de 25%, e para chamar apenas o cálculo de probabilidade se houver alguma diferença entre a confiança atual e a anterior. Isso proporcionou ganhos significativos em desempenho.

<h3>O que poderia melhorar ⚒️</h3>

Uma melhoria futura seria refinar o cálculo da probabilidade de Markov e fazer uma comparação mais direta entre os dois algoritmos para acionar o alarme quando os dois tiverem alguma certeza de que está havendo uma invasão.

<h2>Como rodar 👨‍💻</h2>
Basta ter o python 3 instalado em sua maquina, junto com as bibliotecas listadas.

Bibliotecas utilizadas:
- numpy
- pandas
- cv2
- imutils
- FPS (de imutils.video)
- Client (de Adafruit_IO)
- time
- b64encode (de base64)

```sh
    pip install opencv-python
```
```sh
    pip install opencv-python-headless
```
```sh 
    pip install opencv-contrib-python
```
```sh
    pip install imutils
```
```sh
    pip install numpy
```
```sh
    pip install pandas
```

<br>Autores:<br>
<a href="https://github.com/JoabUrbano">Joab Urbano</a><br>
<a href="https://github.com/luizgustavoou">Luiz Gustavo</a><br>

Código de visão computacional baseado no trabalho de <a href="https://pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/">Adrian Rosebrock</a>.
