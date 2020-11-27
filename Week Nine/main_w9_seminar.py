import random as rand
import copy
# WEEK 9 - SEMINAR 4

# ---- Problem 1: Voronoi Diagrams ----

def generate_voronoi(width:int, height:int, seeds:list)->list:
    rand.seed(50)
    result = [[-1 for i in range(width)] for i in range(height)]
    seed_count = len(seeds)
    colors = [rand.randint(0x0F0F0F, 0xFFFFFF) for i in range(seed_count)]
    # place seeds
    for i in range(len(seeds)):
        seed = seeds[i]
        result[seed[1]][seed[0]] = colors[i]  

    flag = True
    m=0
    while(flag):
        flag = False
        next_result = copy.deepcopy(result)
        for x in range(width):
            for y in range(height):
                if not flag and result[y][x] == -1:
                    flag = True
                    print(f"{m}: found -1 at {x}x{y}")
                else:
                    col = result[y][x]
                    if y-1 >= 0 and next_result[y-1][x]==-1: next_result[y-1][x] = col
                    if y+1 < height and next_result[y+1][x] == -1: next_result[y+1][x] = col
                    if x-1 >= 0 and next_result[y][x-1]==-1: next_result[y][x-1] = col
                    if x+1 < width and next_result[y][x+1]==-1: next_result[y][x+1] = col
        result = next_result
        #if(m%2==0): save_to_file(result, f"temp/diagram_{m//2}")
        m+=1
    # re-add points
    for i in range(len(seeds)):
        seed = seeds[i]
        result[seed[1]][seed[0]] = 0
    
    return result

def distance(x1,y1,x2,y2):
    return ((y2-y1)**2 + (x2-x1)**2)**0.5

def generate_voronoi_alt(width:int, height:int, seeds:list)->list:
    rand.seed(50)
    result = [[-1 for i in range(width)] for i in range(height)]
    seed_count = len(seeds)
    colors = [rand.randint(0x0F0F0F, 0xFFFFFF) for i in range(seed_count)]
    for x in range(width):
        for y in range(height):
            dist = 999999999
            closest = -1
            for i in range(seed_count):
                new_dist = distance(x,y,seeds[i][0],seeds[i][1])
                if new_dist < dist:
                    dist = new_dist
                    closest = i
            result[y][x] = colors[closest]
    for i in range(len(seeds)):
        seed = seeds[i]
        result[seed[1]][seed[0]] = 0
    return result



def save_to_file(img:list, name:str):
    height = len(img)
    width = len(img[0])
    f = open(f"{name}.ppm", "w")
    f.write(f"P3 {width} {height} 255\n")
    for row in img:
        for cell in row:
            r,g,b = col_to_rgb(cell)
            f.write(f" {r} {g} {b} ")
        f.write("\n")
    f.close()

def col_to_rgb(color:int):
    red = (color >> 16) & 0xFF
    green = (color >> 8) & 0xFF
    blue = color & 0xFF
    return red,green,blue

#result = [[-1 for i in range(128)] for i in range(128)]
#for i in range(len(result)):
#        for j in range(len(result[i])):
#            result[i][j] = rand.randint(0,0xFFFFFF)
#save_to_file(result, "test")

def random_points(point_count: int, width:int, height:int) -> list:
    result = []
    for i in range(point_count):
        result.append( (rand.randint(0,width-1), rand.randint(0,height-1)) )
    return result

width = 128
height = 300
points = random_points(10,width,height)
img = generate_voronoi(width,height,points)#[(10,10),(32,5),(5,50),(50,50)]
save_to_file(img, "diagram")
img = generate_voronoi_alt(width,height,points)
save_to_file(img, "diagram_iter")