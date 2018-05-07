import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    amb=calculate_ambient(ambient,areflect)
    dif= calculate_diffuse(light,dreflect,normal)
    spec=calculate_specular(light,sreflect,view,normal)
    color=[]
    for i in range(0,3):
        color.append(amb[i]+diff[i]+spec[i])
    print color
    return limit_color(color)

def calculate_ambient(alight, areflect):
    amb=[]
    for i in range(0,3):
        amb.append(alight[i]*areflect[i])
    return limit_color(amb)

def calculate_diffuse(light, dreflect, normal):
    diff=[]
    for i in range(0,3):
        diff.append(light[COLOR][i]*dreflect[i]*dot_product(normalize(normal),normalize(light[LOCATION])))
        return limit_color(diff)

def calculate_specular(light, sreflect, view, normal):
    normal=normalize(normal)
    light_location=normalize(light[LOCATION])
    view = normalize(view)

    if(dot_product(normal,light_location)<=0):
        return[0,0,0]
    else:
        s=[]
        r=[]
        ndl=2*dot_product(normal,light_location)
        for i in range(0,3):
            r.append(ndl*normal[i]-light_location[i])
        cosa=dot_product(r,view)
        for i in range (0,3):
            s.append(light[COLOR][i]*sreflect[i]*(cosa** SPECULAR_EXP))
        return limit_color(s)

def limit_color(color):
    for i in range (0,3):
        rgb=color[i]
        rgb=int(rgb)
        if(rgb<0):
            rgb=0
        elif (rgb>255):
            rgb=255
        color[i]=rgb
    return color

#vector functions
def normalize(vector):
    bot=((vector[0]**2)+(vector[1]**2)+(vector[2]**2))**0.5
    for i in range(0,3):
        vector[i]=vector[i]/bot
    return vector


def dot_product(a, b):
    output=0
    for i in range(0,3):
        output+=a[i]*b[i]
    return output

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
