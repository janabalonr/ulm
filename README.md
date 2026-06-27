Pipeline Básico
Objetivo: conocer, reproducir e implementar técnicas existentes de Criptografía Neuronal Adversaria.

Etapa 1: Base conceptual

OK

Etapa 2: Implementación mínima Alice–Bob–Eve

Implementar en Python/PyTorch:

- mensajes binarios aleatorios
- llaves binarias aleatorias
- Alice: MLP o CNN pequeña
- Bob: MLP/CNN
- Eve: MLP/CNN
Nota: quizas ir por MLP y luego tirar por CNN sea ideal para aprender a modelar
- entrenamiento alternado
- entrenar Eve para atacar
- entrenar Alice+Bob para reconstruir y confundir a Eve.

- Comparar contra XOR/OTP simple.


Etapa 3: Reproducción de variantes conocidas

Implementar variantes:

- ANC básica tipo Google Brain (implementados en AdversarialTracrProject/src)
- ANC no determinista usando nonce
- CPA-ANC con ataque de texto plano elegido
- Autoencoder convolucional para comunicación segura
- Cifrado de imágenes simple con autoencoder.

Tu documento menciona variantes como CPA-ANC, CCA-ANES y el problema del determinismo cuando el mismo mensaje y llave generan siempre el mismo cifrado. Asi que conviene explorar algo de esto para ver como va, estamos en etapa exploratoria y de conocimiento.

Etapa 4: Benchmark a partir de los modelos generados

Comparar modelos con:

- BER Bob
- BER Eve
- entropía del ciphertext
- correlación mensaje–cifrado
- NIST SP800-22 (en caso de querer avanzar algo más)
- Tiempo de entrenamiento (ver en mayor profundidad temas de optimización si es necesario)
- tamaño del modelo (más profundidad)


Lo ideal es tener un repositorio con notebooks o bien con los scripts y TODOS los resultados con exportación de tablas, plots, etc, a latex.

- XOR/OTP baseline.
- Alice–Bob–Eve básico.
- ANC con nonce.
- ANC sobre imágenes pequeñas.
- Comparación de métricas.
>>>>>>> e9a556f (Se actualiza cryptography, redes_neuronales_2025 y xai, se elimina carpetas duplicadas.)
