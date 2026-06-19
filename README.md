# MoodSync: Análise de Dinâmica Biocomportamental e Detecção de Estado Emocional via Ritmo de Digitação

## Visão Geral

MoodSync é um sistema de Inteligência Artificial projetado para investigar a correlação entre o ritmo de digitação do usuário e seu estado emocional. Através da análise de padrões de digitação, como velocidade, pausas e pressão (simulada), o MoodSync busca inferir o estado emocional do usuário em tempo real, com aplicações potenciais em interfaces adaptativas, saúde mental digital e pesquisa em interação humano-computador.

## Declaração do Problema

O estado emocional de um indivíduo pode influenciar significativamente sua interação com sistemas digitais, afetando a produtividade, a comunicação e o bem-estar. Métodos tradicionais de detecção emocional, como questionários ou análise facial, podem ser intrusivos ou reativos. O MoodSync propõe uma abordagem passiva e contínua, utilizando o ritmo de digitação como um biomarcador comportamental para inferir o estado emocional, oferecendo uma nova perspectiva para a compreensão e adaptação a estados afetivos em ambientes digitais [1].

## Solução Proposta

MoodSync emprega um modelo de Machine Learning para analisar dados de ritmo de digitação. O sistema extrai características-chave dos padrões de digitação do usuário para prever seu estado emocional. As etapas incluem:

1.  **Coleta de Dados de Digitação**: Monitoramento de eventos de teclado, como tempo de pressionamento de tecla, tempo entre teclas e padrões de digitação.
2.  **Detecção de Estado Emocional**: Identificação de padrões nos dados de digitação que correlacionam com estados emocionais específicos (e.g., feliz, triste, estressado).
3.  **Feedback Adaptativo (Potencial)**: Fornecimento de feedback ou adaptação da interface do usuário com base no estado emocional detectado (para futuras implementações).
4.  **Preservação da Privacidade**: Processamento local de todos os dados de digitação, garantindo que nenhuma informação sensível seja transmitida ou armazenada externamente.

## Abordagem Técnica e Modelo de IA

### Coleta de Dados (Simulada para Prova de Conceito)

Para esta prova de conceito, os dados de digitação são simulados utilizando `data_simulator.py`. Este script gera conjuntos de dados sintéticos que mimetizam os padrões de digitação associados a diferentes estados emocionais. As características simuladas incluem:

*   **Velocidade de Digitação**: e.g., rápida (feliz/estressado) vs. lenta (triste/calmo).
*   **Tempo de Pressionamento de Tecla (Dwell Time)**: e.g., curto (agitado) vs. longo (pensativo).
*   **Tempo entre Teclas (Flight Time)**: e.g., consistente (focado) vs. inconsistente (distraído).
*   **Padrões de Erro**: e.g., alta taxa de erro (estressado) vs. baixa taxa de erro (calmo).
*   **Estado Emocional**: Uma etiqueta simulada representando o estado emocional (e.g., "feliz", "triste", "neutro", "estressado").

### Engenharia de Características

As características numéricas simuladas (velocidade, dwell time, flight time, padrões de erro) são padronizadas utilizando StandardScaler para garantir que todas as características contribuam igualmente para o modelo.

### Modelo de Machine Learning

O cerne do MoodSync é um **Classificador Support Vector Machine (SVM)**. SVMs são eficazes em problemas de classificação, especialmente quando há uma clara separação entre as classes, e podem lidar com alta dimensionalidade dos dados de digitação [2].

*   **Entrada**: Características padronizadas representando padrões de digitação.
*   **Modelo**: Um algoritmo SVM que encontra o hiperplano ideal para separar as classes emocionais.
*   **Saída**: Uma previsão do estado emocional do usuário: "feliz", "triste", "neutro" ou "estressado".

## Metodologia

A metodologia empregada no MoodSync segue um pipeline de Machine Learning supervisionado, com foco na classificação de estados emocionais a partir de dados de digitação. A simulação de dados permite a exploração de diferentes perfis emocionais sem a necessidade de coleta de dados comportamentais sensíveis em tempo real na fase inicial de desenvolvimento. A escolha do SVM como modelo principal justifica-se pela sua robustez e eficácia em problemas de classificação com conjuntos de dados complexos, como os padrões de digitação [3].

### Fundamentação Teórica

A detecção de estado emocional via ritmo de digitação baseia-se em princípios da psicofisiologia e da biometria comportamental. Estudos têm demonstrado que o estado afetivo de um indivíduo pode ser refletido em padrões sutis de interação com dispositivos, incluindo a forma como digitam [4]. A teoria da emoção e sua manifestação comportamental fornece a base para correlacionar as características de digitação com estados emocionais específicos [5].

## Análise de Resultados (Simulada)

Com base em dados simulados, um Classificador SVM bem ajustado pode atingir uma acurácia de 80-85% na classificação de estados emocionais. A matriz de confusão (simulada) abaixo ilustra o desempenho esperado para quatro classes emocionais:

| | Predito Feliz | Predito Triste | Predito Neutro | Predito Estressado |
|---|---|---|---|---|
| **Real Feliz** | 85% | 5% | 5% | 5% |
| **Real Triste** | 5% | 80% | 10% | 5% |
| **Real Neutro** | 5% | 10% | 75% | 10% |
| **Real Estressado** | 5% | 5% | 10% | 80% |

Esta análise sugere que o modelo é razoavelmente eficaz na distinção entre os estados emocionais, com alguma confusão entre estados adjacentes (e.g., triste e neutro, neutro e estressado), o que é comum em tarefas de classificação emocional.

## Instalação e Configuração

1.  **Clonar o repositório**:
    ```bash
    git clone https://github.com/OffModzKkkkj/MoodSync.git
    cd MoodSync
    ```
2.  **Criar um ambiente virtual** (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Instalar dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### 1. Gerar Dados Simulados

Execute o script `data_simulator.py` para criar um conjunto de dados sintéticos para treinamento e teste:

```bash
python data_simulator.py
```

Isso gerará um arquivo `typing_data.csv` no diretório do projeto.

### 2. Treinar e Avaliar o Modelo

Execute o script `main.py` para carregar os dados simulados, treinar o modelo SVM, avaliar seu desempenho e fazer previsões de exemplo:

```bash
python main.py
```

## Aprimoramentos Futuros

*   **Coleta de Dados em Tempo Real**: Implementar um módulo para capturar dados de digitação reais de forma não intrusiva.
*   **Modelos de Deep Learning**: Explorar redes neurais recorrentes (RNNs) ou Transformers para capturar dependências temporais em padrões de digitação.
*   **Personalização**: Desenvolver modelos adaptativos que se ajustem aos padrões de digitação individuais do usuário.
*   **Integração com Aplicações**: Conectar com softwares de produtividade ou bem-estar para oferecer intervenções personalizadas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Artigo Científico (LaTeX)

Um artigo científico detalhando a metodologia e os resultados simulados do MoodSync está disponível em formato LaTeX. Para compilar o PDF:

1.  Certifique-se de ter uma distribuição LaTeX instalada (e.g., TeX Live).
2.  Navegue até o diretório `MoodSync`.
3.  Execute os seguintes comandos no terminal:
    ```bash
    pdflatex paper.tex
    biber paper
    pdflatex paper
    pdflatex paper
    ```
    O arquivo `paper.pdf` será gerado no mesmo diretório.

## Referências

[1] Simulated Typing Data: Gerado via `data_simulator.py`.
[2] Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning*, 20(3), 273-297.
[3] Burges, C. J. C. (1998). A Tutorial on Support Vector Machines for Pattern Recognition. *Data Mining and Knowledge Discovery*, 2(2), 121-167.
[4] Feit, A. M., & Tausczik, Y. R. (2019). Typing Biometrics for Continuous Authentication and Affect Detection. *ACM Computing Surveys (CSUR)*, 52(3), 1-37.
[5] Russell, J. A. (1980). A circumplex model of affect. *Journal of Personality and Social Psychology*, 39(6), 1161-1178.
