# Aula 02 — Engenharia de Prompt

## 1. Identificação

Disciplina: Tendências em Ciências da Computação
Turma: N1
Grupo: Individual
Data: 21/08/2026
Integrante: Kaua

---

## 2. Problema escolhido

### Contexto

No desenvolvimento de sistemas de software, a análise de requisitos é uma etapa importante para compreender o que o sistema deve fazer e quais necessidades dos usuários precisam ser atendidas.

Entretanto, estudantes que estão iniciando na área de Computação podem ter dificuldades para identificar e diferenciar requisitos funcionais e não funcionais, além de transformar uma descrição de problema em requisitos claros e organizados.

Nesse contexto, uma ferramenta de Inteligência Artificial Generativa pode ser utilizada como apoio para analisar uma descrição de sistema e sugerir possíveis requisitos.

### Problema

Como utilizar uma ferramenta de Inteligência Artificial Generativa para auxiliar estudantes de Computação na identificação e organização de requisitos de um sistema?

---

## 3. Objetivo

Utilizar uma ferramenta de Inteligência Artificial Generativa para auxiliar na identificação de requisitos funcionais e não funcionais a partir da descrição de um sistema, avaliando a qualidade da resposta obtida e refinando o prompt para produzir um resultado mais claro, organizado e adequado ao contexto.

---

## 4. Prompt inicial

```text
Analise os requisitos de um sistema acadêmico e liste os requisitos funcionais e não funcionais.
```

### Resultado inicial

A partir do prompt inicial, a IA apresentou uma resposta semelhante a:

**Requisitos funcionais:**

1. Cadastrar alunos.
2. Cadastrar professores.
3. Cadastrar disciplinas.
4. Permitir realizar login.
5. Consultar notas.
6. Emitir relatórios.

**Requisitos não funcionais:**

1. O sistema deve ser seguro.
2. O sistema deve ser rápido.
3. O sistema deve ser fácil de utilizar.
4. O sistema deve estar disponível para os usuários.

Embora a resposta apresente exemplos pertinentes, ela é bastante genérica e não considera informações específicas sobre o contexto do sistema acadêmico.

---

## 5. Análise crítica

### O que funcionou?

O prompt inicial conseguiu orientar a IA para o tema de requisitos de software. A resposta apresentou exemplos de requisitos funcionais e não funcionais e organizou as informações de maneira relativamente simples.

### O que não funcionou?

O principal problema foi a falta de contexto. O prompt não especificava qual era o sistema acadêmico, quem seriam seus usuários ou quais funcionalidades deveriam ser consideradas.

Além disso, alguns requisitos foram apresentados de maneira muito genérica, como "o sistema deve ser rápido" e "o sistema deve ser seguro".

### O que faltou?

Faltaram informações como:

* contexto do sistema;
* usuários envolvidos;
* objetivo do sistema;
* quantidade de requisitos;
* diferenciação clara entre requisitos funcionais e não funcionais;
* descrição dos requisitos;
* critérios para avaliar a qualidade da resposta;
* formato específico para apresentação.

### O que precisa ser validado?

Os requisitos gerados pela IA precisam ser comparados com as necessidades reais do sistema. Também é necessário verificar se cada requisito foi corretamente classificado como funcional ou não funcional e se a descrição representa uma necessidade real.

### A IA fez alguma suposição inadequada?

Sim. Como o prompt não forneceu informações suficientes, a IA precisou assumir quais funcionalidades um sistema acadêmico deveria possuir. Essas suposições podem não representar os requisitos reais de um sistema específico.

---

## 6. Prompt refinado

```text
Você é um analista de requisitos de software e também professor de Engenharia de Software.

CONTEXTO:

Estamos analisando um sistema acadêmico desenvolvido por estudantes de Computação. O sistema terá três tipos principais de usuários: administrador, professor e aluno.

O objetivo do sistema é permitir o gerenciamento de informações acadêmicas, incluindo usuários, disciplinas, atividades e notas.

Os estudantes que utilizarão sua resposta estão aprendendo Engenharia de Software e possuem conhecimentos básicos sobre requisitos funcionais e não funcionais.

OBJETIVO:

Auxiliar os estudantes a identificar e organizar requisitos funcionais e não funcionais para esse sistema acadêmico.

TAREFA:

1. Identifique 8 requisitos funcionais.
2. Identifique 5 requisitos não funcionais.
3. Classifique cada requisito corretamente.
4. Explique brevemente cada requisito.
5. Informe qual usuário está relacionado ao requisito funcional, quando aplicável.
6. Aponte possíveis ambiguidades ou pontos que precisam ser validados com o cliente.

RESTRIÇÕES:

- Utilize linguagem clara e adequada para estudantes iniciantes.
- Não invente funcionalidades que não estejam relacionadas ao contexto apresentado.
- Evite requisitos excessivamente genéricos.
- Cada requisito deve representar uma necessidade específica do sistema.

FORMATO:

Apresente os requisitos em duas tabelas.

Tabela 1:
| ID | Requisito Funcional | Usuário | Descrição |

Tabela 2:
| ID | Requisito Não Funcional | Categoria | Descrição |

Depois das tabelas, apresente uma seção chamada "Pontos a validar", contendo as informações que ainda precisam ser confirmadas com o cliente.

CRITÉRIOS DE QUALIDADE:

A resposta deve ser clara, objetiva, coerente, tecnicamente consistente e adequada para estudantes iniciantes de Computação.
```

---

## 7. Resultado refinado

Após o refinamento do prompt, a resposta esperada da IA pode ser organizada da seguinte maneira:

### Requisitos funcionais

| ID   | Requisito Funcional   | Usuário                          | Descrição                                                                               |
| ---- | --------------------- | -------------------------------- | --------------------------------------------------------------------------------------- |
| RF01 | Realizar login        | Administrador, Professor e Aluno | O sistema deve permitir que os usuários acessem o sistema utilizando suas credenciais.  |
| RF02 | Gerenciar usuários    | Administrador                    | O sistema deve permitir cadastrar, alterar e excluir usuários.                          |
| RF03 | Gerenciar disciplinas | Administrador e Professor        | O sistema deve permitir cadastrar e consultar informações das disciplinas.              |
| RF04 | Consultar disciplinas | Aluno                            | O sistema deve permitir que o aluno consulte as disciplinas nas quais está matriculado. |
| RF05 | Cadastrar atividades  | Professor                        | O sistema deve permitir que o professor cadastre atividades para suas disciplinas.      |
| RF06 | Consultar atividades  | Aluno                            | O sistema deve permitir que o aluno visualize as atividades disponíveis.                |
| RF07 | Registrar notas       | Professor                        | O sistema deve permitir que o professor registre e altere as notas dos alunos.          |
| RF08 | Consultar notas       | Aluno                            | O sistema deve permitir que o aluno consulte suas notas.                                |

### Requisitos não funcionais

| ID    | Requisito Não Funcional | Categoria       | Descrição                                                                           |
| ----- | ----------------------- | --------------- | ----------------------------------------------------------------------------------- |
| RNF01 | Segurança               | Segurança       | O sistema deve proteger os dados dos usuários contra acesso não autorizado.         |
| RNF02 | Usabilidade             | Usabilidade     | A interface deve ser simples e adequada aos diferentes tipos de usuários.           |
| RNF03 | Desempenho              | Desempenho      | As operações principais do sistema devem apresentar tempo de resposta adequado.     |
| RNF04 | Disponibilidade         | Disponibilidade | O sistema deve permanecer disponível durante os períodos definidos para utilização. |
| RNF05 | Integridade             | Integridade     | O sistema deve preservar a consistência dos dados acadêmicos armazenados.           |

### Pontos a validar

Alguns aspectos ainda precisam ser confirmados com o cliente ou responsável pelo sistema:

* Quais dados serão utilizados para autenticação?
* O administrador poderá alterar todos os dados dos usuários?
* Como serão definidas as permissões de cada perfil?
* Quais critérios serão utilizados para medir o desempenho?
* Qual será o período de disponibilidade esperado?
* Quais regras serão utilizadas para alteração das notas?
* Quais requisitos de segurança deverão ser obrigatoriamente atendidos?

---

## 8. Técnicas utilizadas

As principais técnicas de Engenharia de Prompt utilizadas foram:

* [x] Role Prompting
* [ ] Few-Shot Prompting
* [x] Contexto
* [x] Restrições
* [x] Formato de saída
* [x] Prompt em etapas
* [x] Refinamento iterativo
* [ ] Outra

### Justificativa

**Role Prompting:** foi utilizado ao definir que a IA deveria atuar como um analista de requisitos e professor de Engenharia de Software.

**Contexto:** foram fornecidas informações sobre o sistema acadêmico, seus usuários e o objetivo do sistema.

**Restrições:** foram estabelecidos limites para evitar requisitos excessivamente genéricos e orientar a linguagem utilizada.

**Formato de saída:** foi especificado que os requisitos deveriam ser apresentados em tabelas.

**Prompt em etapas:** a tarefa foi dividida em diferentes ações, como identificar, classificar, explicar e apontar pontos que precisam ser validados.

**Refinamento iterativo:** o segundo prompt foi construído a partir dos problemas identificados no primeiro resultado.

---

## 9. Comparação

| Critério    | Prompt Inicial           | Prompt Refinado                      |
| ----------- | ------------------------ | ------------------------------------ |
| Clareza     | Baixa                    | Alta                                 |
| Contexto    | Pouco contexto           | Contexto detalhado                   |
| Relevância  | Genérica                 | Adequada ao sistema proposto         |
| Organização | Lista simples            | Tabelas estruturadas                 |
| Precisão    | Limitada                 | Maior precisão                       |
| Utilidade   | Serve como ponto inicial | Mais útil para análise de requisitos |

### Análise da comparação

O prompt refinado produziu um resultado mais adequado porque apresentou informações sobre o contexto do problema, definiu o papel da IA, estabeleceu um objetivo específico, determinou quais informações deveriam ser produzidas e definiu um formato de saída.

O prompt inicial deixava muitas informações em aberto, fazendo com que a IA precisasse realizar suposições.

Dessa forma, o **Prompt B — refinado** produziu o resultado mais adequado para o objetivo da atividade.

---

## 10. Validação

A resposta produzida pela IA não deve ser considerada automaticamente correta.

Para validar os requisitos, é necessário verificar se cada requisito corresponde realmente a uma necessidade do sistema e se sua classificação está correta.

A validação pode ser realizada por meio de:

1. Comparação dos requisitos com o objetivo do sistema.
2. Verificação da classificação entre funcional e não funcional.
3. Identificação de requisitos genéricos ou ambíguos.
4. Revisão dos requisitos por estudantes ou professores da área.
5. Confirmação das informações com o cliente ou responsável pelo sistema.

Também é importante considerar que a IA pode produzir informações incorretas, incompletas ou baseadas em suposições. Portanto, a resposta precisa ser analisada criticamente antes de ser utilizada.

---

## 11. Ética e responsabilidade

O uso de Inteligência Artificial para auxiliar na análise de requisitos apresenta alguns riscos.

A IA pode gerar requisitos que não correspondem às necessidades reais do sistema ou fazer suposições que não foram informadas pelo usuário. Também pode apresentar respostas aparentemente corretas, mas que contenham erros técnicos.

Por isso, os resultados produzidos pela IA não devem ser utilizados de forma automática.

A responsabilidade pela utilização das informações continua sendo das pessoas envolvidas no projeto. É necessário verificar as respostas, questionar possíveis erros e confirmar informações importantes com fontes confiáveis e com o responsável pelo sistema.

Nesse caso, a IA deve ser utilizada como uma ferramenta de apoio à análise humana, e não como substituta do conhecimento e da tomada de decisão dos profissionais.

---

## 12. Take Away

A realização da atividade mostrou que Engenharia de Prompt não consiste apenas em fazer uma pergunta para uma Inteligência Artificial.

Um prompt mais estruturado, com contexto, objetivo, tarefa, restrições, formato e critérios de qualidade, permite direcionar melhor a resposta da IA.

Também foi possível perceber que o primeiro resultado nem sempre é suficiente. É necessário analisar a resposta, identificar problemas, refinar o prompt e testar novamente.

A principal aprendizagem do grupo foi que a qualidade da interação com uma IA depende não somente da ferramenta utilizada, mas também da capacidade humana de formular instruções claras, avaliar criticamente os resultados e validar as informações antes de utilizá-las.

---

## 13. Link

...
