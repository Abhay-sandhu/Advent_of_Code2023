from pprint import pprint
with open('Day5_If You Give A Seed A Fertilizer\\input.txt', 'r') as file:
    almanac = file.readlines()

seed_soil_map = {}
soil_fertilizer_map = {}
fertilizer_water_map = {}
water_light_map = {}
light_temp_map = {}
temp_humidity_map = {}
humidity_location_map = {}

Maps = [seed_soil_map, soil_fertilizer_map, fertilizer_water_map, water_light_map, light_temp_map, temp_humidity_map, humidity_location_map]

seeds = [int(seed) for seed in almanac[0].split(':')[1].strip().split()]
seed_pairs = [(seeds[x], seeds[x + 1]) for x in range(len(seeds)-1)]
seed_list = []
for i in range(len(seed_pairs)):
    seed_list.append((seed_pairs[i][0], seed_pairs[i][0] + seed_pairs[i][1]))

start = 3

for idx,map in enumerate(Maps):
    for i in range(start,len(almanac)):
        line = [int(x) for x in almanac[i].strip().split()] # line = [destination start, source start, range]
        if line == []:
            start = i+2
            break
        if idx == 0:
            for x in seed_list:
                inter = (0,0)
                if not (x[0] > line[1]+ line[2] or x[1] < line[1]):
                    inter = (max(x[0], line[1]), min(x[1], line[1] + line[2]))
                    map[inter] = (line[0]+inter[0]-line[1], line[0]+inter[1]-line[1])
        else:
            for x in Maps[idx-1]:
                inter = (0,0)
                if not (Maps[idx-1][x][0] > line[1]+ line[2] or Maps[idx-1][x][1] < line[1]):
                    inter = (max(Maps[idx-1][x][0], line[1]), min(Maps[idx-1][x][1], line[1] + line[2]))
                    map[inter] = (line[0]+inter[0]-line[1], line[0]+inter[1]-line[1])
               
    if idx == 0:
        for x in seed_list:
            xc = (0,0)
            #xc1 = (0,0)
            #xc2 = (0,0)
            for y in map:
                inter = (0,0)
                if not ((y[1] < x[0]) or y[0] > x[1]):
                    inter = (max(x[0], y[0]), min(x[1], y[1]))
                
                #if((x[0] < inter[0]) and (x[1] > inter[1])):
                #    xc1 = (x[0], inter[0])
                #    xc2 = (inter[1], x[1])
                if((x[0] == inter[0]) and (x[1] == inter[1])):
                    xc = (0,0)
                elif (x[0] == inter[0]):
                    xc = (inter[1], x[1])
                elif (x[1] == inter[1]):
                    xc = (x[0], inter[0])
                x = xc
                if x == (0,0):
                    break
            map[x] = x
                
                
    else:
        for x in Maps[idx-1]:
            z = Maps[idx-1][x]
            xc = (0,0)
            #xc1 = (0,0)
            #xc2 = (0,0)
            for y in map:
                inter = (0,0)
                if not ((y[1] < z[0]) or y[0] > z[1]):
                    inter = (max(z[0], y[0]), min(z[1], y[1]))
                
                #if((x[0] < inter[0]) and (x[1] > inter[1])):
                #    xc1 = (x[0], inter[0])
                #    xc2 = (inter[1], x[1])
                if((z[0] == inter[0]) and (z[1] == inter[1])):
                    xc = (0,0)
                elif (z[0] == inter[0]):
                    xc = (inter[1], z[1])
                elif (z[1] == inter[1]):
                    xc = (z[0], inter[0])
                z = xc
                if z == (0,0):
                    break
            map[z] = z

locations = []
for x in humidity_location_map.values():
    if x[0] > 0:
        locations.append(x[0])
pprint(min(locations))