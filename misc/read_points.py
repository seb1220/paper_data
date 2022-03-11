from datetime import datetime, date
import pickle

with open('points.pkl', 'rb') as f:
    points_list = pickle.load(f)


print(points_list)

formatted_list = []

for i in points_list:
    if 0 <= i[0] <= 151:
        formatted_list.append((round(i[0], 2), round(i[1], 2), round(i[2], 2) if i[2] <= 180 else round((i[2] - 360), 2)))

with open("pid_comp.txt", "a") as writter:
    #print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    text = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "\n"
    writter.write(text)
    writter.write(str(formatted_list))
    dx = round(formatted_list[-1][0] - formatted_list[0][0], 2)
    dy = round(formatted_list[-1][1] - formatted_list[0][1], 2)
    da = round(formatted_list[-1][2] - formatted_list[0][2], 2)
    writter.write("\n")
    writter.write("Diff: x: " + str(dx) + " y: " + str(dy) + " angle: " + str(da))
    writter.write("\n")
    writter.close()

print(formatted_list)
