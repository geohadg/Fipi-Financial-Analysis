---
title: Fipi v1 Bug Report and Fixes
---
2025-01-27 20:55
Tags:   [[Fipi]]  [[Python]]
# Bugs to Fix:

Matplotlib Pie Chart Labels Overlap
# Fixes:

## Graph Labels Problem

My first obvious solution is to try to rotate the graph such that the smaller categories end up horizontal and re-order the arrays of amounts and keys to spilt them up onto the poles of the graph, then drop any amount and key that accounts for less that 1% of the total
	
another possible fix ive seen is the plt.tight_layout() function
	
to help improve visibility ive decided to add borders to the chart aswell with
```
 **wedgeprops={'edgecolor': 'black', 'linewidth': 2}
```
I also decided that if a category makes up for less than 1% of the graph it wouldnt appear and instead only be visible in the legend

I ran into an issue when trying to remove elements from a list based on less than threshold however, I believe this was the result of me trying to iterate and remove by index within for loop:
```
for i in range(len(sums)):
	if sums[i] < threshold:
		del sums[i]
	
```
this would throw an index error as after removing an element it changes the length of the list, so rather I make note of the indexes I should delete from sums and keys and delete them after exiting the for loop
### Starting Code for the Graph Function

```
def graph(sums, keys):

	"""Produces a pie chart from given list of sums and labels"""

	self.ax.clear()

	self.ax.legend(labels=[])

	explodelist = []



	minsum = min(sums)

	for i in range(len(sums)):

		if sums[i] == minsum:

			explodelist.append(0.1)



		else:

			explodelist.append(0)



	print(explodelist)

	print(sums)

	displaysums = []

	s = sum(sums)



	for i in range(len(sums)):

		displaysums.append(f"{keys[i]}: {str(int(sums[i]))}$")




	_, texts =self.ax.pie(sums, labels=keys, explode=explodelist, labeldistance=1.2, radius=1.2, colors=['#fcc98d', '#fcbd74', '#e98d6b', '#e3685c', '#d63c56', '#c93673', '#9e3460', '#8f3371', '#6c2b6d', '#511852'], startangle=0)

	#autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 1 else '',

	for key in texts:

		key.set_color("#fcae74")



	self.ax.legend(bbox_to_anchor=(-0.95, 0.5), loc='center left', labels=displaysums)

	toolbar = NavigationToolbar2Tk(self.canvas, self.graphframe, pack_toolbar=False)

	toolbar.update()

	toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)  

	self.canvas.draw()

	self.canvas.get_tk_widget().pack(side=tkinter.RIGHT, anchor="e", fill="x")
```
![[unoptimizedgraph-fipi-v1.png]]
## Finished Code for the Graph Function
```
 def graph(sums, keys):

            """Produces a pie chart from given list of sums and labels"""

            self.ax.clear()

            explodelist = []

            displaysums = []

            indexestodelete = []

            s = sum(sums)

            threshold = s*0.01

            for i in range(len(sums)):

                displaysums.append(f"{keys[i]}: {str(int(sums[i]))}$")

                sums[i] = sums[i].astype(int)

                if sums[i] < threshold:

                    indexestodelete.append(i)

            for index in indexestodelete:

                del keys[index]

                del sums[index]


            for i in range(len(sums)):

                if sums[i] == min(sums) or sums[i] == max(sums):

                    explodelist.append(0.2)


                else:

                    explodelist.append(0)

  

            _, texts =self.ax.pie(sums, labels=keys, explode=explodelist, labeldistance=1.2, radius=1.2, colors=['#fcc98d', '#fcbd74', '#e98d6b', '#e3685c', '#d63c56', '#c93673', '#9e3460', '#8f3371', '#6c2b6d', '#511852'], startangle=0, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

            #autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 1 else '',

            for key in texts:

                key.set_color("#fcae74")

            self.ax.legend(bbox_to_anchor=(-0.95, 0.5), loc='center left', labels=displaysums, )

            toolbar = NavigationToolbar2Tk(self.canvas, self.graphframe, pack_toolbar=False)

            toolbar.update()

            toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)  

            self.canvas.draw()

            self.canvas.get_tk_widget().pack(side=tkinter.RIGHT, anchor="e", fill="x")
```
![[optimizedgraph-fipi-v1.png]]
# Notes

Yes I am aware that the Interest and Fee/Interest Categories are duplicates, and was a result of quicksilver and savor csv files being pre-categorized and my script didnt clear or change the category to match that of other accounts. This has been remedied by manually changing the category name inside the quicksilver function with a .loc command in pandas
```
df.loc[df["Category"] == "Fee/Interest Charge", "Category"] = "Interest"
```

Feel free to give suggestions I am open to any ways of cleaning up this code and decreasing time complexity
# Report

The Graph Function now works as intended and doesnt make labels appear on top of one another
see [[Fipi v2 Bug Report and Fixes]] for next iteration