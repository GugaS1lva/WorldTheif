# WorldTheif - Baixador de Vídeos

Um projeto de automação em Python para baixar vídeos do YouTube e Instagram com facilidade, usando a biblioteca yt_dlp.

## Propósito

Este projeto permite o download de vídeos de duas das plataformas mais populares: YouTube e Instagram. Ele oferece uma maneira rápida e eficiente de armazenar conteúdo offline com o uso de scripts especializados para cada plataforma.

## Como Funciona

Cada script verifica a URL e baixa o vídeo na melhor qualidade disponível e coloca tudo dentro da pasta Files que está na raiz do projeto. Os scripts são separados para facilitar o uso específico para cada plataforma:
- **YTTheif.py**: Script para baixar vídeos do YouTube.
- **IGTheif.py**: Script para baixar vídeos do Instagram.

## Instalação

Siga as instruções abaixo para instalar o Python e as bibliotecas necessárias para rodar este projeto.

### 1. Instalar o Python

Primeiro, você precisa ter o Python instalado. Para isso:

1. Baixe o instalador do Python [neste link](https://www.python.org/downloads/).
2. Durante a instalação, **marque a opção "Add Python to PATH"**.
3. Conclua a instalação e, em seguida, verifique a instalação no terminal:
   ```bash
   python --version
   ```
   Você deverá ver a versão do Python instalada.

### 2. Instalar Bibliotecas Necessárias

Para manter sua instalação organizada e evitar conflitos com instalações globais, é altamente recomendado o uso de um ambiente virtual. Siga as instruções abaixo para configurar o ambiente e instalar a biblioteca necessária:

#### a) Criação e Ativação do Ambiente Virtual

1. Abra o terminal ou prompt de comando na raiz deste repositório.
2. Crie um ambiente virtual executando:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual (se funcionar, você verá escrito no seu terminal `(venv)`):
   - **Windows:**
     ```bash
     source venv/Scripts/activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

#### b) Instalação do yt-dlp no Ambiente Virtual

Com o ambiente virtual ativado, instale a biblioteca utilizando o comando:
```bash
python -m pip install yt-dlp
```

### 3. Rodar o Projeto

#### Baixar vídeos do YouTube

1. Abra o terminal ou prompt de comando na pasta onde o script `YTTheif.py` está localizado.
2. Insira a URL do vídeo do YouTube que deseja baixar diretamente no código, substituindo a URL de exemplo na linha 25 pela URL do seu vídeo.
3. Execute o script com o comando:
   ```bash
   python YTTheif.py
   ```

#### Baixar vídeos do Instagram

1. Abra o terminal ou prompt de comando na pasta onde o script `IGTheif.py` está localizado.
2. Insira a URL do vídeo do Instagram (como reels) que deseja baixar diretamente no código, substituindo a URL de exemplo na linha 25 pela URL do seu vídeo.
3. Execute o script com o comando:
   ```bash
   python IGTheif.py
   ```

### Exemplos de Uso

- **Baixar um vídeo individual (YouTube ou Instagram)**:
  - Para baixar um único vídeo, altere a variável `urls` para a URL específica do vídeo que deseja baixar.
- **Baixar múltiplos vídeos (YouTube ou Instagram)**:
  - Insira uma lista de URLs na variável `urls` e o script baixará cada um dos vídeos automaticamente.

## Créditos

Desenvolvido por **Gustavo Antonio da Silva - [Guga :coffee:]**. Para mais informações ou sugestões de melhorias, entre em contato pelo [Instagram @gugas1lva.dev](https://www.instagram.com/gugas1lva.dev/).
