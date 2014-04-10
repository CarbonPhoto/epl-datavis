__author__ = 'SaleemSaddm'

import pprint
import  matplotlib.pyplot as plt


fileepl = open("epl_data.txt", "r")

k = fileepl.readlines()


Teams = ["Arsenal", "Manchester City", "Manchester United", "Chelsea", "Tottenham Hotspur", "Everton", "Liverpool", "Newcastle United", "Leeds United", "Aston Villa", "Blackburn Rovers", "Nottingham Forest", "Norwich City" ]


teamdict = {}

years = []

year = 0
flag2 = 0
for team in Teams:
    flag = 0
    temp = []
    for line in k:
            if "England" in line:
                if flag == 1:
                    rank = "23"
                    temp.append(24-int(rank))
                    flag = 0
                year = line.split()[1][-2:]
                if flag2 == 0:
                    years.append(year)
                flag = 1
            if team in line:
                rank = filter(lambda x: x.isdigit(), line.split()[0])
                temp.append(24-int(rank))
                flag = 0

            if line.startswith("end"):
                if flag == 1:
                    rank = "23"
                    temp.append(24-int(rank))

    teamdict[team] = temp
    flag2 =1



ind = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]


rankings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "Relegated", ]
rankings.reverse()

ax = plt.gca()
fig = plt.gcf()
ax.set_xticks(ind)
ax.set_yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
ax.set_xticklabels(years)
ax.set_yticklabels(rankings, fontsize=20)

#plt.grid(color='white', linestyle='-', linewidth=1)
ax.set_ylim([0, 24.5])
ax.set_xlim([0.5, 21.5])


'''
ranklist5 = teamdict["Arsenal"]
p5 = plt.plot(ind, ranklist5, linewidth=20.0, color='#ed0206', marker="o", markersize = 25, markerfacecolor="w", markeredgewidth = 5, markeredgecolor = "#ed0206")

ranklist = teamdict["Aston Villa"]
p1 = plt.plot(ind, ranklist, linewidth=20.0, color='#94bee3', marker="o", markersize = 25, markerfacecolor="#78003a", markeredgewidth = 5, markeredgecolor = "#94bee3")

ranklist10 = teamdict["Blackburn Rovers"]
p10 = plt.plot(ind, ranklist10, linewidth=20.0, color='#009fde', marker="o", markersize = 25, markerfacecolor="#e00016", markeredgewidth = 5, markeredgecolor = "#009fde")

ranklist7 = teamdict["Chelsea"]
p7 = plt.plot(ind, ranklist7, linewidth=20.0, color='#044794', marker="o", markersize = 25, markerfacecolor="w", markeredgewidth = 5, markeredgecolor = "#044794")

ranklist9 = teamdict["Leeds United"]
p9 = plt.plot(ind, ranklist9, linewidth=20.0, color='w', marker="o", markersize = 25, markerfacecolor="#2c4d9c", markeredgewidth = 5, markeredgecolor = "w")

ranklist2 = teamdict["Liverpool"]
p2 = plt.plot(ind, ranklist2, linewidth=20.0, color='#cf0026', marker="o", markersize = 25, markerfacecolor="#00a193", markeredgewidth = 5, markeredgecolor = "#cf0026")

ranklist3 = teamdict["Manchester United"]
p3 = plt.plot(ind, ranklist3, linewidth=20.0, color='#d9020d', marker="o", markersize = 25, markerfacecolor="#000000", markeredgewidth = 5, markeredgecolor = "#d9020d")

ranklist4 = teamdict["Manchester City"]
p4 = plt.plot(ind, ranklist4, linewidth=20.0, color='#5ec0eb', marker="o", markersize = 25, markerfacecolor="w", markeredgewidth = 5, markeredgecolor = "#5ec0eb")

ranklist8 = teamdict["Newcastle United"]
p8 = plt.plot(ind, ranklist8, linewidth=20.0, color='black', marker="o", markersize = 25, markerfacecolor="w", markeredgewidth = 5, markeredgecolor = "black")

ranklist11 = teamdict["Nottingham Forest"]
p11 = plt.plot(ind, ranklist11, linewidth=20.0, color='#e33232', marker="o", markersize = 25, markerfacecolor="w", markeredgewidth = 5, markeredgecolor = "#e33232")

ranklist12 = teamdict["Norwich City"]
print ranklist12
p12 = plt.plot(ind, ranklist12, linewidth=20.0, color='#00a64d', marker="o", markersize = 25, markerfacecolor="#ffee00", markeredgewidth = 5, markeredgecolor = "#00a64d")

ranklist6 = teamdict["Tottenham Hotspur"]
p6 = plt.plot(ind, ranklist6, linewidth=20.0, color='#001d57', marker="o", markersize = 25, markerfacecolor="w", markeredgewidth = 5, markeredgecolor = "#001d57")

ranklist13 = teamdict["Everton"]
p13 = plt.plot(ind, ranklist13, linewidth=20.0, color='#00509c', marker="o", markersize = 25, markerfacecolor="#ffdd1c", markeredgewidth = 5, markeredgecolor = "#00509c")
'''

ips = [23,16,19,22,23,23,23,23,23,5,18,23,23,23,23,23,23,23,23,23,23]
ips2 = [24-x for x in ips]
p13 = plt.plot(ind, ips2, linewidth=20.0, color='#3a63a1', marker="o", markersize = 25, markerfacecolor="#de2c35", markeredgewidth = 5, markeredgecolor = "#3a63a1")


plt.tick_params(\
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off


plt.tick_params(\
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    right='off',      # ticks along the bottom edge are off
    left='off',         # ticks along the top edge are off
    labelleft='off') # labels along the bottom edge are off



fig.set_size_inches(40,10)
plt.savefig("../../Desktop/fun/epl/ips.png",bbox_inches='tight', dpi = 96, pad_inches=0, transparent = True)

