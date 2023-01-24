# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:47:30 2022

@author: guillaume
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
#from manim_voiceover.services.recorder import RecorderService

class MonPythagore(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="fr"))
        #self.set_speech_service(RecorderService())
        self.Pythagore()
        self.wait(3)
        self.clear()
        self.PythagoreNonRectangle()


    def Pythagore(self):
  
        text_to_remove = []
        cycle = [LEFT, DOWN, RIGHT, UP]
        def montre_longueur(triangle, idx):
            [A, B, C] = [triangle.get_vertices()[i] for i in range(3)]
            [I, J, K] = [0.5*(B+C), 0.5*(A+C), 0.5*(A+B)]
            txt_a = MathTex('a').next_to(I, cycle[idx], buff=0.1).scale(0.5)
            txt_b = MathTex('b').next_to(J, cycle[(idx+1)%4], buff=0.1).scale(0.5)
            txt_c = MathTex('c').next_to(K, cycle[(idx+3)%4], buff=0.1).scale(0.5)
            text_to_remove.append(txt_a)
            text_to_remove.append(txt_b)
            text_to_remove.append(txt_c)
            # self.add(txt_a, txt_b, txt_c)
            self.play(FadeIn(txt_a, txt_b, txt_c))
        
        a, b = 4, 2
        A = [a, 0, 0]
        B = [0, b, 0]
        C = [0, 0, 0]
        tri = Polygon(A, B, C).set_fill(BLUE, opacity=0.5)
        tri.shift(6*LEFT+3*DOWN)
        indice = 0
        with self.voiceover(text='Prenons un triangle rectangle de cotés a, b et c') as tracker:
            self.play(tri.animate)
            montre_longueur(tri, indice)
        new_petit_carre = [tri.get_vertices()[0]]
        new_grand_carre = [tri.get_vertices()[2]]
        # def rotate_and_shift(triangle, direction):
        #     new_tri = triangle.copy()
        #     self.add(new_tri)
        #     self.play(Rotate(new_tri, PI/2, about_point = new_tri.get_vertices()[2]))
        #     self.play(new_tri.animate.shift((a+b)*direction))
        #     return (new_tri)
        O = [0.5*(tri.get_vertices()[0][0] + tri.get_vertices()[1][0] - tri.get_vertices()[0][1] + tri.get_vertices()[1][1]),
             0.5*(tri.get_vertices()[0][1] + tri.get_vertices()[1][1] + tri.get_vertices()[0][0] - tri.get_vertices()[1][0]),
             0]
        def rotate_and_shift(triangle, direction):
            new_tri = triangle.copy()
            self.add(new_tri)
            self.play(Rotate(new_tri, PI/2, about_point = O))
            return (new_tri)
        triangles = [tri]
        with self.voiceover(text="appliquons lui une rotation de 90 degrés, et répétons cette opération pour former un carré"):
            for d in [RIGHT, UP, LEFT]:
                aux = rotate_and_shift(tri, d)
                triangles.append(aux)
                new_petit_carre.append(aux.get_vertices()[0])
                new_grand_carre.append(aux.get_vertices()[2])
                tri = aux
                indice += 1
                montre_longueur(aux, indice)
        petit_sommets = VGroup(*[Dot(new_petit_carre[i], color=RED) for i in range(4)])
        petit_carre = Polygon(*new_petit_carre).set_fill(RED, opacity = 0.25)
        with self.voiceover(text="on a créé un premier petit carré au centre"):
            self.play(Create(petit_sommets))
            self.play(Create(petit_carre))
        grand_sommets = VGroup(*[Dot(new_grand_carre[i], color=WHITE) for i in range(4)])
        grand_carre = Polygon(*new_grand_carre).set_fill(WHITE, opacity = 0.25)
        with self.voiceover(text="et un second plus grand"):
            self.play(Create(grand_sommets))
            self.play(Create(grand_carre))
        self.wait(2)
        
        self.remove(*text_to_remove)
        self.remove(*[petit_sommets, grand_sommets])
        
        white = VGroup(grand_carre.copy(), *[t.copy() for t in triangles])
        with self.voiceover(text="on peut arranger nos triangles de cette manière"):
            self.play(white.animate.shift((a+b+1)*RIGHT))
            self.play(Rotate(white[1], -PI/2, about_point = white[1].get_vertices()[0]))
            self.play(Rotate(white[4], PI/2, about_point = white[4].get_vertices()[1]))
        
        self.wait(2)
        with self.voiceover(text="on fait ainsi apparaitre un premier carré de coté a"):
            montre_longueur(triangles[0], 0)
            self.play(FadeIn(MathTex("a").scale(0.5).next_to(white[1].get_left(), LEFT)))
            self.play(FadeIn(MathTex("a").scale(0.5).next_to(triangles[0].get_bottom(), UP).shift((a+b+1)*RIGHT)))
        with self.voiceover(text="et un autre de coté b"):
            self.play(FadeIn(MathTex("b").scale(0.5).next_to(white[4].get_left(), LEFT)))
            self.play(FadeIn(MathTex("b").scale(0.5).next_to(triangles[3].get_top(), UP).shift((a+b+1)*RIGHT)))
        with self.voiceover(text="l'aire du carré rouge est c carré"):
            c2 = MathTex(r"{{c^2}}").next_to(grand_carre.get_center(), 0.5*LEFT)
            self.play(FadeIn(c2))
        mid_A =  white[1].get_vertices()[0] + [-0.5*a, 0.5*a, 0]
        mid_B =  white[4].get_vertices()[1] + [-0.5*b, -0.5*b, 0]
        a2 = MathTex(r"{{a^2}}").next_to(mid_A, 0.5*LEFT)
        b2 = MathTex(r"{{b^2}}").next_to(mid_B, 0.5*LEFT)
        with self.voiceover(text="qui doit donc être égale à l'aire du carré de coté a"):
            self.play(FadeIn(a2))
        with self.voiceover(text="+ l'aire du carré de coté b"):
            self.play(FadeIn(b2))
        with self.voiceover(text="On a ainsi montré le théorème de Pythagore: c carré égal a carré + b carré"):
            eq = MathTex(r"{{c^2}} = {{a^2}} + {{b^2}}").to_edge(UP).shift(0.2*UP).set_color(TEAL)
            variables = VGroup(c2.copy(), a2.copy(), b2.copy())
            self.play(TransformMatchingTex(variables, eq), run_time=3)
            self.play(Create(SurroundingRectangle(eq, color=RED)))


    def PythagoreNonRectangle(self):
        
        def inter(A, B, C, D):
            a1 = (B[1] - A[1])/(B[0] - A[0])
            b1 = A[1] - a1 * A[0]
            a2 = (D[1] - C[1])/(D[0] - C[0])
            b2 = C[1] - a2 * C[0]
            x = - (b2 - b1)/(a2 - a1)
            y = a1 * x + b1
            return ([x, y, 0])
                
        a, b = 3, 2
        A = [a, 0, 0]
        B = [0, b, 0]
        C = [0.5, 0.5, 0]
        C_carre = [0, 0, 0]
        tri_rect = Polygon(A, B, C_carre).set_fill(BLUE, opacity=0.2).shift(6*LEFT+3*DOWN)
        orig_tri = Polygon(A, B, C).set_fill(BLUE, opacity=0.5)
        orig_tri.shift(6*LEFT+3*DOWN)
        text = VGroup(Text("Modifions le triangle rectangle pour qu'il devienne quelconque"), 
                      Text("et appliquons les mêmes transformations")
                      ).arrange(DOWN).scale(0.5).to_edge(UP)
        # self.add(text)
        # self.play(
        #     AnimationGroup(
        #          *[Write(t) for t in text],
        #          lag_ratio=1),
        #     )
        with self.voiceover(text="que se passe-t-il si le triangle de départ n'est plus rectangle?"):
            pass
        with self.voiceover(text="Modifions le triangle rectangle pour qu'il devienne quelconque") as tracker:
            self.play(Write(text[0]))
            self.play(Transform(tri_rect, orig_tri), run_time=tracker.duration)
        # self.play(Create(orig_tri))
        O = [0.5*(orig_tri.get_vertices()[0][0] + orig_tri.get_vertices()[1][0] - orig_tri.get_vertices()[0][1] + orig_tri.get_vertices()[1][1]),
             0.5*(orig_tri.get_vertices()[0][1] + orig_tri.get_vertices()[1][1] + orig_tri.get_vertices()[0][0] - orig_tri.get_vertices()[1][0]),
             0]
        def rotate_and_shift(triangle, direction):
            new_tri = triangle.copy()
            self.add(new_tri)
            self.play(Rotate(new_tri, PI/2, about_point = O))
            return (new_tri)
        # def rotate_and_shift(triangle, direction):
        #     new_tri = triangle.copy()
        #     self.add(new_tri)
        #     self.play(Rotate(new_tri, PI/2, about_point = new_tri.get_vertices()[2]))
        #     direction = (new_tri.get_vertices()[1][1] - tri.get_vertices()[0][1]) * DOWN 
        #     direction += (new_tri.get_vertices()[1][0] - tri.get_vertices()[0][0]) * LEFT
        #     self.play(new_tri.animate.shift(direction))
        #     return (new_tri)
        
        new_groups, corners, petit_tris, new_tris = [], [], [], []
        A, C = orig_tri.get_vertices()[0], orig_tri.get_vertices()[2]
        tri = orig_tri
        with self.voiceover(text="et appliquons les mêmes transformations"):
            self.play(Write(text[1]))
            for d in range(3): 
                aux = rotate_and_shift(tri, d)
                new_A, new_C = aux.get_vertices()[0], aux.get_vertices()[2]
                corner = inter(A, C, new_A, new_C)
                corners.append(corner)
                petit_tri = Polygon(corner, aux.get_vertices()[2], aux.get_vertices()[1])
                petit_tri.set_fill(color=WHITE, opacity=0.5)
                new_groups.append(VGroup(aux, petit_tri))
                petit_tris.append(petit_tri)
                new_tris.append(aux)
                tri = aux
                A, C = new_A, new_C
        self.remove(*text)
        text = VGroup(Text("On retrouve bien le carré central"),
                      Text("Mais le grand carré est devenu un octogone."),
                      Text("Pour récupérer le grand carré, il faut ajouter 4 triangles identiques")
                      ).arrange(DOWN).scale(0.5).to_edge(UP)

        corner = Dot(corners[1]).rotate(angle=PI/2, about_point=corners[0]).get_center()
        last_tri = Polygon(corner, orig_tri.get_vertices()[2], orig_tri.get_vertices()[1])
        last_tri.set_fill(color=WHITE, opacity=0.5)
        corners.append(corner)
        petit_tris.append(last_tri)
        new_groups.append(VGroup(orig_tri, last_tri))
        new_tris.append(orig_tri)
        carre_rouge = Polygon(*[t.get_vertices()[0] for t in new_tris], 
                              fill_opacity=0.5, fill_color=RED)
        
        with self.voiceover(text="On retrouve bien le carré central, mais le grand carré est devenu un octogone") as tracker:
            self.play(
                AnimationGroup(
                    Create(carre_rouge),
                     *[Write(t) for t in text[:-1]],
                     lag_ratio=1),
                )
        with self.voiceover(text="pour récupérer le grand carré, il faut ajouter 4 triangles identiques"):
            self.play(Write(text[-1]))
            self.play(Create(petit_tris[0]))
            tri_copy = [t.copy() for t in petit_tris]
            for i in range(3):
                self.play(Rotate(tri_copy[i], 
                             angle=PI/2, 
                             about_point=inter(corners[0], corners[2], corners[1], corners[3])))
        self.wait(2)
        
        self.remove(carre_rouge)
        
        with self.voiceover(text="on se retrouve dans la configuration précédente"):
            self.play(Create(Polygon(*corners, fill_opacity=0.1, fill_color=WHITE)))
            white = VGroup(*[m.copy() for m in new_groups])
            self.play(white.animate.shift((a+b+1)*RIGHT))
        self.wait(2)
        self.remove(tri_copy[1])
        self.remove(tri_copy[2])
        # self.remove(orig_tri)
        # self.remove(tri)
        # self.remove(aux)
        self.remove(tri_rect)
        self.play(Rotate(new_groups[3], -PI/2, about_point=new_groups[3][0].get_vertices()[0]))
        self.play(Rotate(new_groups[2], PI/2, about_point=new_groups[2][0].get_vertices()[1]))
        
        aa, bb = corners[2], new_groups[2][0].get_vertices()[1]
        cc = new_groups[2][1].get_vertices()[0]
        dd = inter(aa, corners[3], cc, new_groups[2][1].get_vertices()[1])
        AA = dd
        BB = corners[3]
        CC = new_groups[3][0].get_vertices()[0]
        DD = new_groups[3][1].get_vertices()[0]
        self.play(Create(Polygon(aa, bb, cc, dd).set_fill(color=YELLOW, opacity=0.2)))
        self.play(Create(Polygon(AA, BB, CC, DD).set_fill(color=RED, opacity=0.2)))
        eq_c = MathTex(r"{{c}}").next_to([3.7,0.7,0],DOWN)
        eq_x = MathTex(r"{{x}}").next_to([-2.5,-1,0],LEFT)
        eq_y = MathTex(r"{{y}}").next_to([-4.5,1.8,0],LEFT)
        self.play(*[Create(eq) for eq in [eq_c, eq_x, eq_y]])
        with self.voiceover(text="on retrouve donc le résultat précédent mais avec des longueurs de triangles qui sont modifiées"):
            eq = MathTex(r"{{c}}^2 = {{x}}^2 + {{y}}^2").to_edge(UP).set_color(TEAL)
            variables = VGroup(eq_c.copy(), eq_x.copy(), eq_y.copy())
            self.remove(*text)
            self.play(TransformMatchingTex(variables, eq), run_time=3)
            self.play(Create(SurroundingRectangle(eq, color=RED)))
        self.wait(2)
        with self.voiceover(text="exprimons x et y en fonction du triangle de départ"):
            txt = Tex("exprimons $x$ et $y$ en fonction du triangle de départ").scale(0.8).to_edge(DOWN, buff=0.1)
            self.play(Write(txt), run_time=3)
        self.wait(2)
        self.clear()
       
        self.play(new_groups[2].animate.rotate(0.18).scale(2).move_to([-2, 0, 0]))
        [A, B, C] = new_groups[2][0].get_vertices()
        H = new_groups[2][1].get_vertices()[0]
        eq_scale=0.7
        self.play(*[Write(MathTex(t).scale(eq_scale).next_to(p, d)) 
                          for t, p, d in zip(["A", 'B', 'C', 'H'], [A, B, C, H], [UR, UP, DOWN, DOWN])])
        I, J, K, L, M = [0.5*(B+C), 0.5*(A+C), 0.5*(A+B), 0.5*(C+H), 0.5*(B+H)]
        self.play(*[Write(MathTex(t).scale(eq_scale).next_to(p, d)) 
                          for t, p, d in zip(["a", 'b', "c", "z", 'y'], [I, J, K, L, M], [RIGHT, DOWN, UP, DOWN, LEFT])])
        br = Brace(Line(A,H)).shift(DOWN)
        x = MathTex("x = b + z").next_to(br, DOWN).scale(eq_scale)
        with self.voiceover(text="on pose x égale b + z"):
            self.play(Create(br), Create(x))
        with self.voiceover(text="on note C chapeau l'angle entre A, C et B"):
            self.play(Create(Angle.from_three_points(A, C, B)),
                      Write(MathTex(r"\hat C").next_to(C, UR).scale(eq_scale)))
        self.play(Create(Angle.from_three_points(B, C, H, radius=0.5)),
            Write(MathTex(r"\pi - \hat C").next_to(C, UL).scale(eq_scale)))

        txt = Tex(r"Dans le triangle rectangle BHC, on a:")
        eq_y = MathTex(r"{{y}}=a sin(\pi - \hat C) = {{a sin(\hat C)}}")
        eq_z = MathTex(r"z=a cos(\pi - \hat C) = -a cos(\hat C)")
        eq_x = MathTex(r"{{x}} = b + z = {{b - a cos(\hat C)}}")
        eq_or = MathTex(r"{{c^2}} = x^2 + y^2")
        eq = MathTex(r"{{c^2}} = {{x}}^2 + {{y}}^2 = ({{b - a cos(\hat C)}})^2 +{{(asin(\hat C))}}^2").next_to(eq_x, DOWN)
        eq2 = MathTex(r"c^2 = b^2 + a^2 -2abcos(\hat C)")
        eqs = VGroup(txt, eq_y, eq_z, eq_x, eq_or, eq, eq2).arrange(DOWN).move_to([3,1.2,0]).scale(eq_scale)
        for e in eqs[:4]:
            self.play(Write(e))
        self.wait(2)
        with self.voiceover(text="Dans la partie précédente, nous avons vu que c carré = x carré + y carré"):
            self.play(Write(eq_or))
        with self.voiceover(text="en remplaçant et en développant, on obtient") as tracker:
            self.play(TransformMatchingTex(VGroup(eq_y.copy(), 
                                                  eq_z.copy(), 
                                                  eq_or.copy()), 
                                           eq), 
                      run_time=tracker.duration)        
        # for e in eqs[4:]:
        #     self.play(Write(e))
        with self.voiceover(text="C'est l'équation d'Al Kashi"):
            self.play(Write(eq2))
            self.play(Create(SurroundingRectangle(eq2, color=RED)))
        
        
#     def Pythagore(self):
#         cycle = [LEFT, DOWN, RIGHT, UP]
#         def montre_longueur(triangle, idx):
#             [A, B, C] = [triangle.get_vertices()[i] for i in range(3)]
#             [I, J, K] = [0.5*(B+C), 0.5*(A+C), 0.5*(A+B)]
#             txt_a = Text('a').next_to(I, cycle[idx], buff=0.1).scale(0.5)
#             txt_b = Text('b').next_to(J, cycle[(idx+1)%4], buff=0.1).scale(0.5)
#             txt_c = Text('c').next_to(K, cycle[(idx+3)%4], buff=0.1).scale(0.5)
#             self.add(txt_a, txt_b, txt_c)
#             self.play(FadeIn(txt_a, txt_b, txt_c))
        
#         a, b = 4, 2
#         A = [a, 0, 0]
#         B = [0, b, 0]
#         C = [0, 0, 0]
#         tri = Polygon(A, B, C).set_fill(BLUE, opacity=0.5)
#         tri.shift(6*LEFT+3*DOWN)
#         indice = 0
#         self.play(tri.animate)
#         montre_longueur(tri, indice)
#         new_petit_carre = [tri.get_vertices()[0]]
#         new_grand_carre = [tri.get_vertices()[2]]
#         def rotate_and_shift(triangle, direction):
#             new_tri = triangle.copy()
#             self.add(new_tri)
#             self.play(Rotate(new_tri, PI/2, about_point = new_tri.get_vertices()[2]))
#             self.play(new_tri.animate.shift((a+b)*direction))
#             return (new_tri)
#         for d in [RIGHT, UP, LEFT]:
#             aux = rotate_and_shift(tri, d)
#             new_petit_carre.append(aux.get_vertices()[0])
#             new_grand_carre.append(aux.get_vertices()[2])
#             tri = aux
#             indice += 1
#             montre_longueur(aux, indice)
#         petit_sommets = VGroup(*[Dot(new_petit_carre[i], color=RED) for i in range(4)])
#         petit_carre = Polygon(*new_petit_carre).set_fill(RED, opacity = 0.25)
#         self.play(Create(petit_sommets))
#         self.play(Create(petit_carre))
#         grand_sommets = VGroup(*[Dot(new_grand_carre[i], color=WHITE) for i in range(4)])
#         grand_carre = Polygon(*new_grand_carre).set_fill(WHITE, opacity = 0.25)
#         self.play(Create(grand_sommets))
#         self.play(Create(grand_carre))
#         self.wait(2)
        
#         white = grand_carre.set_fill(WHITE, opacity=1).animate.move_to([3, 3, 0]).scale(0.3)
#         self.play(white)
#         # self.play(FadeIn(Text("a+b").rotate(PI/2).next_to(white.get_right(), RIGHT, buff=0.1).scale(0.5)))
#         # self.play(FadeIn(Text("a+b").next_to(white.get_bottom(), DOWN, buff=0.1).scale(0.5)))

#         angle = np.arctan(a/b)
#         # print("angle=", angle)
# #        red = petit_carre.copy().set_fill(RED, opacity=1).animate.rotate(-angle).next_to(white.get_bottom(), DOWN).scale(0.3)
#         red = petit_carre.copy().set_fill(RED, opacity=1).animate.rotate(-angle).move_to([1,1,0]).scale(0.3)
#         self.play(red)
#         # self.play(FadeIn(Text("c").next_to(red.get_right(), RIGHT, buff=0.1).scale(0.5)))
#         # self.play(FadeIn(Text("c").next_to(red.get_bottom(), DOWN, buff=0.1).scale(0.5)))
        
#         # blue = tri.copy().animate.set_fill(BLUE, opacity=1).rotate(PI/2).next_to(red.get_bottom(), 2*DOWN).scale(0.3)
#         # self.play(blue)
#         # self.play(FadeIn(Text("a").next_to(blue.get_left(), LEFT, buff=0.1).scale(0.5)))
#         # self.play(FadeIn(Text("b").next_to(blue.get_bottom(), DOWN, buff=0.1).scale(0.5)))

        
#         # self.play(FadeIn(Text("(a+b)²").next_to(white.get_right(), 2*RIGHT)))
#         # self.play(FadeIn(Text("=").move_to([4, 1, 0])))
#         # self.play(FadeIn(Text("c²").next_to(red.get_right(), 2*RIGHT)))
#         # self.play(FadeIn(Text("+ 4").move_to([2, -3, 0])))
        # self.play(FadeIn(Text("c²").next_to(red.get_right(), 2*RIGHT)))
        
