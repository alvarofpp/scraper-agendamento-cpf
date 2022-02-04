# Scraper para agendamento de CPF

Para fazer a segunda via do CPF é necessário fazer um agendamento pelo site do
[ITEP-RN][itep-rn], sendo que as vagas são poucas e normalmente acabam rápido.
Como não divulgam (ou eu pelo menos não encontrei) o horário que liberam o agendamento,
decidi criar um scraper para ficar coletando dados da página de agendamento a fim de conseguir
identificar o melhor dia e horário da semana para tentar uma vaga.

## Executar o scraper

Para facilitar a manipulação do scraper, criei alguns comandos via `make`.

### Build

Constrói a imagem do scraper:

```shell
make build
```

Constrói a imagem do scraper sem utilizar o _cache_:

```shell
make build-no-cache
```

### Up

Executa o scraper:

```shell
make up
```

Executa o scraper em _background_:

```shell
make up-silent
```

### Down

```shell
make build
```

### Logs

Visualizar os logs do container. Esse comando só é útil quando você executa o scraper
em _background_:

```shell
make logs
```

[itep-rn]: https://www3.itep.rn.gov.br/agendamento/Agendamento
