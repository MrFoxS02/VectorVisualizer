import math

class vector_2D_transform:
    
    def add(self, *vectors):
        return [(sum([v[i] for v in vectors])) for i in range(len(vectors[0]))]
    
    def lenght(self, v:list)->float:
        return math.sqrt(v[0] ** 2 + v[1] ** 2)
    
    def multiplication(self, v:list, scalar=1)->list:
        return [v[i] * scalar for i in range(len(v))]
    
    def translate(self, translation, vectors):
        try:
            return [self.add(translation, v) for v in vectors]
        except:
            if len(translation) != len(vectors[0]):
                print('IndexError: нессответствующие размерности векторов')
            else:
                print('Err')
                
    def substract(self, v1:list, v2:list)->list:
        return (v1[0] - v2[0], v1[1] - v2[1])
    
    def distance(self, v1:list, v2:list)->float:
        return self.lenght(self.substract(v1, v2))
    
    def perimetr(self, vectors:list)->float:
        distances = [self.distance(vectors[i], vectors[(i+1)%len(vectors)])
                            for i in range(len(vectors))]
        return sum(distances)
    
    def to_polar(self, decart_vector:list)->list:
        return(self.lenght(decart_vector), math.atan2(decart_vector[1], decart_vector[0]))
    
    def to_cartesian(self, polar_vector:list)->list:
        length, angle = polar_vector[0], polar_vector[1]
        return (length*math.cos(angle), length*math.sin(angle))
    
    def rotate(self, vector:list, rot_ang:float = math.pi / 4)->list:
        polar_vector = [(math.sqrt(x ** 2 + y ** 2), math.atan2(y, x)) for x, y in vector]
        polar_rotate_vector = [(l, (ang + rot_ang)) for l, ang in polar_vector]
        dec_rotate_vector = [(l * math.cos(ang), l * math.sin(ang)) for l, ang in polar_rotate_vector]
        return dec_rotate_vector
    
    def get_regular_polygon(self, n:int, r:int = 1) -> list:
        return [self.to_cartesian((r, 2*math.pi*k/n)) for k in range(0,n)]