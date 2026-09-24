# Pythagorean Theorem — Visual Proof

A visual proof of the **Pythagorean theorem** created using [Manim Community](https://www.manim.community/).

The animation uses geometric transformations to demonstrate the relationship between the sides of a right triangle.

## Theorem

For a right triangle with legs \(a\) and \(b\), and hypotenuse \(c\):

$$
a^2 + b^2 = c^2
$$

## Animation

The project visualizes the proof by constructing and transforming geometric shapes rather than relying solely on algebraic manipulation.

The final animation is available here:

**`preview.mp4`**

## Built With

* Python
* Manim Community Edition 0.21.0
* LaTeX

## Files

```text
pythagorean-theorem/
│
├── pythagorean_theorem.py
├── preview.mp4
└── README.md
```

## Running the Animation

From the project directory:

```bash
manim -pqm pythagorean_theorem.py vod
```

For a higher-quality render:

```bash
manim -p -qh pythagorean_theorem.py vod
```

## What I Learned

This project was created while learning Manim and explores:

* Creating and positioning geometric objects
* Animating transformations
* Working with mathematical expressions using `MathTex`
* Grouping and arranging objects
* Using transformations to communicate mathematical ideas visually

---

**Part of my [Manim Projects](../) repository.**
