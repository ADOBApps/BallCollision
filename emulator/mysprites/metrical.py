"""
# Author: Acxel Orozco
# Date: 15/09/2022
"""


class Metrical:

    def __init__(self):
        class_name = self.__class__.__name__
        print(class_name, "Started")
        print("Analytical class for Collision")
        print()

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "Destroyed")

    def elastic_collision(
        self,
        obj_1: dict,
        obj_2: dict
    ) -> dict:
        """
        Perfect elastic collision suppose one object quiet
        """
        print(f"propiedades obj1: {obj_1}")
        print(f"propiedades obj2: {obj_2}")
        s1 = obj_1['speed_i']
        s2 = obj_2['speed_i']
        m1 = obj_1['mass']
        m2 = obj_2['mass']
        if obj_2['quiet']:
            if m1 == m2:
                v1_x = 0.0
                v1_y = 0.0
            else:
                v1_x = ((m1 - m2) * s1[0]) / (m1 + m2)
                v1_y = ((m1 - m2) * s1[1]) / (m1 + m2)
            v2_x = (2 * m1 * s1[0]) / (m1 + m2)
            v2_y = (2 * m1 * s1[1]) / (m1 + m2)
        if obj_1['quiet']:
            if m1 == m2:
                v2_x = 0.0
                v2_y = 0.0
            else:
                v2_x = ((m1 - m2) * s2[0]) / (m1 + m2)
                v2_y = ((m1 - m2) * s2[1]) / (m1 + m2)
            v1_x = (2 * m1 * s2[0]) / (m1 + m2)
            v1_y = (2 * m1 * s2[1]) / (m1 + m2)
        return {'v1': [v1_x, v1_y], 'v2': [v2_x, v2_y]}
