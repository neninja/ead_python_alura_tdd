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

## Anotações

- https://dzone.com/articles/7-popular-unit-test-naming
- https://github.com/spotify/should-up
- **Lei de Demeter**/**Princípio do menor conhecimento** diz que devemos ter o menor conhecimento sobre a implementação da classe. Dessa forma, evitamos o acoplamento entre as classes do sistema. 
