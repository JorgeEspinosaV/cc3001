## Ejercicio 3 [ Jorge Espinosa V ]

Para el método de Stooge Sort tenemos la ecuación que modela el tiempo de ejecución:

$$
T(n) = 3\cdot T\left(\dfrac{2n}{3}\right) + 1
$$

Donde el primer término $3\cdot T\left(\dfrac{2n}{3}\right)$ corresponde a la llamada recursiva de ordenar los primeros $\dfrac{2}{3}$, luego los ultimos $\dfrac{2}{3}$ para luego "finalizar" con los primeros $\dfrac{2}{3}$ de la lista, es decir,
 $$T(n) = T\left(\dfrac{2n}{3}\right) + T\left(\dfrac{2n}{3}\right)+T\left(\dfrac{2n}{3}\right)$$

Hay que recordar el paso inicial, si el primer elemento del array se compara con el último elemento del array por ende se le suma $+1$ por este paso adicional.

Para obtener la solución de $T(n)$ se utiliza el teo maestro, ya que, $T(n)$ es de la forma:

$$
T(n) = a\cdot T\left(\dfrac{n}{b}\right) + f(n)
$$

con $f(n) = O(n^c) = kn^c$, donde $a=3$, $b=\dfrac{3}{2}$ y $f(n) = 1$
obteniendo como solución:

 
$$
T(n) = O\left(n^{\log_{\frac{3}{2}}{3}}\right)
$$

Obtenemos esa solución ya que $a > b^c = 3 > 1$.



