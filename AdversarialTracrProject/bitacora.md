# Bitácora de cambios

## Actividades realizadas

- Crea módulo de Alice en PyTorch en `src/alice.py`.
- Ajustada la arquitectura para seguir la versión original de Abadi & Andersen (2016):
  - Entrada: concatenación mensaje + clave → vector `2N`.
  - Capa fully connected de tamaño `2N × 2N`.
  - Cuatro convoluciones 1D con ventanas y strides correspondientes a `[4,1,2]`, `[2,2,4]`, `[1,4,4]`, `[1,4,1]`.
  - Salida final de tamaño `N` con activación `tanh`.
- Corregido el `padding` en PyTorch para mantener la reducción de longitud intencional y evitar errores en capas con stride.
- Verificado que el script `src/alice.py` se ejecuta correctamente y produce salida de tamaño `[batch_size, N]`.

## Notas

- El repositorio Git detecta el directorio `AdversarialTracrProject` como un nuevo conjunto de archivos no rastreados.
- Este commit incluirá tanto el código actualizado como el archivo de bitácora.
