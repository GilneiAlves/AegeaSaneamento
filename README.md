# Case Power BI — Análise Operacional de Saneamento

## Objetivo

Este projeto tem como objetivo analisar dados operacionais de uma concessionária de saneamento utilizando **Power BI**, com foco em indicadores de eficiência operacional, perdas de água, reclamações de clientes e estimativa de faturamento por cidade.

O dashboard foi desenvolvido para apoiar **tomada de decisão gerencial**, identificando oportunidades de melhoria na operação e na qualidade do serviço prestado.

---

# Estrutura do Projeto

O projeto utiliza quatro bases de dados simuladas.

## Tabelas

### cidades

Tabela de dimensão contendo informações das cidades atendidas.

| coluna | descrição |
|------|-----------|
id_cidade | identificador da cidade |
cidade | nome da cidade |
estado | estado |
populacao | população estimada |

---

### clientes

Tabela contendo os tipos de clientes e tarifas praticadas.

| coluna | descrição |
|------|-----------|
id_cliente | identificador do cliente |
id_cidade | cidade do cliente |
tipo_cliente | residencial, comercial, industrial ou público |
tarifa_m3 | tarifa média por metro cúbico |

---

### consumo_agua

Tabela com os dados de distribuição e faturamento de água.

| coluna | descrição |
|------|-----------|
id_consumo | identificador da leitura |
id_cidade | cidade |
data | data da medição |
volume_distribuido_m3 | volume total distribuído |
volume_faturado_m3 | volume faturado |

---

### indicadores_operacionais

Tabela contendo indicadores operacionais da rede.

| coluna | descrição |
|------|-----------|
id_cidade | cidade |
data | período |
reclamacoes | número de reclamações registradas |
rompimentos_rede | número de rompimentos na rede |
tempo_medio_reparo_h | tempo médio de reparo em horas |

---

# Modelagem de Dados

O modelo segue o padrão **Star Schema**, onde a tabela `cidades` atua como dimensão principal.

Relacionamentos:

cidades (1) ──── consumo_agua (N)
cidades (1) ──── clientes (N)
cidades (1) ──── indicadores_operacionais (N)


Também foi criada uma **tabela calendário** para análise temporal.

---

# Perguntas de Negócio

O dashboard foi desenvolvido para responder às seguintes perguntas:

1. Qual cidade apresenta maior perda de água?
2. Qual a evolução mensal das perdas?
3. Qual cidade possui maior número de reclamações por 100 mil habitantes?
4. Existe relação entre rompimentos de rede e reclamações?
5. Qual o faturamento estimado por cidade?

---

# Métricas Utilizadas

## Perda de Água

```DAX
Perda de Água =
SUM(consumo_agua[volume_distribuido_m3]) -
SUM(consumo_agua[volume_faturado_m3])```

```
Percentual de Perda
```
Perc Perda =
DIVIDE(
    [Perda de Água],
    SUM(consumo_agua[volume_distribuido_m3])
)
```

Reclamações por 100 mil habitantes
```
Reclamacoes 100k =
DIVIDE(
    SUM(indicadores_operacionais[reclamacoes]),
    MAX(cidades[populacao])
) * 100000

```
Tarifa Média
```
Tarifa Média =
AVERAGE(clientes[tarifa_m3])

```
Faturamento Estimado
```
Faturamento Estimado =
SUM(consumo_agua[volume_faturado_m3]) *
[Tarifa Média]

```


# Principais Insights
Perdas de água

Foi possível identificar diferenças relevantes entre as cidades no percentual de perda, indicando possíveis problemas de infraestrutura ou medição.

# Relação entre rompimentos e reclamações

A análise mostrou uma correlação positiva entre rompimentos de rede e número de reclamações, sugerindo que falhas operacionais impactam diretamente a percepção do serviço pelos clientes.

# Indicadores normalizados por população

O indicador de reclamações por 100 mil habitantes permite comparação justa entre cidades com populações diferentes.

## Autor

**Gilnei Alves de Freitas**  
Analista de Dados Sênior  
🔗[LinkedIn](https://www.linkedin.com/in/gilnei-freitas/) | [Email](mailto:gilnei147@gmail.com)

---

## Licença

Este projeto é de uso demonstrativo para fins de portfólio e aprendizado. Os dados utilizados foram fictícios ou anonimizados.