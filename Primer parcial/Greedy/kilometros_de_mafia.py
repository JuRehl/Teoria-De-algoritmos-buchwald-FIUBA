def asignar_mafias(pedidos):
    pedidosOrd = sorted(pedidos, key=lambda x: x[1])  # ordena por km fin
    result = []
    for pedido in pedidosOrd:
        if len(result) == 0 or result[-1][1] < pedido[0]:
            result.append(pedido)
    return result