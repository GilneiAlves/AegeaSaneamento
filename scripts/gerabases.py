# Generate synthetic datasets for the Power BI case and save as CSV with ';' separator
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# ---------- Cities ----------
states = ["SP","RJ","MG","PR","SC","RS","MT","GO","BA","PE"]
city_names = [
    "Campinas","Ribeirão Preto","Londrina","Cuiabá","Sorocaba","Uberlândia","Joinville","Caxias do Sul",
    "Anápolis","Feira de Santana","Santos","Maringá","Blumenau","Pelotas","Várzea Grande","Aparecida de Goiânia",
    "Juiz de Fora","Ponta Grossa","Itajaí","Caruaru"
]

cities = []
for i, name in enumerate(city_names, start=1):
    cities.append({
        "id_cidade": i,
        "cidade": name,
        "estado": random.choice(states),
        "populacao": random.randint(120000, 1500000)
    })

df_cidades = pd.DataFrame(cities)

# ---------- Clients ----------
tipos = ["Residencial","Comercial","Industrial","Publico"]
clientes = []
client_id = 1

for city_id in df_cidades["id_cidade"]:
    n = random.randint(60, 140)
    for _ in range(n):
        tipo = random.choice(tipos)
        tarifa = {
            "Residencial": round(random.uniform(3.8,5.2),2),
            "Comercial": round(random.uniform(5.0,7.5),2),
            "Industrial": round(random.uniform(7.0,10.0),2),
            "Publico": round(random.uniform(4.0,6.0),2)
        }[tipo]

        clientes.append({
            "id_cliente": client_id,
            "id_cidade": city_id,
            "tipo_cliente": tipo,
            "tarifa_m3": tarifa
        })
        client_id += 1

df_clientes = pd.DataFrame(clientes)

# ---------- Water Consumption (daily for 2 years) ----------
start = datetime(2023,1,1)
end = datetime(2024,12,31)
days = (end-start).days + 1

consumo = []
consumo_id = 1

for city_id in df_cidades["id_cidade"]:
    base = random.randint(20000,90000)
    for d in range(days):
        date = start + timedelta(days=d)
        distribuido = base + np.random.normal(0, base*0.08)
        perda = np.random.uniform(0.15,0.35)
        faturado = distribuido*(1-perda)

        consumo.append({
            "id_consumo": consumo_id,
            "id_cidade": city_id,
            "data": date.strftime("%Y-%m-%d"),
            "volume_distribuido_m3": round(distribuido,2),
            "volume_faturado_m3": round(faturado,2)
        })
        consumo_id += 1

df_consumo = pd.DataFrame(consumo)

# ---------- Operational Indicators (monthly) ----------
dates_month = pd.date_range("2023-01-01","2024-12-01",freq="MS")

indicadores = []

for city_id in df_cidades["id_cidade"]:
    for d in dates_month:
        indicadores.append({
            "id_cidade": city_id,
            "data": d.strftime("%Y-%m"),
            "reclamacoes": random.randint(20,250),
            "rompimentos_rede": random.randint(5,80),
            "tempo_medio_reparo_h": round(random.uniform(2.5,8.5),2)
        })

df_indicadores = pd.DataFrame(indicadores)

# ---------- Save CSVs ----------
path_base = "/mnt/data/"

files = {
    "cidades.csv": df_cidades,
    "clientes.csv": df_clientes,
    "consumo_agua.csv": df_consumo,
    "indicadores_operacionais.csv": df_indicadores
}

paths = {}

for name, df in files.items():
    path = path_base + name
    df.to_csv(path, sep=";", index=False)
    paths[name] = path

paths
