from MGTH import *

# Generacion de las matrices generales de transformacion homogenea
T0_1 = get_general_matrix(thetai='t1')
T1_2 = get_general_matrix(a_i1='L2', thetai='t2')
T2_3 = get_general_matrix(a_i1='L3', alpha_i1=pi, di='d3')
T3_e = get_general_matrix(di='Le')

show_matrix_4x4(T0_1, 'T0_1')
show_matrix_4x4(T1_2, 'T1_2')
show_matrix_4x4(T2_3, 'T2_3')
show_matrix_4x4(T3_e, 'T3_e')

T0_e = T0_1*T1_2*T2_3*T3_e
T0_e_subs = T0_e.subs({'t1': 0, 't2': 0, 'd3': 0}) 
show_matrix_4x4(T0_e_subs, 'T0_e')