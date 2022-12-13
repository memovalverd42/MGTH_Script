from MGTH import *

# Generacion de las matrices generales de transformacion homogenea
T0_1 = get_general_matrix(thetai='t1')
T1_2 = get_general_matrix(alpha_i1=pi/2, di='L1', thetai='t2+90')
T2_3 = get_general_matrix(a_i1='L2', di='L3', thetai='t3')
T3_e = get_general_matrix(a_i1='Le')

# Sustitucion de valores iniciales en 0
T0_1_subs = T0_1.subs('t1', 0)
T1_2_subs = T1_2.subs('t2+90', pi/2)
T2_3_subs = T2_3.subs('t3', 0)
T3_e_subs = T3_e

# Mostrar matrices:
show_matrix_4x4(T0_1, 'T0_1 Sustituida')
show_matrix_4x4(T1_2, 'T1_2 Sustituida')
show_matrix_4x4(T2_3, 'T2_3 Sustituida')
show_matrix_4x4(T3_e, 'T3_e Sustituida')

# show_matrix_4x4(T0_1_subs, 'T0_1 Sustituida')
# show_matrix_4x4(T1_2_subs, 'T1_2 Sustituida')
# show_matrix_4x4(T2_3_subs, 'T2_3 Sustituida')
# show_matrix_4x4(T3_e_subs, 'T3_e Sustituida')

# Multiplicacion para obtener la matriz de e con respecto a 0

# Opcion simbolica
T0_e = T0_1*T1_2*T2_3*T3_e
# show_matrix_4x4(T0_e, 'T0_e Simbolica')

# Opcion sustituida
T0_e_subs = T0_e.subs({'t1': 0, 't2+90': pi/2, 't3': 0}) 
# show_matrix_4x4(T0_e_subs, 'T0_e Sustituida')           





