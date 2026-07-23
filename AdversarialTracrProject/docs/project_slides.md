---
title: "Interpretabilidad Guiada por Ground-Truth Compilado"
subtitle: "Diagnóstico de un Cuello de Botella de Capacidad en Criptografía Neuronal Adversarial"
author: "Juan Rodrigo Anabalón Riquelme, Juan B. Cabral"
bibliography: referencias.bib
header-includes:
  - \usepackage{booktabs}

---

# El problema

- Abadi \& Andersen (2016) entrenan tres redes adversarialmente —Alice, Bob, Eve— para que emerja un cifrado end-to-end, sin prescribir ningún algoritmo criptográfico.
- El cifrado que emerge en los pesos de Alice **no es legible directamente**: en la formulación original ni siquiera es un XOR limpio.
- Agregamos un término auxiliar que empuja explícitamente a Alice hacia XOR bit a bit, para tener una referencia con semántica conocida.
- Pregunta abierta: ¿cómo verificar, más allá de una métrica agregada, si la red realmente implementó la operación esperada?

[@abadi2016learning]

---

# Pregunta de investigación

\begin{center}
\Large
¿El vocabulario de variables de un modelo compilado con Tracr puede usarse como generador de hipótesis para sondear una red adversarial opaca, revelando algo que las métricas agregadas no muestran?
\end{center}

\vspace{1em}

Encontramos que **sí**: el sondeo revela una heterogeneidad de convergencia por posición, invisible en la métrica agregada, y permite diagnosticar mecánicamente su causa.

---

# Contribuciones

- Metodología de **sondeo lineal por posición**, usando como target las variables categóricas de un programa RASP compilado con Tracr, aplicada a la capa oculta de Alice.
- Identificación de una **heterogeneidad no uniforme** en la convergencia de Alice hacia XOR, y su explicación mecánica en términos de la norma de los pesos de salida.
- Una **ablación controlada** que aísla el efecto del balance de la función de pérdida ($\alpha$, $\beta$) del efecto de la capacidad de la capa oculta.

---

# Esquema ANC (Alice, Bob, Eve)

- Alice y Bob son un MLP de una sola capa oculta (a diferencia del "mix \& transform" convolucional original) — deliberado, porque esa capa oculta es el objeto de estudio.
- Alice: concatena mensaje + clave ($2N$ bits) $\to$ capa oculta ReLU (\texttt{hidden\_size}) $\to$ cifrado sigmoide ($N$ bits).
- Bob: cifrado + clave $\to$ mensaje reconstruido. Eve: solo cifrado, sin clave.

\begin{equation*}
  \mathcal{L}_{\text{Alice}} = \mathcal{L}_{\text{Bob}} - \alpha\,\mathcal{L}_{\text{Eve}} + \beta\,\mathcal{L}_{\text{XOR}}
\end{equation*}

$\mathcal{L}_{\text{XOR}}$ es el término —ausente en el esquema original— que fija un blanco conocido contra el cual comparar.

---

# Modelo de referencia compilado con Tracr

- Cifrado XOR escrito como programa **RASP**: mensaje en posiciones $[0,N)$, clave en $[N,2N)$.
- \texttt{Select}/\texttt{Aggregate} sobre índices de posición trae el bit de clave a la posición del mensaje; un \texttt{SequenceMap} calcula el XOR.
- Compilado con \texttt{tracr}: transformer mínimo (1 capa, 1 cabeza), con residual stream de variables **categóricas etiquetadas**.
- Dos etiquetas son el vocabulario usado como hipótesis: \texttt{aggregate\_2} (bit de clave alineado) y \texttt{sequence\_map\_1} (bit XOR de salida).

[@lindner2023tracr; @weiss2021thinking]

---

# Sondeo lineal guiado por el vocabulario de Tracr

Para cada posición de salida $i$, ¿está el bit XOR de esa posición codificado linealmente en la capa oculta de Alice?

- **\texttt{input}** (control): mensaje + clave crudos. XOR no es linealmente separable en esas dos variables — cota inferior teórica.
- **\texttt{hidden}**: activaciones post-ReLU de \texttt{fc1} de Alice, análogo funcional del residual stream de Tracr.

Sonda = regresión logística (\texttt{nn.Linear} + \texttt{BCEWithLogitsLoss}), 4096 ejemplos de entrenamiento, 1024 held-out.

[@alain2016understanding; @minsky1969perceptrons]

---

# Resultado 1: heterogeneidad invisible en la métrica agregada

Con $N{=}8$, $\alpha{=}1.0$, $\beta{=}0.5$, 22\,000 pasos: \texttt{xor\_match} agregado $\approx 0.83$, nunca llega a 1.0.

\footnotesize
\begin{center}
\begin{tabular}{lcccccccc}
\toprule
Posición & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\midrule
\texttt{input} (control) & 0.501 & 0.485 & 0.467 & 0.529 & 0.479 & 0.521 & 0.503 & 0.515 \\
\texttt{hidden} (Alice)  & 1.000 & 0.500 & 0.521 & 1.000 & 0.634 & 1.000 & 1.000 & 1.000 \\
\bottomrule
\end{tabular}
\end{center}
\normalsize

5 de 8 posiciones son perfectamente legibles, 2 quedan al azar, 1 intermedia — consistente aritméticamente con $0.83 \approx (5{\times}1.0 + 3{\times}0.5)/8$.

---

# Resultado 2: el colapso se explica por la norma de los pesos

- 5 semillas, 40 pares (norma de fila de \texttt{fc2.weight}, \texttt{xor\_match} por posición).
- Correlación de Pearson: $r = 0.97$.
- Bajo el umbral de norma $4.0$: \texttt{xor\_match} entre $0.481$ y $0.872$ (media $0.559$).
- Sobre el umbral: \texttt{xor\_match} entre $0.875$ y $1.000$ (media $0.991$) — sin superposición.
- 0/16 unidades ReLU muertas en las 5 semillas: el colapso es específico de la conexión oculta$\to$salida, no de la capa compartida.
- Interpretación: un **óptimo local estable** del minimax — "rendirse" en un bit intercambia precisión de Bob por confusión de Eve.

---

# Resultado 3: el balance de pérdida modula pero no elimina el colapso

\footnotesize
\begin{center}
\begin{tabular}{lcc}
\toprule
Configuración & \texttt{xor\_match} & Posiciones colapsadas (/8) \\
\midrule
$\alpha{=}1.0,\beta{=}0.5$ (original) & $0.850 \pm 0.059$ & $2.60 \pm 1.02$ \\
$\alpha{=}1.0,\beta{=}0.1$            & $0.500 \pm 0.002$ & $8.00 \pm 0.00$ \\
$\alpha{=}2.0,\beta{=}0.5$            & $0.915 \pm 0.032$ & $1.60 \pm 0.49$ \\
$\alpha{=}3.0,\beta{=}1.0$            & $0.921 \pm 0.014$ & $1.60 \pm 0.49$ \\
\bottomrule
\end{tabular}
\end{center}
\normalsize

- Bajar $\beta$ no reduce el colapso: lo **generaliza** a las 8 posiciones (Alice deja de converger a XOR).
- Subir $\alpha$ ayuda pero no monótonamente, y las mejores configuraciones convergen a un piso de $1.60\pm0.49$.

---

# Resultado 4: el colapso es un cuello de botella de capacidad

\footnotesize
\begin{center}
\begin{tabular}{lcc}
\toprule
\texttt{hidden\_size} & \texttt{xor\_match} & Colapsadas (/8) \\
\midrule
16 ($=2N$, original) & $0.921 \pm 0.014$ & $1.60 \pm 0.49$ \\
32 ($=4N$)            & $1.000 \pm 0.000$ & $0.00 \pm 0.00$ \\
64 ($=8N$)            & $1.000 \pm 0.000$ & $0.00 \pm 0.00$ \\
128 ($=16N$)          & $1.000 \pm 0.000$ & $0.00 \pm 0.00$ \\
\bottomrule
\end{tabular}
\end{center}
\normalsize

**Resultado más contundente:** duplicar el ancho de la capa oculta ($16\to32$) elimina el colapso por completo, en las 5 semillas, sin excepción. Capacidad y balance de pérdida son efectos independientes que se combinan: juntos llegan a \texttt{xor\_match}$=1.000$ con 0 posiciones colapsadas.

---

# Discusión: Tracr como generador de hipótesis

- Alice (MLP) y el modelo compilado (transformer) **no comparten estructura de circuito** — la comparación no es peso a peso.
- Lo que se transfiere no es una arquitectura sino un **vocabulario de variables**: la noción de que cada posición de salida tiene un bit categórico legible al 100\% en el modelo con semántica conocida.
- Ese vocabulario se convierte en una hipótesis falsable sobre la red opaca, y resulta cierta solo parcialmente — ese es el hallazgo.
- Consistente con el argumento de que la interpretabilidad depende de si la base de representación natural de un modelo coincide con una base interpretable por humanos.

[@olah2022mechanistic; @olah2020zoom]

---

# De síntoma agregado a diagnóstico mecánico

Cadena reproducible como metodología general:

1. Síntoma agregado: \texttt{xor\_match} se estanca en $\approx 0.83$–$0.92$.
2. Hipótesis guiada por vocabulario interpretable (Tracr).
3. Sondeo lineal por posición $\to$ heterogeneidad específica.
4. Inspección de pesos $\to$ mecanismo exacto (colapso de norma).
5. Ablación causal (capacidad) $\to$ causa raíz confirmada.

---

# Limitaciones

- Tarea deliberadamente simple (XOR, $N{=}8$); no está claro si el patrón se replica en cifrados más complejos.
- Umbral de colapso (norma $<4.0$) elegido post-hoc a partir de un hueco empírico, no de un criterio independiente.
- El sondeo lineal establece **legibilidad**, no necesidad causal — no se hizo activation patching dentro de Alice.
- 5 semillas por configuración: suficiente para el patrón cualitativo, modesto para estadística fina.

---

# Conclusiones

- El vocabulario de variables de un modelo compilado con Tracr puede transferirse como hipótesis de diagnóstico sobre una red opaca **no relacionada arquitectónicamente**.
- El sondeo lineal reveló una heterogeneidad de convergencia por posición invisible en la métrica agregada.
- El colapso es, mayormente, un **cuello de botella de capacidad** de la arquitectura original de Abadi \& Andersen — no una limitación fundamental del esquema ANC.
- Duplicar \texttt{hidden\_size} + reajustar $(\alpha,\beta)$ elimina el colapso por completo.

---

# Referencias
