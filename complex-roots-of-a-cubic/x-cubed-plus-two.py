from manim import *
from numpy import pi

class ComplexPlaneExample(Scene):
    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_color": GRAY}, x_range=(-10, 10, 0.1), y_range=(-10, 10, 0.1)) # .add_coordinates()

        output = ComplexPlane(x_range=(-10, 10, 0.1), y_range=(-10, 10, 0.1))

        self.add(plane)
        
        self.add()
        
        self.play(output.animate.apply_complex_function(lambda z:z**3 + 2), run_time=5)
        self.wait(2)