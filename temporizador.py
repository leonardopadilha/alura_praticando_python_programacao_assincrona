# Crie um programa que aguarde 3 segundos antes de exibir a mensagem final

# Saída esperada:
# Iniciando temporizador...
# Tempo finalizado após 3 segundos

import asyncio

async def temporizador():
  print("Iniciando temporizador...")
  await asyncio.sleep(3)
  print("Tempo finalizado após 3 segundos")


asyncio.run(temporizador())