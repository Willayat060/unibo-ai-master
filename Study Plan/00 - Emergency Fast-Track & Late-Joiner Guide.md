# Late-Joiner Emergency Survival Guide: November 5 to Exams
**UniBo Master in Artificial Intelligence – First Semester**  
*For Students Joining Mid-Semester (~6 Weeks Behind the Cohort)*

---

## 1. Take a Breath: The Italian Exam System Is on Your Side

If you just joined UniBo on November 5 and were told "exams are next month," your immediate reaction is likely panic. **Do not panic.**

The Italian university exam system (*sistema degli appelli*) operates completely differently from UK or US systems:
1. **December exams are NOT your only chance**: December dates (e.g., Dec 21–22) are *pre-appelli* (early sittings). The official Winter Exam Session runs across **January and February 2027**.
2. **Every course has multiple exam calls**:
   - **Call 1 (Early)**: Late December (optional for most courses).
   - **Call 2 (Winter 1)**: Mid/Late January 2027.
   - **Call 3 (Winter 2)**: Early/Mid February 2027.
   - *(Plus recovery sessions in June/July and September).*
3. **You NEVER have to take all 4 exams at once**: In Italy, students strategically distribute their exams across the exam windows.
4. **FAIKR Modules are 100% Independent**: In *Fundamentals of AI*, you can sit Module 1 in December or January, and Modules 2 & 3 in January or February. If you pass Module 1, your grade is saved permanently!

---

## 2. The 3-Wave Strategic Exam Distribution

Do **NOT** attempt to study 4 graduate courses simultaneously from scratch in 6 weeks. Instead, adopt the **3-Wave Triage**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE 3-WAVE ATTACK PLAN                          │
├────────────────────────┬───────────────────────┬───────────────────────┤
│ WAVE 1: DEC 21–22      │ WAVE 2: MID-LATE JAN  │ WAVE 3: EARLY FEB     │
│ (Target: 1 Exam)       │ (Target: 2 Exams)     │ (Target: 1 Exam / Ret)│
│                        │                       │                       │
│ • FAIKR Module 1       │ • FAIKR Modules 2 & 3 │ • StatMathAI or MLDM  │
│   (Search, Games,      │ • ILAI (Python,       │   (Whichever was      │
│   Planning - highly    │   Logic, Prolog)      │   deferred)           │
│   structured, 32 pts)  │ • OR MLDM (Python ML) │ • Or Grade Improvement│
└────────────────────────┴───────────────────────┴───────────────────────┘
```

### Why Target FAIKR Module 1 in December?
- Module 1 (Prof. Michela Milano) is algorithmic, deterministic, and visual: State Space Search ($A^*$, IDA*), Minimax & $\alpha$-$\beta$ pruning, and CSP (AC-3).
- It carries **32 points** (the largest single chunk of your FAIKR grade).
- Passing it on December 21 immediately locks in half your FAIKR grade, relieving enormous pressure for January.

---

## 3. Urgent "Day 1" Administrative Actions (Do These Today!)

1. **Enroll on Virtuale (`virtuale.unibo.it`)**:
   - Log in with your `@studio.unibo.it` credentials.
   - Self-enroll in all 4 course pages immediately to access all lecture slides, announcements, and lab code.
2. **Check Microsoft Teams**:
   - UniBo courses broadcast and record lectures on MS Teams. Search for the course teams and watch recorded lectures on $1.5\times$ speed for the topics taught in October.
3. **Contact the Course Tutors**:
   - Send a brief, polite email to let them know you matriculated today:
     - **FAIKR Tutors**: Matteo Francobaldi (`matteo.francobaldi2@unibo.it`), Chiara Bellatreccia (`chiara.bellatreccia2@unibo.it`).
     - **ILAI Tutor**: Federico Ruggeri (`federico.ruggeri6@unibo.it`).
     - *Key Question to Ask*: "Are there any mandatory in-class lab attendance requirements or group project registration deadlines I need to catch up on?"
4. **Find the Student Community**:
   - Join the Telegram / WhatsApp group for the LM AI 2026/2027 cohort. Italian student groups actively share past exam sheets (*compiti passati*), lecture notes (*sbobine*), and solution hints.

---

## 4. The 80/20 High-Yield Topic Matrix

To catch up 6 weeks of material in 40 days, cut out low-yield reading and focus strictly on high-probability exam questions:

### 1. FAIKR (Focus for December)
- [ ] **Uninformed vs Informed Search**: Master $A^*$ tree vs graph search, heuristic admissibility ($h(n) \le h^*(n)$), consistency ($h(n) \le c + h(n')$).
- [ ] **Adversarial Games**: Practice drawing Minimax trees with $\alpha$-$\beta$ pruning until you can do them flawlessly with zero hesitation.
- [ ] **CSPs**: Trace the AC-3 algorithm step-by-step; MRV and Degree heuristics.
- [ ] **GraphPlan**: Action mutexes (*Inconsistent Effects*, *Interference*, *Competing Needs*) and proposition mutexes.

### 2. Machine Learning & Data Mining (Focus for January)
- [ ] **Data Warehousing / DFM**: Know how to draw a Dimensional Fact Model from a business specification.
- [ ] **Classification Metrics**: Memorize Confusion Matrix calculations: Precision, Recall, $F_1$, and Cohen's Kappa ($\kappa$).
- [ ] **Scikit-Learn Boilerplate**: Practice writing an end-to-end `ColumnTransformer` + `Pipeline` + `GridSearchCV` without looking at docs.
- [ ] **Association Rules**: Support, Confidence, Lift, and Apriori principle.

### 3. StatMathAI (Focus for January/February)
- [ ] **Matrix Algebra & Spectral Theorem**: Orthonormal diagonalization $A = Q \Lambda Q^\top$.
- [ ] **SVD & PCA**: Understand how SVD ($X = U \Sigma V^\top$) connects to the covariance matrix $S = \frac{1}{n-1}\tilde{X}^\top \tilde{X}$ and Principal Component scores $Z = \tilde{X}V$.
- [ ] **Exam Cheatsheet Familiarity**: Download [`StatMathAI-CheatSheet.pdf`](file:///c:/Users/Wilayat Hussain/Documents/UniBo/Statistical%20and%20Mathematical%20Methods%20for%20Artificial%20Intelligence/01%20-%20Reference%20&%20Cheatsheets/StatMathAI-CheatSheet.pdf) and identify where every formula lives.

### 4. ILAI (Focus for January)
- [ ] **Python Aliasing & Memory**: Mutable vs immutable, shallow vs deep copy.
- [ ] **NumPy Broadcasting**: Array shapes and dimension matching rules.
- [ ] **Logic Resolution**: CNF conversion (Skolemization!) and resolution refutation.
- [ ] **Prolog Recursion**: Writing `member`, `append`, `reverse`, and understanding Green vs Red cuts.

---

## 5. Daily Catch-Up Study Rhythm (Next 40 Days)

Allocate **6 hours per day** of focused, distraction-free study:

- **Block 1 (09:00 – 11:30) | FAIKR Module 1**: Lecture slides + manual algorithmic tracing (preparing for the Dec 21 exam).
- **Block 2 (12:00 – 13:30) | Current Week's Classes**: Keep up with ongoing lectures so you don't fall further behind in November.
- **Block 3 (15:00 – 17:30) | Hands-on Coding / Math**: Alternating between MLDM Python labs and StatMath problem sets.
- **Block 4 (18:00 – 19:00) | Active Recall & Flashcards**: Review formulas, definitions, and theorems covered during the day.

