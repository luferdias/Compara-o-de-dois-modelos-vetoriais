#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de PDF
==============

Este script gera um PDF contendo:
- Código-fonte do projeto
- Imagens geradas
- Documentação
"""

from fpdf import FPDF
import os
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Comparação de Modelos Vetoriais', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'Análise e Visualização de Representações Vetoriais', 0, 1, 'C')
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')
        
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(3)
        
    def chapter_body(self, body):
        self.set_font('Courier', '', 9)
        self.multi_cell(0, 4, body)
        self.ln()

print("=" * 70)
print("GERAÇÃO DE PDF")
print("=" * 70)

# Criar PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# ============================================================================
# PÁGINA 1: INTRODUÇÃO E DOCUMENTAÇÃO
# ============================================================================
pdf.add_page()

pdf.chapter_title("1. INTRODUCAO")
introducao = """
Este documento apresenta uma analise comparativa de dois modelos de 
representacao vetorial de texto:

1. Embeddings por Palavra (Word2Vec)
   - Gera vetores para palavras individuais
   - Captura relacoes semanticas entre palavras
   
2. Embeddings por Sentenca (Media de Word2Vec)
   - Gera vetores para sentencas completas
   - Calcula a media dos vetores das palavras da sentenca
   - Captura o significado geral da sentenca

Ambos os modelos sao reduzidos a 2 dimensoes usando PCA (Principal 
Component Analysis) para visualizacao.
"""
pdf.chapter_body(introducao)

pdf.chapter_title("2. FRAGMENTOS UTILIZADOS")

fragmentos_info = """
### Palavras (8 fragmentos):
  1. cachorro
  2. cao (semanticamente similar a "cachorro")
  3. feliz
  4. alegre (semanticamente similar a "feliz")
  5. computador
  6. livro
  7. arvore
  8. cidade

### Sentencas (8 fragmentos):
  S1: O cachorro esta brincando no parque.
  S2: O cao corre feliz no jardim. (similar a S1)
  S3: Estou muito feliz hoje.
  S4: Estou alegre e contente. (similar a S3)
  S5: O computador esta processando dados.
  S6: Estou lendo um livro interessante.
  S7: A arvore esta florida.
  S8: A cidade esta muito movimentada.

Nota: Ha pelo menos 2 pares de fragmentos semanticamente similares
em cada conjunto, conforme requisito.
"""
pdf.chapter_body(fragmentos_info)

pdf.chapter_title("3. PARAMETROS UTILIZADOS")

parametros = """
### Word2Vec (para palavras):
  - vector_size: 50 (dimensao dos vetores)
  - window: 3 (tamanho da janela de contexto)
  - min_count: 1 (frequencia minima da palavra)
  - epochs: 100 (numero de epocas de treinamento)
  - seed: 42 (semente para reprodutibilidade)

### Word2Vec (para sentencas):
  - vector_size: 100 (dimensao dos vetores)
  - window: 5 (tamanho da janela de contexto)
  - min_count: 1 (frequencia minima da palavra)
  - epochs: 200 (numero de epocas de treinamento)
  - seed: 42 (semente para reprodutibilidade)
  - Metodo: Media dos vetores das palavras da sentenca

### PCA (Principal Component Analysis):
  - n_components: 2 (reducao para 2D)
  - random_state: 42 (reprodutibilidade)
  
A PCA e aplicada para reduzir a alta dimensionalidade dos vetores
originais para 2 dimensoes, permitindo visualizacao em graficos 2D.
"""
pdf.chapter_body(parametros)

# ============================================================================
# PÁGINA 2: VISUALIZAÇÕES
# ============================================================================
pdf.add_page()

pdf.chapter_title("4. VISUALIZACOES")

# Adicionar imagem principal
if os.path.exists('visualizacao_vetores.png'):
    pdf.image('visualizacao_vetores.png', x=10, y=None, w=190)
    print("[OK] Imagem principal adicionada ao PDF")
else:
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 10, '[Imagem visualizacao_vetores.png não encontrada]', 0, 1, 'C')

# ============================================================================
# PÁGINA 3: LEGENDA DAS SENTENÇAS
# ============================================================================
pdf.add_page()

pdf.chapter_title("5. LEGENDA DAS SENTENCAS")

if os.path.exists('legenda_sentencas.png'):
    pdf.image('legenda_sentencas.png', x=10, y=None, w=190)
    print("[OK] Legenda adicionada ao PDF")
else:
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 10, '[Imagem legenda_sentencas.png não encontrada]', 0, 1, 'C')

# ============================================================================
# PÁGINAS 4+: CÓDIGO-FONTE
# ============================================================================
pdf.add_page()

pdf.chapter_title("6. CODIGO-FONTE")

pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5, "Abaixo está o código-fonte completo do projeto:")
pdf.ln(3)

# Ler e adicionar código-fonte
codigo_arquivos = [
    'comparacao_vetores.py',
    'gerar_pdf.py'
]

def sanitize_text(text):
    """Remove caracteres especiais que não são suportados por latin-1"""
    replacements = {
        'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a',
        'ẽ': 'e', 'é': 'e', 'è': 'e', 'ê': 'e',
        'ĩ': 'i', 'í': 'i', 'ì': 'i', 'î': 'i',
        'õ': 'o', 'ó': 'o', 'ò': 'o', 'ô': 'o',
        'ũ': 'u', 'ú': 'u', 'ù': 'u', 'û': 'u',
        'ç': 'c',
        'Ã': 'A', 'Á': 'A', 'À': 'A', 'Â': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E',
        'Í': 'I', 'Ì': 'I', 'Î': 'I',
        'Õ': 'O', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U',
        'Ç': 'C',
        '✓': '[OK]',
        '→': '->',
        '↔': '<->',
        '"': '"',
        '"': '"',
        ''': "'",
        ''': "'",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Remove outros caracteres não-ASCII
    text = text.encode('latin-1', errors='replace').decode('latin-1')
    return text

for arquivo in codigo_arquivos:
    if os.path.exists(arquivo):
        pdf.chapter_title(f"6.{codigo_arquivos.index(arquivo)+1}. {arquivo}")
        
        with open(arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        
        # Sanitize código
        codigo = sanitize_text(codigo)
            
        # Dividir código em linhas e adicionar com numeração
        linhas = codigo.split('\n')
        codigo_numerado = ""
        for i, linha in enumerate(linhas, 1):
            # Limitar linha se muito longa
            if len(linha) > 85:
                linha = linha[:85] + "..."
            codigo_numerado += f"{i:4d} | {linha}\n"
        
        pdf.chapter_body(codigo_numerado)
        print(f"[OK] Codigo de {arquivo} adicionado ao PDF")

# ============================================================================
# PÁGINA FINAL: INSTRUÇÕES DE EXECUÇÃO
# ============================================================================
pdf.add_page()

pdf.chapter_title("7. INSTRUCOES DE EXECUCAO")

instrucoes = """
### Pre-requisitos:
  - Python 3.7 ou superior
  - pip (gerenciador de pacotes Python)

### Instalacao:

1. Clone o repositorio ou baixe os arquivos

2. Instale as dependencias:
   $ pip install -r requirements.txt

3. Execute o script principal:
   $ python comparacao_vetores.py
   
   Este script ira:
   - Gerar embeddings para palavras e sentencas usando Word2Vec
   - Aplicar PCA para reducao dimensional
   - Criar visualizacoes (arquivos PNG)
   - Exibir analise de similaridade

4. Gere o PDF (opcional):
   $ python gerar_pdf.py
   
   Isso criara o arquivo 'relatorio_vetores.pdf'

### Arquivos gerados:
  - visualizacao_vetores.png: Graficos com projecoes PCA
  - legenda_sentencas.png: Legenda das sentencas
  - relatorio_vetores.pdf: Este documento

### Observacoes:
  - Nao requer conexao com internet (modelos treinados localmente)
  - Os resultados sao reproduziveis (seed fixada)
  - As imagens sao salvas em alta resolucao (300 DPI)
  - Execucao rapida (< 30 segundos)
"""
pdf.chapter_body(instrucoes)

pdf.chapter_title("8. CONCLUSAO")

conclusao = """
Este projeto demonstra a aplicacao de duas tecnicas de vetorizacao
de texto e sua visualizacao atraves de PCA:

- Word2Vec para palavras captura relacoes entre palavras individuais
- Word2Vec medio para sentencas captura o significado geral
- PCA permite visualizar os vetores em 2D
- Fragmentos semanticamente similares aparecem proximos no espaco

A analise mostra que ambos os metodos conseguem identificar 
similaridades semanticas, com palavras/sentencas similares 
agrupadas proximas no espaco vetorial reduzido.

O metodo de media de vetores para sentencas e uma abordagem simples
mas eficaz para gerar embeddings de sentencas quando modelos 
pre-treinados nao estao disponiveis.
"""
pdf.chapter_body(conclusao)

# ============================================================================
# SALVAR PDF
# ============================================================================
output_file = 'relatorio_vetores.pdf'
pdf.output(output_file)

print("\n" + "=" * 70)
print(f"[OK] PDF gerado com sucesso: {output_file}")
print("=" * 70)
print(f"\nTamanho do arquivo: {os.path.getsize(output_file) / 1024:.2f} KB")
print(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
