# Infinite Series — Sum of a Geometric Series

A mathematical animation created using [Manim Community](https://www.manim.community/) and Python to visualize the infinite geometric series whose sum converges to 1.

The animation explores how an infinite number of progressively smaller terms can add up to a finite value.

## Mathematical Concept

The infinite series is:

\[
\frac12+\frac14+\frac18+\frac1{16}+\cdots=1
\]

Each term is half the size of the previous term. As more terms are added, the partial sum gets closer and closer to 1.

For a geometric series with first term \(a\) and common ratio \(r\), where \(|r|<1\), the infinite sum is:

\[
S_\infty=\frac{a}{1-r}
\]

For this series, \(a=\frac12\) and \(r=\frac12\), giving:

\[
S_\infty=\frac{\frac12}{1-\frac12}=1
\]

## Animation

The animation visualizes the addition of successive terms and illustrates how the sum approaches 1.

**Preview:** [Watch the animation](./preview.mp4)

## Built With

- Python
- Manim Community Edition 0.21.0
- LaTeX

## Files

```text
infinite-series/
│
├── infinite_series.py
├── preview.mp4
└── README.md
```

## Running the Animation

From the project directory, run:

```bash
manim -pqm infinite_series.py vod
```

For a higher-quality render:

```bash
manim -p -qh infinite_series.py vod
```

Replace `vod` with your scene class name if it differs.

## What I Learned

This project explores:

- Visualizing infinite series and convergence
- Representing mathematical concepts through animation
- Animating successive terms and partial sums
- Using Manim to communicate abstract mathematical ideas

---

**Part of my [Manim Projects](../) repository.**