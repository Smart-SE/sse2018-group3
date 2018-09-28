
import diagnosis
import radar_graph
import line_graph

import json

jfile = open("sensor.json","r")
sensor = json.load(jfile)

print(sensor)

anger_hist = sensor["hist"]
anger_data = sensor["data"]
diag_list = ["",""]



diagnosis.check(anger_data,diag_list)
print(diag_list)

radar_graph.create_radar_graph(anger_data)
line_graph.create_line_graph(anger_hist)

