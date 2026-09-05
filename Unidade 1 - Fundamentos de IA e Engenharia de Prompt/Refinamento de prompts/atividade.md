# Atividade - Refinamento de Prompts

## Identificação

* **Nome:** Kaua Sousa
* **Turma:** Ciência da Computação
* **Data:** 05/09/2026
* **Ferramenta de IA utilizada:** ChatGPT

---

## Problema escolhido

### Contexto

Estou estudando Ciência da Computação e estou aprendendo programação em Python. O objetivo da atividade é analisar como diferentes formas de elaborar um prompt podem modificar a resposta produzida por uma Inteligência Artificial Generativa.

O tema escolhido foi **listas em Python**, uma estrutura de dados bastante utilizada na programação.

### Problema

Investigar se o refinamento de um prompt consegue produzir uma explicação mais clara, organizada e adequada para um estudante que está começando a estudar listas em Python.

### Objetivo

Obter uma explicação sobre listas em Python que seja compreensível para um estudante iniciante, apresentando conceitos fundamentais, exemplos práticos e erros comuns.

---

# Prompt 1

## Prompt

```text
Explique listas em Python.
```

## Resultado

Listas em Python são estruturas de dados utilizadas para armazenar vários valores em uma única variável. Elas podem conter diferentes tipos de dados e são representadas utilizando colchetes.

Exemplo:

```python
frutas = ["maçã", "banana", "laranja"]
```

É possível acessar os elementos utilizando índices:

```python
print(frutas[0])
```

Nesse caso, será exibido `"maçã"`.

Algumas operações comuns com listas são:

```python
frutas.append("uva")
frutas.remove("banana")
print(len(frutas))
```

O método `append()` adiciona um elemento, `remove()` remove um elemento e `len()` informa a quantidade de elementos da lista.

As listas são muito importantes em Python porque permitem organizar e manipular conjuntos de dados de maneira simples.

## Análise

### O que funcionou?

* A resposta apresentou uma definição correta sobre listas.
* Foram utilizados exemplos de código.
* Alguns métodos importantes foram apresentados.
* A explicação foi relativamente curta e fácil de entender.

### O que faltou?

* Não foi definido o nível de conhecimento do estudante.
* Não houve uma explicação detalhada sobre índices.
* Não foram apresentados outros conceitos importantes, como alteração de elementos e acesso a vários elementos.
* Não foi apresentado um erro comum.
* Não houve exercício para praticar.

### O que ficou genérico?

O prompt não informou para quem a explicação deveria ser feita nem quais aspectos das listas deveriam ser abordados. Por isso, a IA precisou decidir sozinha a profundidade e o conteúdo da resposta.

### O que poderia ser melhor?

Seria interessante informar o público, definir os tópicos que devem ser apresentados, solicitar exemplos comentados e estabelecer um formato específico para a resposta.

---

# Prompt 2

## Primeiro refinamento

### Alterações realizadas

* **Papel:** atuar como professor de programação.
* **Contexto:** estudante está começando a estudar estruturas de dados.
* **Objetivo:** compreender o funcionamento básico das listas.
* **Público:** estudante iniciante de Ciência da Computação.
* **Formato:** utilizar subtítulos e exemplos de código.
* **Restrições:** utilizar linguagem simples e evitar conceitos avançados.
* **Critérios:** a explicação deve permitir que o estudante consiga utilizar uma lista básica sozinho.

## Prompt

```text
Atue como professor de programação em Python.

CONTEXTO:
Estou estudando Ciência da Computação e já conheço
variáveis e estruturas condicionais, mas ainda estou
começando a estudar estruturas de dados.

OBJETIVO:
Quero compreender o conceito e o funcionamento básico
das listas em Python.

TAREFA:
Explique:
1. O que é uma lista;
2. Como criar uma lista;
3. Como acessar elementos utilizando índices;
4. Como adicionar e remover elementos;
5. Como descobrir o tamanho de uma lista;
6. Um exemplo prático utilizando uma lista.

FORMATO:
Utilize subtítulos e exemplos de código comentados.

RESTRIÇÕES:
- Utilize linguagem simples;
- Não utilize conceitos avançados;
- Explique os termos técnicos utilizados;
- Não ultrapasse aproximadamente 600 palavras.

CRITÉRIO DE QUALIDADE:
Ao final da explicação, um estudante iniciante deverá
conseguir criar uma lista e realizar operações básicas nela.
```

## Resultado

### 1. O que é uma lista?

Uma lista é uma estrutura de dados que permite armazenar vários valores em uma única variável.

Exemplo:

```python
frutas = ["maçã", "banana", "laranja"]
```

Nesse exemplo, a variável `frutas` armazena três elementos.

### 2. Como criar uma lista?

As listas são criadas utilizando colchetes `[]`.

```python
numeros = [10, 20, 30, 40]
nomes = ["Ana", "João", "Carlos"]
```

### 3. Como acessar elementos?

Cada elemento possui uma posição chamada índice. Em Python, o primeiro índice é `0`.

```python
frutas = ["maçã", "banana", "laranja"]

print(frutas[0])
```

Resultado:

```text
maçã
```

O elemento `"maçã"` está no índice `0`, `"banana"` no índice `1` e `"laranja"` no índice `2`.

### 4. Adicionar e remover elementos

Para adicionar um elemento ao final da lista, podemos utilizar `append()`:

```python
frutas.append("uva")
```

Para remover um elemento, podemos utilizar `remove()`:

```python
frutas.remove("banana")
```

### 5. Descobrir o tamanho

A função `len()` informa quantos elementos existem na lista:

```python
print(len(frutas))
```

### 6. Exemplo prático

```python
notas = [7, 8, 9]

notas.append(10)

print(notas)
print(len(notas))
```

Nesse exemplo, uma lista de notas foi criada, uma nova nota foi adicionada e depois foram exibidos os elementos e a quantidade de notas.

Com esses conceitos, já é possível criar listas e realizar algumas operações básicas em Python.

---

# Comparação - Prompt 1 × Prompt 2

| Critério                | Prompt 1 | Prompt 2 |
| ----------------------- | -------: | -------: |
| Clareza                 |        3 |        5 |
| Precisão                |        4 |        5 |
| Relevância              |        3 |        5 |
| Organização             |        3 |        5 |
| Adequação ao público    |        2 |        5 |
| Atendimento ao objetivo |        3 |        5 |
| Utilidade prática       |        3 |        5 |
| **Total**               |   **21** |   **35** |

## Análise das melhorias

O Prompt 2 apresentou uma melhora significativa porque deixou de solicitar apenas uma explicação genérica e passou a definir o papel da IA, o contexto, o público, o objetivo, os conteúdos necessários, o formato e os critérios de qualidade.

A resposta também ficou mais organizada e adequada para alguém que está começando a estudar Python.

Entretanto, ainda seria possível melhorar o resultado solicitando, por exemplo, uma explicação sobre erros comuns e uma atividade prática para verificar se o estudante realmente compreendeu o conteúdo.

---

# Prompt 3

## O que ainda precisava melhorar?

Apesar da melhora obtida no Prompt 2, ainda faltavam alguns elementos:

* explicar erros comuns;
* mostrar uma situação prática mais próxima da realidade;
* verificar a compreensão do estudante;
* apresentar um exercício;
* destacar possíveis dificuldades de iniciantes.

## Hipótese de melhoria

Acredito que a resposta ficará melhor porque, além de explicar o conteúdo, o novo prompt solicitará uma abordagem mais didática, um exemplo prático, um erro comum e um exercício para verificar a compreensão.

## Prompt

```text
Atue como um professor de programação em Python
especializado no ensino de estudantes iniciantes.

CONTEXTO:
Sou estudante de Ciência da Computação e já conheço
variáveis, operadores e estruturas condicionais, mas
estou começando a estudar estruturas de dados.

OBJETIVO:
Quero compreender listas em Python de forma que consiga
utilizá-las em pequenos programas sem depender de uma
explicação pronta.

TAREFA:
Explique listas em Python apresentando:

1. Uma definição simples;
2. Uma analogia com uma situação do cotidiano;
3. Como criar uma lista;
4. Como acessar elementos utilizando índices;
5. Como alterar elementos;
6. Como adicionar elementos;
7. Como remover elementos;
8. Como descobrir o tamanho da lista;
9. Um exemplo prático completo;
10. Um erro comum cometido por iniciantes e como evitá-lo.

FORMATO:
- Utilize subtítulos;
- Apresente exemplos de código;
- Comente os principais trechos dos códigos;
- Utilize uma pequena tabela para resumir as principais operações;
- Finalize com um exercício prático.

RESTRIÇÕES:
- Utilize linguagem acessível;
- Não utilize conceitos avançados;
- Explique termos técnicos;
- Não utilize bibliotecas externas;
- Não apresente a solução do exercício.

CRITÉRIO DE QUALIDADE:
A explicação deve permitir que um estudante iniciante
consiga explicar com suas próprias palavras o que é uma
lista e criar um pequeno programa utilizando operações
básicas.

FINALIZAÇÃO:
Depois do exercício, apresente duas perguntas de
verificação da compreensão, sem fornecer as respostas.
```

## Resultado

### O que são listas?

Uma lista em Python é uma estrutura utilizada para armazenar vários valores em uma única variável.

Uma forma simples de imaginar uma lista é pensar em uma **lista de compras**. Em vez de guardar cada produto em uma variável diferente, podemos colocar todos eles dentro de uma única lista.

```python
compras = ["arroz", "feijão", "leite"]
```

A variável `compras` agora possui três elementos.

### Criando uma lista

Utilizamos colchetes:

```python
numeros = [10, 20, 30, 40]
nomes = ["Ana", "Carlos", "Maria"]
```

### Acessando elementos

Cada elemento possui um índice. Em Python, a contagem começa pelo índice `0`.

```python
nomes = ["Ana", "Carlos", "Maria"]

print(nomes[0])
```

Resultado:

```text
Ana
```

Podemos pensar nos índices da seguinte maneira:

| Índice | Elemento |
| -----: | -------- |
|      0 | Ana      |
|      1 | Carlos   |
|      2 | Maria    |

### Alterando elementos

Podemos substituir um elemento utilizando seu índice:

```python
nomes[1] = "João"
```

Agora a lista será:

```text
["Ana", "João", "Maria"]
```

### Adicionando elementos

O método `append()` adiciona um elemento ao final da lista:

```python
nomes.append("Pedro")
```

### Removendo elementos

O método `remove()` pode ser utilizado para remover um elemento:

```python
nomes.remove("Ana")
```

### Descobrindo o tamanho

A função `len()` informa a quantidade de elementos:

```python
print(len(nomes))
```

### Exemplo prático

Imagine um programa que armazena as notas de um estudante:

```python
notas = [7, 8, 6]

notas.append(9)

notas[0] = 8

print(notas)
print(len(notas))
```

O programa cria uma lista com três notas, adiciona uma nova nota, altera a primeira nota e depois mostra a lista e sua quantidade de elementos.

### Erro comum

Um erro comum é tentar acessar um índice que não existe.

Por exemplo:

```python
nomes = ["Ana", "João"]

print(nomes[2])
```

Essa tentativa gera um erro porque os índices disponíveis são `0` e `1`.

### Principais operações

| Operação  | Exemplo             | Função               |
| --------- | ------------------- | -------------------- |
| Criar     | `lista = [1, 2, 3]` | Cria uma lista       |
| Acessar   | `lista[0]`          | Acessa um elemento   |
| Alterar   | `lista[0] = 5`      | Modifica um elemento |
| Adicionar | `lista.append(4)`   | Adiciona elemento    |
| Remover   | `lista.remove(2)`   | Remove elemento      |
| Tamanho   | `len(lista)`        | Conta elementos      |

### Exercício

Crie uma lista chamada `alunos` contendo três nomes.

Depois:

1. Adicione um quarto nome;
2. Altere o segundo nome;
3. Remova um dos nomes;
4. Mostre a lista final;
5. Mostre quantos alunos existem na lista.

**Não utilize a solução pronta.**

### Perguntas de verificação

1. Por que o primeiro elemento de uma lista em Python possui índice `0`?

2. Qual é a diferença entre utilizar `append()` e `remove()`?

---

# Comparação final

| Critério                | Prompt 1 | Prompt 2 | Prompt 3 |
| ----------------------- | -------: | -------: | -------: |
| Clareza                 |        3 |        5 |        5 |
| Precisão                |        4 |        5 |        5 |
| Relevância              |        3 |        5 |        5 |
| Organização             |        3 |        5 |        5 |
| Adequação ao público    |        2 |        5 |        5 |
| Atendimento ao objetivo |        3 |        5 |        5 |
| Utilidade prática       |        3 |        5 |        5 |
| **Total**               |   **21** |   **35** |   **35** |

## Análise final

A maior evolução ocorreu entre o Prompt 1 e o Prompt 2. O primeiro prompt era muito genérico e deixava praticamente todas as decisões para a IA.

O Prompt 2 definiu melhor o público, o contexto, o objetivo e os conteúdos que deveriam ser abordados. Isso fez com que a resposta ficasse mais organizada e direcionada.

O Prompt 3 manteve as melhorias do segundo prompt e acrescentou elementos voltados à aprendizagem, como analogia, erro comum, exercício e perguntas de verificação.

Nesse caso, o Prompt 3 não aumentou necessariamente a nota em todos os critérios, mas tornou a resposta mais útil para o processo de aprendizagem.

---

# Validação

A qualidade da resposta foi analisada verificando se:

* os conceitos apresentados estavam relacionados ao funcionamento de listas em Python;
* os exemplos de código eram coerentes com as explicações;
* os índices apresentados estavam corretos;
* os métodos `append()` e `remove()` foram utilizados de acordo com suas funções;
* a função `len()` foi apresentada corretamente;
* o exemplo de erro relacionado ao índice inexistente era coerente;
* a resposta realmente atendia ao objetivo definido no prompt.

Também foi considerado que uma resposta bem escrita não deve ser aceita automaticamente apenas por parecer correta. É necessário analisar os exemplos e, quando necessário, verificar as informações em documentação ou outras fontes confiáveis.

---

# Reflexão

### 1. Qual foi a principal diferença entre os prompts?

A principal diferença foi o nível de especificidade. O primeiro prompt apenas solicitava uma explicação, enquanto os prompts seguintes passaram a informar o público, o contexto, o objetivo, os conteúdos, o formato e as restrições.

### 2. Quais elementos tiveram maior impacto?

Os elementos que tiveram maior impacto foram o público, o objetivo, a estrutura solicitada e os critérios de qualidade. Essas informações ajudaram a direcionar a resposta para um estudante iniciante.

### 3. Um prompt maior é necessariamente melhor?

Não. Um prompt maior pode simplesmente possuir mais palavras sem fornecer informações úteis. O mais importante é apresentar instruções relevantes e claras para alcançar o objetivo.

### 4. O que ocorre quando o objetivo não é claro?

A IA precisa interpretar o que o usuário deseja e pode produzir uma resposta genérica ou diferente daquilo que era esperado.

### 5. Quais informações são indispensáveis?

As informações mais importantes são o objetivo, o contexto, o público e a tarefa. Dependendo do caso, também é importante informar o formato, as restrições e os critérios de qualidade.

### 6. Como essa habilidade pode ser utilizada profissionalmente?

Um profissional de Ciência da Computação pode utilizar prompts refinados para auxiliar na programação, documentação, testes, análise de problemas, estudos, comparação de tecnologias e desenvolvimento de soluções.

### 7. Quais riscos existem ao confiar automaticamente na IA?

A IA pode apresentar informações incorretas, exemplos com erros, generalizações ou informações que parecem verdadeiras, mas não são. Por isso, é necessário verificar e validar as respostas.

### 8. Houve alguma situação em que o Prompt 3 ficou pior que o Prompt 2?

Não de forma significativa neste exemplo. O Prompt 3 manteve a estrutura do Prompt 2 e acrescentou elementos relacionados à aprendizagem. Entretanto, em outros casos, adicionar muitas instruções poderia deixar a resposta excessivamente limitada ou complexa.

### 9. Existe um ponto em que adicionar mais instruções começa a prejudicar a resposta?

Sim. Quando existem instruções desnecessárias, contraditórias ou excessivamente específicas, elas podem dificultar a interpretação da tarefa e tornar a resposta menos natural ou menos útil.

### 10. O que você faria para verificar se a resposta tecnicamente está correta?

Eu compararia as informações apresentadas com fontes confiáveis, como documentação oficial da linguagem, livros, materiais da disciplina e outras referências acadêmicas ou técnicas.

---

# Take Away

> **"Um bom prompt não é simplesmente um prompt longo. Ele precisa ser claro, específico, contextualizado e direcionado ao objetivo que se deseja alcançar."**

## Cinco recomendações

1. Defina claramente o objetivo antes de escrever o prompt.

2. Informe o contexto e o público que receberá a resposta.

3. Especifique o formato e os elementos que devem aparecer no resultado.

4. Analise a primeira resposta e utilize os problemas encontrados para refinar o prompt.

5. Sempre verifique e valide as informações produzidas pela IA antes de utilizá-las.

---

# Conclusão

A atividade demonstrou que o refinamento de prompts é um processo iterativo. A primeira tentativa pode apresentar uma resposta adequada, mas genérica. Ao analisar suas limitações e adicionar informações relevantes ao prompt, é possível direcionar melhor a Inteligência Artificial.

O principal aprendizado foi perceber que **refinar um prompt não significa simplesmente escrever mais, mas fornecer as informações certas para diminuir ambiguidades e aproximar a resposta do objetivo desejado**.

Além disso, o refinamento não elimina a necessidade de pensamento crítico. Mesmo quando a resposta melhora, ela deve ser analisada e validada antes de ser utilizada.
