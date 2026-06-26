# Integración de Adversarial Neural Cryptography y Tracr para la Interpretabilidad de Algoritmos de Cifrado

**Integrantes:** Juan Rodrigo Anabalón R.  
**Curso:** Explainable Artificial Intelligence. FAMAF. UNC  
**Fecha:** Mayo 2026  

---

## Objetivo
El objetivo de este trabajo es investigar el uso de modelos compilados mediante Tracr como una referencia de verdad interpretativa (ground-truth) para validar hipótesis sobre los algoritmos de cifrado que emergen de forma opaca en redes de Adversarial Neural Cryptography (ANC).
El enfoque se centra en utilizar la estructura transparente de un transformer compilado como una especificación formal que permita contrastar si las activaciones y representaciones de una red Alice entrenada (MLP) son consistentes con la implementación exacta de un cifrado conocido (como una operación XOR bit a bit) compilado en Tracr.

---

## Plan de actividades

| Tarea                   | Descripción                                                                 | S1 | S2 | S3 | S4 | S5 | S6 |
|--------------------------|-----------------------------------------------------------------------------|----|----|----|----|----|----|
| Revisión bibliográfica   | Estudiar trabajos de Abadi (2016) sobre ANC y DeepMind (2023) sobre Tracr   | X  | X  |    |    |    |    |
| Implementación ANC       | Implementación ANC clásica Alice, Bob, Eve                                  |    | X  |    |    |    |    |
| Programación en RASP     | Codificar XOR Alice en RASP                                                 |    | X  | X  |    |    |    |
| Compilación Tracr        | Impl. Tracr para crear modelo transformer con pesos y estructura conocidos  |    |    | X  | X  |    |    |
| Comparación              | Analizar diferencias entre el cifrado emergente (ANC) y el explícito (Tracr)|    |    |    |    | X  |    |
| Informe final            | Elaborar documento con hallazgos y limitaciones                             |    |    |    |    |    | X  |

---

## Propuesta experimental
1. Implementar un ANC clásico Alice, Bob, Eve. 
1. Reimplementar cifrado básico (XOR con clave compartida) en RASP y compilarlo con Tracr.
3. Comparar las operaciones XOR emergentes de Alice con las operaciones explícitas compiladas en Tracr.
4. Evaluar interpretabilidad: verificar si Tracr permite identificar las variables críticas (difusión de bits, dependencia de la clave) que aparece de forma opaca en ANC.

---

Este bosquejo busca tender un puente entre **interpretabilidad** y **Adversarial Neural Cryptography (ANC)**, mostrando cómo Tracr puede servir como laboratorio para explicar y analizar los mecanismos internos de la criptografía neuronal adversarial.

---

## Referencias
- Weiss, G., Goldberg, Y., & Yahav, E. (2021). *Thinking Like Transformers*. Proceedings of the 38th International Conference on Machine Learning (ICML), PMLR 139.  
- Lindner, D., Kramár, J., Farquhar, S., Rahtz, M., McGrath, T., & Mikulik, V. (2023). *Tracr: Compiled Transformers as a Laboratory for Interpretability*. NeurIPS 2023. arXiv:2301.05062.  
- Abadi, M., & Andersen, D. G. (2016). *Learning to Protect Communications with Adversarial Neural Cryptography*. arXiv:1610.06918.  

