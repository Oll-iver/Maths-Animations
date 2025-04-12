from manim import *



class ElementaryMatrix(Scene):
    def construct(self):
        # Create Matrix A = 4 3; 6 3 with label "A = " centered at top of screen
        matrix_A_label = MathTex("A = ")
        matrix_A = Matrix(
            [[4, 3], [6, 3]],
            left_bracket="[",
            right_bracket="]",
            element_alignment_corner=ORIGIN
        )
        matrix_A_group = VGroup(matrix_A_label, matrix_A).arrange(RIGHT)
        matrix_A_group.to_edge(UP)
        self.play(Write(matrix_A_group))
        self.wait(1)

        # Create Matrix E = 1 0; -1.5 1 that converts A into REF, with label "E = " below the matrix A.
        matrix_E_label = MathTex("E = ")
        matrix_E = Matrix(
            [[1, 0], [-1.5, 1]],
            left_bracket="[",
            right_bracket="]",
            element_alignment_corner=ORIGIN
        )
        matrix_E_group = VGroup(matrix_E_label, matrix_E).arrange(RIGHT)
        matrix_E_group.next_to(matrix_A_group, DOWN, buff=0.5)
        self.play(Write(matrix_E_group))
        self.wait(2)

        # Text below the matrix E stating that E is being applied to A
        multiplication_text = Text("Applying E to A:")
        multiplication_text.scale(0.5)
        multiplication_text.next_to(matrix_E_group, DOWN, buff=0.5)
        self.play(Write(multiplication_text))

        # Matrix result_matrix equal to E*A with label "E cdot A"
        result_matrix_label = MathTex("E \\cdot A = ")
        result_matrix = Matrix(
            [[4, 3], [0, -1.5]],
            left_bracket="[",
            right_bracket="]",
            element_alignment_corner=ORIGIN
        )
        result_matrix_group = VGroup(result_matrix_label, result_matrix).arrange(RIGHT)
        result_matrix_group.next_to(multiplication_text, DOWN, buff=0.3)
        self.play(Write(result_matrix_group))
        self.wait(2)

        # Text explanation for row 1 of EA
        operation_text_row1 = Text("Row 1 of EA equals 1 times row 1 of A plus 0 times row 2 of A.")
        operation_text_row1.scale(0.4)
        operation_text_row1.wrap_width = 6
        operation_text_row1.next_to(result_matrix_group, DOWN, buff=0.3)
        self.play(Write(operation_text_row1))

        # Duplicate `1` and `0` from E and move them to the right of corresponding rows in A
        one_from_E = matrix_E.get_rows()[0][0].copy()  # Duplicate "1" from E
        zero_from_E = matrix_E.get_rows()[0][1].copy()  # Duplicate "0" from E
        plus_sign = MathTex("+")  # Plus sign

        # Create coloured rectangles around relevant rows of A, E, EA
        rect_E_row1 = SurroundingRectangle(matrix_E.get_rows()[0], color = YELLOW, buff = 0.1)
        rect_A_row1 = SurroundingRectangle(matrix_A.get_rows()[0], color = BLUE, buff = 0.1)
        rect_result_matrix = SurroundingRectangle(result_matrix.get_rows()[0], color = RED, buff = 0.1)


        # Position plus sign between the two previously copied values and animate them into place
        self.play(
            one_from_E.animate.move_to(matrix_A.get_rows()[0].get_left() + RIGHT * 2.5),
            zero_from_E.animate.move_to(matrix_A.get_rows()[1].get_left() + RIGHT * 2.5),
            Create(rect_E_row1), Create(rect_A_row1), Create(rect_result_matrix)
        )
        
        # Place plus sign between the two values
        plus_sign.next_to(one_from_E, DOWN, buff=0.1)

        # Show the complete equation for row 1 calculation
        self.play(Write(plus_sign))
        self.wait(2)

        # Clean up after explanation
        self.play(FadeOut(one_from_E), FadeOut(zero_from_E), FadeOut(plus_sign), FadeOut(operation_text_row1),
        FadeOut(rect_result_matrix),FadeOut(rect_A_row1),FadeOut(rect_E_row1))

        # Explanation for row 2, in an almost identical style to row 1.
        operation_text_row2 = Text("Row 2 of EA equals -1.5 times row 1 of A plus 1 times row 2 of A.")
        operation_text_row2.scale(0.4)
        operation_text_row2.wrap_width = 6
        operation_text_row2.next_to(result_matrix_group, DOWN, buff=0.3)

        # Display row 2 explanation
        self.play(Write(operation_text_row2))
        self.wait(2)


        # Duplicate `-1.5` and `1` from E and move them to the right of corresponding rows in A
        onetwo_from_E = matrix_E.get_rows()[1][0].copy()  
        twotwo = matrix_E.get_rows()[1][1].copy()  
        plus_sign = MathTex("+")  

        #Create rectangles around relevant rows of E, A, EA; one more than last time. After writing the code I realise some of this is repeated and redundant, but I am tired.
        rect_E_row2 = SurroundingRectangle(matrix_E.get_rows()[1], color = YELLOW, buff = 0.1)
        rect_A_row2 = SurroundingRectangle(matrix_A.get_rows()[1],color = BLUE, buff = 0.1)
        rect_A_row1 = SurroundingRectangle(matrix_A.get_rows()[0], color = BLUE, buff = 0.1)
        rect_result_matrix2= SurroundingRectangle(result_matrix.get_rows()[1], color = RED, buff = 0.1)


        # Animate the two values from E into place next to A
        self.play(
            onetwo_from_E.animate.move_to(matrix_A.get_rows()[0].get_left() + RIGHT * 2.5),
            twotwo.animate.move_to(matrix_A.get_rows()[1].get_left() + RIGHT * 2.5),
            Create(rect_E_row2), Create(rect_A_row2), Create(rect_result_matrix2), Create(rect_A_row1)
        )
        
        # Place plus sign between the two values
        plus_sign.next_to(onetwo_from_E, DOWN, buff=0.1)

        # Show the complete equation for row 2 calculation
        self.play(Write(plus_sign))
        self.wait(2)

        # Clean up after explanation
        self.play(FadeOut(onetwo_from_E), FadeOut(twotwo), FadeOut(plus_sign), FadeOut(operation_text_row2),
        FadeOut(rect_result_matrix2),FadeOut(rect_A_row2),FadeOut(rect_E_row2), FadeOut(rect_A_row1))


        # Fade out all elements to end the scene
        self.play(FadeOut(matrix_A_group), FadeOut(matrix_E_group), FadeOut(multiplication_text), 
                  FadeOut(result_matrix_group))
        self.wait(1)
