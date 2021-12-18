# ead_python_alura_tdd

> Projeto referente a [este](https://cursos.alura.com.br/course/tdd-com-python) curso.

## Inicialização

- Crie o ambiente

```sh
docker-compose up -d
```
> ``docker-compose ps`` ``docker-compose down``

## Execução

```sh
docker-compose exec app pytest -q --tb=line
#docker-compose exec app pytest -q --tb=line tests/test_leilao.py
#docker-compose exec app pytest -q --tb=line tests/test_usuario.py
```

> Também é possível acessar o container através de ``docker-compose exec app bash``
