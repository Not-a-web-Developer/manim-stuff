from manim import *
from numpy import pi

class ComplexPlaneExample(Scene):
    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_color": GRAY}).add_coordinates()

        output = ComplexPlane()

        self.add(plane)
        
        self.add()
        
        self.play(output.animate.apply_complex_function(lambda z:z**2 + 1), run_time=5)
        self.wait(2)

class ComplexFunctionRealLine(Scene):
    def construct(self):
        plane = ComplexPlane().add_coordinates()

        output = NumberLine(rotation=pi/2)

        self.add(plane)
        
        self.add()
        
        self.play(output.animate.apply_complex_function(lambda z:z**2 + 1), run_time=5)
        self.wait(2)