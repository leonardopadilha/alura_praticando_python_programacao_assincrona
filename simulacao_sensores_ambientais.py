"""
Lucas está desenvolvendo um sistema de monitoramento ambiental. Para isso, ele precisa criar sensores assíncronos que coletam dados periodicamente, sem que o programa fique travado esperando por cada um.

O sistema deve ter três sensores, que coletam e exibem dados em intervalos diferentes:

Sensor de temperatura: Atualiza os dados a cada 2 segundos.
Sensor de umidade: Atualiza os dados a cada 3 segundos.
Sensor de qualidade do ar: Atualiza os dados a cada 5 segundos.
O sistema nunca deve parar de rodar, exibindo os valores atualizados de cada sensor assim que novos dados estiverem disponíveis.

Dica: Utilize uma corrotinas para resolver este problema e use o método random.choice para definir a temperatura e qualidade do ar.

Saída esperada:

[2s] Temperatura: 22°C
[3s] Umidade: 60%
[4s] Temperatura: 23°C
[5s] Qualidade do ar: Boa
[6s] Umidade: 58%
[8s] Temperatura: 21°C
[10s] Qualidade do ar: Regular
...
"""

import asyncio
import random

async def sensor_temperatura():
  while True:
    await asyncio.sleep(2)
    temp = random.randint(20, 30)
    print(f"[{2}s] Temperatura: {temp}ºC")

async def sensor_umidade():
  while True:
    await asyncio.sleep(3)
    umidade = random.randint(50, 70)
    print(f"[{3}s] Umidade: {umidade}%")

async def sensor_qualidade_ar():
  while True:
    await asyncio.sleep(5)
    qualidade = random.choice(["Boa", "Regular", "Ruim"])
    print(f"[{5}s Qualidade do ar: {qualidade}]")

async def main():
  await asyncio.gather(sensor_temperatura(), sensor_umidade(), sensor_qualidade_ar())

asyncio.run(main())