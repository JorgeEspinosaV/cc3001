def particionLomuto(a,p):
    # retorna el punto de corte, el número de elementos <p y la lista particionada
    n = len(a)
    (i, j) = (0, 0)
    while j <= (n-1):
        if a[j] > p:
            j += 1
        else:
            (a[i], a[j]) = (a[j], a[i])
            j += 1
            i += 1
    # escribir acá el algoritmo de partición de Lomuto
    
    return (p,i,a)

def verifica_particion(t): # imprime y chequea partición
    (p,m,a)=t
    # p=punto de corte, m=número de elementos <p, a=lista completa particionada
    print(a[0:m],p,a[m:])
    print("Partición OK" if (m==0 or max(a[0:m])<p) and (m==len(a) or min(a[m:])>p)
          else "Error")
    
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],50))
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],0))
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],100))
