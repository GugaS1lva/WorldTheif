# YouTube Video Downloader

Um projeto de automação em Python para baixar vídeos do YouTube com facilidade, usando a biblioteca `yt_dlp`.

## Propósito

Este projeto permite o download de vídeos do YouTube com diferentes resoluções, de forma rápida e eficiente. Ideal para quem deseja armazenar conteúdo offline diretamente do YouTube.

## Como Funciona

O script verifica o formato da URL e baixa o vídeo na melhor qualidade disponível. Ele é capaz de processar tanto URLs individuais quanto listas de vídeos.

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

No terminal ou prompt de comando, use o seguinte comando para instalar o `yt_dlp`:

```bash
pip install yt_dlp
```

### 3. Rodar o Projeto

Agora você pode executar o script para baixar vídeos:

1. Abra o terminal ou prompt de comando na pasta onde o script está localizado.
2. Insira a url do vídeo que deseja baixar diretamente no código, substituindo a url de exemplo na linha 25 pela url do seu video.
3. Execute o script com o comando:
   ```bash
   python YTTheif.py
   ```

### Exemplos de Uso

- **Baixar um vídeo individual**:
  - Altere a variável `urls` para uma URL específica.
- **Baixar múltiplos vídeos**:
  - Coloque uma lista de URLs em `urls` e o script baixará cada um dos vídeos automaticamente.

## Créditos

Desenvolvido por **Gustavo Antonio da Silva - [ Guga ☕ ]**. Para mais informações ou sujestões de melhorias, entre em contato pelo [Instagram @gugas1lva.dev](https://www.instagram.com/gugas1lva.dev/).
