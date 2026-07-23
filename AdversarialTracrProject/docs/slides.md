---
title: "\\emoji{wtf} XAI Lecture 21"
subtitle: "An Introduction to Circuits"
bibliography: references.bib

---

# Disclaimer

\input{../disclaimer.tex}

---


# Paper 1

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/paper1.png}
\end{center}

[@olah_mechanistic_2022]


---

# Motivations 

- Reverse engineering analogy: Mechanistic interpretability aims to reverse engineer neural networks, similar to analyzing a compiled binary program.  
- Curse of dimensionality: The motivation to overcome the exponential complexity of input spaces that makes naive interpretability infeasible.  
- Variables and activations: Understanding activations as decomposable variables, enabling clearer reasoning about network behavior.  
- Interpretable bases: The drive to find representations aligned with neurons or clear directions, avoiding polysemantic entanglement.  
- Personal intuitions: The essay serves as an informal note to share intuitions that motivate ongoing work in mechanistic interpretability.  

---

# Contributions

- Formalizing the reverse engineering analogy: Establishes a conceptual framework comparing mechanistic interpretability to reverse engineering compiled programs.  
- Addressing the curse of dimensionality: Highlights how mechanistic interpretability can provide non-exponential descriptions of network behavior.  
- Variables and activations: Emphasizes the need to decompose activations into understandable variables, enabling clearer reasoning about neural networks.  
- Interpretable bases: Identifies the privileged role of neuron-aligned bases and discusses challenges posed by polysemantic neurons.  
- Modularity and interpretable features: Reframes modularity as the ability to decompose representations into interpretable components rather than isolated modules.  

---

# Analogy: Programs vs Neural Networks

| Regular Computer Programs      | Neural Networks                        |
|--------------------------------|----------------------------------------|
| Reverse Engineering            | Mechanistic Interpretability           |
| Program Binary                 | Network Parameters                     |
| VM / Processor / Interpreter   | Network Architecture                   |
| Program State / Memory         | Layer Representation / Activations     |
| Variable / Memory Location     | Neuron / Feature Direction             |

---

# Attacking the Curse of Dimensionality

- The curse of dimensionality refers to the exponential growth of complexity in high-dimensional input spaces.  
- Mechanistic interpretability seeks to bypass this by reverse engineering networks rather than exhaustively exploring inputs.  
- By decomposing activations into interpretable variables, researchers can describe network behavior without brute-force enumeration.  
- Interpretable bases aligned with neurons or clear directions reduce dimensional complexity and make analysis tractable.  
- The essay motivates interpretability as a way to achieve concise, non-exponential descriptions of neural network mechanisms.  
---

# Simple Memory Layout & Neurons

- In computer programs, a simple memory layout allows variables to be stored in clear, distinct locations.  
- Mechanistic interpretability draws an analogy: neurons can act like memory slots, each aligned with a specific feature direction.  
- Just as reverse engineering benefits from a straightforward memory map, analyzing networks is easier when activations correspond to interpretable neurons.  
- The challenge arises when neurons are polysemantic, encoding multiple features at once, breaking the simplicity of the layout.  
- The essay emphasizes that having a “simple memory layout” in neural networks — where neurons map cleanly to features — is crucial for effective interpretability.  
---

# Conclusions

- Mechanistic interpretability provides a framework for reverse engineering neural networks, analogous to analyzing compiled programs.  
- The approach offers a way to overcome the curse of dimensionality by focusing on interpretable variables and bases rather than brute-force exploration.  
- Understanding activations as variables and aligning features with neurons enables clearer reasoning about network mechanisms.  
- The importance of interpretable bases is highlighted, as polysemantic neurons pose significant challenges to analysis.  
- The essay serves as an informal but influential note, motivating further research into building coherent, interpretable frameworks for complex models.  
---


# Paper 2 

\begin{center}
\includegraphics[width=0.9\columnwidth]{imgs/paper2.png}
\end{center}
[@olah2020zoom]
---

# Motivations

- Scientific inspiration: Just as the microscope enabled the birth of cell biology, zooming in on neural networks may open a new paradigm for interpretability.  
- Beyond black-box views: Instead of treating networks as opaque systems, the paper motivates analyzing individual neurons and weights as meaningful objects of study.  
- Biological analogy: The approach mirrors biology and neuroscience, where cells and synapses are investigated to understand larger systems.  
- Discovery of circuits: Connections between neurons form circuits that implement recognizable algorithms, motivating a systematic study of these structures.  
- Hypothesis-driven research: The authors propose that features are fundamental units, connected into circuits, and that these patterns may be universal across models.  
- Foundation for interpretability: If these hypotheses hold, circuits could provide a rigorous, falsifiable basis for understanding neural networks.  

---
# Historical Inspiration & Black-Box Challenge

\begin{columns}

  \column{0.6\textwidth}
    \begin{itemize}
      \item Historical analogy: The invention of the microscope allowed scientists to move beyond speculation and directly observe cells.  
      \item Overcoming the black-box: Zooming in on neural networks mirrors this shift, enabling analysis of neurons and weights instead of treating models as opaque systems.  
      \item Curse of dimensionality: By focusing on interpretable variables and circuits, researchers avoid brute-force exploration of vast input spaces, making analysis tractable.  
      \item Scientific paradigm: Just as cell biology emerged from microscopy, mechanistic interpretability can emerge from detailed study of circuits.  
    \end{itemize}

  \column{0.4\textwidth}
    \begin{center}
      \includegraphics[width=0.9\columnwidth]{imgs/micrographia2.jpg}

   \vspace{0.5em}

   \footnotesize Hooke’s \textit{Micrographia} revealed a rich microscopic world as seen through a microscope, including the initial discovery of cells.  
   Images from the National Library of Wales.
  \end{center}

\end{columns}

---

# Three Speculative Claims (Introduction)

- Circuits research is still in its early stage, similar to cell biology after the invention of the microscope.  
- Speculative claims can guide progress, offering hypotheses to test and refine.  
- Neural networks may follow universal principles, with circuits as fundamental units.  
- The next section introduces three claims to spark debate and future research.  
---

# Three Speculative Claims (Overview)

\footnotesize
**Three Speculative Claims about Neural Networks**  

- *Claim 1: Features* — Fundamental units, corresponding to directions in activation space.  
- *Claim 2: Circuits* — Features connected by weights, forming computational subgraphs.  
- *Claim 3: Universality* — Similar features and circuits appear across models and tasks.  

---

# Claim 1: Features

- Features are the fundamental unit of neural networks.  
- They correspond to **directions** in activation space, defined as linear combinations of neurons in a layer.  
- Individual neurons can often represent useful features, but in polysemantic cases combinations of neurons provide clearer insight.  
- Features can be rigorously studied and understood, offering a structured way to analyze network behavior.  
- This claim positions features as the basic building blocks for interpretability.  

---
# Example 1: Curve Detectors

\begin{columns}

\column{0.5\textwidth}

\begin{itemize}
  \item Curve detectors are an early example of interpretable features in vision models.  
  \item They respond strongly to curved shapes, acting as specialized feature directions.  
  \item These detectors illustrate how features can correspond to meaningful visual concepts.  
  \item Studying them shows that circuits can implement recognizable algorithms.  
  \item This example supports the claim that features are fundamental units of neural networks.  
\end{itemize}

\column{0.5\textwidth}

\begin{center}
  \includegraphics[width=0.9\columnwidth]{imgs/curves.png}

  \vspace{0.5em}

  \footnotesize Example of curve detectors in vision models.  
  They highlight how features correspond to interpretable directions in activation space.
\end{center}

\end{columns}

---


# Arguments (Slide 1)

\begin{columns}
  \column{0.1\textwidth}
    \includegraphics[width=\linewidth]{imgs/arg-fv.png}

  \column{0.9\textwidth}
    \textbf{Argument 1: Feature Visualization} \newline
    Optimizing the input to cause curve detectors to fire reliably produces curves. 
    This establishes a causal link, since everything in the resulting image was added to cause the neuron to fire more. 
    You can learn more about feature visualization \href{https://distill.pub/2017/feature-visualization/}{here}.
\end{columns}

\vspace{1em}

\begin{columns}
  \column{0.1\textwidth}
    \includegraphics[width=\linewidth]{imgs/arg-data.png}

  \column{0.9\textwidth}
    \textbf{Argument 2: Dataset examples} \newline
    The ImageNet images that cause these neurons to strongly fire are reliably curves in the expected orientation. 
    The images that cause them to fire moderately are generally less perfect curves or curves off orientation.
\end{columns}

\vspace{1em}

---
# Arguments (Slide 2)

\begin{columns}
  \column{0.1\textwidth}
    \includegraphics[width=\linewidth]{imgs/arg-synthetic.png}

  \column{0.9\textwidth}
    \textbf{Argument 3: Synthetic Examples} \newline
    Curve detectors respond as expected to a range of synthetic curves images created with varying orientations, curvatures, and backgrounds. 
    They fire only near the expected orientation, and do not fire strongly for straight lines or sharp corners.
\end{columns}

\vspace{1em}

\begin{columns}
  \column{0.1\textwidth}
    \includegraphics[width=\linewidth]{imgs/arg-tune.png}

  \column{0.9\textwidth}
    \textbf{Argument 4: Joint Tuning} \newline
    If we take dataset examples that cause a neuron to fire and rotate them, they gradually stop firing and the curve detectors in the next orientation begins firing. 
    This shows that they detect rotated versions of the same thing. Together, they tile the full 360 degrees of potential orientations.
\end{columns}
---
# Arguments (Slide 3)

\begin{columns}
  \column{0.1\textwidth}
    \includegraphics[width=\linewidth]{imgs/arg-weights.png}

  \column{0.9\textwidth}
    \textbf{Argument 5: Feature Implementation (circuit-based argument)} \newline
    By looking at the circuit constructing the curve detectors, we can read a curve detection algorithm off of the weights. 
    We also don’t see anything suggestive of a second alternative cause of firing, although there are many smaller weights we don’t understand the role of.
\end{columns}

\vspace{1em}

\begin{columns}
  \column{0.1\textwidth}
    \includegraphics[width=\linewidth]{imgs/arg-use.png}

  \column{0.9\textwidth}
    \textbf{Argument 6: Feature Use (circuit-based argument)} \newline
    The downstream clients of curve detectors are features that naturally involve curves (e.g. circles, 3d curvature, spirals…). 
    The curve detectors are used by these clients in the expected manner.
\end{columns}

\vspace{1em}
---
# Argument 7: Handwritten Circuits (Slide 4)

\begin{columns}
  \column{0.1\textwidth}
    \includegraphics[width=\linewidth]{imgs/arg-hand.png}

  \column{0.9\textwidth}
    \textbf{Argument 7: Handwritten Circuits (circuit-based argument)} \newline
    Based on our understanding of how curve detectors are implemented, we can do a cleanroom reimplementation, 
    hand setting all weights to reimplement curve detection. 
    These weights are an understandable curve detection algorithm, and significantly mimic the original curve detectors.
\end{columns}
---

# Example 2: High-Low Frequency Detectors (Image)

\begin{columns}
  \column{0.45\textwidth}
    \includegraphics[width=\linewidth]{imgs/high-low.png}

  \column{0.55\textwidth}
    \textbf{Visualization of High-Low Frequency Detectors} \newline
    The image shows how these detectors activate in response to alternating bands of high and low frequency signals. 
    Bright regions indicate strong activation, highlighting the detector’s sensitivity to structured frequency contrasts. 
    This visualization makes clear that the feature corresponds to a meaningful and interpretable direction in the model’s activation space.
\end{columns}
---
# Example 3: Pose-Invariant Dog Head Detector

\begin{columns}
  \column{0.5\textwidth}
    \includegraphics[width=\linewidth]{imgs/dog-pose.png}

  \column{0.5\textwidth}
    \textbf{Pose-Invariant Dog Head Detector} \newline
    This detector activates reliably for dog heads across a wide range of poses and orientations. 
    It demonstrates that neural networks can learn features that are robust to changes in viewpoint, 
    capturing the semantic concept of a “dog head” rather than a specific angle. 
    The visualization shows consistent activation regardless of whether the dog is facing forward, sideways, or tilted, 
    highlighting the feature’s invariance to pose.
\end{columns}
---
# Claim 2: Circuits

Features connect through weights, forming circuits that can be rigorously studied.
Neurons are linear combinations of previous layers, so understanding features also means analyzing their connections.  
Surprisingly, circuits are not messy: they reveal rich, often symmetric structures.  
Weights become interpretable, allowing us to read meaningful algorithms directly from them.  
This opens the door to studying circuits as tractable and meaningful objects.
---

# Circuit 1: Curve Detectors

- Curve detectors are a family of units detecting curves in different angular orientations.  
- They are implemented from earlier, less sophisticated curve detectors and line detectors.  
- These detectors feed into the next layer to create 3D geometry and complex shape detectors.  
- While there are many smaller connections to other features, the main story is the interaction between early curve detectors and full curve detectors.  
- This section focuses on how curve detectors are built from earlier features and connect to the rest of the model.
---
# Circuit 1: Curve Detectors (Visualization)

\begin{center}
  \includegraphics[width=0.8\textwidth]{imgs/curve-circuit.png}

  \vspace{0.5em}

  {\tiny Visualization of how curve detectors emerge from earlier line and curve features. 
  The diagram highlights the connections that build up to full curve detectors, 
  showing their role as building blocks for higher-level geometry and shape recognition.}
\end{center}
---
# Circuit 1: Curve Detectors (Weights)

\begin{center}
  \begin{minipage}{0.45\textwidth}
    \includegraphics[width=\linewidth]{imgs/curve-weights-a.png}

   \vspace{0.3em}

   {\tiny The raw weights between the early curve detector and late curve detector in the same orientation are a curve of positive weights surrounded by small negative or zero weights.}
  \end{minipage}
  \hfill
  \begin{minipage}{0.45\textwidth}
    \includegraphics[width=\linewidth]{imgs/curve-weights-b.png}

   \vspace{0.3em}

   {\tiny This can be interpreted as looking for “tangent curves” at each point along the curve.}
  \end{minipage}
\end{center}
\vspace{1em}

\small
The connection between early and late curve detectors reveals a structured pattern in the weights. 
Strong positive values align with the curve’s orientation, while surrounding negative or zero weights suppress irrelevant activations. 
This arrangement can be interpreted as the detector searching for “tangent curves” along each point of the curve, 
showing how meaningful algorithms can be read directly from the weight matrices.
---
# Excitation and Inhibition in Curve Detectors

\begin{center}
  \includegraphics[width=0.6\textwidth]{imgs/excited-inhibited.png}

  \vspace{0.5em}

\end{center}
  \tiny Curve detectors are excited by earlier detectors in similar orientations and inhibited by detectors in opposing orientations. 
  This pattern shows that weights are meaningful, reflecting geometric symmetries. 
  Strong positive weights align with tangent curves, while negative weights suppress opposite orientations. 
  The rotation of weights with detector orientation illustrates an equivariant circuit structure.
---
# Circuit 2: Oriented Dog Head Detection

- This circuit detects dog heads with sensitivity to orientation.
- Built from earlier pose-invariant dog head detectors combined with orientation-specific features.
- Highlights how circuits integrate semantic concepts (dog head) with geometric properties (orientation).
- Demonstrates that interpretable algorithms emerge from feature connections.
---
# Circuit 2: Oriented Dog Head Detection (Visualization)

\begin{center}
  \includegraphics[width=0.6\textwidth]{imgs/oriented-dog-head.png}

  \vspace{0.5em}

\end{center}
  \tiny Visualization of oriented dog head detectors. 
  The circuit shows how orientation-specific features modulate the activation of dog head detectors, 
  producing selective responses depending on the head’s angle.
---
# Circuit 2: Oriented Dog Head Detection (Unioning Over Cases)

\begin{center}
  \includegraphics[width=0.6\textwidth]{imgs/oriented-weights-a.png}

  \vspace{0.5em}

\end{center}
  \tiny The network detects dog heads facing left and right through mirrored pathways. 
  These pathways inhibit each other, creating XOR-like properties. 
  By unioning over cases, the model builds invariant multifaceted units that respond to both orientations. 
  Connections show selectivity, e.g., “head with neck” units activate only on the correct side.
---
# Circuit 2: Oriented Dog Head Detection (Union Step)

\begin{center}
  \includegraphics[width=0.4\textwidth]{imgs/union-step.png}

  \vspace{0.5em}

\end{center}
  \tiny The union step shows how the network merges left- and right-facing dog head detectors. 
  Excitation regions extend differently depending on orientation, allowing snouts to converge at the same point. 
  This mechanism refines invariance by aligning features across orientations. 
  The circuit illustrates how detailed weight structures encode sophisticated geometric relationships, 
  a topic to be explored further in future analysis.
---
# Circuit 3: Cars in Superposition

\begin{columns}
 \column{0.5\textwidth}

  \begin{itemize}
    \item In mixed4c, a mid-late layer of InceptionV1, there is a car detecting neuron.  
    \item This neuron integrates features from previous layers.  
    \item It looks for wheels at the bottom of its convolutional window.  
    \item It also looks for windows at the top, combining both cues to detect cars.  
  \end{itemize}

 \column{0.5\textwidth}
  \begin{center}
    \includegraphics[width=\linewidth]{imgs/cars-superposition.png}

   \vspace{0.5em}

   {\tiny Visualization of the car detector in superposition.  
    The neuron combines wheel and window features to identify cars.}
   \end{center}
\end{columns}
---
# Circuit 3: Cars in Superposition (Superposition Phenomenon)

\begin{columns}
  \column{0.4\textwidth}
    \begin{center}
      \includegraphics[width=\linewidth]{imgs/cars-superposition.png}

   \vspace{0.5em}

   {\tiny Visualization of car features mixing with dog detectors.}
    \end{center}

  \column{0.6\textwidth}

  \begin{itemize}
     \item Instead of creating another pure car detector, the model spreads car features across neurons linked to dog detectors.
     \item This suggests polysemantic neurons are deliberate, intertwining car and dog detection.
     \item The phenomenon is called \textit{superposition}.
     \item Superposition conserves neurons, allowing reuse for more important tasks.
     \item As long as cars and dogs don’t co-occur, the model can later retrieve the dog feature accurately without dedicating a separate neuron.
   \end{itemize}
\end{columns}
---
# Circuit 3: Cars in Superposition (Superposition Phenomenon)

\begin{columns}
  \column{0.5\textwidth}
    \begin{center}
    \includegraphics[width=\linewidth]{imgs/cars-superposition2.png}

    \vspace{0.5em}

   {\tiny Visualization of car features mixing with dog detectors.}
    \end{center}

  \column{0.5\textwidth}

   \begin{itemize}
      \item Instead of creating another pure car detector, the model spreads car features across neurons linked to dog detectors.  
      \item This suggests polysemantic neurons are deliberate, intertwining car and dog detection.  
      \item The phenomenon is called \textit{superposition}.  
      \item Superposition conserves neurons, allowing reuse for more important tasks.  
      \item As long as cars and dogs don’t co-occur, the model can later retrieve the dog feature accurately without dedicating a separate neuron.  
    \end{itemize}
\end{columns}

---

# Recurring Patterns in Circuits

\begin{itemize}
  \item In InceptionV1 and other models, recurring abstract patterns appear:
    \begin{itemize}
      \item Equivariance (curve detectors).  
      \item Unioning over cases (pose-invariant dog head detector).  
      \item Superposition (car detector).  
    \end{itemize}
  \item In biology, a circuit motif is a recurring pattern in complex graphs such as transcription networks or biological neural networks.  
  \item Motifs are useful because understanding one motif provides leverage across all graphs where it occurs.  
  \item Studying motifs may become more important than analyzing individual circuits in the long run.  
  \item A solid foundation of well-understood circuits is necessary before deeper motif investigations.  
\end{itemize}

---
# Claim 3: Universality

\begin{itemize}
  \item Universality refers to the recurrence of similar features and circuits across different models and tasks.  
  \item Neural networks often develop analogous detectors, even when trained on distinct datasets.  
  \item This suggests the presence of general principles guiding feature formation.  
  \item Universality highlights the potential for transferable insights across architectures.  
\end{itemize}
---
# Claim 3: Universality (Example)

\begin{columns}
  \column{0.5\textwidth}
    \begin{center}
      \includegraphics[width=\linewidth]{imgs/unit-2-3.png}

   \vspace{0.5em}

   {\tiny Visualization of a universal feature appearing across models.}
    \end{center}

  \column{0.5\textwidth}
    \begin{itemize}
      \item Certain units, such as curve detectors or object parts, emerge repeatedly.
      \item The same structural motifs can be observed in different architectures.
      \item These recurring features strengthen the claim of universality.
    \end{itemize}
\end{columns}
---
# Claim 3: Universality (Implications)

\begin{itemize}
  \item Universality implies that studying one circuit can provide understanding of many others.
  \item Shared motifs across models suggest deeper algorithmic principles.
  \item This perspective shifts focus from isolated circuits to generalizable structures.
  \item Recognizing universality may accelerate interpretability research.
\end{itemize}
---
# Interpretability as a Natural Science

\begin{itemize}
  \item Interpretability is framed as a natural science: the study of circuits and features in neural networks resembles the study of biological systems.  
  \item Progress depends on careful observation, cataloging, and comparison of recurring motifs across models.  
  \item The discipline emphasizes empirical investigation rather than purely theoretical speculation.  
  \item Just as biology advanced by identifying structures and functions, interpretability advances by mapping circuits and their roles.  
  \item This perspective positions interpretability as a systematic field, aiming to uncover general principles of artificial intelligence.  
\end{itemize}
---
# References



