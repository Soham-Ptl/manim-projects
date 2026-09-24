from manim import *
from math import sqrt
from math import atan

class pythagorean_theorem(Scene):
    def construct(self):

        self.wait(1.5)
        # does the intro and give the triangle a background
        self.intro()

        tri1 = Polygon(LEFT * 2, UP * 3, ORIGIN, fill_color=BLUE, fill_opacity=0.5)
        sq = Square(side_length=5, stroke_color=BLUE)
        sq.z_index = 1
        tri1.z_index = 2
        a_label = MathTex(r"a")
        b_label = MathTex(r"b")
        c_label = MathTex(r"c")

        a_label.next_to(tri1, DOWN)
        b_label.next_to(tri1, RIGHT)
        c_label.move_to(LEFT + 1.75 * UP * 1.1)
        grp = VGroup(tri1, a_label, b_label, c_label)
        grp.z_index = 2

        self.play(Create(grp) , run_time = 2.5)
        self.play(FadeOut(self.text))
        self.play(grp.animate.shift(RIGHT * 2.5 + DOWN * 2.5))
        tri2 = tri1.copy()
        tri3 = tri1.copy()
        tri4 = tri1.copy()
        self.play( Create(sq), Create(tri2), Create(tri3), Create(tri4))

        self.play(tri2.animate.rotate( PI / 2).shift(UP * 2.5 + LEFT * 0.5))
        self.play(tri3.animate.rotate( PI ).shift(UP * 2 + LEFT * 3))
        self.play(tri4.animate.rotate( 3 * PI / 2).shift( LEFT * 2.5 + DOWN * 0.5))

        a2 = a_label.copy()
        a3 = a_label.copy()
        a4 = a_label.copy()
        b2 = b_label.copy()
        b3 = b_label.copy()
        b4 = b_label.copy()
        c2 = c_label.copy()
        c3 = c_label.copy()
        c4 = c_label.copy()

        a2.next_to(tri2, RIGHT)
        b2.next_to(tri2, UP)
        a3.next_to(tri3, UP)
        b3.next_to(tri3, LEFT)
        a4.next_to(tri4, LEFT)
        b4.next_to(tri4, DOWN)
        c2.shift(UP * 1.9 + LEFT * 0.75)
        c3.shift(UP * 1.35 + LEFT * 2.9)
        c4.shift(DOWN * 0.75 + LEFT * 2.1)
        

        grp2 = VGroup(tri2, a2, b2, c2)
        grp3 = VGroup(tri3, a3, b3, c3)
        grp4 = VGroup(tri4, a4, b4, c4)
        grp2.z_index = 2
        grp3.z_index = 2
        grp4.z_index = 2
        

        self.play(Create(a2), Create(b2), Create(a3), Create(b3), Create(a4), Create(b4), Create(c2), Create(c3), Create(c4))
        self.wait(1)

        # formation of big square
        self.square1() 
        
        self.wait(1)
        self.play(Indicate(c_label), Indicate(c2), Indicate(c3), Indicate(c4), run_time = 2)
        area1 = MathTex(r"c^2")
        area1.next_to(self.sq1, DOWN)
        self.play(Write(area1))
        self.wait(1)

        self.play(FadeOut(c_label), FadeOut(c2), FadeOut(c3), FadeOut(c4))
        grp.remove(c_label)
        grp2.remove(c2)
        grp3.remove(c3)
        grp4.remove(c4)
        
        # The relocation of the triangles forming 2 smaller squares
        self.play(grp4.animate.shift(UP * 3 + RIGHT * 2))
        self.play(grp3.animate.shift(DOWN * 2))
        self.play(grp.animate.shift(LEFT * 3))
        self.wait(1)

        # formation of 1st smaller square
        self.square2()
        self.play(Indicate(a3), Indicate(a4), run_time = 2)

        area2 = MathTex(r"a^2")
        area2.next_to(self.sq2, DOWN)
        plus1 = MathTex(r"+")
        plus1.next_to(self.sq2, RIGHT)
        plus2 = plus1.copy()
        plus2.next_to(area2, RIGHT)
        self.play(Write(area2))
        self.wait(1)
        self.play(Write(plus1), Write(plus2))

        # formation of 2nd smaller square
        self.square3()
        self.play(Indicate(b_label), Indicate(b4), run_time = 2)
        area3 = MathTex(r"b^2")
        area3.next_to(plus2, RIGHT)
        self.play(Write(area3))
        self.wait(1)


        # removes the primary construction of the project
        self.play(
            FadeOut(grp),
            FadeOut(grp2),
            FadeOut(grp3),
            FadeOut(grp4),
            FadeOut(sq)
        )
        
        lhs = VGroup(self.sq1, area1)
        rhs = VGroup(self.sq2, self.sq3, area2, area3, plus1, plus2)
        equal = MathTex(r"=")
        equal.shift(UP)

        self.play(
            lhs.animate.shift(RIGHT * 3.5),
            rhs.animate.shift(LEFT * 3),
            Write(equal)
        )
        self.wait(1)
        self.play(
            FadeOut(lhs),
            FadeOut(rhs),
            FadeOut(equal),
        )

        self.wait(0.5)
        equation = MathTex(r"c^2 = a^2 + b^2")
        equation.set_color(BLUE).scale(2)
        self.play(Write(equation))
        self.wait(1)
        self.play(
            Circumscribe(equation, buff = 0.3, color = WHITE),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(equation))
        self.wait(1)


    # Does the introduction to the video 
    def intro(self):
        self.text = VGroup(
            Text("Lets take a triangle with sides 'a', 'b' and"),
            Text("'c' such that c is the hypotenuse")
        ).arrange(DOWN)
        self.play(Write(self.text), run_time = 2)
        self.wait(1)
        self.play(self.text.animate.to_edge(DOWN, buff = 1.5).scale(0.5))


    # Constructs the square with area c^2
    def square1(self):
        c = sqrt(13)
        self.sq1 = Square(side_length = c, fill_color="GREEN", fill_opacity = 0.25, stroke_opacity = 0)
        angle = atan(3.0/2)
        self.sq1.rotate(angle)
        self.play(Create(self.sq1))
        self.wait(1.5)
        self.play(self.sq1.animate.rotate(-angle).scale(0.25).move_to(LEFT * 5 + UP), run_time = 1.5)

    # Constructs the square with area a^2
    def square2(self):
        a = 2
        self.sq2 = Square(side_length = a, fill_color="RED", fill_opacity = 0.25, stroke_opacity = 0)
        self.sq2.shift(1.5 * LEFT + 1.5 * UP)
        self.play(Create(self.sq2))
        self.wait(1.5)
        self.play(self.sq2.animate.scale(0.25).move_to(RIGHT * 4 + UP), run_time = 1.5)

    # Constructs the square with area b^2
    def square3(self):
        b = 3
        self.sq3 = Square(side_length = b, fill_color="RED", fill_opacity = 0.25, stroke_opacity = 0)
        self.sq3.shift(1 * RIGHT + 1 * DOWN)
        self.play(Create(self.sq3))
        self.wait(1.5)
        self.play(self.sq3.animate.scale(0.25).move_to(RIGHT * 5.5 + UP), run_time = 1.5)


