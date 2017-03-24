import sys
import os
import math

# The entire encoding is based
# on Godel's numberings:
#
#                       | <<x, y>> = 2^x (2y + 1)    
# forall x, y natural = |
#                       | <x, y> = 2^x (2y + 1) - 1
#
###################################################

#  Decode prog(e) as list:
#    
#         | [] = 0
#  list = | 
#         | (x : rest) = <<x, rest>>
#    
def decode_list(program):
    if program == 0:
        return []
    
    body_x = 0
    while (program % 2 == 0):
        program = program / 2
        body_x = body_x + 1
    
    rest = (program - 1) / 2
    
    prog_list = []
    prog_list.append(body_x)
    return prog_list + decode_list(rest)

#  Decode body(x):
#              
#            | [Ri+ -> Lj] = <<2i, j>>
#  body(x) = | [Ri- -> Lj, Lk] = <<2i + 1,<j, k>>>
#            | [HALT] = 0
#            
def decode_body(ind, body_x):
    if body_x == 0:
        body_enc = 'L' + str(ind) + ': HALT'
        return body_enc 
    y = 0
    while (body_x % 2 == 0):
        body_x = body_x / 2
        y = y + 1
    
    z = (body_x - 1) / 2
    if (y % 2 == 0):
        body_enc = 'L' + str(ind) + ': R' + str(y / 2) + '+ => L' + str(z)
        return body_enc 
    else:
        i = (y - 1) / 2
        z = z + 1

        j = 0
        while (z % 2 == 0):
            z = z / 2
            j = j + 1

        k = (z - 1) / 2
        body_enc = 'L' + str(ind) + ': R' + str(i) 
        body_enc = body_enc + '- => L' + str(j) + ', L' + str(k)
        return body_enc


list_ = decode_list(int (sys.argv[1]))
for i in range(len(list_)):
    print decode_body(i, list_[i])

