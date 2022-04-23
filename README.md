# Interface gráfica de controle de guindaste

## Como executar

Faça a instalação do [poetry](https://python-poetry.org/docs/#installation). Essa instalação pode se diferenciar para cada sistema operacional.
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Depois da instalação, entre dentro do repositório e execute para configurar o ambiente dentro do projeto.
```bash
poetry config --local virtualenvs.in-project true
```
E posteriormente execute o seguinte comando para instalar o ambiente. Isso somente será necessário uma única vez.

```bash
poetry install
```
Com o ambiente e suas dependências instaladas execute o seguinte comando para entrar no ambiente.
```bash
poetry shell
```
Dessa forma, sempre que for necessário entrar no ambiente, é só executar o `poetry shell` novamente.
