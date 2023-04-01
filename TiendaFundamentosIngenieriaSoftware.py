producto=["Manzana"]
precio=[10]
while True:
    try:
        a = int(input("Inicio dame uno de los siguientes valores \n1.usuario \n2.administrador\n3.salir\n"))
        if a==1:
            while True:
                auser=int(input("Producto \n1.Cotizar \n2.salir\n"))
                if auser==1:
                    for i in range(len(producto)):
                        print(i,":",producto[i]," su precio es: $",precio[i])
                    productoC=int(input("selecciona el producto que quieres comprar "))
                    dinero=int(input("Cuanto tienes para comprar por el producto? "))
                    alcanza=dinero/precio[productoC]
                    for i in range(int(alcanza)):
                        print(producto[productoC],"x",alcanza)
                if auser==2:
                    print("Menu principal")
                    break
                if auser>2:
                    print("Dame un valor valido")
        if a==2:
            while True:
                contraseña=int(input("Escribe la contraseña para entrar en administracion"))
                if contraseña==1:
                    while True:
                        admin = int(input("Producto \n1.Nuevo \n2.Modificar \n3.Salir \n"))
                        if admin == 1:
                            newproducto=input("Dame el nuevo producto: \n")
                            newprecio=int(input("Dame el nuevo precio \n"))
                            producto.append(newproducto)
                            precio.append(newprecio)
                            print("Se guardo")
                            for i in range(len(producto)):
                                print(i,":",producto[i]," su precio es: ",precio[i])
                        if admin == 2:
                            for i in range(len(producto)):
                                print(i,":",producto[i]," su precio es: ",precio[i])
                            productoM=int(input("Que producto deseas modificar"))
                            modproducto=input("Dame el nuevo nombre del producto")
                            modprecio=int(input("Dame el nuevo precio"))
                            precio[productoM]=modprecio
                            producto[productoM]=modproducto
                            for i in range(len(producto)):
                                print(i,":",producto[i]," su precio es: ",precio[i])
                        if admin == 3:
                            print("Menu principal")
                            break
                        if admin > 3:
                            print("Dame un valor valido")
                if contraseña!=1:
                    print("Contraseña incorrecta, volviendo al menu principal")
                    break
        if a==3:
            print("salir")
            break
        if a>3:
            print("Selecciona otra opcion")
    except ValueError:
        print("Eso no es un numero")
