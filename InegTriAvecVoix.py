# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:40:17 2022

@author: guillaume
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

# class test(MovingCameraScene):
#     def construct(self):
#         circle = Circle(radius=1).to_corner(UP+RIGHT)
#         square = Square().to_corner(UP+LEFT)
#         self.play(Create(circle), Create(square))

#         self.camera.frame.save_state()
#         self.play(self.camera.frame.animate.set(width=2*circle.width).move_to(circle))
#         self.play(Restore(self.camera.frame))


class InegaliteTriangulaire(VoiceoverScene, MovingCameraScene):
    def construct(self):
        
        self.set_speech_service(GTTSService(lang="fr"))
        #self.set_speech_service(RecorderService())

        a = 2
        b = ValueTracker(1.)
        A = [-a, 0, 0]
        B = [1, b.get_value(), 0]
        C = [a, 0, 0]
        H = [1, 0, 0]
        pt_H = Dot(H, color=GREEN)
        R = 1 + a
        theta = np.arctan(b.get_value()/R)
        M = [- a + R * np.cos(theta), R * np.sin(theta), 0]
        pt_M = Dot(M, color=YELLOW)
        cercle_M = Circle(radius=R).shift(a*LEFT)
        R2 = a - 1
        theta2 = np.arctan(b.get_value()/R2)
        N = [a - R2 * np.cos(theta2), R2 * np.sin(theta2), 0]
        pt_N = Dot(N, color=YELLOW)
        cercle_N = Circle(radius=R2).shift(a*RIGHT)
        BH = Line(B, H)
        sc = 1
        tri = Polygon(A, B, C).set_fill(BLUE, opacity=0.5)
        txt_a = MathTex('A').next_to(A, LEFT).scale(sc)
        txt_b = MathTex('B').next_to(B, UP).scale(sc)
        txt_c = MathTex('C').next_to(C, RIGHT).scale(sc)
        txt_h = MathTex('H').next_to(H, DOWN).scale(sc)
        txt_m = MathTex('M').next_to(M, LEFT).scale(sc)
        txt_n = MathTex('N').next_to(N, RIGHT).scale(sc)
        g = VGroup(tri, txt_a, txt_b, txt_c)
        
        phrases = [
            "On part d'un triangle ABC quelconque dans le plan.",
            "On cherche à déterminer une relation entre les distances AB, AC et BC.",
            "Supposons que AC soit le côté le plus long.",
            "Comme le plus court chemin entre deux points est toujours la ligne droite, on s'attend à ce que la distance AC soit supérieure à AB + BC.",
            "Dis autrement, il est plus court d'aller directement de A à C plutôt que de passer de A à B puis de B à C.",
            "Voyons pourquoi c'est vrai, et dans quel cas il y a égalité."
        ]

        with self.voiceover(text = phrases[0]):
            self.play(Create(g.shift(2*DOWN)))
        with self.voiceover(text=" ".join(phrases[1:])) as tracker:
            self.play(FadeOut(Paragraph(
                "L'inégalité triangulaire.",
                "la ligne droite entre 2 points est la distance la plus courte.",
                "Oui, mais pourquoi?").scale(0.7).to_edge(UP)), run_time=tracker.duration)
        self.wait(2)

        phrases = [
            "Notons H le projeté orthogonal de B sur AC.",
            "On va montrer que A H est inférieure à AB.",
            "Et que HC est aussi inférieure à BC.",
            "Comme les points A, H et C sont alignés, on a A H + HB = AC.",
            "On aura bien prouvé que AC < AB + BC."
        ]
        texte = VGroup(*[Tex(p) for p in phrases]).arrange(DOWN).scale(0.8).to_corner(UP+RIGHT)
        with self.voiceover(text=" ".join(phrases)) as tracker:
            self.play(
                Create(texte), 
                Create(pt_H.shift(2*DOWN)), 
                Create(txt_h.shift(2*DOWN)),
                Create(BH.shift(2*DOWN)),
            run_time=3)
        
        g.add(pt_H, BH, txt_h)
        self.play(g.animate.shift(4*LEFT+2*UP))
        self.remove(*texte)

        phrases = [
            "Montrons que A H < AB.",
            "Traçons le cercle de centre A qui passe par H.",
            "Il coupe la droite AB en un point M"
        ]
        # texte = VGroup(*[Text(p) for p in phrases]).arrange(DOWN).scale(0.8).to_edge(UR)
        self.camera.frame.save_state()
        with self.voiceover(text=" ".join(phrases)) as tracker:
            cercle_M = Circle(radius=R)
            self.play(
                # Create(texte), 
                Create(cercle_M.shift((4+a)*LEFT)),
                Create(pt_M.shift(4*LEFT)), 
                Create(txt_m.shift(4*LEFT)),
            run_time=3)
            self.play(self.camera.frame.animate.set(width=2).move_to(pt_M))
        self.play(Restore(self.camera.frame))

        phrases=[
            "On a donc A M  = A H.",
            "Les points A, M et B sont alignés. Et donc, AB = A M + MB.",
            "Comme B se trouve sur la tangente à C issue de H, B se situe à l'extèrieur du cercle.",
            "On a donc AB > A M et AB > A H, ce que nous voulions démontrer."
        ]
        eqs = VGroup(
            *[
            Tex(r"Donc, $AM = AH$"), 
            Tex(r"Or, $AB = AM + MB$"),
            Tex(r"Ainsi, $AB > AM$"),
            MathTex(r"AB > AH"),
        ]).arrange(DOWN).to_edge(UR)
        for p, e in zip(phrases, eqs):
            with self.voiceover(text=p) as tracker:
                self.play(Create(e), run_time=tracker.duration)

        phrases = [
            "De même, en considérant le cercle de centre C qui passe par H.",
            "Il coupe la droite BC en N.",
            "Et on obtient BC > B H"] 
        eqs.add(MathTex(r"BC > HC").next_to(eqs.get_bottom(), DOWN))       
        with self.voiceover(text=" ".join(phrases)) as tracker:
            cercle_N = Circle(radius=R2).shift((4-a)*LEFT)
            self.play(
                Create(cercle_N),
                Create(pt_N.shift(4*LEFT)),
                Create(txt_n.shift(4*LEFT)))
            self.wait(1)
            self.play(Create(eqs[-1]))

        dessin = g.add(pt_M, pt_N, txt_m, txt_n, cercle_M, cercle_N)

        eqs.add(MathTex(r"AB+BC \geq AH+HC = AC").to_edge(RIGHT))
        with self.voiceover(text="Comme les points A, H et C sont alignés, on a AB + BC > A H + HC qui vaut AC"):
            self.play(Create(eqs[-1]))

        self.wait(2)
        phrases = [
            "Regardons maintenant les cas où il y égalité.",
            "Sur le dessin, on voit que, pour aller de A à  C en passant par B, cela rajoute seulement les distances BM et BN.",
            "Et ces deux distances seront d'autant plus petites que B se rapproche de H.",
            "Faisons donc tendre B vers H et voyons ce qui se passe."
        ]
        with self.voiceover(text=phrases[0]):
            self.remove(*eqs)
            self.play(dessin.animate.shift(2*RIGHT))

        with self.voiceover(text=phrases[1]) as tracker:
            self.play(
                Indicate(Line(np.array(M), np.array(B)).shift(2*LEFT),scale_factor=2),
                Indicate(Line(np.array(B), np.array(N)).shift(2*LEFT),scale_factor=2), 
                run_time=tracker.duration
                )
               
        with self.voiceover(text=" ".join(phrases[2:])):
            pass
        self.clear()

        phrases=[
            "A mesure que B se rapproche de H, les distances MB et NB se rapprochent de 0.",
            "Elles sont nulles lorsque B = H et que les points A B et C sot alignés."
            ]
        with self.voiceover(text=" ".join(phrases)):
            self.show_limit()

        phrases = [
            "On vient donc de voir que dans un triangle quelconque, la longueur du plus grand côté est supérieure à la somme des deux autres côtés",
            "Et qu'il y a égalité lorsque les points A B et C sont alignés."
        ]
        with self.voiceover(text=" ".join(phrases)) as tracker:
            self.play(self.camera.frame.animate.set(width=20), run_time=0.5*tracker.duration)
            self.play(Create(MathTex(r"AC \leq AB + BC").to_edge(UP)),run_time=0.25*tracker.duration)

    def show_limit(self):

        a = 2
        b = ValueTracker(1.)
        A = [-a, 0, 0]
        B = [1, b.get_value(), 0]
        C = [a, 0, 0]
        H = [1, 0, 0]
        pt_H = Dot(H, color=GREEN)
        R = 1 + a
        theta = np.arctan(b.get_value()/R)
        M = [- a + R * np.cos(theta), R * np.sin(theta), 0]
        pt_M = Dot(M, color=YELLOW)
        cercle_M = Circle(radius=R).shift(a*LEFT)
        R2 = a - 1
        theta2 = np.arctan(b.get_value()/R2)
        N = [a - R2 * np.cos(theta2), R2 * np.sin(theta2), 0]
        pt_N = Dot(N, color=YELLOW)
        cercle_N = Circle(radius=R2).shift(a*RIGHT)
        BH = Line(B, H)
        sc = 0.8
        txt_a = MathTex('A').next_to(A, LEFT).scale(sc)
        txt_b = MathTex('B').next_to(B, UP).scale(sc)
        txt_c = MathTex('C').next_to(C, RIGHT).scale(sc)
        txt_h = MathTex('H').next_to(H, DOWN).scale(sc)
        txt_m = MathTex('M').next_to(M, LEFT).scale(sc)
        txt_n = MathTex('N').next_to(N, RIGHT).scale(sc)
        tri = Polygon(A, B, C).set_fill(BLUE, opacity=0.5)
        tri.add_updater(lambda 
                        m:m.become(Polygon(A, np.array([1, b.get_value(),0]), C))
        )
        BH = Line(B, H).add_updater(
            lambda m:m.become(
                Line(np.array([1, b.get_value(),0]), H))
        )
        pt_M.add_updater(
            lambda m:m.become(
                Dot(
                    [- a + R * np.cos(np.arctan(b.get_value()/R)), 
                    R * np.sin(np.arctan(b.get_value()/R)), 0], color=YELLOW)))
        txt_m.add_updater(lambda m:m.next_to(pt_M, LEFT))
        txt_n.add_updater(lambda m:m.next_to(pt_N, RIGHT))
        pt_B = Dot(B)
        pt_B.add_updater(lambda m:m.become(Dot(np.array([1, b.get_value(),0]))))
        txt_b.add_updater(lambda m:m.next_to(pt_B, UP if b.get_value()>0 else DOWN))
        pt_N.add_updater(
            lambda m:m.become(
                Dot(
                    [a - R2 * np.cos(np.arctan(b.get_value()/R2)), 
                    R2 * np.sin(np.arctan(b.get_value()/R2)), 0], color=YELLOW)))
        self.add(tri, txt_a, txt_b, txt_c, BH, pt_B, pt_M, txt_m, cercle_M, cercle_N, pt_N, txt_n, pt_H, txt_h)
        value = np.linspace(1., -1., 10)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(height=2).move_to(pt_H))
        for v in value:
            print(v)
            self.play(b.animate.set_value(v), 
                    rate_func=linear)
        self.play(Restore(self.camera.frame))
        self.wait()