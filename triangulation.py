# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 08:37:48 2022

@author: guillaume
"""

from manim import *

class LoidesSinus(Scene):
    def construct(self):
            cycle = [LEFT, DOWN, RIGHT, UP]
            dict_color = {"A": RED,
                          "a": RED,
                          "\alpha": RED,
                          "B": YELLOW,
                          "b": YELLOW,
                          "\beta": YELLOW,
                          "C": BLUE,
                          "c": BLUE,
                          "\gamma": BLUE, 
                          "sin(": WHITE} 
            sc = 0.5
            sc_f = 1.5
            ind_kw = {
                'run_time': 4
                }
            play_kw = {
                'run_time': 3
                }
            sur_kw = {
                'run_time': 1
                }
            def montre_longueur(triangle, idx):
                [A, B, C] = [triangle.get_vertices()[i] for i in range(3)]
                [I, J, K] = [0.5*(B+C), 0.5*(A+C), 0.5*(A+B)]
                txtA = Tex('A', substrings_to_isolate=["A"]).next_to(A, RIGHT)
                txtB = Tex('B', substrings_to_isolate=["B"]).next_to(B, LEFT)
                txtC = Tex('C', substrings_to_isolate=["C"]).next_to(C, LEFT)
                txt_a = Tex('a', substrings_to_isolate=["a"]).next_to(I, cycle[idx])
                txt_b = Tex('b', substrings_to_isolate=["b"]).next_to(J, cycle[(idx+1)%4])
                txt_c = Tex('c', substrings_to_isolate=["c"]).next_to(K, cycle[(idx+3)%4])
                angleA = Angle.from_three_points(B, A, C, color=RED)
                angleB = Angle.from_three_points(A, B, C, color=YELLOW, other_angle=True)
                angleC = Angle.from_three_points(B, C, A, color=GREEN, other_angle=True)
                txt_aa = MathTex(r"\alpha").next_to(angleA, LEFT, buff=0.1)
                txt_bb = MathTex(r"\beta").next_to(angleB, DR, buff=0.1)
                txt_cc = MathTex(r"\gamma").next_to(angleC, UP, buff=0.1)
                notation = (txtA, txtB, txtC, txt_a, txt_b, txt_c, angleA, txt_aa, angleB, txt_bb, angleC, txt_cc)
                for elt in notation:
                    elt.set_color_by_tex_to_color_map(dict_color).scale(sc)
                self.play(FadeIn(txtA, txtB, txtC), **play_kw)
                self.play(FadeIn(txt_a, txt_b, txt_c), **play_kw)
                self.play(FadeIn(angleA, txt_aa, angleB, txt_bb, angleC, txt_cc), **play_kw)
                figure = VGroup(triangle, *notation)
                self.play(figure.animate.shift(4*LEFT), play_kw)
                titre = Text("Rappels sur la loi des sinus")
                eq1 = MathTex(r"{{{a}} \over sin({{\alpha)}}} = {{{b}} \over sin({{\beta}})} = {{{c}} \over sin({{\gamma}})}")
                eq2 = MathTex(r"\text{Or, }{{\alpha}} = \pi - ({{\beta}}+ {{\gamma}})")
                eq3 = Tex("et comme $sin(\pi-x)=sin(x)$, on a:")
                eq4 = MathTex(r"{{{a}} \over {{sin(\pi - ({{\beta}} + {{\gamma}}))}}} = {{{b}} \over sin({{\beta}})} = {{{c}} \over sin({{\gamma}})}") 
                eq5 = MathTex(r"{{{a}} \over {{{{sin(}}{{\beta}} + {{\gamma}})}}} = {{{b}} \over sin({{\beta}})} = {{{c}} \over sin({{\gamma}})}")
                
                eqs = Group(titre, eq1, eq2, eq3, eq4, eq5).scale(sc).arrange(DOWN, buff=0.25).next_to(triangle.get_right(), 3*RIGHT)
                for i, eq in enumerate(eqs[:-1]):
                    eq.set_color_by_tex_to_color_map(dict_color)
                    self.play(Write(eq), **play_kw)
                    if i==2:
                        self.remove(txt_aa)
                        self.play(FadeIn(MathTex(r"\pi - ({{\beta}} + {{\gamma}})").scale(0.5).next_to(angleA, LEFT).set_color_by_tex_to_color_map(dict_color)))
                eq5.set_color_by_tex_to_color_map(dict_color)
                self.play(TransformMatchingTex(eq4, eq5), **play_kw)
                ref = Tex(r"On peut donc calculer 2 côtés à partir d'un côté et de deux angles:").scale(0.5).next_to(eq5.get_bottom(), DOWN, buff=0.5)
                self.play(Write(ref), **play_kw)
                self.wait(2)
                self.play(Indicate(Line(B,C).shift(4*LEFT), scale_factor=sc_f),
                          Indicate(Dot(A).shift(4*LEFT), scale_factor=sc_f),
                          Indicate(Dot(B).shift(4*LEFT), scale_factor=sc_f),
                          Indicate(Dot(C).shift(4*LEFT), scale_factor=sc_f),
                          Indicate(angleB, scale_factor=sc_f),
                          Indicate(angleC, scale_factor=sc_f),
                          **ind_kw)
                eq = MathTex(r"{{b}} = {{a}} {sin({{\beta}} ) \over sin({{\beta}} + {{\gamma}})}").scale(0.5).next_to(ref, DOWN)
                self.play(Write(eq.set_color_by_tex_to_color_map(dict_color)), **play_kw)
                self.play(Create(SurroundingRectangle(eq, color=YELLOW)), **sur_kw)
                eq2 = MathTex(r"{{c}} = {{a}} {sin({{\gamma}} ) \over sin({{\beta}} + {{\gamma}})}").scale(0.5).next_to(eq, DOWN)
                self.play(Write(eq2.set_color_by_tex_to_color_map(dict_color)), **play_kw)
                self.play(Create(SurroundingRectangle(eq2, color=YELLOW)), **sur_kw)
                
                
            a, b = 4, 3
            A = [a, 1, 0]
            B = [-1, b, 0]
            C = [0, -1, 0]
            tri = Polygon(A, B, C).set_fill(BLUE, opacity=0.5)
            self.play(tri.animate, **play_kw)
            montre_longueur(tri, 0)


# class triangles(Scene):

#     def construct(self):

#         def inter(A, B, C, D):
#             a1 = (B[1] - A[1])/(B[0] - A[0])
#             b1 = A[1] - a1 * A[0]
#             a2 = (D[1] - C[1])/(D[0] - C[0])
#             b2 = C[1] - a2 * C[0]
#             x = - (b2 - b1)/(a2 - a1)
#             y = a1 * x + b1
#             return ([x, y, 0])
        

#         LoiDesSinus()
        
#         self.clear()
        
#         dict_color = {
#                       "\alpha _1": GREEN,
#                       "\alpha _2": YELLOW,
#                       }
#         play_kw = {"run_time": 3}
        
#         A = [-6, 0, 0]
#         B = [0, 1, 0]
#         C = [-2, 2,0]
#         D = [1, -2, 0]
#         sc = 0.5
#         points = [Dot(p, color=RED) for p in [A, B, C, D]]
#         txt = [Text(p) for p in ["A", "B", "C", "D"]]
#         AB = Line(start=A, end=B, color=WHITE)
#         AD = Line(start=A, end=D, color=WHITE)
#         CD = Line(start=C, end=D, color=WHITE)
#         BC = Line(start=B, end=C, color=WHITE)
#         BD = Line(start=B, end=D, color=WHITE)
#         H = Dot(inter(A, B, C, D), color=RED)
#         # instructions = ([Text('Mesure la distance AC'), 
#         #                 Text('Mesure les angles a, A et C. On en déduit:'), 
#         #                 MathTex(r'CD = AC \frac{sin(A)}{sin(A+C)} et AD = AC \frac{sin(C)}{sin(A+C)}'), 
#         #                 MathTex(r"AH=AD\frac{sin(\hat D)}{sin(\hat a +\hat D)}"),
#         #                 Text("De même, mesure les angles c, B et b"),
#         #                 Text("on en déduit BH et BC par:"),
#         #                 MathTex(r'BC = CD \frac{sin(B)}{sin(c)} et BH = BC \frac{sin(C)}{sin(c+b)}'), 
#         #                 Text('Enfin'),
#         #                 MathTex(r'AB = AH + HB')
#         #                 ])
#         # x = Group(*instructions).scale(0.5*sc).arrange(DOWN, buff=0.25).move_to([6,0,0])
        
#         self.play(Create(points[0]), Create(txt[0].next_to(A, LEFT).scale(sc)), 
#                   Create(points[1]), Create(txt[1].next_to(B).scale(sc)))
#         obj = Text("On cherche la distance AB").move_to([4,3,0]).scale(sc)
#         ref = obj
#         self.play(AnimationGroup(Create(AB), Write(obj), lag_ratio=0.25), **play_kw)
#         self.play(FadeOut(Tex("Prenons 2 points C et D de part et d'autre de AB").scale(sc).next_to(ref, DOWN)),
#                   Create(points[2]), Write(txt[2].next_to(C, UP).scale(sc)), 
#                   Create(points[3]), Write(txt[3].next_to(D).scale(sc)), **play_kw)
                
#         self.play(FadeOut(Tex("Mesure la distance AC").scale(sc).next_to(ref, DOWN)),
#                   Create(Line(start=A, end=C, color=RED)), **play_kw)
#         dist_CD = Tex("On va calculer la distance CD").scale(sc).next_to(ref, DOWN)
#         self.play(Write(dist_CD), Create(AD), Create(CD), **play_kw) 
#         ref = dist_CD
#         a1 = Angle.from_three_points(D, A, B, color=RED, radius=0.5)
#         eq_a1 = MathTex(r"\alpha _1").scale(sc).set_color(RED)
#         self.play(FadeOut(Tex(r"Mesure $\alpha _1$ l'angle DAB").scale(sc).next_to(ref, DOWN)), 
#                   Create(a1), Write(eq_a1.next_to(a1, DOWN)), **play_kw)
#         a2 = Angle.from_three_points(B, A, C, color=RED)
#         eq_a2 = MathTex(r"\alpha _2").scale(sc).set_color(RED)
#         self.play(FadeOut(Tex(r"Mesure $\alpha _2$ l'angle CAD").scale(sc).next_to(ref, DOWN)),
#                   Create(a2), Write(eq_a2.next_to(a2, UP)), **play_kw)
#         c2 = Angle.from_three_points(A, C, D, color=RED)
#         eq_c2 = MathTex(r"\gamma _2").scale(sc).set_color(RED)
#         self.play(FadeOut(Tex(r"Mesure $\gamma _2$ l'angle ACD").scale(sc).next_to(ref, DOWN)),
#                   Create(c2), Write(eq_c2.next_to(c2, DOWN, buff=0.1)), **play_kw)
#         d2 = Angle.from_three_points(C, D, A, color=YELLOW)
#         eq_d2 = MathTex(r"\pi - (\gamma _2 + \alpha _2 + \alpha _1)").scale(sc).set_color(YELLOW)
#         self.play(FadeOut(Text("On en déduit l'angle CDA").scale(sc).next_to(ref, DOWN)),
#                   Create(d2), Write(eq_d2.next_to(d2, LEFT+DOWN, buff=0.1)), **play_kw)        
#         self.play(FadeOut(Text(r"par la loi des sinus, on peut calculer CD").scale(sc).next_to(ref, DOWN)), 
#                   **play_kw)
#         eq_CD1 = MathTex(r"{{{AC}} \over {{sin(\alpha _1 + \alpha _2+ \gamma _2)}}} = {{{CD}} \over {{sin(\alpha _1 + \alpha _2)}}}").scale(sc).next_to(ref, DOWN)
#         eq_CD2 = MathTex(r"{{AC}} = {{sin(\alpha _1 + \alpha _2+ \gamma _2)}} {{{CD}} \over {{sin(\alpha _1 + \alpha _2)}}}").scale(sc).next_to(ref, DOWN)
#         eq_CD = MathTex(r"{{CD}} = {{AC}} {{{sin(\alpha _1 + \alpha _2)}} \over {{sin(\alpha _1 + \alpha _2+ \gamma _2)}}}").scale(sc).next_to(ref, DOWN)
#         self.play(TransformMatchingTex(eq_CD1, eq_CD2), **play_kw)
#         self.play(TransformMatchingTex(eq_CD2, eq_CD), **play_kw)
#         ref = eq_CD
#         self.play(FadeOut(Text(r"On note H le point d'intersection de AB et CD").scale(sc).next_to(ref, DOWN)), 
#                   Create(H), Create(Text('H').next_to(H, DOWN).scale(sc)), **play_kw)
#         dist_AH = Tex("On va calculer la distance AH").scale(sc).next_to(ref, DOWN)
#         self.play(Write(dist_AH), **play_kw)
#         ref = dist_AH
#         self.play(FadeOut(Tex(r"dans le triangle AHC, on connaît AC et les 3 angles").scale(sc).next_to(ref, DOWN)),
#                   **play_kw)
#         self.play(FadeOut(Tex(r"on en déduit donc AH").scale(sc).next_to(ref, DOWN)),          
#                   Create(Line(start=A, end=H, color=RED)), **play_kw)
#         eq_AH = MathTex(r"AH = AC {sin(\gamma _2) \over sin(\gamma _2 + \alpha _2)}").scale(sc).next_to(ref, DOWN)
#         self.play(Write(eq_AH), **play_kw)
#         self.play(Create(SurroundingRectangle(eq_AH, color=YELLOW)), run_time=1)
#         ref = eq_AH
#         self.play(FadeOut(Text(r"On va calculer BH sur le même principe").scale(sc).next_to(ref, DOWN)), **play_kw)
#         dist_BD = Tex("On va calculer BC").scale(sc).next_to(ref, DOWN)
#         ref = dist_BD
#         self.play(Write(dist_BD), Create(BC), Create(BD), **play_kw)
#         c1 = Angle.from_three_points(B, C, D, other_angle=True, radius=0.5, color=RED)
#         eq_c1 = MathTex(r"\gamma _1").scale(sc).set_color(RED)
#         self.play(FadeOut(Tex(r"Mesure $\gamma _1$ l'angle DCB").scale(sc).next_to(ref, DOWN)),
#                   Create(c1), Write(eq_c1.next_to(c1, DR, buff=0.1)), **play_kw)
#         b1 = Angle.from_three_points(C, B, H, color=RED)
#         eq_b1 = MathTex(r"\beta _1").scale(sc).set_color(RED)
#         self.play(FadeOut(Tex(r"Mesure $\beta _1$ l'angle CBH").scale(sc).next_to(ref, DOWN)),
#                   Create(b1), Write(eq_b1.next_to(b1, LEFT, buff=0.1)), **play_kw)
#         b2 = Angle.from_three_points(A, B, D, radius=0.5, color=RED)
#         eq_b2 = MathTex(r"\beta _2").scale(sc).set_color(RED)
#         self.play(FadeOut(Tex(r"Mesure $\beta _2$ l'angle CBD").scale(sc).next_to(ref, DOWN)),
#                   Create(b2), Write(eq_b2.next_to(b2, LEFT, buff=0.1)), **play_kw)
#         self.play(FadeOut(Tex(r"dans le triangle CBD, on connaît CD et les 3 angles").scale(sc).next_to(ref, DOWN)), 
#                   **play_kw)
#         eq_BC = MathTex(r"BC = CD {sin(\gamma _1 + \beta _1+\beta _2) \over sin(\beta _1 + \beta _2)}").scale(sc)    
#         self.play(FadeOut(Tex(r"on en déduit donc BC").scale(sc).next_to(ref, DOWN)),**play_kw)          
#         self.play(Write(eq_BC.next_to(ref, DOWN)), **play_kw)
#         ref = eq_BC
#         dist_BH = Tex(r"et enfin HB, en considérant le triangle CHB").scale(sc).next_to(ref, DOWN)
#         self.play(Write(dist_BH), **play_kw)      
#         ref = dist_BH
#         eq_BH = MathTex(r"HB = BC {sin(\gamma _1 ) \over sin(\gamma _1+ \beta _1)}").scale(sc).next_to(ref, DOWN)
#         self.play(Write(eq_BH), **play_kw)
#         self.play(Create(SurroundingRectangle(eq_BH, color=YELLOW)), run_time=1)
#         ref = eq_BH
#         # self.play(Create(Line(start=H, end=B, color=RED)))
#         self.play(Create(Line(start=A, end=B, color=GREEN)))
#         eq_AB = Tex(r"AB = AH + HB").scale(sc).next_to(ref, DOWN).set_color(GREEN)
#         self.play(Write(eq_AB), **play_kw)
#         self.play(Create(SurroundingRectangle(eq_AB, color=YELLOW)), run_time=1)
#         # self.remove(obj)
#         # self.play(x.animate)

class TriangulationDetaillee(Scene):
    def construct(self):
            
        def inter(A, B, C, D):
            a1 = (B[1] - A[1])/(B[0] - A[0])
            b1 = A[1] - a1 * A[0]
            a2 = (D[1] - C[1])/(D[0] - C[0])
            b2 = C[1] - a2 * C[0]
            x = - (b2 - b1)/(a2 - a1)
            y = a1 * x + b1
            return ([x, y, 0])

        play_kw = {"run_time": 3}
        scale_factor=1.5
        sc = 0.6
        
        A = [-6, 0, 0]
        B = [0, 1, 0]
        C = [-5, 4,0]
        D = [-2, -2, 0]
        
        points = [Dot(p, color=RED) for p in [A, B, C, D]]
        txt = [Text(p) for p in ["A", "B", "C", "D"]]
        AB = Line(start=A, end=B, color=WHITE)
        AC = Line(start=A, end=C, color=RED)
        AD = Line(start=A, end=D, color=WHITE)
        CD = Line(start=C, end=D, color=WHITE)
        BC = Line(start=B, end=C, color=WHITE)
        BD = Line(start=B, end=D, color=WHITE)
        H = Dot(inter(A, B, C, D), color=RED)

        
        self.play(Create(points[0]), Create(txt[0].next_to(A, LEFT).scale(sc)), 
                  Create(points[1]), Create(txt[1].next_to(B).scale(sc)))

        obj = Text("On cherche la distance AB").move_to([4,3.5,0]).scale(sc)
        ref = obj
        self.play(AnimationGroup(Create(AB), Write(obj), lag_ratio=0.25), **play_kw)
        self.play(FadeOut(Tex("Prenons 2 points C et D de part et d'autre de AB").scale(sc).next_to(ref, DOWN)),
                  Create(points[2]), Write(txt[2].next_to(C, UP).scale(sc)), 
                  Create(points[3]), Write(txt[3].next_to(D).scale(sc)), **play_kw)              
        self.play(Create(CD), **play_kw) 
        self.play(FadeOut(Tex("Mesure la distance AC").scale(sc).next_to(ref, DOWN)),
                  Create(AC), **play_kw)
        self.play(FadeOut(Tex(r"On note H le point d'intersection de AB et CD").scale(sc).next_to(ref, DOWN)), 
                  Create(H), Create(Text('H').next_to(H, DOWN).scale(sc)), **play_kw)
        dist_AH = Tex("On va calculer AH dans le triangle ACH").scale(sc).next_to(ref, DOWN)
        self.play(Write(dist_AH), **play_kw)
        ref = dist_AH
        a2 = Angle.from_three_points(B, A, C, color=RED)
        eq_a2 = MathTex(r"\alpha _2").scale(sc).set_color(RED)
        c2 = Angle.from_three_points(A, C, D, color=RED)
        eq_c2 = MathTex(r"\gamma _2").scale(sc).set_color(RED)
        self.play(FadeOut(Tex(r"Mesure $\alpha _2$ et $\gamma _2$").scale(sc).next_to(ref, DOWN)),
                  Create(a2), Write(eq_a2.next_to(a2, UP)), 
                  Create(c2), Write(eq_c2.next_to(c2, DOWN, buff=0.1)), **play_kw)
        self.play(FadeOut(Tex(r"dans le triangle AHC, on connaît AC et les 2 angles adjacents").scale(sc).next_to(ref, DOWN)),
                  Indicate(AC, scale_factor=scale_factor),
                  Indicate(Dot(C), scale_factor=scale_factor),
                  Indicate(Dot(A), scale_factor=scale_factor),
                  Indicate(H, scale_factor=scale_factor),
                  Indicate(eq_a2, scale_factor=scale_factor), 
                  Indicate(eq_c2, scale_factor=scale_factor),
                  Indicate(a2, scale_factor=scale_factor), 
                  Indicate(c2, scale_factor=scale_factor),
                  **play_kw)
        self.play(FadeOut(Tex(r"on en déduit donc AH").scale(sc).next_to(ref, DOWN)),          
                  Create(Line(start=A, end=H, color=RED)), **play_kw)
        eq_AH = MathTex(r"AH = AC {sin(\gamma _2) \over sin(\gamma _2 + \alpha _2)}").scale(sc).next_to(ref, DOWN)
        self.play(Write(eq_AH), **play_kw)
        self.play(Create(SurroundingRectangle(eq_AH, color=YELLOW)), run_time=1)
        ref = eq_AH
        dist_BH = Tex("On va calculer BH dans le triangle BHC").scale(sc).next_to(ref, DOWN)
        self.play(Write(dist_BH), Create(BC),**play_kw)
        ref = dist_BH
        c1 = Angle.from_three_points(B, C, D, other_angle=True, radius=0.5, color=RED)
        eq_c1 = MathTex(r"\gamma _1").scale(sc).set_color(RED)
        b1 = Angle.from_three_points(C, B, H, color=RED)
        eq_b1 = MathTex(r"\beta _1").scale(sc).set_color(RED)
        self.play(FadeOut(Tex(r"Mesure $\gamma _1$ et $\beta _1$").scale(sc).next_to(ref, DOWN)),
                  Create(c1), Write(eq_c1.next_to(c1, DR, buff=0.1)), 
                  Create(b1), Write(eq_b1.next_to(b1, LEFT, buff=0.1)), **play_kw)
        self.play(FadeOut(Tex(r"dans le triangle BHC, on connaît 2 angles adjacents à H").scale(sc).next_to(ref, DOWN)),
                  Indicate(BC, scale_factor=scale_factor),
                  Indicate(Dot(C), scale_factor=scale_factor),
                  Indicate(Dot(B), scale_factor=scale_factor),
                  Indicate(H, scale_factor=scale_factor),
                  Indicate(eq_c1, scale_factor=scale_factor), 
                  Indicate(eq_b1, scale_factor=scale_factor),
                  Indicate(c1, scale_factor=scale_factor),
                  Indicate(b1, scale_factor=scale_factor),
                  **play_kw)
        self.play(FadeOut(Tex(r"on en déduit donc HB en fonction de BC").scale(sc).next_to(ref, DOWN)),          
                  Create(Line(start=H, end=B, color=RED)), **play_kw)
        eq_BH = MathTex(r"HB = BC {sin(\gamma _1 ) \over sin(\gamma _1+ \beta _1)}").scale(sc).next_to(ref, DOWN)
        self.play(Write(eq_BH), **play_kw)
        self.play(Create(SurroundingRectangle(eq_BH, color=YELLOW)), run_time=1)
        ref = eq_BH
        dist_BC = Tex("Il faut donc calculer BC").scale(sc).next_to(ref, DOWN)
        self.play(Write(dist_BC), Create(BD), **play_kw)
        ref = dist_BC
        b2 = Angle.from_three_points(A, B, D, radius=0.5, color=RED)
        eq_b2 = MathTex(r"\beta _2").scale(sc).set_color(RED)
        self.play(FadeOut(Tex(r"Mesure $\beta _2$ l'angle CBD").scale(sc).next_to(ref, DOWN)),
                  Create(b2), Write(eq_b2.next_to(b2, LEFT, buff=0.1)), **play_kw)
        self.play(FadeOut(Tex(r"dans le triangle CBD, on connaît CD et les 3 angles").scale(sc).next_to(ref, DOWN)),
                  Indicate(BC, scale_factor=scale_factor),
                  Indicate(Dot(C), scale_factor=scale_factor),
                  Indicate(Dot(B), scale_factor=scale_factor),
                  Indicate(Dot(D), scale_factor=scale_factor),
                  Indicate(eq_c1, scale_factor=scale_factor), 
                  Indicate(eq_b1, scale_factor=scale_factor), 
                  Indicate(eq_b2, scale_factor=scale_factor), 
                  Indicate(c1, scale_factor=scale_factor), 
                  Indicate(b1, scale_factor=scale_factor), 
                  Indicate(b2, scale_factor=scale_factor),
                  **play_kw)
        eq_BC = MathTex(r"BC = CD {sin(\gamma _1 + \beta _1+\beta _2) \over sin(\beta _1 + \beta _2)}").scale(sc)    
        self.play(FadeOut(Tex(r"on en déduit donc BC").scale(sc).next_to(ref, DOWN)),
                  BC.animate.set_color(RED), **play_kw)          
        self.play(Write(eq_BC.next_to(ref, DOWN)), **play_kw)
        ref = eq_BC
        dist_CD = Tex("On va calculer CD dans le triangle ACD").scale(sc).next_to(ref, DOWN)
        self.play(Write(dist_CD), 
                  Create(AD), **play_kw) 
        ref = dist_CD
        a1 = Angle.from_three_points(D, A, B, color=RED, radius=0.5)
        eq_a1 = MathTex(r"\alpha _1").scale(sc).set_color(RED)
        self.play(FadeOut(Tex(r"Mesure $\alpha _1$ l'angle DAB").scale(sc).next_to(ref, DOWN)), 
                  Create(a1), 
                  Write(eq_a1.next_to(a1, DOWN)), **play_kw)
        self.play(FadeOut(Tex(r"dans le triangle ACD, on connaît AC et les 2 angles").scale(sc).next_to(ref, DOWN)),
                  Indicate(AC, scale_factor=scale_factor),
                  Indicate(Dot(C), scale_factor=scale_factor),
                  Indicate(Dot(A), scale_factor=scale_factor),
                  Indicate(Dot(D), scale_factor=scale_factor),
                  Indicate(eq_c2, scale_factor=scale_factor), 
                  Indicate(eq_a1, scale_factor=scale_factor), 
                  Indicate(eq_a2, scale_factor=scale_factor), 
                  Indicate(c2, scale_factor=scale_factor), 
                  Indicate(a1, scale_factor=scale_factor), 
                  Indicate(a2, scale_factor=scale_factor),
                  **play_kw)
        eq_CD = MathTex(r"CD = AC {sin(\alpha _1 + \alpha _2) \over sin(\alpha _1 + \alpha _2+ \gamma _2)}").scale(sc).next_to(ref, DOWN)
        self.play(Write(eq_CD), 
                  AD.animate.set_color(RED), **play_kw)
        ref = eq_CD
        endef = Tex(r"En définitive:").scale(sc).next_to(ref, DOWN)
        self.play(Write(endef))
        ref = endef
        eq_AB = MathTex(r"AB = AH + HB").scale(sc).next_to(ref, DOWN)
        self.play(Write(eq_AB))
        self.play(Create(SurroundingRectangle(eq_AB, color=YELLOW)), run_time=1)


class TriangulationSimplifiee(Scene):
    def construct(self):
            
        def inter(A, B, C, D):
            a1 = (B[1] - A[1])/(B[0] - A[0])
            b1 = A[1] - a1 * A[0]
            a2 = (D[1] - C[1])/(D[0] - C[0])
            b2 = C[1] - a2 * C[0]
            x = - (b2 - b1)/(a2 - a1)
            y = a1 * x + b1
            return ([x, y, 0])
        
        def triangule(A, B, C, ang1, ang2, line):
            self.play(Indicate(Dot(A), scale_factor=scale_factor), 
                      Indicate(Dot(B), scale_factor=scale_factor), 
                      Indicate(Dot(C), scale_factor=scale_factor),
                      Indicate(ang1, scale_factor=scale_factor), 
                      Indicate(ang2, scale_factor=scale_factor), 
                      Indicate(line, scale_factor=scale_factor), **play_kw)
            self.play(Create(Line(A, B, color=RED)), 
                      Create(Line(A, C, color=RED)), 
                      Create(Line(C, B, color=RED)))
            self.wait(2)
        
        play_kw = {"run_time": 5}
        scale_factor=1.5
        sc = 0.6
        
        A = [-6, 0, 0]
        B = [6, 0, 0]
        C = [-4, 1, 0]
        D = [-3, -3, 0]
        E = [0, 2.25, 0]
        F = [4, -2, 0]
        G = [4, 2.5, 0]
        
        obj = Tex(r"On cherche à mesure la distance de 2 points qui sont très éloignés")
        self.play(Write(obj).scale(sc).to_edge(UP), **play_kw)
        
        self.play(Create(Dot(A)), Create(Tex("A").scale(sc).next_to(A, LEFT)), 
                  Create(Dot(B)), Create(Tex("B").scale(sc).next_to(B, RIGHT)),
                  Create(Line(A, B)))
        

        points = [C, D, E, F]
        dots = [Dot(p, color=RED) for p in points]
        txt = [Tex(p).scale(sc) for p in ["C", "D", "E", 'F']]
        for d, p, t in zip(dots, points, txt):
            self.play(Create(d), Write(t.next_to(p)))

        mes = [inter(A, B, p, q) for p, q in zip(points[:-1], points[1:])]
        # for p, t in zip(mes, ["H", "I", "J", "K"]):
        #     self.play(Create(Dot(p)), Write(Text(t).next_to(p)))
        AC = Line(A, C, color=RED)
        CD = Line(C, D)
        AD = Line(A, D)
        self.play(Create(AC))
        self.play(Create(CD))
        self.play(Create(Dot(mes[0])), Write(Tex("G").scale(sc).next_to(mes[0], UR)))
        c1 = Angle.from_three_points(A, C, D)
        a1 = Angle.from_three_points(C, A, B, other_angle=True)
        a2 = Angle.from_three_points(D, A, B)
        a3 = Angle.from_three_points(D, A, C)
        triangule(A, C, mes[0], a1, c1, AC)
        self.remove(a1, a2, a3, c1)
        
        self.play(Create(Line(A, D)))
        triangule(A, C, D, a3, c1, AC)
        CD = Line(C, D)
        DE = Line(D, E)
        self.remove(a3, c1)
        
        self.play(Create(DE))
        self.play(Create(Dot(mes[1])), Write(Tex("H").scale(sc).next_to(mes[1], DOWN)))        
        self.wait(2)
        GD = Line(D, mes[0])
        d1 = Angle.from_three_points(mes[1], D, mes[0])
        g1 = Angle.from_three_points(C, mes[0], A)
        g2 = Angle.from_three_points(D, mes[0], mes[1])
        self.play(Indicate(g1, scale_factor=scale_factor), 
                  Indicate(g2, scale_factor=scale_factor), **play_kw)
        triangule(mes[0], mes[1], D, d1, g2, GD)
        self.remove(d1, g1, g2)
        
        self.play(Create(Line(C, E)))
        self.wait(2)
        c2 = Angle.from_three_points(E, C, D, other_angle=True)
        e1 = Angle.from_three_points(C, E, D)
        #self.play(Create(c2), Create(e1))
        triangule(C, D, E, c2, e1, CD)
        self.remove(c2, e1)

        EF = Line(E, F)
        EI = Line(E, mes[1])
        self.play(Create(EF)) 
        self.play(Create(Dot(mes[2])), Write(Tex("I").scale(sc).next_to(mes[2], DOWN)))
        self.wait(2)
        e2 = Angle.from_three_points(mes[1], E, mes[2])
        h1 = Angle.from_three_points(B, mes[1], E)
        h2 = Angle.from_three_points(A, mes[1], D)
        self.play(Indicate(h1, scale_factor=scale_factor), 
                  Indicate(h2, scale_factor=scale_factor), **play_kw)
        triangule(E, mes[1], mes[2], e2, h1, EI)
        self.remove(e2, h1, h2)
        self.wait(2)
        
        DE = Line(D, E)
        DF = Line(D, F)
        self.play(Create(DF))
        self.wait(2)
        d2 = Angle.from_three_points(F, D, E)
        e2 = Angle.from_three_points(D, E, F)
        triangule(D, E, F, d2, e2, DE)
        self.remove(d2, e2)
        
        FI = Line(mes[-1], F)
        BF = Line(B, F)
        self.play(Create(BF))
        i1 = Angle.from_three_points(E, mes[-1], A)
        i2 = Angle.from_three_points(F, mes[-1], B)
        self.play(Indicate(i1, scale_factor=scale_factor), 
                  Indicate(i2, scale_factor=scale_factor), **play_kw)
        b1 = Angle.from_three_points(mes[-1], B, F)
        triangule(F, B, mes[-1], i2, b1, FI)
        self.remove(i1, i2, b1)
        self.wait(1)
        
        res = [Tex(r"A l'aide de mesures d'angles et de la mesure d'un côté, on calcule AB de proche en proche:"),
               MathTex(r"AB = AG + GH + HI + IB")]
        x = Group(*res).scale(sc).arrange(DOWN).to_edge(UP)
        
        self.play(x.animate, **play_kw)
        self.wait(3)
        self.clear()


class Triangulation(Scene):
    def construct(self):
        
        self.sc = 0.5
        self.scale_factor = 1.5
        self.ind_rt = 4
        self.play_rt = 3
        self.sur_rt = 1
        
        self.LoiDesSinus()
        self.wait(2)
        self.clear()
        self.TriangulationSimplifiee()
        self.play(Write(Tex(r"Regardons plus précisément avec 2 points")))
        self.wait(2)
        self.clear()
        self.TriangulationDetaillee()

          
    def LoiDesSinus(self):
        dict_color = {"A": RED,
                      "a": RED,
                      "\alpha": RED,
                      "B": YELLOW,
                      "b": YELLOW,
                      "\beta": YELLOW,
                      "C": BLUE,
                      "c": BLUE,
                      "\gamma": BLUE, 
                      "sin(": WHITE} 
        a, b = 4, 3
        A = [a, 0, 0]
        B = [-1, b-1, 0]
        C = [0, -2, 0]
        title = Title(r"Loi des sinus")
        self.add(title)
        self.wait()
        tri = Polygon(A, B, C).set_fill(BLUE, opacity=0.5)
        self.play(tri.animate) 
        cycle = [LEFT, DOWN, RIGHT, UP]
        [A, B, C] = [tri.get_vertices()[i] for i in range(3)]
        [I, J, K] = [0.5*(B+C), 0.5*(A+C), 0.5*(A+B)]
        txtA = Tex('A', substrings_to_isolate=["A"]).next_to(A, RIGHT)
        txtB = Tex('B', substrings_to_isolate=["B"]).next_to(B, LEFT)
        txtC = Tex('C', substrings_to_isolate=["C"]).next_to(C, LEFT)
        txt_a = Tex('a', substrings_to_isolate=["a"]).next_to(I, cycle[0])
        txt_b = Tex('b', substrings_to_isolate=["b"]).next_to(J, cycle[1])
        txt_c = Tex('c', substrings_to_isolate=["c"]).next_to(K, cycle[3])
        angleA = Angle.from_three_points(B, A, C, color=RED)
        angleB = Angle.from_three_points(A, B, C, color=YELLOW, other_angle=True)
        angleC = Angle.from_three_points(B, C, A, color=GREEN, other_angle=True)
        txt_aa = MathTex(r"\alpha").next_to(angleA, LEFT, buff=0.1)
        txt_bb = MathTex(r"\beta").next_to(angleB, DR, buff=0.1)
        txt_cc = MathTex(r"\gamma").next_to(angleC, UP, buff=0.1)
        notation = (txtA, txtB, txtC, txt_a, txt_b, txt_c, angleA, txt_aa, angleB, txt_bb, angleC, txt_cc)
        for elt in notation:
            elt.set_color_by_tex_to_color_map(dict_color).scale(self.sc)
        self.play(FadeIn(txtA, txtB, txtC), run_time=self.play_rt)
        self.play(FadeIn(txt_a, txt_b, txt_c), run_time=self.play_rt)
        self.play(FadeIn(angleA, txt_aa, angleB, txt_bb, angleC, txt_cc), run_time=self.play_rt)
        figure = VGroup(tri, *notation)
        self.play(figure.animate.shift(4*LEFT), run_time=self.play_rt)
        titre = Text("Rappels sur la loi des sinus")
        eq1 = MathTex(r"{{{a}} \over sin({{\alpha)}}} = {{{b}} \over sin({{\beta}})} = {{{c}} \over sin({{\gamma}})}")
        eq2 = MathTex(r"\text{Or, }{{\alpha}} = \pi - ({{\beta}}+ {{\gamma}})")
        eq3 = Tex("et comme $sin(\pi-x)=sin(x)$, on a:")
        eq4 = MathTex(r"{{{a}} \over {{sin(\pi - ({{\beta}} + {{\gamma}}))}}} = {{{b}} \over sin({{\beta}})} = {{{c}} \over sin({{\gamma}})}") 
        eq5 = MathTex(r"{{{a}} \over {{{{sin(}}{{\beta}} + {{\gamma}})}}} = {{{b}} \over sin({{\beta}})} = {{{c}} \over sin({{\gamma}})}")
        
        eqs = Group(#titre, 
                    eq1, 
                    eq2, 
                    eq3, 
                    eq4, 
                    eq5).scale(self.sc).arrange(DOWN, buff=0.25).next_to(tri.get_right(), 2.5*RIGHT)
        for i, eq in enumerate(eqs[:-1]):
            eq.set_color_by_tex_to_color_map(dict_color)
            self.play(Write(eq), run_time=self.play_rt)
            if i==2:
                self.remove(txt_aa)
                self.play(FadeIn(MathTex(r"\pi - ({{\beta}} + {{\gamma}})").scale(self.sc).next_to(angleA, LEFT).set_color_by_tex_to_color_map(dict_color)))
        eq5.set_color_by_tex_to_color_map(dict_color)
        ref = eqs[-2].get_bottom()
        self.play(TransformMatchingTex(eq4, eq5), run_time=self.play_rt)
        self.play(eq5.animate.shift(UP))
        ref = Tex(r"On peut donc calculer 2 côtés").scale(self.sc).next_to(eq5.get_bottom(), DOWN, buff=0.5)
        self.play(Write(ref), run_time=self.play_rt)
        ref = Tex(r"à partir d'un côté et de deux angles:").scale(self.sc).next_to(ref, DOWN, buff=0.5)
        self.play(Write(ref), run_time=self.play_rt)        
        self.wait()
        self.play(Indicate(Line(B,C).shift(4*LEFT), scale_factor=self.scale_factor),
                  Indicate(Dot(A).shift(4*LEFT), scale_factor=self.scale_factor),
                  Indicate(Dot(B).shift(4*LEFT), scale_factor=self.scale_factor),
                  Indicate(Dot(C).shift(4*LEFT), scale_factor=self.scale_factor),
                  Indicate(angleB, scale_factor=self.scale_factor),
                  Indicate(angleC, scale_factor=self.scale_factor),
                  Indicate(txt_bb, scale_factor=self.scale_factor),
                  Indicate(txt_cc, scale_factor=self.scale_factor),
                  run_time=self.ind_rt)
        eq = MathTex(r"{{b}} = {{a}} {sin({{\beta}} ) \over sin({{\beta}} + {{\gamma}})}").scale(self.sc).next_to(ref, DOWN)
        self.play(Write(eq.set_color_by_tex_to_color_map(dict_color)), run_time=self.play_rt)
        self.play(Create(SurroundingRectangle(eq, color=YELLOW)), run_time=self.sur_rt)
        eq2 = MathTex(r"{{c}} = {{a}} {sin({{\gamma}} ) \over sin({{\beta}} + {{\gamma}})}").scale(self.sc).next_to(eq, DOWN)
        self.play(Write(eq2.set_color_by_tex_to_color_map(dict_color)), run_time=self.play_rt)
        self.play(Create(SurroundingRectangle(eq2, color=YELLOW)), run_time=self.sur_rt)
        self.wait(2)
        
    def TriangulationSimplifiee(self):
        # Montrer les triangles au fur et a mesure???
        A = [-6, 0, 0]
        B = [6, 0, 0]
        C = [-4, 1, 0]
        D = [-3, -3, 0]
        E = [0, 2.25, 0]
        F = [4, -2, 0]
        G = [4, 2.5, 0]
        
        def inter(A, B, C, D):
            a1 = (B[1] - A[1])/(B[0] - A[0])
            b1 = A[1] - a1 * A[0]
            a2 = (D[1] - C[1])/(D[0] - C[0])
            b2 = C[1] - a2 * C[0]
            x = - (b2 - b1)/(a2 - a1)
            y = a1 * x + b1
            return ([x, y, 0])
        
        def triangule(A, B, C, ABC, ang1, ang2, line):
            txt = "Dans le triangle "+ABC
            self.play(FadeOut(Text(txt).scale(self.sc).to_edge(UP)),
                      Indicate(Polygon(A, B, C).set_fill(color=BLUE, opacity=0.2), 
                               scale_factor=self.scale_factor, color=BLUE), 
                      run_time=self.play_rt)
            self.play(FadeOut(Text(r"On connaît un côté et deux angles").scale(self.sc).to_edge(UP)),
                      Indicate(Dot(A), scale_factor=self.scale_factor), 
                      Indicate(Dot(B), scale_factor=self.scale_factor), 
                      Indicate(Dot(C), scale_factor=self.scale_factor),
                      Indicate(ang1, scale_factor=self.scale_factor), 
                      Indicate(ang2, scale_factor=self.scale_factor), 
                      Indicate(line, scale_factor=self.scale_factor), 
                      run_time=self.play_rt)
            self.play(FadeOut(Text(r"On en déduit les deux autres côtés et l'autre angle").scale(self.sc).to_edge(UP)),
                      Create(Line(A, B, color=RED)), 
                      Create(Line(A, C, color=RED)), 
                      Create(Line(C, B, color=RED)), 
                      run_time=self.play_rt)
            self.wait(2)
        
        title = Title(r"Triangulation")
        self.add(title)
        self.wait()
        obj = [Tex(r"On cherche à mesurer la distance entre 2 points qui sont très éloignés, par exemple distants de plusieurs milliers de kilomètres le long d'un méridien."),
               Tex(r"En identifiant des points de part et d'autre de A et B, on va construire des triangles successifs qui ont des côtés communs."),
               Tex(r"En mesurant les angles entre ces points et en utilisant la loi des sinus, on va pouvoir calculer la distance de proche en proche"), 
               Text(r"Voyons cela sur un exemple")]
        ref = obj[0].to_edge(UP)
        for o  in obj:
            self.play(Write(o.scale(0.7).next_to(ref, DOWN)), run_time=3)
            self.wait(2)
            ref = o
        
        self.clear()
        title = Title(r"Triangulation")
        self.add(title)
        g = VGroup(Dot(A), 
                   Tex("A").scale(self.sc).next_to(A, LEFT), 
                   Dot(B), Tex("B").scale(self.sc).next_to(B, RIGHT),
                   Line(A, B), 
                   Dot(C), 
                   Tex("C").scale(self.sc).next_to(C, RIGHT))
        
        self.play(g.animate.shift(3*DOWN))
        
        obj = [Tex(r"On pourrait mesure AB directement dans le triangle ABC, comme vu précédemment."),
               Tex(r"Mais on suppose que B n'est pas visible depuis C, de sorte qu'on ne puisse pas mesurer l'angle ACB."),
               Tex(r"On va donc utiliser la triangulation pour calculer la distance AB de proche en proche."), 
               Tex(r"On suppose tout de même que l'on peut toujours mesurer l'angle CAB, ce qui est possible avec un théodolite en supposant que AB indique le nord magnétique")]
        ref = obj[0].to_edge(UP)
        for i, o  in enumerate(obj):
            if i == 0:
                self.play(Write(o.scale(0.7).next_to(ref, DOWN)), 
                          Create(Polygon(A, B, C, fill_color=BLUE, fill_opacity=0.2).shift(3*DOWN)), run_time=self.play_rt)
            else:
                self.play(Write(o.scale(0.7).next_to(ref, DOWN)), run_time=self.play_rt)
            self.wait(2)
            ref = o
        
        self.clear()

        self.play(g.animate.shift(3*UP))
        
        points = [C, D, E, F]
        dots = [Dot(p, color=RED) for p in points]
        txt = [Tex(p).scale(self.sc) for p in ["C", "D", "E", 'F']]
        for d, p, t in zip(dots, points, txt):
            self.play(Create(d), Write(t.next_to(p)))

        mes = [inter(A, B, p, q) for p, q in zip(points[:-1], points[1:])]
        # for p, t in zip(mes, ["H", "I", "J", "K"]):
        #     self.play(Create(Dot(p)), Write(Text(t).next_to(p)))
        AC = Line(A, C, color=RED)
        CD = Line(C, D)
        AD = Line(A, D)
        self.play(Create(AC))
        self.play(Create(CD))
        self.play(Create(Dot(mes[0])), Write(Tex("G").scale(self.sc).next_to(mes[0], UR)))
        c1 = Angle.from_three_points(A, C, D)
        a1 = Angle.from_three_points(C, A, B, other_angle=True)
        a2 = Angle.from_three_points(D, A, B)
        a3 = Angle.from_three_points(D, A, C)
        triangule(A, C, mes[0], "ACG", a1, c1, AC)
        self.remove(a1, a2, a3, c1)
        
        self.play(Create(Line(A, D)))
        triangule(A, C, D, "ACD", a3, c1, AC)
        CD = Line(C, D)
        DE = Line(D, E)
        self.remove(a3, c1)
        
        self.play(Create(DE))
        self.play(Create(Dot(mes[1])), Write(Tex("H").scale(self.sc).next_to(mes[1], DOWN)))        
        self.wait(2)
        GD = Line(D, mes[0])
        d1 = Angle.from_three_points(mes[1], D, mes[0])
        g1 = Angle.from_three_points(C, mes[0], A)
        g2 = Angle.from_three_points(D, mes[0], mes[1])
        self.play(
            FadeOut(Text("Ces deux angles sont égaux").scale(self.sc).to_edge(UP)), 
            Indicate(g1, scale_factor=self.scale_factor), 
            Indicate(g2, scale_factor=self.scale_factor), 
            run_time=self.play_rt)
        triangule(mes[0], mes[1], D, "DHG", d1, g2, GD)
        self.remove(d1, g1, g2)
        
        self.play(Create(Line(C, E)))
        self.wait(2)
        c2 = Angle.from_three_points(E, C, D, other_angle=True)
        e1 = Angle.from_three_points(C, E, D)
        #self.play(Create(c2), Create(e1))
        triangule(C, D, E, "CDE", c2, e1, CD)
        self.remove(c2, e1)

        EF = Line(E, F)
        EI = Line(E, mes[1])
        self.play(Create(EF)) 
        self.play(Create(Dot(mes[2])), Write(Tex("I").scale(self.sc).next_to(mes[2], DOWN)))
        self.wait(2)
        e2 = Angle.from_three_points(mes[1], E, mes[2])
        h1 = Angle.from_three_points(B, mes[1], E)
        h2 = Angle.from_three_points(A, mes[1], D)
        self.play(
            FadeOut(Text("Ces deux angles sont égaux").scale(self.sc).to_edge(UP)), 
            Indicate(h1, scale_factor=self.scale_factor),
            Indicate(h2, scale_factor=self.scale_factor), 
            run_time=self.play_rt)
        triangule(E, mes[1], mes[2], "EHI", e2, h1, EI)
        self.remove(e2, h1, h2)
        self.wait(2)
        
        DE = Line(D, E)
        DF = Line(D, F)
        self.play(Create(DF))
        self.wait(2)
        d2 = Angle.from_three_points(F, D, E)
        e2 = Angle.from_three_points(D, E, F)
        triangule(D, E, F, "DEF", d2, e2, DE)
        self.remove(d2, e2)
        
        FI = Line(mes[-1], F)
        BF = Line(B, F)
        self.play(Create(BF))
        i1 = Angle.from_three_points(E, mes[-1], A)
        i2 = Angle.from_three_points(F, mes[-1], B)
        self.play(
            FadeOut(Text("Ces deux angles sont égaux").scale(self.sc).to_edge(UP)), 
            Indicate(i1, scale_factor=self.scale_factor),
            Indicate(i2, scale_factor=self.scale_factor), 
            run_time=self.play_rt)
        b1 = Angle.from_three_points(mes[-1], B, F)
        triangule(F, B, mes[-1], "FBI", i2, b1, FI)
        self.remove(i1, i2, b1)
        self.wait(1)
        
        res = [Tex(r"A l'aide de mesures d'angles et de la mesure d'un côté, on a pu calculer la distance AB de proche en proche:"),
               MathTex(r"AB = AG + GH + HI + IB")]
        x = Group(*res).scale(self.sc).arrange(DOWN).move_to([0, 3.5, 0])
        
        self.play(x.animate, run_time=self.play_rt)
        self.wait(3)
        self.clear()
        
    def TriangulationDetaillee(self):
            A = [-6, 0, 0]
            B = [0, 1, 0]
            C = [-5, 3.25,0]
            D = [-2, -2, 0]
            
            def inter(A, B, C, D):
                a1 = (B[1] - A[1])/(B[0] - A[0])
                b1 = A[1] - a1 * A[0]
                a2 = (D[1] - C[1])/(D[0] - C[0])
                b2 = C[1] - a2 * C[0]
                x = - (b2 - b1)/(a2 - a1)
                y = a1 * x + b1
                return ([x, y, 0])
            
            points = [Dot(p, color=RED) for p in [A, B, C, D]]
            txt = [Text(p) for p in ["A", "B", "C", "D"]]
            AB = Line(start=A, end=B, color=WHITE)
            AC = Line(start=A, end=C, color=RED)
            AD = Line(start=A, end=D, color=WHITE)
            CD = Line(start=C, end=D, color=WHITE)
            BC = Line(start=B, end=C, color=WHITE)
            BD = Line(start=B, end=D, color=WHITE)
            H = Dot(inter(A, B, C, D), color=RED)

            self.play(Create(points[0]), Create(txt[0].next_to(A, LEFT).scale(self.sc)), 
                      Create(points[1]), Create(txt[1].next_to(B).scale(self.sc)))

            obj = Text("On cherche la distance AB").move_to([3.5,3.5,0]).scale(self.sc)
            ref = obj
            self.play(AnimationGroup(Create(AB), Write(obj), lag_ratio=0.25), run_time=self.play_rt)
            self.play(FadeOut(Tex("Prenons 2 points C et D de part et d'autre de AB").scale(self.sc).next_to(ref, DOWN)),
                      Create(points[2]), Write(txt[2].next_to(C, UP).scale(self.sc)), 
                      Create(points[3]), Write(txt[3].next_to(D).scale(self.sc)), run_time=self.play_rt)              
            self.play(Create(CD), run_time=self.play_rt) 
            self.play(FadeOut(Tex("Mesure la distance AC").scale(self.sc).next_to(ref, DOWN)),
                      Create(AC), run_time=self.play_rt)
            self.play(FadeOut(Tex(r"On note H le point d'intersection de AB et CD").scale(self.sc).next_to(ref, DOWN)), 
                      Create(H), Create(Text('H').next_to(H, DOWN).scale(self.sc)), run_time=self.play_rt)
            dist_AH = Tex("On va calculer AH dans le triangle ACH").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(dist_AH), run_time=self.play_rt)
            ref = dist_AH
            a2 = Angle.from_three_points(B, A, C, color=RED)
            eq_a2 = MathTex(r"\alpha _2").scale(self.sc).set_color(RED)
            c2 = Angle.from_three_points(A, C, D, color=RED)
            eq_c2 = MathTex(r"\gamma _2").scale(self.sc).set_color(RED)
            self.play(FadeOut(Tex(r"Mesure $\alpha _2$ et $\gamma _2$").scale(self.sc).next_to(ref, DOWN)),
                      Create(a2), Write(eq_a2.next_to(a2, UP)), 
                      Create(c2), Write(eq_c2.next_to(c2, DOWN, buff=0.1)), run_time=self.play_rt)
            self.play(FadeOut(Tex(r"dans le triangle AHC, on connaît AC et les 2 angles adjacents").scale(self.sc).next_to(ref, DOWN)),
                      Indicate(AC, scale_factor=self.scale_factor),
                      Indicate(Dot(C), scale_factor=self.scale_factor),
                      Indicate(Dot(A), scale_factor=self.scale_factor),
                      Indicate(H, scale_factor=self.scale_factor),
                      Indicate(eq_a2, scale_factor=self.scale_factor), 
                      Indicate(eq_c2, scale_factor=self.scale_factor),
                      Indicate(a2, scale_factor=self.scale_factor), 
                      Indicate(c2, scale_factor=self.scale_factor),
                      run_time=self.play_rt)
            self.play(FadeOut(Tex(r"on en déduit donc AH").scale(self.sc).next_to(ref, DOWN)),          
                      Create(Line(start=A, end=H, color=RED)), run_time=self.play_rt)
            eq_AH = MathTex(r"AH = AC {sin(\gamma _2) \over sin(\gamma _2 + \alpha _2)}").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(eq_AH), run_time=self.play_rt)
            self.play(Create(SurroundingRectangle(eq_AH, color=YELLOW)), run_time=1)
            ref = eq_AH
            dist_BH = Tex("On va calculer BH dans le triangle BHC").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(dist_BH), Create(BC),run_time=self.play_rt)
            ref = dist_BH
            c1 = Angle.from_three_points(B, C, D, other_angle=True, radius=0.5, color=RED)
            eq_c1 = MathTex(r"\gamma _1").scale(self.sc).set_color(RED)
            b1 = Angle.from_three_points(C, B, H, color=RED)
            eq_b1 = MathTex(r"\beta _1").scale(self.sc).set_color(RED)
            self.play(FadeOut(Tex(r"Mesure $\gamma _1$ et $\beta _1$").scale(self.sc).next_to(ref, DOWN)),
                      Create(c1), Write(eq_c1.next_to(c1, DR, buff=0.1)), 
                      Create(b1), Write(eq_b1.next_to(b1, LEFT, buff=0.1)), run_time=self.play_rt)
            self.play(FadeOut(Tex(r"dans le triangle BHC, on connaît 2 angles adjacents à H").scale(self.sc).next_to(ref, DOWN)),
                      Indicate(BC, scale_factor=self.scale_factor),
                      Indicate(Dot(C), scale_factor=self.scale_factor),
                      Indicate(Dot(B), scale_factor=self.scale_factor),
                      Indicate(H, scale_factor=self.scale_factor),
                      Indicate(eq_c1, scale_factor=self.scale_factor), 
                      Indicate(eq_b1, scale_factor=self.scale_factor),
                      Indicate(c1, scale_factor=self.scale_factor),
                      Indicate(b1, scale_factor=self.scale_factor),
                      run_time=self.play_rt)
            self.play(FadeOut(Tex(r"on en déduit donc HB en fonction de BC").scale(self.sc).next_to(ref, DOWN)),          
                      Create(Line(start=H, end=B, color=RED)), run_time=self.play_rt)
            eq_BH = MathTex(r"HB = BC {sin(\gamma _1 ) \over sin(\gamma _1+ \beta _1)}").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(eq_BH), run_time=self.play_rt)
            self.play(Create(SurroundingRectangle(eq_BH, color=YELLOW)), run_time=1)
            ref = eq_BH
            dist_BC = Tex("Il faut donc calculer BC").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(dist_BC), Create(BD), run_time=self.play_rt)
            ref = dist_BC
            b2 = Angle.from_three_points(A, B, D, radius=0.5, color=RED)
            eq_b2 = MathTex(r"\beta _2").scale(self.sc).set_color(RED)
            self.play(FadeOut(Tex(r"Mesure $\beta _2$ l'angle CBD").scale(self.sc).next_to(ref, DOWN)),
                      Create(b2), Write(eq_b2.next_to(b2, LEFT, buff=0.1)), run_time=self.play_rt)
            self.play(FadeOut(Tex(r"dans le triangle CBD, on connaît CD et les 3 angles").scale(self.sc).next_to(ref, DOWN)),
                      Indicate(BC, scale_factor=self.scale_factor),
                      Indicate(Dot(C), scale_factor=self.scale_factor),
                      Indicate(Dot(B), scale_factor=self.scale_factor),
                      Indicate(Dot(D), scale_factor=self.scale_factor),
                      Indicate(eq_c1, scale_factor=self.scale_factor), 
                      Indicate(eq_b1, scale_factor=self.scale_factor), 
                      Indicate(eq_b2, scale_factor=self.scale_factor), 
                      Indicate(c1, scale_factor=self.scale_factor), 
                      Indicate(b1, scale_factor=self.scale_factor), 
                      Indicate(b2, scale_factor=self.scale_factor),
                      run_time=self.play_rt)
            eq_BC = MathTex(r"BC = CD {sin(\gamma _1 + \beta _1+\beta _2) \over sin(\beta _1 + \beta _2)}").scale(self.sc)    
            self.play(FadeOut(Tex(r"on en déduit donc BC").scale(self.sc).next_to(ref, DOWN)),
                      BC.animate.set_color(RED), run_time=self.play_rt)          
            self.play(Write(eq_BC.next_to(ref, DOWN)), run_time=self.play_rt)
            ref = eq_BC
            dist_CD = Tex("On va calculer CD dans le triangle ACD").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(dist_CD), 
                      Create(AD), run_time=self.play_rt) 
            ref = dist_CD
            a1 = Angle.from_three_points(D, A, B, color=RED, radius=0.5)
            eq_a1 = MathTex(r"\alpha _1").scale(self.sc).set_color(RED)
            self.play(FadeOut(Tex(r"Mesure $\alpha _1$ l'angle DAB").scale(self.sc).next_to(ref, DOWN)), 
                      Create(a1), 
                      Write(eq_a1.next_to(a1, DOWN)), run_time=self.play_rt)
            self.play(FadeOut(Tex(r"dans le triangle ACD, on connaît AC et les 2 angles").scale(self.sc).next_to(ref, DOWN)),
                      Indicate(AC, scale_factor=self.scale_factor),
                      Indicate(Dot(C), scale_factor=self.scale_factor),
                      Indicate(Dot(A), scale_factor=self.scale_factor),
                      Indicate(Dot(D), scale_factor=self.scale_factor),
                      Indicate(eq_c2, scale_factor=self.scale_factor), 
                      Indicate(eq_a1, scale_factor=self.scale_factor), 
                      Indicate(eq_a2, scale_factor=self.scale_factor), 
                      Indicate(c2, scale_factor=self.scale_factor), 
                      Indicate(a1, scale_factor=self.scale_factor), 
                      Indicate(a2, scale_factor=self.scale_factor),
                      run_time=self.play_rt)
            eq_CD = MathTex(r"CD = AC {sin(\alpha _1 + \alpha _2) \over sin(\alpha _1 + \alpha _2+ \gamma _2)}").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(eq_CD), 
                      AD.animate.set_color(RED), run_time=self.play_rt)
            ref = eq_CD
            endef = Tex(r"En définitive:").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(endef))
            ref = endef
            eq_AB = MathTex(r"AB = AH + HB").scale(self.sc).next_to(ref, DOWN)
            self.play(Write(eq_AB))
            self.play(Create(SurroundingRectangle(eq_AB, color=YELLOW)), run_time=1)