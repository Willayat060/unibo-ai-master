# Course Guide: Introduction to Languages for Artificial Intelligence (ILAI)
**Instructors & Tutors:** Prof. Paolo Felli (`paolo.felli@unibo.it`), Federico Ruggeri (`federico.ruggeri6@unibo.it`), Michael Lodi  
**Course Location:** [`Introduction to Languages for Artificial Intelligence/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Introduction%20to%20Languages%20for%20Artificial%20Intelligence)

---

## 1. Course Philosophy & Pedagogical Structure

ILAI is designed to equip students with **two distinct computational mindsets** required in modern artificial intelligence:
1. **Imperative & Vectorized Scientific Computing (Python & NumPy)**: Deep understanding of Python memory models, OOP architecture, and vectorized array computation for data manipulation.
2. **Declarative & Symbolic AI (Logic, Prolog & MiniZinc)**: Specifying *what* a solution looks like using formal logic and constraints, letting inference engines search for the solution.

---

## 2. Topic Checklist & Concept Mastery

### Track 1: Python Deep Dive & Scientific Computing
*Lectures & Notes:* [`02 - Python Lectures/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Introduction%20to%20Languages%20for%20Artificial%20Intelligence/02%20-%20Python%20Lectures), [`03 - Lab Notes/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Introduction%20to%20Languages%20for%20Artificial%20Intelligence/03%20-%20Lab%20Notes)  
*Code Packages:* [`04 - Lab Code & Files/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Introduction%20to%20Languages%20for%20Artificial%20Intelligence/04%20-%20Lab%20Code%20&%20Files)

- [ ] **Python Memory Model & Aliasing (`files-L4`)**:
  - Python variables are name bindings (references) to heap objects, not typed memory buckets.
  - Mutable (`list`, `dict`, `set`) vs Immutable (`int`, `float`, `tuple`, `str`, `frozenset`).
  - Identity (`is`) checks memory address `id()`; equality (`==`) checks value equivalence `__eq__()`.
  - Aliasing bug: `a = [1, 2]; b = a; b.append(3)` mutates `a`!
  - Shallow copy (`list.copy()`, `copy.copy()`) copies only outer references; nested objects remain shared. Deep copy (`copy.deepcopy()`) duplicates the entire recursive object tree.
- [ ] **Comprehensions & Generators (`files-L5`)**:
  - List/dict/set comprehensions: syntax, readability, speed advantages over `for` loops.
  - Generator functions with `yield`: lazy evaluation, constant memory consumption $O(1)$ across infinite streams or multi-gigabyte data feeds.
  - Generator expressions: `(x**2 for x in data)` vs list comprehension `[x**2 for x in data]`.
- [ ] **Object-Oriented Architecture & Design Patterns (`files-L6`, `files-L7`)**:
  - Encapsulation, `self`, dunder methods (`__init__`, `__repr__`, `__str__`, `__getitem__`, `__len__`).
  - **Inheritance vs Delegation**: When to subclass vs when to wrap an inner object and delegate method calls (Composition over Inheritance).
  - Abstract Base Classes (`from abc import ABC, abstractmethod`): Enforcing interface contracts.
- [ ] **NumPy Lab Mastery (`6 - NumPy lab.pdf`, `files-L9`)**:
  - Memory buffer layout: Continuous C-order vs Fortran-order, shapes, strides, and `dtype`.
  - **Views vs Copies**: Basic slicing (`arr[1:5]`) creates a memory view (modifying it changes original array!); advanced indexing (`arr[[0, 2]]` or boolean masks) returns a copy.
  - **Broadcasting Rules**: Two dimensions are compatible when:
    1. They are equal, OR
    2. One of them is 1.
    - Adding dimensions with `np.newaxis` or `None`.
  - Vectorized operations: Eliminating Python loops for multi-order-of-magnitude speedups. Axis reductions (`np.sum(A, axis=0)` vs `np.sum(A, axis=1)`).

---

### Track 2: Logic, Logic Programming & Constraint Solving
*Lectures & Notes:* [`01 - Logic & Theory Lectures/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Introduction%20to%20Languages%20for%20Artificial%20Intelligence/01%20-%20Logic%20&%20Theory%20Lectures)

- [ ] **Propositional Logic & Resolution (`1.Intro.Logica` to `4.Resolution_PL`)**:
  - Truth tables, validity, satisfiability, tautologies, contradictions.
  - Clausal Normal Form (CNF): sets of clauses where each clause is a disjunction of literals.
  - Resolution inference rule: from $(A \lor B)$ and $(\neg B \lor C)$, infer $(A \lor C)$.
  - Resolution refutation proofs.
- [ ] **First-Order Logic & Foundations of LP (`5.First_Order_Logic`, `6.LP`)**:
  - Predicates, functions, quantifiers, substitution, Most General Unifier (MGU).
  - Horn clauses: clauses with at most one positive literal:
    - Definite clause: $H \leftarrow B_1 \land B_2 \land \dots \land B_n$ (one positive head, negative body literals).
    - Fact: $H \leftarrow \text{true}$.
    - Goal / Query: $\leftarrow B_1 \land B_2 \land \dots \land B_n$.
- [ ] **Prolog Mastery (`7.Prolog.pdf`)**:
  - Declarative reading (logical implication) vs Procedural reading (procedure calls).
  - The Execution Model: SLD-resolution, depth-first search of the goal tree with backtracking.
  - List manipulation via `[Head | Tail]`:
    - `member(X, [X|_]). member(X, [_|T]) :- member(X, T).`
    - `append([], L, L). append([H|T], L, [H|R]) :- append(T, L, R).`
    - Accumulator pattern for tail recursion.
  - **The Cut Operator (`!`)**:
    - Discards all alternative choice points created since the parent goal was entered.
    - *Green Cut*: Improves execution efficiency without changing declarative solutions.
    - *Red Cut*: Changes the logical set of answers (dangerous if not reasoned carefully).
  - Negation as Failure (`\+`): Closed World Assumption (if a statement cannot be proved from the knowledge base, it is assumed false).
- [ ] **Constraint Programming & MiniZinc (`8.Constraint_Programming_I`, `9.MiniZinc.pdf`)**:
  - Variables, Domains, Constraints.
  - MiniZinc model anatomy:
    ```minizinc
    % Parameters and decision variables
    int: n = 8;
    array[1..n] of var 1..n: q; % n-queens
    
    % Constraints
    include "alldifferent.mzn";
    constraint alldifferent(q);
    constraint alldifferent([q[i] + i | i in 1..n]);
    constraint alldifferent([q[i] - i | i in 1..n]);
    
    % Solve and output
    solve satisfy;
    output ["Queen positions: ", show(q)];
    ```
  - Global constraints: `alldifferent`, `cumulative`, `circuit`.
  - Symmetry breaking constraints (ordering symmetric solutions to prune search spaces).
- [ ] **Neurosymbolic AI Overview (`10.Neurosymbolic.pdf`)**:
  - Strengths and limitations of pure symbolic AI (interpretable, sound, brittle to noise, poor at sensory data) vs pure deep learning (robust, pattern recognition, data-hungry, uninterpretable black box).
  - Hybrid paradigms: Knowledge Graph embeddings, Logic Tensor Networks, DeepProbLog.

---

## 3. Practical Coding Practice Routine

1. **Extract and test each Python ZIP file** (`files-L2` to `files-L9`): Run each script, predict the output *before* running, and verify if aliasing or class delegation behaves as expected.
2. **Prolog Coding Drills**: Implement classical recursive predicates without using built-ins:
   - `len(List, N)`
   - `reverse(List, Reversed)` (both naive and accumulator version)
   - `flatten(NestedList, FlatList)`
   - Solve a puzzle (e.g. 4-Queens or Einstein riddle) using pure Prolog unification and backtracking.
3. **MiniZinc CSP Exercises**:
   - Model the Map Coloring problem with 4 colors.
   - Model the Send + More = Money cryptarithmetic puzzle.

