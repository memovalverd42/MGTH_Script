from sympy import Matrix, Symbol, sin, cos, pi

def get_general_matrix(a_i1=0, alpha_i1=0, di=0, thetai=0):
    a = Symbol(a_i1) if isinstance(a_i1, str) else a_i1
    alpha = Symbol(alpha_i1) if isinstance(alpha_i1, str) else alpha_i1
    d = Symbol(di) if isinstance(di, str) else di
    t = Symbol(thetai) if isinstance(thetai, str) else thetai

    matrix_T = Matrix([
        [cos(t), -sin(t), 0, a], 
        [sin(t)*cos(alpha), cos(t)*cos(alpha), -sin(alpha), -d*sin(alpha)],
        [sin(t)*sin(alpha), cos(t)*sin(alpha), cos(alpha), d*cos(alpha)],
        [0, 0, 0, 1]
    ])

    return matrix_T

def show_matrix_4x4(matriz, name = None):
    if name != None: print(f"\n********** Matriz {name} *************")
    # print('\n')
    print(matriz[0:4])
    print(matriz[4:8])
    print(matriz[8:12])
    print(matriz[12:16], '\n')