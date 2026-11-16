# Course Guide: Fundamentals of Artificial Intelligence & Knowledge Representation (FAIKR)
**Course Professors:** Prof. Michela Milano (M1), Prof. Paola Mello (M2), Prof. Roberta Calegari (M3)  
**Tutors:** Matteo Francobaldi (`matteo.francobaldi2@unibo.it`), Chiara Bellatreccia (`chiara.bellatreccia2@unibo.it`)

---

## 1. Exam Structure & Grading Formula

The exam is split into **three independent written module components**:

$$\text{Final Grade} = \frac{\text{Module 1 Score} + \text{Module 2 Score} + \text{Module 3 Score}}{2}$$

| Component | Content Focus | Max Raw Points | Contribution to Final /30 |
| :--- | :--- | :--- | :--- |
| **Module 1** | Search, Games, Constraints, Planning | 32 points (+ up to 2 bonus points from Challenges, capped at 32) | 16.0 points |
| **Module 2** | First-Order Logic, Deductive Planning, Prolog | 21 points | 10.5 points |
| **Module 3** | Probabilistic Reasoning, Bayesian Networks | 11 points | 5.5 points |
| **Total** | | **64 raw points** | **32.0 max scale** |

> [!IMPORTANT]
> **Grading Mechanics & Honors (30L)**:
> - Rounding: Results between 18.0 and 30.0 are rounded up.
> - **30 with Honours (30 e Lode)** is granted strictly when the final score is $\ge 31.0$.
> - **Independent Grade Retention**: Grades for individual modules are recorded independently. If you score well on Module 1 but poorly on Modules 2/3, you can accept Module 1 and retake only Modules 2 and 3 in the next exam call.

---

## 2. Official Exam Dates (A.A. 2026/2027)

| Exam Call | Module 1 Date | Modules 2 & 3 Date | Time & Classroom |
| :--- | :--- | :--- | :--- |
| **Early Call** | December 21, 2026 | December 22, 2026 | 10:00–13:00, Room 2.5 |
| **Winter Call 1** | January 19, 2027 | January 18, 2027 | 10:00–13:00, Room 2.3 |
| **Winter Call 2** | February 3, 2027 | February 2, 2027 | 10:00–13:00, Room 0.5 |

---

## 3. Detailed Syllabus & Topic Breakdown

### Module 1: Search, Games, Constraints & Planning (Prof. Michela Milano)
*Folder:* [`01 - Module 1 (Search, Games & Constraints)/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Fundamentals%20of%20Artificial%20Intelligence%20and%20Knowledge%20Representation/01%20-%20Module%201%20(Search,%20Games%20&%20Constraints))

1. **State Space Representation & Search Strategies**:
   - *Uninformed Search*: Breadth-First Search (BFS), Uniform-Cost Search (UCS / Dijkstra), Depth-First Search (DFS), Depth-Limited Search (DLS), Iterative Deepening (IDDFS). Know the exact Time Complexity, Space Complexity, Completeness, and Optimality proofs.
   - *Informed Search*: Greedy Best-First Search and $A^*$ Search.
     - **Admissible Heuristics**: $h(n) \le h^*(n)$ (guarantees optimality for tree search).
     - **Consistent / Monotonic Heuristics**: $h(n) \le c(n, a, n') + h(n')$ (guarantees optimality for graph search without re-opening closed nodes).
     - **Dominance**: If $h_2(n) \ge h_1(n)$ for all $n$, $h_2$ expands fewer or equal nodes.
2. **Local Search & Metaheuristics**:
   - Hill Climbing (local maxima, ridges, plateaus), Simulated Annealing (cooling schedules, Boltzmann distribution probability), Local Beam Search, Genetic Algorithms, and Swarm Intelligence (Particle Swarm Optimization, Ant Colony Optimization).
3. **Adversarial Search / Games**:
   - Minimax decision rule in zero-sum, perfect information games.
   - **$\alpha$-$\beta$ Pruning**: Pruning condition ($\alpha \ge \beta$). Be able to trace alpha-beta pruning trees by hand with 100% precision! Node ordering determines best-case complexity $O(b^{m/2})$.
4. **Constraint Satisfaction Problems (CSPs)**:
   - Variables, Domains, Constraints (unary, binary, higher-order).
   - Constraint Propagation: Arc Consistency (**AC-3 algorithm**).
   - Backtracking search with heuristics: Minimum Remaining Values (MRV / most constrained variable), Degree heuristic (tie-breaker), Least Constraining Value (LCV). Forward Checking.
5. **Automated Planning**:
   - STRIPS / PDDL language: States (positive literals), Actions (Preconditions, Add-list, Delete-list).
   - Progression (forward state-space search) vs Regression (backward goal-directed search).
   - **GraphPlan**:
     - Constructing planning graphs: Alternating proposition levels $S_i$ and action levels $A_i$.
     - Persistence actions (no-ops).
     - **Mutual Exclusion (Mutex) Relations**:
       - *Between Actions*: Inconsistent Effects, Interference, Competing Needs.
       - *Between Propositions*: Inconsistent Support (all actions achieving them are pairwise mutex).
     - Graph expansion until leveling off, followed by backward search.

---

### Module 2: Logic & Knowledge Representation (Prof. Paola Mello)
*Folder:* [`02 - Module 2 (Logic & Deductive Planning)/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Fundamentals%20of%20Artificial%20Intelligence%20and%20Knowledge%20Representation/02%20-%20Module%202%20(Logic%20&%20Deductive%20Planning))

1. **First-Order Logic (FOL) Formalism**:
   - Syntax: Constants, Predicates, Functions, Variables, Quantifiers ($\forall, \exists$).
   - Semantics: Interpretations, Models, Entailment ($\alpha \models \beta$), Satisfiability, Validity.
2. **Automated Theorem Proving & Resolution**:
   - Step-by-step conversion to **Conjunctive Normal Form (CNF)**:
     1. Eliminate biconditionals ($\alpha \leftrightarrow \beta$) and implications ($\alpha \to \beta$).
     2. Move negations inward (De Morgan’s laws, quantifier negations).
     3. Standardize variables (rename apart).
     4. **Skolemization**: Drop $\exists$ quantifiers by introducing Skolem constants or Skolem functions depending on preceding $\forall$ quantifiers.
     5. Drop universal quantifiers.
     6. Distribute $\lor$ over $\land$ into clauses.
   - Unification: Most General Unifier (MGU) algorithm.
   - Resolution Refutation Proof: Add $\neg \text{Goal}$ to knowledge base and derive the empty clause $\square$.
3. **Reasoning over Time & Deductive Planning**:
   - Situation Calculus: Situations, Fluents, Effect Axioms, Frame Problem, Successor-State Axioms.
4. **Logic Programming (Prolog)**:
   - Definite clauses, Horn clauses, SLD-resolution, unification, backtracking depth-first execution.

---

### Module 3: Probabilistic Reasoning & Uncertainty (Prof. Roberta Calegari)
*Folder:* [`03 - Module 3 (Probabilistic Reasoning & Uncertainty)/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Fundamentals%20of%20Artificial%20Intelligence%20and%20Knowledge%20Representation/03%20-%20Module%203%20(Probabilistic%20Reasoning%20&%20Uncertainty))

1. **Bayesian Networks**:
   - Directed Acyclic Graph (DAG) + Conditional Probability Tables (CPTs).
   - Joint Distribution Factorization:
     $$P(X_1, X_2, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))$$
   - Counting free parameters in CPTs vs full joint distribution.
2. **Conditional Independence & d-Separation**:
   - The 3 fundamental path motifs:
     - **Chain ($X \to Y \to Z$)**: $X \perp Z \mid Y$ (blocked when $Y$ is observed).
     - **Fork ($X \leftarrow Y \to Z$)**: $X \perp Z \mid Y$ (blocked when $Y$ is observed).
     - **Collider / V-structure ($X \to Y \leftarrow Z$)**: $X \perp Z$ when $Y$ and its descendants are **unobserved**; observing $Y$ (or its descendants) *activates* the path ("explaining away").
   - **Markov Blanket**: A node is conditionally independent of all other nodes in the network given its:
     $$\text{MB}(X) = \text{Parents}(X) \cup \text{Children}(X) \cup \text{Parents of Children}(X)$$
3. **Exact Inference**:
   - Enumeration algorithm (summing out hidden variables).
   - Variable Elimination (reordering factors, eliminating variables iteratively).
4. **Noisy-OR Distributions**:
   - Used for modeling multiple independent causes of a single binary effect.
   - Inhibition probability $q_i = P(\text{effect fails} \mid \text{cause}_i \text{ is true and other causes false})$.
   - Formula:
     $$P(\text{Effect} = \text{true} \mid \text{active causes } X_1, \dots, X_k) = 1 - \prod_{i: X_i = \text{true}} q_i$$

---

## 4. Student Challenge Strategy (+2 Bonus Points)
*Folder:* [`04 - Challenges & Labs/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Fundamentals%20of%20Artificial%20Intelligence%20and%20Knowledge%20Representation/04%20-%20Challenges%20&%20Labs)

Participating in one of the challenges can add up to **+2 bonus points** to your Module 1 score (which directly adds +1.0 point to your final grade out of 30!).

### Option A: Tablut Challenge (Recommended)
- **Problem**: Write an AI player in Python/Java/C++ to play *Tablut* (ancient Viking board game).
- **Core Algorithms**:
  - Minimax with $\alpha$-$\beta$ pruning.
  - Iterative Deepening with transposition tables (Zobrist hashing) to respect the per-move time limit.
  - Handcrafted heuristic function: King safety, King mobility, count of defenders vs attackers, open escape paths to borders.
- **Why Choose This**: Directly reinforces your study of Module 1 Game theory and allows easy empirical testing against baseline bots.

### Option B: NAO Planning Challenge
- **Problem**: Model a robotic dance/action routine for the humanoid robot NAO using automated planning tools.
- **Core Algorithms**: PDDL domain and problem definition, action preconditions/effects, solver integration.
- **Why Choose This**: Excellent if you are particularly interested in robotics and formal planning systems.

---

## 5. Study Checklist & High-Yield Pitfalls

- [ ] **Hand-trace $\alpha$-$\beta$ pruning**: Practice on at least 5 different game trees without looking at the solution. Common mistake: forgetting that $\alpha$ is updated only at MAX nodes and $\beta$ only at MIN nodes.
- [ ] **GraphPlan Mutexes**: Practice identifying all 3 action mutex conditions and proposition mutexes on the classical Dinner-Date or Cargo domains.
- [ ] **Skolemization with nested quantifiers**: Remember that $\forall x \exists y$ requires a Skolem function $f(x)$, whereas an unquantified $\exists y$ requires a Skolem constant $C$.
- [ ] **Bayesian Network Free Parameters**: For a binary variable with $k$ binary parents, the CPT requires $2^k$ rows, each with 1 free parameter ($2^k$ free parameters total). A full joint requires $2^{k+1} - 1$ parameters.
- [ ] **Solve `Excercise-FAIKR_M3_course_slides_2026.pdf`**: Complete every exercise on pages 1–46 covering medical test Bayes update, coin toss inference, nuclear plant alarm network, and Noisy-OR service availability.

