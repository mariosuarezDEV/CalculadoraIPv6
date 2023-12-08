def regla1(ipv6):
    # Regla 1: Eliminar ceros a la izquierda en cada bloque
    ipv6 = ":".join([block.lstrip("0") or "0" for block in ipv6.split(":")])
    return ipv6

def regla2(direccion_ipv6):
    bloques = direccion_ipv6.split(':')  # Dividir la dirección en bloques
    direccion_simplificada = []
    segmentos = 0

    for bloque in bloques:
        if bloque == '0000':
            segmentos += 1
        else:#prueba
            direccion_simplificada.append(bloque)  # Agregar bloque a la dirección simplificada
            if segmentos > 0:
                direccion_simplificada.append('')  # Agregar "::" si hay segmentos de ceros antes
                segmentos = 0

    direccion_simplificada = ':'.join(direccion_simplificada)  # Unir los bloques nuevamente

    return direccion_simplificada

def regla3(ipv6):
    resultado = regla1(ipv6), regla2(ipv6)
    return resultado