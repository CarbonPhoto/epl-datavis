__author__ = 'elric-dev'

import  matplotlib.pyplot as plt





ind = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
first =  [84, 92, 89, 82, 75, 78, 79, 91, 80, 87, 83, 90, 95, 91, 89, 87, 90, 86, 80, 89, 89]
second = [74, 84, 88, 78, 68, 77, 78, 73, 70, 80, 78, 79, 83, 83, 83, 85, 86, 85, 71, 89, 78]
third =  [72, 77, 77, 71, 68, 65, 75, 69, 69, 77, 69, 75, 77, 82, 68, 83, 83, 75, 71, 70, 75]
forth =  [71, 71, 74, 63, 68, 63, 67, 67, 68, 71, 67, 60, 61, 67, 68, 76, 72, 70, 68, 69, 73]


ax = plt.gca()
fig = plt.gcf()
ax.set_xticks(ind)
ax.set_yticks(list(xrange(0,98,2)))
#ax.set_yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
#ax.set_xticklabels(years)
#ax.set_yticklabels(rankings, fontsize=20)

#plt.grid(color='white', linestyle='-', linewidth=1)
ax.set_ylim([58, 97])
ax.set_xlim([0.5, 21.5])
ax.set_axis_bgcolor("black")



p1 = plt.plot(ind, first,  linewidth=20.0, color='#023858', marker="o", markersize = 25, markerfacecolor="#a6bddb", markeredgewidth = 5, markeredgecolor = "#023858")
p2 = plt.plot(ind, second, linewidth=20.0, color='#800026', marker="o", markersize = 25, markerfacecolor="#feb24c", markeredgewidth = 5, markeredgecolor = "#800026")
p3 = plt.plot(ind, third,  linewidth=20.0, color='#004529', marker="o", markersize = 25, markerfacecolor="#addd8e", markeredgewidth = 5, markeredgecolor = "#004529")
p4 = plt.plot(ind, forth,  linewidth=20.0, color='#4d004b', marker="o", markersize = 25, markerfacecolor="#9ebcda", markeredgewidth = 5, markeredgecolor = "#4d004b")


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
plt.savefig("test_pt3.png",bbox_inches='tight', dpi = 96, pad_inches=0, transparent = 'true')

