# Transformation and Modeling of SDFs for Timed Automata with UPPAAL

This repository contains a formal modeling and verification project using UPPAAL, focusing on transforming Synchronous Dataflow (SDF) graphs into Timed Automata (TA).


### 00- Transform SDF to Timed Automata in UPPAAL

This folder contains the initial model, which directly transforms an SDF graph into timed automata. The model was developed based on the article:

**"Resource-Constrained Optimal Scheduling of Synchronous Dataflow Graphs via Timed Automata."**

Ahmad, Waheed \& de Groote, Robert \& Hölzenspies, Philip \& Stoelinga, Mariëlle \& Pol, Jaco. (2014). 72-81. 10.1109/ACSD.2014.13.

**Uppaal VERIFIER results:**

\- No deadlock (counters need to be removed);

### 01- SDF modeled as a timed automaton with arbitrary deadlines (initial approach) and CPU capacity checking

This folder extends the project in the `00` folder, with the aim of adding a check of the maximum load limit on each processor and starting the arbitrary deadline implementation

**Uppaal VERIFIER results:**

\- No deadlock (counters need to be removed);
\- No processor exceeds the load limit (counters need to be removed);

### 02- Multi-SDF in UPPAAL

This folder extends the project in folder `01`, with the aim of generalizing and making the system more flexible to add more resources and elements.

The main improvements are:

\- Support for **multiple SDF graphs**;

\- Improve scalability of the system.


### 03- Scheduler Framework for SDF

This folder extends the project UPPAAL project SchedulerFramework example to support SDF.




