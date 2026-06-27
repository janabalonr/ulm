# Criptografía Liviana
## Programa de Actividad Curricular

---

## Competencias del Perfil de Egreso

### Competencia Principal
**Seguridad en Sistemas de Información:** El estudiante es capaz de analizar, diseñar e implementar mecanismos criptográficos adecuados a entornos con recursos computacionales limitados, garantizando la confidencialidad, integridad y autenticidad de la información en sistemas embebidos, IoT y dispositivos de baja capacidad.

### Competencias Complementarias
- **Pensamiento computacional aplicado:** Capacidad de evaluar la eficiencia algorítmica de soluciones criptográficas en función de restricciones de memoria, energía y procesamiento.
- **Comunicación técnica:** Habilidad para documentar, comparar y fundamentar la selección de esquemas criptográficos livianos en contextos de ingeniería de sistemas.
- **Trabajo colaborativo:** Disposición para participar activamente en proyectos de análisis e implementación de seguridad en equipos multidisciplinares.

---

## Descripción de la Actividad Curricular

La asignatura **Criptografía Liviana** introduce al estudiante en los fundamentos teóricos y prácticos de los esquemas criptográficos diseñados para operar en entornos con restricciones severas de recursos: memoria reducida, bajo consumo energético, procesadores de baja potencia y latencia mínima. Se estudian los principios matemáticos subyacentes, los estándares internacionales vigentes (ISO/IEC 29192, NIST Lightweight Cryptography), y se aplican estos conceptos mediante prácticas de implementación en plataformas embebidas y simuladores.

El curso articula teoría criptográfica clásica con las demandas actuales del Internet de las Cosas (IoT), redes de sensores inalámbricos (WSN), tarjetas inteligentes y sistemas ciberfísicos, preparando al estudiante para tomar decisiones técnicas fundamentadas en contextos industriales y de investigación.

| | |
|---|---|
| **Tipo de actividad** | Teórico-Práctica |
| **Créditos** | 5 SCT |
| **Horas semanales** | 3 horas teóricas / 2 horas laboratorio |
| **Requisitos** | Fundamentos de Criptografía, Sistemas Digitales |
| **Nivel** | Pregrado (7.° semestre) |

---

## Resultados de Aprendizaje

Al finalizar exitosamente la asignatura, el estudiante será capaz de:

**RA1 — Fundamentos**
Explicar los principios matemáticos y de diseño que diferencian la criptografía liviana de la criptografía convencional, identificando las restricciones de hardware que motivan su desarrollo.

**RA2 — Cifrado por bloques y flujo liviano**
Analizar y comparar los principales algoritmos de cifrado liviano (PRESENT, SIMON, SPECK, GIFT, ASCON), evaluando sus propiedades de seguridad, rendimiento y adecuación a plataformas específicas.

**RA3 — Funciones hash y autenticación livianas**
Describir el funcionamiento de funciones hash livianas (PHOTON, SPONGENT) y esquemas de autenticación de mensaje (MAC) eficientes, y aplicarlos en escenarios de integridad de datos.

**RA4 — Criptografía de clave pública liviana**
Evaluar esquemas de clave pública adaptados a recursos limitados, incluyendo curvas elípticas eficientes y esquemas post-cuánticos seleccionados por NIST para entornos restringidos.

**RA5 — Implementación**
Implementar algoritmos criptográficos livianos en plataformas embebidas (microcontroladores AVR/ARM, Arduino, FPGA), optimizando el uso de memoria RAM/ROM y el consumo energético.

**RA6 — Evaluación y selección**
Seleccionar y justificar la combinación de primitivas criptográficas livianas adecuada para un caso de uso real, considerando el modelo de amenaza, los recursos disponibles y los estándares aplicables.

---

## Contenidos y Metodologías

| Unidad | Tema | Contenidos | Metodología | Evaluación |
|--------|------|------------|-------------|------------|
| **1** | **Introducción y Fundamentos** | Motivación: IoT, sensores y dispositivos restringidos. Definición de entornos con recursos limitados (memoria, energía, latencia). Comparación con criptografía convencional. Métricas de eficiencia: área de silicio, ciclos de reloj, bytes de código. Estándares: ISO/IEC 29192, proceso NIST LWC. | Clases expositivas con ejemplos reales. Análisis de casos de uso (smart metering, RFID, WSN). Lectura guiada de documentación NIST. | Prueba de diagnóstico. Foro de discusión en línea. |
| **2** | **Cifrado por Bloques Liviano** | Estructura de redes de sustitución-permutación (SPN) y redes de Feistel livianas. Algoritmos: PRESENT, GIFT, SIMON, SPECK, SKINNY. Análisis de seguridad: resistencia a criptoanálisis diferencial y lineal. Comparativa de rendimiento en hardware y software. | Clases expositivas con demostraciones en Python. Laboratorio: implementación de SIMON/SPECK en Python y Arduino. Análisis comparativo en grupos. | Laboratorio 1. Informe técnico comparativo (grupal). |
| **3** | **Cifrado de Flujo Liviano** | Generadores de números pseudoaleatorios (PRNG) para entornos limitados. Algoritmos: Grain, Trivium, Mickey. Propiedades de seguridad: período, correlación, aleatoriedad estadística. Ataques conocidos y mitigaciones. | Clases expositivas. Resolución de ejercicios en aula. Demostración con simuladores de hardware. | Taller práctico evaluado. |
| **4** | **Funciones Hash y MAC Livianos** | Construcción esponja (Sponge Construction). Algoritmos: PHOTON, SPONGENT, ASCON-Hash. Códigos de autenticación de mensaje (MAC): PRESENT-MAC, LightMAC. Aplicaciones: integridad en firmware, autenticación en RFID. | Clases expositivas. Laboratorio: implementación de ASCON-Hash en microcontrolador. Estudio de casos de integridad en actualizaciones OTA. | Laboratorio 2. |
| **5** | **Cifrado Autenticado (AEAD) Liviano** | Concepto de AEAD (Authenticated Encryption with Associated Data). ASCON como estándar NIST 2023. Otros finalistas: GIFT-COFB, TinyJAMBU, Romulus. Análisis de rendimiento y seguridad provable. | Clases expositivas. Análisis de la documentación oficial de ASCON. Ejercicios de diseño de protocolos seguros con AEAD. | Prueba solemne 1. |
| **6** | **Criptografía de Clave Pública Liviana** | Limitaciones de RSA/DSA en entornos restringidos. Criptografía de Curva Elíptica (ECC): curvas eficientes (Curve25519, NIST P-256). Esquemas de intercambio de llaves: ECDH liviano. Introducción a criptografía post-cuántica liviana: CRYSTALS-Kyber, SPHINCS+. | Clases expositivas con énfasis matemático. Resolución guiada de ejercicios de aritmética en curvas. Demostración de ECDH en Python. | Taller matemático evaluado. |
| **7** | **Implementación en Hardware y Software** | Optimización en C para microcontroladores (AVR, ARM Cortex-M). Implementación en FPGA: flujo de diseño básico. Perfiles de hardware vs. software. Medición de consumo energético (power profiling). Técnicas anti-análisis de canal lateral (introducción). | Laboratorio: implementación de ASCON en Arduino Nano. Medición de ciclos y RAM con profiler. Actividad de optimización de código. | Laboratorio 3 (mayor ponderación). Demostración en vivo. |
| **8** | **Protocolos y Aplicaciones** | Protocolos de autenticación liviana: HB, HB+. Protocolos de establecimiento de sesión en IoT: TLS 1.3 con suites livianas. MQTT con seguridad liviana. Casos de estudio: redes de sensores agrícolas, salud conectada, vehículos autónomos. | Análisis de casos de estudio en grupos. Debate técnico: selección de primitivas para un escenario asignado. Revisión de literatura científica reciente. | Presentación grupal de caso de estudio. |
| **9** | **Evaluación, Estandarización y Futuro** | Proceso de estandarización NIST LWC: criterios y resultados. Herramientas de benchmarking: FELICS, SUPERCOP. Tendencias: criptografía cuántico-resistente liviana, seguridad en edge computing. Ética y regulación en seguridad de dispositivos IoT. | Seminario de presentaciones estudiantiles. Invitado experto (sesión sincrónica o grabada). Revisión crítica de artículos de conferencias (CHES, CryptHW). | Proyecto final — presentación y defensa. |

---

## Sistema de Evaluación

| Instrumento | Ponderación |
|---|---|
| Laboratorios 1, 2 y 3 | 30 % |
| Prueba Solemne 1 (Unidades 1–5) | 20 % |
| Talleres evaluados | 15 % |
| Informe técnico comparativo (grupal) | 10 % |
| Presentación de caso de estudio (grupal) | 10 % |
| Proyecto final (individual/parejas) | 15 % |

> **Condición de aprobación:** Nota final ≥ 4,0 (escala 1,0–7,0). El proyecto final es de carácter integrador y su entrega es requisito para aprobar la asignatura.

---

## Bibliografía

### Textos Fundamentales

1. Eisenbarth, T., Kumar, S., Paar, C., Poschmann, A., & Uhsadel, L. (2007). *A Survey of Lightweight Cryptography Implementations*. IEEE Design & Test of Computers, 24(6), 522–533.

2. Beierle, C., Jean, J., Kölbl, S., Leander, G., Moradi, A., Peyrin, T., Sasaki, Y., Sasdrich, P., & Sim, S. M. (2016). *The GIFT Cipher Family*. Proceedings of CHES 2016, LNCS 9813, 321–345.

3. McKay, K., Bassham, L., Sönmez Turan, M., & Mouha, N. (2017). *Report on Lightweight Cryptography* (NISTIR 8114). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.IR.8114

4. Dobraunig, C., Eichlseder, M., Mendel, F., & Schläffer, M. (2021). *ASCON v1.2: Lightweight Authenticated Encryption and Hashing*. Journal of Cryptology, 34(3). https://doi.org/10.1007/s00145-021-09398-7

5. Paar, C., & Pelzl, J. (2010). *Understanding Cryptography: A Textbook for Students and Practitioners*. Springer. ISBN 978-3-642-04100-6.

### Estándares y Documentación Oficial

6. ISO/IEC 29192-2:2019. *Information Security — Lightweight Cryptography — Part 2: Block Ciphers*. International Organization for Standardization.

7. NIST. (2023). *Lightweight Cryptography Standardization: ASCON*. https://csrc.nist.gov/projects/lightweight-cryptography

8. NIST. (2022). *Status Report on the Final Round of the NIST Lightweight Cryptography Standardization Process* (NISTIR 8454). https://doi.org/10.6028/NIST.IR.8454

### Lecturas Complementarias

9. Avanzi, R., et al. (2021). *CRYSTALS-Kyber Algorithm Specifications and Supporting Documentation*. NIST PQC Round 3 Submission.

10. Bogdanov, A., Knudsen, L. R., Leander, G., Paar, C., Poschmann, A., Robshaw, M. J. B., Seurin, Y., & Vikkelsoe, C. (2007). *PRESENT: An Ultra-Lightweight Block Cipher*. Proceedings of CHES 2007, LNCS 4727, 450–466.

11. Beaulieu, R., Shors, D., Smith, J., Treatman-Clark, S., Weeks, B., & Wingers, L. (2015). *The SIMON and SPECK Families of Lightweight Block Ciphers*. Cryptology ePrint Archive, Report 2013/404. https://eprint.iacr.org/2013/404

12. Kerckhof, S., Durvaux, F., Hocquet, C., Bol, D., & Standaert, F. X. (2012). *Towards Green Cryptography: A Comparison of Lightweight Ciphers from the Energy Viewpoint*. Proceedings of CHES 2012, LNCS 7428, 390–407.

13. Manifavas, C., Hatzivasilis, G., Fysarakis, K., & Papaefstathiou, Y. (2016). *A Survey of Lightweight Stream Ciphers for Embedded Systems*. Security and Communication Networks, 9(10), 1226–1246.

### Recursos en Línea

14. FELICS — Fair Evaluation of Lightweight Cryptographic Systems: https://felics.uni.lu

15. Cryptography and Hardware Security (CHES) — Conference Proceedings: https://tches.iacr.org

16. Cryptology ePrint Archive (IACR): https://eprint.iacr.org

---

*Programa elaborado conforme a las directrices del proceso NIST Lightweight Cryptography Standardization (2019–2023) y los descriptores de competencias del marco nacional de cualificaciones para educación superior.*
