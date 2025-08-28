"""
Marcos é dono de uma loja online e precisa de um sistema que processe pedidos de forma assíncrona. O sistema deve seguir a
seguinte lógica:
- Primeiro, verificar se o pagamento foi aprovado;
- Se o pagamento for aprovado, verificar se há estoque disponível;
- Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
- Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.

A lista de pedidos já está definida no sistema, com o status do pagamento e do estoque previamente cadastrados. Confirma o
código:
pedidos = [
  {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
  {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
  {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
  {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
  {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False}
]

O programa deve simular essa lógica para três pedidos, exibindo mensagens conforme o processamento ocorre.

Saída esperada:
Processando pedido #101.
Pagamento aprovado para pedido #101.
Estoque disponível para pedido #101.
Pedido #101 confirmado! Enviado pra entrega

Processando pedido #102.
Pagamento aprovado para pedido #102.
Estoque indisponível para pedido #102. Pedido cancelado.

Processando pedido #103.
Pagamento recusado para pedido #103. Pedido cancelado.

Todos os pedidos foram processados!
"""

import asyncio

pedidos = [
  {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
  {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
  {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
  {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
  {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False}
]

async def verificar_pagamentos(pedido):
  await asyncio.sleep(1)
  if pedido["pagamento_aprovado"]:
    print(f"Pagamento aprovado para o pedido #{pedido['id']}.\n")
    return True
  else:
    print(f"Pagamento recusado para o pedido #{pedido['id']}. Pedido cancelado\n")
    return False

async def verificar_estoque(pedido):
  await asyncio.sleep(1)
  if pedido["estoque_disponivel"]:
    print(f"Estoque disponível para o pedido #{pedido['id']}.\n")
    return True
  else:
    print(f"Estoque indisponível para o pedido #{pedido['id']}. Pedido cancelado.\n")
    return False

async def processar_pedido(pedido):
  print(f"Processando pedido #{pedido['id']}...\n")

  pagamento_ok = await verificar_pagamentos(pedido)
  if not pagamento_ok:
    return
  
  estoque_ok = await verificar_estoque(pedido)
  if not estoque_ok:
    return

  print(f"Pedido #{pedido['id']} confirmado! Enviado pra entrega.\n")


async def main():
  for pedido in pedidos:
    await processar_pedido(pedido)

  print("\nTodos os pedidos foram processados!\n")

asyncio.run(main())