# Comparação de Modelos Vetoriais

Este projeto compara dois métodos de representação vetorial de texto em português:
- **Embeddings por Palavra** (Word2Vec)
- **Embeddings por Sentença** (Média de Word2Vec)

## 📋 Descrição

O projeto gera representações vetoriais de fragmentos de texto, aplica PCA (Principal Component Analysis) para redução de dimensionalidade e visualiza os resultados em gráficos 2D. 

### Características

✓ 8 fragmentos de texto (palavras e sentenças)  
✓ Pelo menos 2 pares semanticamente similares em cada modelo  
✓ Aplicação de PCA para visualização  
✓ Geração automática de PDF com código e imagens  
✓ Análise de similaridade entre fragmentos  

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luferdias/Compara-o-de-dois-modelos-vetoriais.git
cd Compara-o-de-dois-modelos-vetoriais
```

2. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

**Nota:** A primeira execução pode demorar alguns minutos devido ao download do modelo Sentence-BERT (~120MB).

## 🎯 Uso

### Execução Básica

1. Execute o script principal:
```bash
python comparacao_vetores.py
```

Este script irá:
- Gerar embeddings para 8 palavras usando Word2Vec
- Gerar embeddings para 8 sentenças usando média de Word2Vec
- Aplicar PCA para reduzir dimensionalidade para 2D
- Criar visualizações (arquivos PNG)
- Exibir análise de similaridade no console

2. Gere o PDF com os resultados:
```bash
python gerar_pdf.py
```

### Arquivos Gerados

- `visualizacao_vetores.png` - Gráfico comparativo dos dois modelos
- `legenda_sentencas.png` - Legenda das sentenças utilizadas
- `relatorio_vetores.pdf` - Relatório completo com código, imagens e documentação

## 📊 Fragmentos Utilizados

### Palavras (8 fragmentos)

1. **cachorro** - Animal doméstico
2. **cão** - Sinônimo de cachorro *(semanticamente similar)*
3. **feliz** - Emoção positiva
4. **alegre** - Sinônimo de feliz *(semanticamente similar)*
5. **computador** - Tecnologia
6. **livro** - Objeto educacional
7. **árvore** - Natureza
8. **cidade** - Local urbano

### Sentenças (8 fragmentos)

1. "O cachorro está brincando no parque."
2. "O cão corre feliz no jardim." *(similar à S1)*
3. "Estou muito feliz hoje."
4. "Estou alegre e contente." *(similar à S3)*
5. "O computador está processando dados."
6. "Estou lendo um livro interessante."
7. "A árvore está florida."
8. "A cidade está muito movimentada."

## ⚙️ Parâmetros PCA

### Para Embeddings de Palavras
- **n_components**: 2 (redução para 2D)
- **random_state**: 42 (reprodutibilidade)

### Para Embeddings de Sentenças
- **n_components**: 2 (redução para 2D)
- **random_state**: 42 (reprodutibilidade)

## 📈 Interpretação dos Resultados

### Word2Vec (Embeddings por Palavra)
- Visualiza palavras como pontos no espaço 2D
- Palavras semanticamente similares aparecem próximas
- Exemplo: "cachorro" e "cão" ficam próximos

### Média de Word2Vec (Embeddings por Sentença)
- Visualiza sentenças como pontos no espaço 2D
- Sentenças com significados similares aparecem próximas
- Exemplo: Sentenças sobre cachorros/cães ficam próximas
- Método: Calcula a média dos vetores de todas as palavras da sentença

### Legendas nos Gráficos
- **Gráfico de Palavras**: Labels diretos com as palavras
- **Gráfico de Sentenças**: Labels S1-S8 (ver legenda separada)

## 🔧 Tecnologias Utilizadas

- **NumPy** - Computação numérica
- **Matplotlib** - Visualização de dados
- **scikit-learn** - PCA e análise de similaridade
- **Gensim** - Word2Vec
- **FPDF** - Geração de PDF
- **Pillow** - Processamento de imagens

## 📄 Estrutura do Projeto

```
.
├── README.md                    # Este arquivo
├── requirements.txt             # Dependências Python
├── comparacao_vetores.py        # Script principal
├── gerar_pdf.py                 # Gerador de PDF
├── visualizacao_vetores.png     # Gráficos gerados (após execução)
├── legenda_sentencas.png        # Legenda (após execução)
└── relatorio_vetores.pdf        # Relatório final (após execução)
```

## 🎓 Conceitos

### Word2Vec
Técnica de aprendizado de máquina que converte palavras em vetores numéricos. Palavras com contextos similares têm vetores próximos.

### Embeddings de Sentença (Média de Word2Vec)
Método que gera um vetor para uma sentença calculando a média dos vetores de todas as suas palavras. Abordagem simples mas eficaz para capturar o significado geral da sentença.

### PCA (Principal Component Analysis)
Técnica de redução de dimensionalidade que projeta dados de alta dimensão em um espaço de menor dimensão, preservando a maior parte da variância.

## 📝 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

## 👥 Autor

Luis Fernando Dias (luferdias)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.