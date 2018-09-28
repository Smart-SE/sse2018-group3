
import diagnosis
import radar_graph
import line_graph

anger = [100,52,33,44,55,16,47,38,39,100]
diag_list = ["",""]


print(anger)

diagnosis.check(anger[0],diag_list)
print(diag_list)

radar_graph.create_radar_graph(anger[0])
line_graph.create_line_graph(anger)

