# Course Guide: Statistical & Mathematical Methods for Artificial Intelligence (StatMathAI)
**Course Location:** [`Statistical and Mathematical Methods for Artificial Intelligence/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Statistical%20and%20Mathematical%20Methods%20for%20Artificial%20Intelligence)  
**Primary Reference:** [`01 - Reference & Cheatsheets/StatMathAI-CheatSheet.pdf`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Statistical%20and%20Mathematical%20Methods%20for%20Artificial%20Intelligence/01%20-%20Reference%20&%20Cheatsheets/StatMathAI-CheatSheet.pdf)

---

## 1. Course Nature & Exam Strategy

StatMathAI provides the **mathematical spine** for modern machine learning, computer vision, and deep learning. 

The exam is a **rigorous written test consisting of analytical exercises, proofs, and numeric derivations**. You will typically be provided with the official **3-page Reference Sheet (`StatMathAI-CheatSheet.pdf`)**. 

> [!TIP]
> **Key Exam Insight**: Having the cheatsheet during the exam does not help unless you already know *how each formula is derived and applied*. Your goal during preparation is to attain fluent manual calculation speed without hesitating on linear algebra rules or matrix calculus identities.

---

## 2. The 3 Mathematical Modules

### Module 1: Linear Algebra, Spectral Theory, SVD & PCA
*Cheatsheet Sections: Matrix Algebra, Spectral Decomposition, SVD, PCA*

1. **Matrix Algebra & Properties**:
   - Column-vector convention: for $A \in \mathbb{R}^{m \times n}, x \in \mathbb{R}^n$, $Ax \in \mathbb{R}^m$, $(AB)^\top = B^\top A^\top$.
   - Symmetric matrices ($A = A^\top$), Orthogonal matrices ($Q^\top Q = Q Q^\top = I$, preserving lengths and angles: $\|Qx\|_2 = \|x\|_2$).
   - Trace identities: $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$, cyclic property $\text{tr}(ABC) = \text{tr}(BCA) = \text{tr}(CAB)$.
   - Positive Definiteness: $A \succ 0 \iff x^\top A x > 0$ for all $x \ne 0 \iff$ all eigenvalues $\lambda_i > 0$.
2. **Eigenvalues, Eigenvectors & Spectral Theorem**:
   - $Av = \lambda v \iff (A - \lambda I)v = 0 \iff \det(A - \lambda I) = 0$.
   - **Spectral Theorem for Real Symmetric Matrices**: Every real symmetric matrix $A \in \mathbb{R}^{n \times n}$ has $n$ real eigenvalues and an orthonormal basis of eigenvectors:
     $$A = Q \Lambda Q^\top = \sum_{i=1}^n \lambda_i q_i q_i^\top$$
3. **Singular Value Decomposition (SVD)**:
   - For any rectangular matrix $X \in \mathbb{R}^{n \times p}$ of rank $r$:
     $$X = U \Sigma V^\top$$
     - $U \in \mathbb{R}^{n \times n}$ is orthogonal (left singular vectors, eigenvectors of $X X^\top$).
     - $V \in \mathbb{R}^{p \times p}$ is orthogonal (right singular vectors, eigenvectors of $X^\top X$).
     - $\Sigma \in \mathbb{R}^{n \times p}$ is diagonal with singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$, where $\sigma_i = \sqrt{\lambda_i(X^\top X)}$.
4. **Principal Component Analysis (PCA)**:
   - Data matrix $X \in \mathbb{R}^{n \times p}$. Mean vector $\bar{x} = \frac{1}{n} X^\top \mathbf{1}_n$.
   - Centered matrix $\tilde{X} = X - \mathbf{1}_n \bar{x}^\top = (I_n - \frac{1}{n}\mathbf{1}\mathbf{1}^\top)X$.
   - Sample Covariance Matrix:
     $$S = \frac{1}{n-1} \tilde{X}^\top \tilde{X}$$
   - **Principal Directions**: Eigenvectors $v_1, v_2, \dots, v_p$ of $S$ sorted by decreasing $\lambda_j$.
   - **Principal Component Scores**: $Z = \tilde{X} V \in \mathbb{R}^{n \times p}$. Column $j$ of $Z$ has sample variance $\lambda_j$.
   - **Proportion of Variance Explained (PVE)**:
     $$\text{PVE}_j = \frac{\lambda_j}{\sum_{k=1}^p \lambda_k} = \frac{\sigma_j^2}{\sum_{k=1}^{\min(n,p)} \sigma_k^2}$$
   - Low-rank reconstruction and error minimization (Eckart-Young-Mirsky theorem).

---

### Module 2: Multivariable Calculus & Matrix Optimization
*Cheatsheet Sections: Matrix Derivatives, Taylor Expansions, Convexity*

1. **Matrix Differentiation**:
   - Gradient of linear form: $\nabla_x (a^\top x) = a$.
   - Gradient of quadratic form: $\nabla_x (x^\top A x) = (A + A^\top)x$. (If $A$ is symmetric: $2Ax$).
   - Matrix trace derivatives: $\nabla_A \text{tr}(AB) = B^\top$, $\nabla_A \text{tr}(A^\top A) = 2A$.
2. **Hessians & Optimality Conditions**:
   - Hessian matrix $H = \nabla^2 f(x) \in \mathbb{R}^{n \times n}$ ($H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$).
   - At critical point $\nabla f(x^*) = 0$:
     - $H(x^*) \succ 0$ (positive definite) $\implies$ Strict local minimum.
     - $H(x^*) \prec 0$ (negative definite) $\implies$ Strict local maximum.
     - $H(x^*)$ indefinite (both positive and negative eigenvalues) $\implies$ Saddle point.
3. **Convex Optimization**:
   - A twice-differentiable function $f$ is convex on a convex domain $\iff \nabla^2 f(x) \succeq 0$ for all $x$.
   - For convex functions, any local minimum is a global minimum.

---

### Module 3: Probability Theory & Statistical Inference
*Cheatsheet Sections: Random Vectors, Distributions, Estimation*

1. **Random Vectors & Affine Transformations**:
   - Mean vector $\mu = \mathbb{E}[X] \in \mathbb{R}^p$.
   - Covariance matrix $\Sigma = \text{Cov}(X) = \mathbb{E}[(X - \mu)(X - \mu)^\top] \in \mathbb{R}^{p \times p}$.
   - **Affine Transformation Law**: For $Y = AX + b$ with constant matrix $A$ and vector $b$:
     $$\mathbb{E}[Y] = A \mu + b, \quad \text{Cov}(Y) = A \Sigma A^\top$$
2. **Multivariate Gaussian Distribution $\mathcal{N}_p(\mu, \Sigma)$**:
   - Probability density function:
     $$f(x) = \frac{1}{(2\pi)^{p/2} |\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x - \mu)^\top \Sigma^{-1} (x - \mu)\right)$$
   - Contour surfaces are ellipsoids centered at $\mu$, with axes aligned along the eigenvectors of $\Sigma$ and lengths proportional to $\sqrt{\lambda_i}$.
   - If $X \sim \mathcal{N}_p(\mu, \Sigma)$, then $Y = AX + b \sim \mathcal{N}_q(A\mu + b, A\Sigma A^\top)$.
3. **Statistical Inference & Estimation**:
   - Likelihood $L(\theta; x) = \prod_{i=1}^n f(x_i; \theta)$, log-likelihood $\ell(\theta; x) = \sum_{i=1}^n \ln f(x_i; \theta)$.
   - Maximum Likelihood Estimator (MLE): $\hat{\theta}_{\text{MLE}} = \arg\max_\theta \ell(\theta)$.
   - Bias: $\text{Bias}(\hat{\theta}) = \mathbb{E}[\hat{\theta}] - \theta$. Unbiased if $\text{Bias} = 0$.
   - Mean Squared Error (MSE): $\text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + \text{Bias}(\hat{\theta})^2$.

---

## 3. Chronological Problem-Solving Plan

Work through the exercise and solution documents stored on disk in strict sequence:

```
[Solutions-Sep15] ──► [Solutions-16-09] ──► [Solutions 22-09] ──► [Solutions-29-09]
         │
         ▼
[Solutions-13-10] ──► [StatMathAI-SupEx-PCA] ──► [Solutions-27-10 / 27-10-b]
         │
         ▼
[Solutions-28-10] ──► [Solutions38-44] ──► [StatMathAI- Exercises.pdf]
```

### The "Derive-First" Practice Protocol
1. Open the exercise statement without opening the solution PDF.
2. Attempt the problem on blank paper with only `StatMathAI-CheatSheet.pdf` on your desk.
3. If stuck for >15 minutes, inspect *only* the first two lines of the solution PDF to see the starting substitution, then close it and finish on your own.
4. Red-pen any arithmetic errors, sign flips, or matrix non-commutativity bugs ($AB \ne BA$).

