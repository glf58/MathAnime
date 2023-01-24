# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 08:37:48 2022

@author: guillaume
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# class MyTest(VoiceoverScene):
#     def construct(self):
#         self.set_speech_service(GTTSService(lang="fr"))
#         #with self.voiceover(text='This circle is drawn as I speak') as tracker:
        
#         with self.voiceover(text='Prenons un cercle') as tracker:
#             # pass
#             # self.play(Create(Circle(radius=2)))
#             self.play(FadeOut(Text(r"On connaît un côté et deux angles")))
            
class Triangulation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="fr"))
        self.sc = 0.5
        self.scale_factor = 1.5
        self.ind_rt = 4
        self.play_rt = 3
        self.sur_rt = 1
        phrase="Imaginons vouloir mesurer précisément la distance entre 2 points très éloignés, de plusieurs dizaines ou milliers de kilomètres par exemple."
        with self.voiceover(text = phrase):
            pass
        phrase = "Une technique simple permet de résoudre ce problème: il s'agit de la triangulation."
        phrase += "Elle consiste à construire une suite de triangles qui ont un côté commun et de mesurer les angles de ces triangles."
        with self.voiceover(text = phrase) as tracker:
            self.play(FadeOut(Text("La Triangulation")), run_time=tracker.duration)
            # pass
        phrase = "Voyons comment cela fonctionne."
        phrase += "Mais avant cela, faisons un petit rappel sur la loi des sinus dans un triangle quelconque."
        with self.voiceover(text = phrase):
            pass
        self.clear()
        self.LoiDesSinus()
        self.wait(2)
        self.clear()
        with self.voiceover(text="Regardons maintenant le principe de la triangulation."):
            pass
        self.TriangulationSimplifiee()
        self.play(Write(Tex(r"Regardons plus précisément avec seulement 2 points de triangulation.").scale(0.7)))
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
        with self.voiceover(text="Prenons un triangle quelconque de longueurs a, b et c et notons les angles alpha, beta et gamma."):
            self.play(tri.animate) 
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
        with self.voiceover(text="la loi des sinus indique que le rapport de la longueur du côté sur le sinus de l'angle opposé est constant."):
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
        with self.voiceover(text="on peut donc calculer 2 côtés à partir d'un côté et deux angles."):
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
               Tex(r"En mesurant les angles entre ces points et en utilisant la loi des sinus, on va pouvoir calculer la distance de proche en proche."), 
               Text(r"Voyons cela sur un exemple")]
        ref = obj[0].to_edge(UP)
        with self.voiceover(text="Pour mesurer la distance entre deux points, on construit des triangles qui ont des côtés communs et on utilise la loi des sinus. Voyons sur un exemple") as tracker:
            for o  in obj:
                self.play(Write(o.scale(0.7).next_to(ref, DOWN)), run_time=tracker.duration/4.)
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
        
        with self.voiceover(text="on a repéré un premier point C."):
            self.play(g.animate.shift(3*DOWN))
        
        obj = [Tex(r"On pourrait mesurer AB directement dans le triangle ABC, comme vu précédemment."),
               Tex(r"Mais on suppose que B n'est pas visible depuis C, de sorte qu'on ne puisse pas mesurer l'angle ACB."),
               Tex(r"On va donc utiliser la triangulation pour calculer la distance AB de proche en proche.")]
            #    Tex(r"On suppose tout de même que l'on peut toujours mesurer l'angle CAB, ce qui est possible avec un théodolite en supposant que AB indique le nord magnétique")]
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
        with self.voiceover(text="ajoutons d'autres points de triangulation le long du chemin"):
            for d, p, t in zip(dots, points, txt):
                self.play(Create(d), Write(t.next_to(p)))

        mes = [inter(A, B, p, q) for p, q in zip(points[:-1], points[1:])]
        # for p, t in zip(mes, ["H", "I", "J", "K"]):
        #     self.play(Create(Dot(p)), Write(Text(t).next_to(p)))
        AC = Line(A, C, color=RED)
        CD = Line(C, D)
        AD = Line(A, D)
        with self.voiceover(text="On va mesurer la distance AG"):
            self.play(Create(AC))
            self.play(Create(CD))
            self.play(Create(Dot(mes[0])), Write(Tex("G").scale(self.sc).next_to(mes[0], UR)))
        c1 = Angle.from_three_points(A, C, D)
        a1 = Angle.from_three_points(C, A, B, other_angle=True)
        a2 = Angle.from_three_points(D, A, B)
        a3 = Angle.from_three_points(D, A, C)
        with self.voiceover(text="Dans le triangle ACG, on a mesuré AC et les angles issus de A et de C. On peut donc calculer AG et CG."):
            triangule(A, C, mes[0], "ACG", a1, c1, AC)
        self.remove(a1, a2, a3, c1)
        
        with self.voiceover(text="Pour progresser, il faut également mesurer la distance GD. Dans le triangle ACD, on calcule CD."):
            self.play(Create(Line(A, D)))
            triangule(A, C, D, "ACD", a3, c1, AC)
        CD = Line(C, D)
        DE = Line(D, E)
        self.remove(a3, c1)
        
        with self.voiceover(text="A ce stade, on a donc réussi à calculer toutes les distances entre les points A, C, G et D."):
            pass
        
        with self.voiceover(text="Avançons et mesurons la distance GH."):
            self.play(Create(DE))
            self.play(Create(Dot(mes[1])), Write(Tex("H").scale(self.sc).next_to(mes[1], DOWN)))        
        self.wait(2)
        GD = Line(D, mes[0])
        d1 = Angle.from_three_points(mes[1], D, mes[0])
        g1 = Angle.from_three_points(C, mes[0], A)
        g2 = Angle.from_three_points(D, mes[0], mes[1])
        with self.voiceover(text="Ces deux angles sont égaux. Si, depuis D, je mesure l'angle entre C et E, je peux mesurer tout le triangle DGH."):
            self.play(
                FadeOut(Text("Ces deux angles sont égaux").scale(self.sc).to_edge(UP)), 
                Indicate(g1, scale_factor=self.scale_factor), 
                Indicate(g2, scale_factor=self.scale_factor), 
                run_time=self.play_rt)
            triangule(mes[0], mes[1], D, "DHG", d1, g2, GD)
        with self.voiceover(text="On a ainsi calculé la distance GH. Pour avancer, il faut également calculer la distance E D."):
            self.remove(d1, g1, g2)
        
        with self.voiceover(text="Dans le triangle CDE, on a déjà calculé la distance CD. En mesurant les angles depuis C et E, on peut calculer E D."):
            self.play(Create(Line(C, E)))
            self.wait(2)
            c2 = Angle.from_three_points(E, C, D, other_angle=True)
            e1 = Angle.from_three_points(C, E, D)
            #self.play(Create(c2), Create(e1))
            triangule(C, D, E, "CDE", c2, e1, CD)
        self.remove(c2, e1)

        EF = Line(E, F)
        EI = Line(E, mes[1])
        with self.voiceover(text="Pour avancer, on répète les étapes précédentes. On va mesurer la distance entre H et I. Puis entre I et B."):
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
        with self.voiceover(text="A l'aide de la mesure d'angles et celle d'un côté, on a ainsi pu déterminer la distance AB de proche en proche."):
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

            obj = Text("On cherche la distance AB").move_to([3.5,3.5,0]).scale(self.sc)
            ref = obj
            with self.voiceover(text="On se donne deux points A et B dont on cherche à mesurer la distance.") as tracker:
                self.play(Create(points[0]), Create(txt[0].next_to(A, LEFT).scale(self.sc)), 
                        Create(points[1]), Create(txt[1].next_to(B).scale(self.sc)), 
                        AnimationGroup(Create(AB), Write(obj), lag_ratio=0.25),
                        run_time=tracker.duration)
            # self.play(AnimationGroup(Create(AB), Write(obj), lag_ratio=0.25), run_time=self.play_rt)
            with self.voiceover(text="Prenons 2 points C et D de part et d'autre de AB."):
                self.play(FadeOut(Tex("Prenons 2 points C et D de part et d'autre de AB").scale(self.sc).next_to(ref, DOWN)),
                        Create(points[2]), Write(txt[2].next_to(C, UP).scale(self.sc)), 
                        Create(points[3]), Write(txt[3].next_to(D).scale(self.sc)), run_time=self.play_rt)              
                self.play(Create(CD), run_time=self.play_rt) 
            with self.voiceover(text="On mesure la distance AC et on va calculer la distance entre A et H."):
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
            with self.voiceover(text="On mesure les angles issus de A et de C"):
                self.play(FadeOut(Tex(r"Mesure $\alpha _2$ et $\gamma _2$").scale(self.sc).next_to(ref, DOWN)),
                        Create(a2), Write(eq_a2.next_to(a2, UP)), 
                        Create(c2), Write(eq_c2.next_to(c2, DOWN, buff=0.1)), run_time=self.play_rt)
            with self.voiceover(text="dans le triangle AHC, on connait AC et les 2 angles. On peut donc calculer A H."):
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
            with self.voiceover(text="De même, on va calculer la distance BH dans le triangle BHC"):
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
            with self.voiceover(text="On a donc exprimé BH en fonction de BC."):
                self.play(FadeOut(Tex(r"on en déduit donc HB en fonction de BC").scale(self.sc).next_to(ref, DOWN)),          
                        Create(Line(start=H, end=B, color=RED)), run_time=self.play_rt)
                eq_BH = MathTex(r"HB = BC {sin(\gamma _1 ) \over sin(\gamma _1+ \beta _1)}").scale(self.sc).next_to(ref, DOWN)
                self.play(Write(eq_BH), run_time=self.play_rt)
                self.play(Create(SurroundingRectangle(eq_BH, color=YELLOW)), run_time=1)
                ref = eq_BH
            with self.voiceover(text="Il faut maintenant calculer BC."):
                dist_BC = Tex("Il faut donc calculer BC").scale(self.sc).next_to(ref, DOWN)
                self.play(Write(dist_BC), run_time=self.play_rt)
            ref = dist_BC
            b2 = Angle.from_three_points(A, B, D, radius=0.5, color=RED)
            eq_b2 = MathTex(r"\beta _2").scale(self.sc).set_color(RED)
            with self.voiceover(text="depuis B, on peut mesurer l'angle entre A et D. Dans le triangle CBD, on peut exprimer BC en fonction de CD. "):
                self.play(Create(BD),
                        FadeOut(Tex(r"Mesure $\beta _2$ l'angle ABD").scale(self.sc).next_to(ref, DOWN)),
                        Create(b2), 
                        Write(eq_b2.next_to(b2, LEFT, buff=0.1)), run_time=self.play_rt)
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
            with self.voiceover(text="Il ne reste plus qu'à calculer CD. Pour cela, on regarde le triangle ACD."):
                dist_CD = Tex("On va calculer CD dans le triangle ACD").scale(self.sc).next_to(ref, DOWN)
                self.play(Write(dist_CD), 
                        Create(AD), run_time=self.play_rt) 
            ref = dist_CD
            a1 = Angle.from_three_points(D, A, B, color=RED, radius=0.5)
            eq_a1 = MathTex(r"\alpha _1").scale(self.sc).set_color(RED)
            with self.voiceover(text="Depuis A, on mesure l'angle entre B et D. Dans le triangle ACD, on connait AC et les 2 angles, on peut donc en déduire CD."):
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
            with self.voiceover(text="Et en définitive, on mesure AB comme la somme de A H et HB."):
                endef = Tex(r"En définitive:").scale(self.sc).next_to(ref, DOWN)
                self.play(Write(endef))
                ref = endef
                eq_AB = MathTex(r"AB = AH + HB").scale(self.sc).next_to(ref, DOWN)
                self.play(Write(eq_AB))
                self.play(Create(SurroundingRectangle(eq_AB, color=YELLOW)), run_time=1)