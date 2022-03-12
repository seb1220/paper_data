with open('basic.txt', 'r') as f:
    text = f.read()

lines = text.split("\n")

all_pos = []
max_size = 0
j = 1
for i in lines:
    j += 1
    if j % 3 == 0:
        ccool_points1337 = []
        points = i.replace("[(", "").replace(")]", "").split(("), ("))
        og_coord = [float(item) for item in points[0].split(", ")]
        old_coord = [float(item) for item in points[0].split(", ")]
        old_coord[0] = old_coord[0] - og_coord[0]
        old_coord[1] = old_coord[1] - og_coord[1]
        old_coord[2] = old_coord[2] - og_coord[2]
        ccool_points1337.append(old_coord)
        for k in range(len(points)):
            coord = [float(item) for item in points[k].split(", ")]
            coord[0] = coord[0] - og_coord[0]
            coord[1] = coord[1] - og_coord[1]
            coord[2] = coord[2] - og_coord[2]
            if (float(coord[0]) - float(old_coord[0])) > 0.8:
                ccool_points1337.append(coord)
                old_coord = coord
                """
        with open("basic_per_cm.txt", "a") as writer:
            for k in ccool_points1337:
                text = "(" + str(round(k[0], 2)) + ", " + str(round(k[1], 2)) + ")"
                writer.write(text + "\n")
            writer.write("\n")
        """
        all_pos.append(ccool_points1337)
        #print(len(ccool_points1337))
        max_size = max(max_size, len(ccool_points1337))

# erst ab hier
# abs

seg1 = []

for i in range(max_size):
    seg1.append([])

for i in range(len(all_pos)):
    if len(all_pos[i]) < max_size:
        for j in range(max_size - len(all_pos[i])):
            all_pos[i].append(all_pos[i][-1])

for i in range(max_size):
    #seg1[i].append([])
    for j in range(len(all_pos)):
        # for k in range(len(all_pos[i][j])):
        seg1[i].append(all_pos[j][i])

result = []
for i in range(max_size):
    xlist = []
    ylist = []
    alist = []
    for j in range(len(seg1[i])):
        xlist.append(seg1[i][j][0])
        ylist.append(abs(seg1[i][j][1]))
        alist.append(abs(seg1[i][j][2]))
    result.append((round(sum(xlist) / len(xlist), 2), round(sum(ylist) / len(ylist), 2), round(sum(alist) / len(alist), 2)))

print(result)

# das musst du verändern für die krassere Ausgabe

with open("basic_per_cm_y.txt", "a") as writer:
    for k in result:
        text = "(" + str(round(k[0], 2)) + ", " + str(round(k[1], 2)) + ")"
        writer.write(text + "\n")
    writer.write("\n")

arr = {1, 2, 3, 4, 5, 6}
print(sum(arr) / len(arr))
#print(all_pos)
#print(max_size)

