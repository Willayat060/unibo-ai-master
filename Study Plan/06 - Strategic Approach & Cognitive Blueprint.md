# Strategic Approach & Cognitive Blueprint: "How You Should Approach Things"
**Mastering the UniBo Artificial Intelligence Curriculum**

---

## 1. The Core Mindset Shift

Graduate-level Artificial Intelligence at the University of Bologna is **not about memorization**; it is about **algorithmic fluency, mathematical precision, and rapid software implementation**.

Students often struggle when they approach these 4 subjects with undergraduate habits—such as passively reading lecture slides or binge-watching videos. To score top marks (28–30L), adopt **active production over passive consumption**:

```
PASSIVE APPROACH (Low Retention, High Stress)
  Reading slides ──► Highlighting text ──► Looking at worked solutions ──► False confidence ──► Exam block
  
ACTIVE PRODUCTION (High Retention, 30L Mastery)
  Read 1 slide ──► Close slide ──► Re-derive on blank paper ──► Code from scratch ──► Explain aloud
```

---

## 2. The 3 Specialized Study Protocols

Because your courses span mathematics, theoretical algorithms, and software engineering, you must switch between **three distinct study modes**:

### Mode 1: The "Derive-First" Protocol (For StatMathAI & FAIKR Module 3)
*Never read a mathematical solution.*
1. **The Blank Page Rule**: When working on an exercise (e.g., finding the principal components of a matrix or computing posterior probability in a Bayes Net), take a blank sheet of paper and write only the problem statement.
2. **Dimension & Type Check**: Write the dimension of every symbol before starting ($X \in \mathbb{R}^{n \times p}$, $w \in \mathbb{R}^p$, $y \in \mathbb{R}^n$). 80% of student math mistakes come from multiplying incompatible matrices.
3. **The 15-Minute Wall**: Struggle for at least 15 minutes before peeking at the solution. If stuck, look only at the first line, cover it, and continue on your own.
4. **Boundary Sanity Check**:
   - Probabilities must strictly be $\in [0, 1]$. If you calculate $1.15$, stop immediately.
   - Variances and eigenvalues of covariance matrices must be non-negative ($\lambda_i \ge 0$).
   - Heuristics must be non-negative ($h(n) \ge 0$) and $h(\text{goal}) = 0$.

### Mode 2: The "Hand-Tracing" Protocol (For FAIKR Modules 1 & 2)
*Written exams require manual algorithmic execution.*
1. **Minimax & $\alpha$-$\beta$ Trees**: Draw out deep game trees. Practice tracing with a pencil, explicitly writing $\alpha$ and $\beta$ values next to every node. Ensure you know the exact instant a branch is pruned ($\alpha \ge \beta$).
2. **GraphPlan Mutex Drills**: On a blank grid, manually draw levels $S_0, A_0, S_1, A_1, S_2$. Explicitly annotate the 3 action mutexes (*Inconsistent Effects*, *Interference*, *Competing Needs*) and proposition mutexes (*Inconsistent Support*).
3. **Logic Resolution**: For FOL questions, practice the 6 steps of CNF conversion by hand: eliminating implications, pushing negations, standardizing variables, Skolemizing (checking for preceding $\forall$), dropping universal quantifiers, and distributing disjunctions.

### Mode 3: The "Bug-First" Protocol (For MLDM & ILAI Labs)
*Writing code that works is only the first half; knowing why it breaks is what wins exams.*
1. **Predict Before Run**: When reading code from `files-L2` to `files-L9`, write down on paper what the output will be before executing the script.
2. **Break It Intentionally**:
   - Mutate an immutable object or create a circular reference to see the traceback.
   - Force an array shape mismatch in NumPy to master broadcasting semantics.
   - In scikit-learn, intentionally leak test data into the training scaler and observe the overfitted score change.
3. **Template Fluency**: Practice typing an entire cross-validated, regularized scikit-learn pipeline inside a blank Jupyter notebook in under 5 minutes without consulting documentation.

---

## 3. Cognitive Techniques for Long-Term Retention

### 1. The Feynman Technique for Complex AI Concepts
If you cannot explain an algorithm in simple language without jargon, you do not understand it.
- **Test yourself on**:
  - *Why does $A^*$ require consistency (monotonicity) for graph search, but only admissibility for tree search?*
  - *Why does observing a collider node in a Bayesian network activate dependence between previously independent causes ("explaining away")?*
  - *Why do we compute the eigenvectors of the sample covariance matrix $S$ in PCA rather than the original matrix $X$?*
  - *What is the difference between a Green Cut and a Red Cut in Prolog?*

### 2. Spaced Repetition (The 1-3-7 Rule)
For high-density theoretical topics:
- **Day 1**: Learn and re-derive the concept.
- **Day 3**: Without looking at your notes, write a 1-page summary from memory.
- **Day 7**: Solve 2 past exam problems on that topic under timed conditions.

---

## 4. Multi-Course Balancing & Context Switching

Managing 4 demanding Master's courses simultaneously leads to mental fragmentation if you switch subjects every 30 minutes.

### The "Complementary Pairing" Strategy
Pair one **mathematical/theoretical** subject with one **coding/hands-on** subject each day:

| Day Pair | Morning Focus (Theory / Math) | Afternoon / Evening Focus (Code / Implementation) |
| :--- | :--- | :--- |
| **Pair 1 (Algorithms & Code)** | **FAIKR** (Search, Games, Planning) | **ILAI** (Python, Prolog, MiniZinc) |
| **Pair 2 (Data & Statistics)** | **StatMathAI** (Linear Algebra, PCA, Calculus) | **MLDM** (Pipelines, scikit-learn, Labs) |

### The 90-Minute Deep Work Block
- Block 1: 90 minutes of pure focus (phone on airplane mode, zero multitasking).
- Break: 15 minutes of movement/offline rest.
- Block 2: 90 minutes of problem-solving or coding.
- *Two 90-minute blocks of deep work achieve more than 8 hours of distracted studying.*

---

## 5. Strategic Challenge Decision: Tablut vs NAO (+2 Points)

The Tablut Challenge or NAO Challenge offers up to **+2 bonus points** on Module 1 of FAIKR.
- **Should you do it?**
  - **YES, IF**: You can start right now in November, work with a partner, and build a clean Minimax bot with basic heuristic evaluation in under 20 total coding hours. It directly boosts your final grade by +1.0 point out of 30!
  - **NO, IF**: You are severely behind on StatMathAI or MLDM labs. Spending 60+ hours fine-tuning a Tablut bot at the expense of failing StatMathAI is a net negative. Protect your core course passing threshold first.

---

## 6. Exam Room Execution Strategy

When you sit down for written exams (FAIKR, StatMathAI, MLDM):

1. **The First 5 Minutes (Triage)**:
   - Read the entire exam paper before writing anything.
   - Categorize questions into:
     - **Green**: Immediately obvious, standard calculations $\to$ Solve these first to bank guaranteed points and build confidence.
     - **Yellow**: Requires substantial manual tracing or algebraic steps $\to$ Solve second.
     - **Red**: Novel proofs or complex edge cases $\to$ Leave for the end.
2. **Show Every Intermediate Step**:
   - Italian university professors award generous partial credit for clear, structured reasoning even if an arithmetic calculation error occurs at the very end.
   - Always state assumptions clearly: *"Assuming tree search with admissible heuristic $h(n)$..."*
3. **The 15-Minute Final Audit**:
   - Never leave an exam early.
   - Check negative signs, matrix multiplication dimensions, and probability normalizations.

