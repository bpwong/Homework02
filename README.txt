Homework02
==========

The third assignment for Astro 250

Part 1:
In bash, enter $python myPlot.py

This will generate a plot, where each subplot
corresponds to the plots they replicate:
plot_data3.png and plot_data4.png. 


Part 2:
In bash, enter $python plotData.py

plotData.py generates a plot using the provided 
data files kept in /txt:
ny_temps.txt, yahoo_data.txt, google_data.txt

An image of the plot generated (NY_Google_Yahoo.png)
can be found in the main folder.



Part 3:
To run in bash, enter $python RectBrush.py.
Be sure iris_data.txt is in /txt

RectBrush.py plots the Iris Flower data and 
allows a user to brush over the data.  

The brush functionality is halfway complete, 
as the data selection process has not been 
finished -- only rectangles can be drawn 
and cleared if 'd' or 'D' is pressed while 
the mouse is over a rectangle(s).

Currently, the colors can be changed by
pressing 'a' or 'A'.  However, to complete the 
brushing, my next step was to look into the 
contains() function and try to use that to 
gather the points within a rectangle patch.
Then I could update the colors accordingly.