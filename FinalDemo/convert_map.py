import ast
import json

from SLAM_eval import parse_user_map


aruco_markers = str('lab_output/slam.txt')
fruits = open('lab_output/targets.txt', 'r')
fruits = ast.literal_eval(fruits.read())
aruco_markers = parse_user_map(aruco_markers)

EstimateMap = {}
inversion, reflection = input("Inversion [Y/N], reflection [Y/N]: ").split(", ",2)
if inversion == 'N' or inversion == 'n' and reflection == 'N' or reflection == 'n':
    for i in range(1,11):
        EstimateMap[f"aruco{i}_0"] = {"y": float(aruco_markers[i][0]), "x": float(-aruco_markers[i][1])}
elif inversion == 'Y' or inversion == 'y' and reflection == 'N' or reflection == 'n':
    for i in range(1,11):
        EstimateMap[f"aruco{i}_0"] = {"y": float(aruco_markers[i][1]), "x": float(aruco_markers[i][0])}
elif inversion == 'N' or inversion == 'n' and reflection == 'Y' or reflection == 'y':
    for i in range(1,11):
        EstimateMap[f"aruco{i}_0"] = {"y": float(-aruco_markers[i][0]), "x": float(-aruco_markers[i][1])}
elif inversion == 'Y' or inversion == 'y' and reflection == 'Y' or reflection == 'y':
    for i in range(1,11):
        EstimateMap[f"aruco{i}_0"] = {"y": float(-aruco_markers[i][1]), "x": float(-aruco_markers[i][0])}


EstimateMap.update(fruits)
print(EstimateMap)

with open('EstimateMap.txt', 'w') as f:
    json.dump(EstimateMap, f)