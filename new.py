import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics 
import pandas as pd

df = pd.read_csv("data.csv")
data = df["reading score"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
deviation = statistics.stdev(data)

print("mean : " + str(mean))
print("median : " + str(median))
print("mode : " + str(mode))
print("standard deviation : " + str(deviation))

first_sd_start,first_sd_end = mean-deviation, mean+deviation
second_sd_start, second_sd_end = mean-(2*deviation), mean+(2*deviation)
third_sd_start, third_sd_end = mean-(3*deviation), mean+(3*deviation)

length_of_first_sd = [data for data in data if data > first_sd_start and data < first_sd_end ]
length_of_second_sd = [data for data in data if data > second_sd_start and data < second_sd_end ]
length_of_third_sd = [data for data in data if data > third_sd_start and data < third_sd_end ]

print("{}%  of data within first sd".format(len(length_of_first_sd)*100.0/len(data)))
print("{}%  of data within second sd".format(len(length_of_second_sd)*100.0/len(data)))
print("{}%  of data within third sd".format(len(length_of_third_sd)*100.0/len(data)))

graph1 = ff.create_distplot([data], ["result"], show_hist=False)
graph1.add_trace(go.Scatter(x=[first_sd_start,first_sd_start], y=[0,0.17], mode="lines", name="mean"))
graph1.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17], mode="lines", name="mean"))
graph1.show()

graph2 = ff.create_distplot([data], ["result"], show_hist=False)
graph2.add_trace(go.Scatter(x=[second_sd_start,second_sd_start], y=[0,0.17], mode="lines", name="mean"))
graph2.add_trace(go.Scatter(x=[second_sd_end,second_sd_end], y=[0,0.17], mode="lines", name="mean"))
graph2.show()

graph3 = ff.create_distplot([data], ["result"], show_hist=False)
graph3.add_trace(go.Scatter(x=[third_sd_start,third_sd_start], y=[0,0.17], mode="lines", name="mean"))
graph3.add_trace(go.Scatter(x=[third_sd_end,third_sd_end], y=[0,0.17], mode="lines", name="mean"))
graph3.show()
