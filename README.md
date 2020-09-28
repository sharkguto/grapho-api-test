# grapho-api-test

Api em python async exemplificando uso de grafos - Exercicio

## Stack

- fastapi
- networkx
- docker
- pytest-cov
- python 3.8

## Dependencias

```bash
sudo python3 -m pip install -r requirements.txt --upgrade
```

## Diagrama do grafo

![grapho1](docs/img/grapho.png)

## Variaveis de ambiente

```bash
SWAGGER_DOCS=1 # deixa ativado a interface de swagger na api
```

## Executar

```bash
docker-compose up --build
```

## Pagina de acesso da api

swagger : `http://0.0.0.0:8080/docs`

## Testes

Executar com pytest, conforme comando abaixo:

```bash
pytest --cov=graphox tests/ --cov-fail-under=70 --disable-pytest-warnings
```

## benchmark

- debug-mode

  ```bash
  wrk -c 400 -t 1 -d 30 http://localhost:8080/v1/friends --latency
  Running 30s test @ http://localhost:8080/v1/friends
  1 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
      Latency   439.72ms   51.11ms 558.76ms   61.24%
      Req/Sec     0.91k   278.58     2.17k    79.86%
  Latency Distribution
      50%  423.53ms
      75%  486.10ms
      90%  518.43ms
      99%  545.27ms
  27065 requests in 30.06s, 5.49MB read
  Requests/sec:    900.26
  Transfer/sec:    187.00KB

  ```

- docker - gunicorn  - production mode

  ```bash
  wrk -c 400 -t 1 -d 30 http://localhost:8080/v1/friends --latency
  Running 30s test @ http://localhost:8080/v1/friends
  1 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
      Latency    44.07ms   12.04ms 207.82ms   70.37%
      Req/Sec     9.13k     0.98k   11.01k    79.33%
  Latency Distribution
      50%   42.68ms
      75%   51.01ms
      90%   56.08ms
      99%   75.75ms
  272586 requests in 30.05s, 55.56MB read
  Requests/sec:   9070.80
  Transfer/sec:      1.85MB
  ```
