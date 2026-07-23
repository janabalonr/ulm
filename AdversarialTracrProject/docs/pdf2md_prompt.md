# Prompt: PDF → Beamer Slides (Pandoc-Markdown)

Convierte los PDFs proporcionados en slides Beamer usando Markdown-Pandoc. Puedes proporcionar múltiples PDFs y generaré slides separadas para cada uno.

## Cómo usar este prompt:

- **Claude.ai (Project):** Agregá este prompt como System Prompt del proyecto y subí el PDF.
- **Claude Code:** `Convertí @slides/original_pdf/Lecture_X.pdf a slides siguiendo @slides/pdf2md_prompt.md`

## Para cada PDF nuevo:

1. **Indica el número de PDF**: "PDF #1", "PDF #2", etc.
2. **Proporciona el documento**
3. **Recibirás slides independientes** con nombre sugerido del archivo

---

## Estructura de carpetas para una nueva lecture:

Cada lecture vive en su propia carpeta. Para crear una nueva (e.g., lecture05):

```
slides/
├── defaults.yaml          # Configuración Pandoc compartida (NO tocar)
├── disclaimer.tex         # Disclaimer compartido (NO tocar)
├── emojis/                # Emojis PNG compartidos (NO tocar)
├── make.py                # Script de compilación (NO tocar)
├── pdf2md_prompt.md       # Este prompt
├── lecture05/             # ← Nueva carpeta
│   ├── slides.md          # Archivo principal de slides (lo que genera este prompt)
│   ├── references.bib     # Bibliografía con las citas usadas en slides.md
│   └── imgs/              # Imágenes extraídas del PDF original
│       ├── figura1.png
│       └── figura2.png
```

**Pasos:**
1. Crear la carpeta `lectureNN/` y subcarpeta `imgs/`
2. Para cada imagen referenciada en slides.md, copiar un placeholder genérico y crear un archivo `imgs/images.md` con la tabla de imágenes a reemplazar:
   ```bash
   # Copiar placeholder para cada imagen
   cp slides/lecture03/imgs/placeholder.png slides/lectureNN/imgs/nombre_imagen.png
   ```
   El archivo `imgs/images.md` debe tener una tabla con columnas: Archivo, Slide PDF, Contenido — para saber qué screenshot extraer manualmente del PDF original.
3. Crear `references.bib` con las entradas BibTeX de los papers citados (formato `[@clave]` en el .md)
4. Crear `slides.md` usando este prompt
5. Compilar con: `python ../make.py slides.md` (desde dentro de la carpeta `lectureNN/`)
6. Para modo watch: `python ../make.py slides.md --watch`
7. Ten en cuenta que normalmente las referencias y las imagenes las toco manualmente.

---

## Formato YAML (header):
```yaml
---
title: "\\emoji{wtf} XAI: [Título del PDF]"
bibliography: references.bib

---
```

## Reglas esenciales:

**Estructura:**
- Separar slides con `---`
- Títulos de slides con `#` (nivel 1)
- Secciones: `# Nombre` seguido de `---`
- Subtítulos dentro de slide con `##`

**Imágenes:**
- Siempre dentro de `\begin{center}...\end{center}`
- Todas las imágenes en la carpeta `imgs/`
```latex
\begin{center}
\includegraphics[width=0.8\columnwidth]{imgs/nombre.png}
\end{center}
```

**Bloques:**
```latex
\begin{block}{Título}
Contenido neutral
\end{block}

\begin{alertblock}{Título}
Contenido importante o advertencias
\end{alertblock}

\begin{exampleblock}{Título}
Ejemplos o hallazgos positivos
\end{exampleblock}

\begin{definition}{}
Definiciones formales
\end{definition}
```

**Columnas (LaTeX):**
```latex
\begin{columns}
\begin{column}{0.48\textwidth}
Izquierda
\end{column}
\begin{column}{0.48\textwidth}
Derecha
\end{column}
\end{columns}
```

**Citas bibliográficas:**
- Usar formato Pandoc: `[@clave]` (e.g., `[@lipton2018mythos]`)
- Las citas se colocan después del contenido relevante, en su propia línea

**Espaciado y formato LaTeX:**
- Espaciado vertical: `\vspace{1cm}`, `\vspace{1em}`, `\vspace{0.5cm}`
- Relleno vertical (empujar contenido al fondo): `\vfill`
- Tamaños de texto: `\Huge`, `\huge`, `\Large`, `\large`, `\small`, `\footnotesize`, `\tiny`
- Formato LaTeX inline: `\textbf{negrita}`, `\textit{cursiva}`
- Color: `\textcolor{primarygreen}{texto}`
- URLs: `\url{https://...}`
- Emojis: `\emoji{nombre}` (e.g., `\emoji{wtf}`, `\emoji{fire}`, `\emoji{test-tube}`)

**Contenido:**
- Máximo 6-8 puntos por slide
- Una idea principal por slide
- Usa viñetas (`-`) y numeración (`1.`)
- `**negrita**`, `*cursiva*`, `` `código` ``
- Tablas markdown estándar
- Mezclar Pandoc markdown y LaTeX crudo es válido y esperado

## Estructura típica:
```markdown
---
[YAML header]
---

# Disclaimer

\input{../disclaimer.tex}

---

# Título Slide 1

Contenido...

---

# Título Slide 2

## Subtítulo

- Punto 1
- Punto 2

\begin{center}
\includegraphics[width=0.7\columnwidth]{imgs/figura.png}
\end{center}

---

# Conclusión

---

\begin{center}
\Huge Thank You!
\end{center}

---

# References {.allowframebreaks}

\footnotesize
```

**CRÍTICO:**
- Todas las imágenes en `imgs/`
- Separar CADA slide con `---`
- Títulos con `#` (nivel 1)
- No alteres el contenido de las slides, que sean todas iguales.
- Mostrame el codigo en un visor de codigo markdown (artefacto)
- La primer slide después del YAML tiene que ser exactamente:

    ```markdown
    ---

    # Disclaimer

    \input{../disclaimer.tex}

    ---
    ```

- La última slide de contenido es "Thank You!", seguida de la slide de References:

    ```markdown
    ---

    \begin{center}
    \Huge Thank You!
    \end{center}

    ---

    # References {.allowframebreaks}

    \footnotesize
    ```
