import tkinter as tk

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


def simplify_ipv6():
    ipv6_address = ipv6_entry.get()
    rule_choice = rule_var.get()

    if rule_choice in [1, 2]:
        if rule_choice == 1:
            result = regla1(ipv6_address)
        else:
            result = regla2(ipv6_address)
    elif rule_choice == 3:
        result = regla2(regla1(ipv6_address))
    else:
        result = "Elección inválida de regla"

    result_label.config(text="Resultado: " + result)

# Crear la ventana principal
window = tk.Tk()
window.title("Simplificación IPv6")

# Label para ingresar la dirección IPv6
ipv6_label = tk.Label(window, text="Dirección IPv6:")
ipv6_label.pack()

ipv6_entry = tk.Entry(window)
ipv6_entry.pack()

# Botones de selección de regla
rule_var = tk.IntVar()

rule1_button = tk.Radiobutton(window, text="Regla 1", variable=rule_var, value=1)
rule1_button.pack(side=tk.LEFT)

rule2_button = tk.Radiobutton(window, text="Regla 2", variable=rule_var, value=2)
rule2_button.pack(side=tk.LEFT)

both_rules_button = tk.Radiobutton(window, text="Ambas Reglas", variable=rule_var, value=3)
both_rules_button.pack(side=tk.LEFT)

# Botón para simplificar la dirección IPv6
simplify_button = tk.Button(window, text="Simplificar", command=simplify_ipv6)
simplify_button.pack()

# Label para mostrar el resultado
result_label = tk.Label(window, text="Resultado:")
result_label.pack()

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()
