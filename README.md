# Verificador de Redirecionamento de URLs

Este programa verifica se URLs específicas estão redirecionando corretamente ou não. Ele é útil para garantir que os links estejam apontando para os destinos esperados, especialmente em grandes conjuntos de URLs como sitemaps.

## Instalação

Para utilizar o programa, siga os passos abaixo:

### 1. Clonar o repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Clonar o repositório

Certifique-se de ter o poetry instalado no seu sistema. Você pode instalar o poetry seguindo as instruções em python-poetry.org.

### 3. Criar e Ativar o Ambiente Virtual

Dentro do diretório do projeto, crie e ative um ambiente virtual utilizando poetry:

```bash
poetry install  # Instala as dependências do projeto
poetry shell    # Ativa o ambiente virtual
poetry add requests
poetry add pandas
```

### 4. Executar o Programa

```bash
cd redirect_links_sitemap
poetry run python nome_do_arquivo.py
```

Modifique o link do site que você quer verificar o sitemap no script: extract_url_sitemap.py