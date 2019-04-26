from tangram import *
path= open("pieces_A.xml")
dict_pieces=available_coloured_pieces(path)
dict_pieces2=available_coloured_pieces("pieces_AA.xml")
shape_A1=available_coloured_pieces("shape_A_1.xml")
shape_A2=available_coloured_pieces("shape_A_2.xml")
tangramA1=available_coloured_pieces("tangram_A_1_a.xml")
tangramA1b=available_coloured_pieces("tangram_A_1_b.xml")
tangramA2=available_coloured_pieces("tangram_A_2_a.xml")
print(are_valid(dict_pieces))
print(are_valid(shape_A1))
print(are_valid(shape_A2))

print("++++++++++++++++++")

print(is_solution(tangramA1,shape_A1))
print(is_solution(tangramA2,shape_A1))
print(is_solution(tangramA2,shape_A2))
print(is_solution(tangramA1b,shape_A1))
