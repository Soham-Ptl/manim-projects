from manim import *


class GeometricSeries(Scene):
    def construct(self):
        N = 13          # total number of squares expliucitly drawn
        S = 4           # side length of the greatest square   
        colors = color_gradient([BLUE, TEAL, GREEN, YELLOW, ORANGE, RED], N)        # the color gradient for colouring the consecutive squares

        # latex to display: 1/2 + 1/4 + 1/8 + 1/16 + ...
        title = MathTex(
            r"\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \cdots",
            font_size=44
        ).to_edge(UP)       
        self.play(Write(title))

        # creates the outer square whose side llength is 1
        square = Square(side_length=S, color=WHITE, stroke_width=4)
        square.shift(DOWN * 0.3)
        one_label = MathTex("1", font_size=36).next_to(square, LEFT)
        self.play(Create(square), FadeIn(one_label))
        self.wait(1)

        
        # labels each square as S0, S1, S2, ...
        sum_text = MathTex(r"S_0 = 0", font_size=40).next_to(square, DOWN)
        self.play(Write(sum_text))

        
        left = square.get_left()[0]
        top = square.get_top()[1]
        w, h = S, S


        # iterates and creates the individual rectangles/square with area 1/2, 1/4 and so on
        shapes = VGroup()
        for n in range(1, N + 1):
            if n % 2 == 1:
                pw, ph = w / 2, h
                center = np.array([left + pw / 2, top - ph / 2, 0])
                from_edge = LEFT
                left += w / 2
                w = w / 2
            else:
                pw, ph = w, h / 2
                center = np.array([left + pw / 2, top - ph / 2, 0])
                from_edge = UP
                top -= h / 2
                h = h / 2

            rect = Rectangle(
                width=pw,
                height=ph,
                fill_color=colors[n - 1],
                fill_opacity=0.75,
                stroke_color=WHITE,
                stroke_width=2,
            ).move_to(center)
            shapes.add(rect)

            new_sum = MathTex(
                rf"S_{{{n}}} = \frac{{{2**n - 1}}}{{{2**n}}}", font_size=40
            ).next_to(square, DOWN)

            self.play(
                GrowFromEdge(rect, from_edge),
                ReplacementTransform(sum_text, new_sum),
                run_time=1.0 if n <= 4 else 0.6,
            )
            sum_text = new_sum

            # writes the area of first 6 rectangles/squares
            if n <= 6:
                label = MathTex(
                    rf"\frac{{1}}{{{2**n}}}", font_size=36 if n <= 4 else 22
                ).move_to(rect)
                shapes.add(label)
                self.play(FadeIn(label), run_time=0.4)

            self.wait(0.5)


        # To show that the remaining area shrinks to 0
        leftover = np.array([left + w / 2, top - h / 2, 0])
        arrow = Arrow(
            square.get_corner(DR) + RIGHT * 1.5 + DOWN * 0.2,
            leftover,
            buff=0.05,
            color=YELLOW,
        )
        note = Text("what's left shrinks to 0", font_size=24, color=YELLOW).next_to(
            arrow.get_start(), RIGHT, buff=0.1
        )
        self.play(GrowArrow(arrow), FadeIn(note))
        self.wait(1)


        # removes all the remaining elements from the scene
        self.play(
            FadeOut(shapes),
            FadeOut(square),
            FadeOut(one_label),
            FadeOut(arrow),
            FadeOut(note),
            FadeOut(sum_text),
        )

        
        # moves the title below and the summation formula above 
        self.play(title.animate.scale(1.2).move_to(UP * 0.8))
        formula = MathTex(
            r"\sum_{n=1}^{\infty} \frac{1}{2^n}", "=", "1", font_size=56
        ).next_to(title, DOWN, buff=0.9)
        self.play(Write(formula), run_time = 1.5)
        self.wait(0.5)
        self.play(FadeOut(formula), FadeOut(title))


        # writes the conclusion and the final infinite series summation
        conclusion = MathTex(
            r"\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} + \cdots \;=\; 1",
            font_size=50,
            color = BLUE
        )
        self.play(Write(conclusion), run_time = 2)
        self.wait(2)
        self.play(FadeOut(conclusion))
        self.wait(1)