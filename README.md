# Who-Is-Who
Juego de Who Is Who (¿Quién es quién?), creado en Python3 junto con Prolog.

El juego utiliza una base de datos escrita en Prolog. Mientras que, Python maneja la lógica del programa.

El jugador debe pensar un personaje de los disponibles en el juego del ¿Quién es Quién? y la máquina intentará adivinar su personaje en el menor número de intentos posibles.

## Tablero

Este es el tablero del juego del ¿Quién es Quién?:

![](docs/tablero.png)

## Propiedades del modelo

Según la siguiente tabla podemos determinar las propiedades de nuestro modelo:

![](docs/propiedades_modelo.png)

 | Observable | Axentes | Determinista | Episódico | Estático | Discreto | Coñecido
 | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 | Parcial | Único | Estocaistico | Episódico | Estático |  Discreto | Conocido |

 - Parcial: El agente no sabe el estado completo del entorno, sólo conoce el resultado al final cuando se revela la elección del jugador (tras responder el jugador a la pregunta de la máquina)
 - Único: El agente no compite ni coopera con ningún otro agente
 - Determinista: El agente puede tomar una decisión tras observar el estado del mundo
 - Episódico: El agente toma una decisión al empezar el turno
 - Estático: El entorno se mantiene costante mientras el agente está seleccionando una acción
 - Discreto: El entorno tiene una serie finita de estados en los que puede encontrarse
 - Conocido: El agente conoce las reglas para poder jugar al juego

## Estructura del agente

El agentes es un agente reactivo basado en modelos, ya que cuenta con un estado interno sobre las características y el número de los personajes restantes. Su estructura es la siguiente:

![](docs/estructura_agente.png)

