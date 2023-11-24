def regla1(ipv6):
    # Regla 1: Eliminar ceros a la izquierda en cada bloque
    ipv6 = ":".join([block.lstrip("0") or "0" for block in ipv6.split(":")])
    return ipv6
