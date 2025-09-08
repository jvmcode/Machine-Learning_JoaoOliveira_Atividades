# 1ª - Explique, com suas palavras, o que é machine learning?

Resposta: 

É um ramo da inteligência artificial que permite que computadores aprendam com dados, sem serem programados explicitamente para cada tarefa. Em vez de seguir regras fixas, os sistemas são treinados com exemplos e ajustam seu desempenho com o tempo. É como ensinar uma máquina a reconhecer padrões e tomar decisões com base neles.

Exemplo:

Um modelo pode aprender a identificar fraudes bancárias analisando milhares de transações;

Prever o clima com base em dados histórico;
____________________________________________________________________________________________________________

# 2ª - Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning?

Resposta:

2.1 Conjunto de Treinamento - É o primeiro conjunto usado para ensinar o modelo. Contém exemplos com entradas e saídas conhecidas. O modelo aprende padrões e ajusta seus parâmetros com base nesses dados.

Exemplo:
Conjunto usado para ensinar o modelo. Ele contém e-mails com rótulos (spam ou não spam):
- "Ganhe dinheiro rápido agora!" → Spam
- "Reunião às 14h com o cliente" → Não spam
- "Oferta imperdível, clique aqui!" → Spam
O modelo aprende que palavras como “dinheiro”, “oferta” e “clique” são comuns em spams.

2.2 Conjunto de Validação - Usado durante o treinamento para ajustar hiperparâmetros (como profundidade de uma árvore ou taxa de aprendizado). Ajuda a detectar problemas como overfitting (quando o modelo aprende demais os dados de treino e não generaliza bem). Não participa diretamente do treinamento, mas orienta melhorias no modelo.

Exemplo:
Número de árvores em uma Random Forest:
- "Seu cartão foi aprovado, acesse o link" → Spam
- "Relatório financeiro do trimestre" → Não spam
Se o modelo errar muito aqui, talvez esteja decorando os dados de treino (overfitting) e precise ser ajustado.

2.3 Conjunto de Teste - Usado após o treinamento completo para avaliar o desempenho final do modelo. Mede como o modelo se comporta com dados nunca vistos antes. Serve como uma estimativa da performance real em produção.

Exemplo:
- "Parabéns! Você foi selecionado para um prêmio" → Spam
- "Atualização do sistema agendada para amanhã" → Não spam
Aqui, medimos métricas como acurácia, precisão e recall para saber se o modelo está pronto para uso.
____________________________________________________________________________________________________________

# 3ª - Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento?

Resposta:

Poderia lidar de algumas formas: Removendo registros ou variáveis com muitos valores faltantes, se não forem relevantes.
Imputar valores usando média, mediana, moda ou técnicas mais avançadas como regressão ou KNN.
Usar modelos que lidam bem com dados ausentes, como árvores de decisão.
Criar indicadores binários para marcar valores ausentes, preservando a informação.
A escolha da técnica depende do tipo de dado, da quantidade de valores ausentes e do impacto no modelo.
___________________________________________________________________________________________________________________________________________________

# 4ª - O que é uma matriz de confusão e como ela é usada para avaliar o desempenho de um modelo preditivo?

Resposta:

Matriz de confusão é uma tabela que compara as previsões do modelo com os valores reais, usada para avaliar modelos de classificação. 
Ela mostra:
VP (Verdadeiro Positivo): acertos em casos positivos

VN (Verdadeiro Negativo): acertos em casos negativos

FP (Falso Positivo): erro ao prever positivo

FN (Falso Negativo): erro ao prever negativo

A partir dela, calculamos métricas como:

Acurácia: taxa de acertos totais

Precisão: acertos entre os positivos previstos

Recall: acertos entre os positivos reais

F1-Score: equilíbrio entre precisão e recall

Ela ajuda a entender onde o modelo está acertando ou errando e a ajustar seu desempenho.
___________________________________________________________________________________________________________________________________________________

# 5ª - Em quais áreas (tais como construção civil, agricultura, saúde, manufatura, entre outras) você acha mais interessante aplicar algoritmos de machine learning?

Resposta:

Embora o machine learning tenha aplicações valiosas em diversas áreas, a saúde se destaca como uma das mais impactantes e transformadoras: Diagnósticos mais rápidos e precisos; Prevenção de doenças; Tratamentos personalizados; Apoio à decisão clínica; Eficiência hospitalar. A aplicação de machine learning na saúde salva vidas, reduz custos e democratiza o acesso à medicina de qualidade. Em comparação com outras áreas, o impacto humano e social é incomparável. É tecnologia com propósito.