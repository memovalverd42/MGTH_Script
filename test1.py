from MGTH import *

# Generacion de las matrices generales de transformacion homogenea
T0_1 = get_general_matrix(thetai='t1')
T1_e = get_general_matrix(a_i1='Le')

show_matrix_4x4(T0_1, 'T0_1')
show_matrix_4x4(T1_e, 'T1_e')

T0_e = T0_1*T1_e
show_matrix_4x4(T0_e, 'T0_e')

T0_e_subs = T0_e.subs('t1', 0)
show_matrix_4x4(T0_e_subs, 'T0_e Sustituida')

