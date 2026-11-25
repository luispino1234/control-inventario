
# Control de inventario

## Descripción
Programa desarrollado en Python para calcular la cantidad de unidades que se deben solicitar para que cada artículo alcance su stock mínimo requerido.

## Problema
Controlar las existencias de cinco artículos mediante una matriz que almacena el código, nombre, stock actual y stock mínimo.

## Funcionamiento
1. Define la matriz de inventario.
2. Recorre los artículos mediante un ciclo `for`.
3. Utiliza la función `calcular_reposicion()` para determinar las unidades necesarias.
4. Si el stock actual es inferior al mínimo, calcula la diferencia.
5. Si el stock actual es igual o superior al mínimo, devuelve cero.
6. Muestra el reporte de reabastecimiento.

## Estructuras de programación
- Lista bidimensional.
- Funciones.
- Condicional `if/else`.
- Ciclo `for`.
- Salida por consola.

## Ejecución
Requiere Python 3.

```bash
python "5.5 Control_Inventario.py"
```

## Resultados esperados

| Artículo | Cantidad a pedir |
|---|---:|
| Teclado | 7 |
| Mouse | 0 |
| Monitor | 5 |
| Impresora | 0 |
| Disco SSD | 8 |

## Datos académicos
- Actividad: Fase 5 – Evaluación final.
- Problema: 3 – Control de inventario.
- Curso: Fundamentos de Programación.
- Universidad: UNAD.
