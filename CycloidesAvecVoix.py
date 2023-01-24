# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:40:17 2022

@author: guillaume
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.recorder import RecorderService
import numpy as np

class cycloides(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="fr"))
        # self.set_speech_service(RecorderService())
        video = "Tout" #Roue, Poly ou Tout
        if video == "Roue":
            self.RouesQuiTournent()
        elif video == "Poly":
            self.PolygoneQuiTourne(True, False)
        elif video == "Tout":
            self.Intro()
            self.wait(3)
            self.clear()
            self.CycAvecRoue()
            with self.voiceover(text="Et si ce n'est plus un cercle qui roule, mais un polygône régulier, que devient la cycloide?"):
                self.play(Write(Tex(r"Et si ce n'est plus un cercle qui roule, mais un polygône régulier").scale(0.8)))
                self.play(Write(Tex(r" que devient la cycloïde?").scale(0.8).next_to(ORIGIN, DOWN)))
                self.wait(2)
            self.clear()
            self.CyclAvecPolygones()
        else:
            print("Mauvais Choix")
        
        
    def Intro(self):
        phrases = ["Prenons un cercle de centre Oméga ", 
                   "et considérons un point fixé sur le rayon vertical.",
                   "La trajectoire de ce point quand le cercle se déplace ",
                   "s'appelle une cycloïde."]
        texte= VGroup(Text(phrases[0], t2c={'cercle':RED, 'centre':BLUE}),
                      Text(phrases[1], t2c ={'point':YELLOW}),
                      Text(phrases[2], t2c={'cercle':RED, 'point':YELLOW}),
                      Text(phrases[3], t2c ={'cycloïde.':GREEN})) \
            .arrange(DOWN).scale(0.8).to_edge(UP)
        # Roue,_  = self.get_roue_qui_tourne(2, [-5, -1.5, 0], 0.5, False)
        roue = Circle(radius=2, stroke_color=RED).move_to([-5, -1.5, 0])
        h=ValueTracker(1)
        rayon = DashedLine(roue.get_center(), roue.get_bottom())#.scale(h,about_edge=UP)
        rayon.add_updater(lambda m, dt: 
                          m.become(DashedLine(roue.get_center(), roue.get_bottom()).scale(h.get_value(), about_edge=UP)))
        centre = Dot(rayon.get_start(), color=BLUE)
        point = Dot(rayon.get_end(), color=YELLOW)
        point.add_updater(lambda m:m.become(Dot(rayon.get_end(), color=YELLOW)))
        h_num = DecimalNumber(h.get_value(), color=RED).scale(0.5)
        # h_num = DecimalNumber(h.get_value(), color=RED, num_decimal_places=2, show_ellipsis=False)
        h_num.add_updater(lambda m: m.set_value(h.get_value()).next_to(rayon, RIGHT))
        self.add(roue, h_num, rayon, centre, point)
        with self.voiceover(text=phrases[0]+phrases[1]):
            self.play(*[Write(t) for t in texte[:2]])
        self.play(h.animate.set_value(0.0), run_time=2)
        self.play(h.animate.set_value(1.), run_time=2)
        with self.voiceover(text=phrases[2]+phrases[3]):
            for t in texte[2:]:
                self.play(Write(t))
        with self.voiceover(text="Voyons quelques exemples de trajectoires pour plusieurs points à différentes hauteurs du rayon"):
            pass
        
    def CycAvecRoue(self):
        r = 0.5
        run_time = 6
        v = (14. - 2. * r) / run_time
        w = v / r
        def avance(m, dt):
            m.rotate(- w * dt, about_point=m[0].get_center()).shift(v * dt * RIGHT)
        
        def build_objects(h, r):
            ligne = Line(7*LEFT, 7*RIGHT)
            roue = Circle(radius=r, stroke_color=RED).move_to ([-7 +r, r, 0])
            rayon = Line(roue.get_center(), roue.get_bottom()).scale(h,about_edge=UP)
            centre = Dot(rayon.get_start(), color=BLUE)
            point = Dot(rayon.get_end(), color=YELLOW)        
            roue_qui_tourne = VGroup(roue, rayon, centre, point)
            cycloide = TracedPath(point.get_center, stroke_width=5, stroke_color=GREEN)
            return (ligne, roue_qui_tourne, cycloide)
        liste_simu, liste_R = [], []        
        for h in [1, 0.75, 0.5, 0.1]:
            L, R, C = build_objects(h, r)
            text = Tex("distance: "+str(h)+" x rayon").scale(0.5).next_to(R.get_top(), UR)
            simu = VGroup(text, L, R, C)
            liste_simu.append(simu)
            liste_R.append(R)
        x = Group(*liste_simu).arrange(UP, buff = 0.2)
        self.add(x)
        for R in liste_R:
            R.add_updater(avance)
        self.play(R.animate, run_time=run_time,rate_func=linear)
        
        for R in liste_R:
            R.suspend_updating()
        self.wait(2)
        self.clear()
        
    def CyclAvecPolygones(self):
        dim = [3, 4,  5, 10]
        espace = 0.01
        scale = (8. - len(dim) * espace)/(2*len(dim)+4)
        print(scale)
        ords = [-4+scale + (8-2*scale)*i/(len(dim)) for i in range(len(dim))]
        center = [0,0,0]

        polys=[self.getPol(n, [-6, y, 0], scale, True, False)[0] for n, y in zip(dim, ords)]
        phrases = ["Prenons un polygône régulier à n côtés avec:", 
                   "son centre,", 
                   "son projeté orthogonal sur l'axe,",
                   "et le sommet à droite sur l'axe"]
        texte= VGroup(Text(phrases[0], t2c={'polygone':BLUE}),
                      Text(phrases[1], t2c={'centre':GREEN}),
                      Text(phrases[2], t2c ={'projeté orthogonal':YELLOW}),
                      Text(phrases[3], t2c={'sommet':RED})
                      ).scale(0.8).arrange(DOWN).to_edge(UP)
        phrase = phrases[0]+phrases[1]+phrases[2]+phrases[3]
        with self.voiceover(phrase) as tracker:
            self.play(*[FadeIn(t) for t in texte], 
                      *[Create(p) for p in polys],
                      run_time=tracker.duration)
        # self.play(*[Create(p) for p in polys])
            self.play(*[Write(MathTex(r"n="+str(n)).scale(0.5).move_to([-5,y+0.25,0])) 
                    for n, y in zip(dim, ords)])
        self.remove(*texte)
        with self.voiceover(text="on va faire rouler les polygones et on cherche la trajectoire du projeté et du sommet"):
            self.play(LaggedStart(
                FadeOut(Text("On va faire rouler les polygones", 
                             t2c={'polygones':BLUE}).scale(0.7).to_edge(UP)),
                FadeOut(Text("et on cherche la trajectoire du projeté et du sommet",
                             t2c={'projeté':YELLOW, 'sommet':RED}).scale(0.7).to_edge(DOWN).shift(RIGHT)),
                      lag_ratio = 0.75, run_time=6))
        with self.voiceover(text="Si on superpose les polygones sur leurs centres respectifs") as tracker:
            self.play(FadeOut(Text("Si on superpose les polygones sur leurs centres respectifs",
                                   t2c={'polygones':BLUE, 'centres':GREEN}).scale(0.7).to_edge(UP)),
                      run_time=tracker.duration)
            new_polys=[self.getPol(n, ORIGIN, 3, True, False)[0] for n, y in zip(dim, ords)]
            self.play(*[ReplacementTransform(p.copy(), new_p) for p, new_p in zip(polys, new_polys)])
            self.wait(2)
        circ = Circle(3, GREEN)
        text = "on retrouve le cercle circonscrit à chaque polygone"
        with self.voiceover(text=text) as tracker:
            self.play(Create(circ))
            self.play(LaggedStart(
                FadeOut(Text(text, t2c={'polygone':BLUE, 'cercle':GREEN}).scale(0.5).to_edge(UP)),
                FadeOut(Text("On devrait donc retrouver la cycloide du cercle").scale(0.5).to_edge(DOWN)),
                lag_ratio = 0.85, run_time=tracker.duration))
        self.remove(*new_polys, circ)
        
        with self.voiceover(text="Voyons ce que cela donne!"):
            pass
        g = []
        i=0
        one_sim_finish=[False]*len(dim)
        finish = False
        idx = [0]*len(dim)
        angles = []
        for n, y in zip(dim, ords):
            x, c = self.getPol(n, [-6, y, 0], scale, True, True)
            angles.append(self.get_angle(x[0], 0))
            # self.play(Create(x))
            g.append(x)
        while not finish and i < 100:
            i += 1
            finish = 1
            # print("i",i)
            animation=[]
            for sim, (n, angle) in enumerate(zip(dim, angles)):
                if not one_sim_finish[sim]:
                    x = g[sim]
                    c = x[0].get_vertices()[idx[sim]%n]
                    animation.append(Rotate(x, -angle, about_point=c))
                    one_sim_finish[sim] = (x[0].get_right()[0]>= 5.3)
                    idx[sim] += 1    
                    finish *= one_sim_finish[sim] 
            self.play(*animation, rate_func=linear, run_time=1)
        self.wait(2)
        with self.voiceover(text="On retrouve bien la cycloide du cercle"):
            self.CycloideAvecRoue(scale, 4-2*scale-0.1)
        
      # attention: comme pol.get_center()  renvoie le centre de la boite qui entoure pol
      # on ne retombe pas sur l'origine. Et les methodes scale ne sont plus exactes
      # on construit donc le polygone a partir du cercle directement
    def getPol(self, n, C, taille, withpointandcenter, withcycloide):
        #self.play(Create(Circle(radius=taille).move_to(C)))
        angle_redressement = 0.5 * (TAU * (n-1) / n - PI)
        thetas = [TAU * k / n - angle_redressement for k in range(n)]
        points = [[C[0] + taille * np.cos(theta), C[1] + taille * np.sin(theta), 0] for theta in thetas]
        pol = Polygon(*points, fill_color=PURPLE, fill_opacity=0.2)
        # self.add(pol)
        x = VGroup(pol)
        cycloides = None
        if withpointandcenter:
            A = pol.get_vertices()[0]        
            dotA = Dot(A, color=RED)
            rayon = DashedLine(C, pol.get_bottom())
            centre = Dot(C, color=GREEN)
            point = Dot(rayon.get_end(), color=YELLOW)
            x.add(dotA, rayon, centre, point)
            # self.add(x)
            if withcycloide:
                cycloides = [TracedPath(p.get_center, stroke_width=2.5, stroke_color=c) \
                                          for p, c in zip([point, dotA], [YELLOW, RED])]
                self.add(*cycloides)
                # self.wait()
        return (x, cycloides)
    
    def get_angle(self, polygone, index):
        n = polygone.get_vertices().shape[0]
        center = polygone.get_vertices()[index]
        prev = polygone.get_vertices()[(index+1)%n]
        if n>=5:
            angle = np.arctan((center[1] - prev[1])/(center[0] - prev[0]))
        elif n == 4:
            angle = 0.5 * PI
        elif n == 3:
            angle = PI + np.arctan((center[1] - prev[1])/(center[0] - prev[0]))
        return angle
    
    def PolygoneVersCercle(self, tailles, center, sc):
        for n in tailles:
            p, _ = self.getPol(n, center, sc, True, False)
            self.play(Create(p))
        self.play(Create(Circle(radius=1, color=GREEN).scale(sc).move_to(center)))
       
    def PolygoneQuiTourne(self, withpointandcenter, with_cycloid):
        dim = [3, 4,  5, 10]
        espace = 0.01
        scale = (8. - len(dim) * espace)/(2*len(dim)+4)
        ords = [-4+scale + (8-2*scale)*i/(len(dim)) for i in range(len(dim))]
        for n, y in zip(dim, ords):
            x, cycloids = self.getPol(n, [-6, y, 0], scale, withpointandcenter, with_cycloid)
            angle = self.get_angle(x[0], 0)
            idx = 0
            i=0 #securite
            while x[0].get_right()[0]<= 5.5 and i<100:
                i+=1
                self.play(Rotate(x, -angle, about_point=x[0].get_vertices()[idx%n]),
                          rate_func=linear, run_time=0.5)
                idx += 1
                
    def RouesQuiTournent(self):
        r = 1.5
        run_time = 4
        v = (14. - 2. * r) / run_time
        w = v / r
        hauteur = [1, 0.5]
        with_text = False
        
        def avance(m, dt):
            m.rotate(- w * dt, about_point=m[0].get_center()).shift(v * dt * RIGHT)
        
        def build_objects(h, r):
            ligne = Line(7*LEFT, 7*RIGHT)
            roue = Circle(radius=r, stroke_color=RED).move_to ([-7 +r, r, 0])
            rayon = Line(roue.get_center(), roue.get_bottom()).scale(h,about_edge=UP)
            centre = Dot(rayon.get_start(), color=BLUE)
            point = Dot(rayon.get_end(), color=YELLOW).scale(1.5)        
            roue_qui_tourne = VGroup(roue, rayon, centre, point)
            return (ligne, roue_qui_tourne)
        liste_simu, liste_R = [], []        
        for h in hauteur:
            L, R = build_objects(h, r)
            if with_text:
                text = Text("distance: "+str(h)+"x rayon").scale(0.5).next_to(R.get_top(), UR)
                simu = VGroup(text, L, R)
            else:
                simu = VGroup(L, R)
            liste_simu.append(simu)
            liste_R.append(R)
        x = Group(*liste_simu).arrange(UP, buff = 0.2)
        self.add(x)
        for R in liste_R:
            self.add(R)
            R.add_updater(avance)
        self.play(R.animate, run_time=run_time,rate_func=linear)
    
    def CycloideAvecRoue(self, r, y):
        run_time = 3
        v = (12) / run_time
        w = v / r
        def avance(m, dt):
            m.rotate(- w * dt, about_point=m[0].get_center()).shift(v * dt * RIGHT) 
        roue = Circle(radius=r, stroke_color=BLUE).move_to([-6, y+r, 0])
        rayon = DashedLine(roue.get_center(), roue.get_bottom())#.scale(h,about_edge=UP)
        centre = Dot(rayon.get_start(), color=GREEN)
        point = Dot(rayon.get_end(), color=YELLOW)        
        roue_qui_tourne = VGroup(roue, rayon, centre, point)
        self.add(roue_qui_tourne)
        self.play(Create(roue_qui_tourne.copy()))
        cycloide = TracedPath(point.get_center, stroke_width=2.5, stroke_color=GREEN)
        roue_qui_tourne.add_updater(avance)
        self.add(cycloide)
        self.play(roue_qui_tourne.animate, run_time=run_time,rate_func=linear)