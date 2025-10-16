# Transformation and Modeling of SDFs for Timed Automata with UPPAAL

This repository contains a formal modeling and verification project using UPPAAL, focusing on transforming Synchronous Dataflow (SDF) graphs into Timed Automata (TA).

## ROADMAP
Goal: Development and validation of an online scheduling algorithm for tasks modeled via SDF transformed into TA.

**Milestones:**

1. [DONE] Implementation and validation of direct transformation from SDF to TA in UPPAAL;

1. [DONE] Implementation of CPU capacity verification before task allocation;

1. [DONE] Support for multiple SDF graphs and model scalability improvements;

1. [DONE] Integration with the UPPAAL Scheduler Framework, adapted to support SDF with arbitrary deadlines;

1. [TESTS:ON-GOING] Implementation of the first version of the scheduling algorithm for resource selection;

1. [] Tests with real cases in term of the number of tasks and processors (The license limits the number of template instances I want to run.); 

1. [] Support for multiple instances of the same task;

1. [] Modeling communication between tasks distributed across different processors;

1. [] Guarantee the preservation of the temporal characteristics of the successor task;

1. [] Support for different Worst-Case Execution Times (WCETs) per processor type;

1. [] Support for sporadic tasks;

**Validation:**
At each milestone, the following conditions are validated:

1. Verification of the absence of deadline violations in allocated tasks;

## PROJECTS

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




