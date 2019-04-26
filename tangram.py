#coding=utf-8

#通过minidom解析xml文件
from xml.dom.minidom import parse
import xml.dom.minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import *
import operator


def available_coloured_pieces(path):
    tree=ET.parse(path)
    collection = tree.getroot()
    dict_new = {}
    for key, valu in enumerate(collection):
        dict_new[key]=valu.attrib['d'][1:len(valu.attrib['d'])-1]
    return dict_new

def are_valid(dict_new):
    list_l=[]
    m = 0
    for key in range(len(dict_new)):
        list_l.append([[]])
        for lon in dict_new[key]:
            if lon == ' ':
                if m != 0:
                    list_l[key][len(list_l[key]) - 1].append(m)
                    m = 0
            else:
                if lon == 'L':
                    list_l[key].append([])
                else:
                    m = m * 10 + int(lon)

    for piece in list_l:
        if len(piece)<3:return False
        if len(piece)>3:
            list_center = []
            '''P×Q = x1*y2 – x2*y1'''
            for j in range(1,len(piece)):
                list_center.append([piece[j][0]-piece[j-1][0],piece[j][1]-piece[j-1][1]])
            list_center.append([piece[0][0]-piece[j][0],piece[0][1]-piece[j][1]])
            qp=list_center[0][0]*list_center[1][1]-list_center[1][0]*list_center[0][1]
            for n in range(2, len(list_center)):
                pq=list_center[n-1][0]*list_center[n][1]-list_center[n][0]*list_center[n-1][1]
                if pq*qp<0:
                    return False
                qp=pq
    return True



#斜率正负正负，正0﹣算一个吧应该
def are_identical_sets_of_coloured_pieces(pieces_1, pieces_2):
    list1=[]
    m=0
    for key in range(len(pieces_1)):
            list1.append([[]])
            for lon in pieces_1[key]:
                if lon == ' ':
                    if m != 0:
                        list1[key][len(list1[key]) - 1].append(m)
                        m = 0
                else:
                    if lon == 'L':
                        list1[key].append([])
                    else:
                        m = m * 10 + int(lon)
    list2=[]
    for key in range(len(pieces_2)):
            list2.append([[]])
            for lon in pieces_2[key]:
                if lon == ' ':
                    if m != 0:
                        list2[key][len(list2[key]) - 1].append(m)
                        m = 0
                else:
                    if lon == 'L':
                        list2[key].append([])
                    else:
                        m = m * 10 + int(lon)
    if len(list1)!=len(list2):return False
    for p1 in list1:
        findp1 = 0
        for p2 in list2:
            findpos1 = 0
            if len(p1)==len(p2):
                for p1pos in p1:
                    findpos1=0
                    for p2pos in p2:
                        if operator.eq(p1pos,p2pos):
                            findpos1=1
                            break
                    if findpos1==0:break
            if findpos1==1:findp1=1
        if findp1==0:
            return False
    return True

def is_solution(tangram, shape):
    tangs = []
    m = 0
    for key in range(len(tangram)):
        tangs.append([[]])
        for lon in tangram[key]:
            if lon == ' ':
                if m != 0:
                    tangs[key][len(tangs[key]) - 1].append(m)
                    m = 0
            else:
                if lon == 'L':
                    tangs[key].append([])
                else:
                    m = m * 10 + int(lon)

    tang_lines=[]
    for pi in tangs:
        for i in range(1,len(pi)):
            if pi[i-1][0]<pi[i][0]:
                tang_lines.append(pi[i-1]+pi[i])
            else:
                if pi[i-1][0]==pi[i][0]:
                    if pi[i-1][1]<pi[i][1]:
                        tang_lines.append(pi[i - 1] + pi[i])
                    else:tang_lines.append(pi[i]+pi[i-1])
                else:
                    tang_lines.append(pi[i]+pi[i-1])
        if pi[0][0] < pi[i][0]:
            tang_lines.append(pi[0] + pi[i])
        elif pi[0][0]==pi[i][0]:
                    if pi[0][1]<pi[i][1]:
                        tang_lines.append(pi[0] + pi[i])
                    else:tang_lines.append(pi[i]+pi[0])
        else:
            tang_lines.append(pi[i] + pi[0])
    shas = []
    for key in range(len(shape)):
        shas.append([])
        for lon in shape[key]:
            if lon == ' ':
                if m != 0:
                    shas[len(shas) - 1].append(m)
                    m = 0
            else:
                if lon == 'L'or lon==[]:
                    shas.append([])
                else:
                    m = m * 10 + int(lon)

    shape_lines=[]

    for i in range(1,len(shas)):
            if shas[i-1][0]<shas[i][0]:
                shape_lines.append(shas[i-1]+shas[i])
            else:
                if shas[i-1][0]==shas[i][0]:
                    if shas[i-1][1]<shas[i][1]:
                        shape_lines.append(shas[i - 1] + shas[i])
                    else:shape_lines.append(shas[i]+shas[i-1])
                else:
                    shape_lines.append(shas[i]+shas[i-1])
    if shas[0][0] < shas[i][0]:
                shape_lines.append(shas[0] + shas[i])
    elif shas[0][0] == shas[i][0]:
                if shas[0][1] < shas[i][1]:
                    shape_lines.append(shas[0] + shas[i])
                else:
                    shape_lines.append(shas[i] + shas[0])
    else:
                shape_lines.append(shas[i] + shas[0])


    i=0
    while i<len(tang_lines)-1:
        '''while改一下'''
        j=0
        while (i+j+1)<len(tang_lines):
            lines =tang_lines[i+j+1]
            if operator.eq(tang_lines[i][:2],lines[2:]) :
                if (tang_lines[i][3] - tang_lines[i][1]) * (lines[2] - lines[0]) == (tang_lines[i][2] - tang_lines[i][0]) * (lines[3] - lines[1]):  # 斜率等
                    tang_lines[i] = lines[:2] + tang_lines[i][2:]
                    tang_lines.pop(i + 1+j)
                    j -= 1
                    i-=1
                    break
                if lines[2] - lines[0]==0 and tang_lines[i][2]-tang_lines[i][0]==0:
                    print("@@@@@@@@@@@@@")
                    tang_lines[i] = lines[:2] + tang_lines[i][2:]
                    tang_lines.pop(i + 1 + j)
                    j -= 1
                    i -= 1
                    break
            if operator.eq(tang_lines[i][2:],lines[:2]):
                if (tang_lines[i][3] - tang_lines[i][1]) * (lines[2] - lines[0]) == (tang_lines[i][2] - tang_lines[i][0]) * (lines[3] - lines[1]):  # 斜率等
                    tang_lines[i] = tang_lines[i][:2] + lines[2:]
                    tang_lines.pop(i + 1+j)
                    j -= 1
                    i-=1
                    break
                if lines[2] - lines[0]==0 and tang_lines[i][2]-tang_lines[i][0]==0:
                    print("@@@@@@@@@@@@@")
                    tang_lines[i] = lines[:2] + tang_lines[i][2:]
                    tang_lines.pop(i + 1 + j)
                    j -= 1
                    i -= 1
                    break
            j+=1
        i+=1
    '''首尾相接'''
    i=0
    while i< len(tang_lines)-1:
        j=0
        while (i+j+1)<len(tang_lines):
            lines=tang_lines[i+j+1]
            if operator.eq(tang_lines[i][:2],lines[:2]):#起点相同
                if operator.eq(tang_lines[i],lines):#相同
                    tang_lines.pop(i)
                    tang_lines.pop(i+j)
                    j=0
                    #break
                else:
                  if ((tang_lines[i][3]-tang_lines[i][1])*(lines[2]-lines[0]))==((tang_lines[i][2]-tang_lines[i][0])*(lines[3]-lines[1])):#斜率等

                    if tang_lines[i][3]<lines[3]:
                        tang_lines[i]=tang_lines[i][2:]+lines[2:]
                    else:tang_lines[i]=lines[2:]+tang_lines[i][2:]
                    tang_lines.pop(i +1+j)
                    j -= 1
                    i-=1
                    print("@@@@@@@@@@@")
                    break
            elif operator.eq(tang_lines[i][2:],lines[2:]):
                    if (tang_lines[i][3]-tang_lines[i][1])*(lines[2]-lines[0])==(tang_lines[i][2]-tang_lines[i][0])*(lines[3]-lines[1]):#斜率等
                        if tang_lines[i][0] < lines[0]:
                            tang_lines[i] = tang_lines[i][:2] + lines[:2]
                        else:
                            tang_lines[i] = lines[:2] + tang_lines[i][:2]
                        tang_lines.pop(i +1+ j)
                        j -= 1
                        i-=1
                        print("~~~~~")
                        break
            j+=1
        i+=1

    if len(tang_lines)!=len(shape_lines):
        return False
    else:
        for ls in shape_lines:
            find=0
            for pi in tang_lines:
                if operator.eq(ls,pi):
                    find=1
                    break
            if find==0:return False
    return True











