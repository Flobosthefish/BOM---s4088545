import importlib

#pyhtml has the webserver and database connection code
import pyhtml

#The actual page content is implemented in the page_1.py file
import page_1
#The actual page content is implemented in the page_2.py file
import page_2
#The actual page content is implemented in the page_3.py file
import page_3

importlib.reload(page_1)
importlib.reload(page_2)
importlib.reload(page_3)

#You'll see more about what's going on in the terminal/console when this is set to True
#Useful for bigger programs.
pyhtml.need_debugging_help=True

#All pages that you want on the site need to be added as below
pyhtml.MyRequestHandler.pages["/home.html"]=page_1; #Page to show when someone accesses "http://localhost/"
pyhtml.MyRequestHandler.pages["/observations.html"]=page_2; #Page to show when someone accesses "http://localhost/page_2.html"
pyhtml.MyRequestHandler.pages["/timeperiod_comparison.html"]=page_3; #Page to show when someone accesses "http://localhost/page_3.html"

#This is to tell we're ready to go live
pyhtml.host_site()

print('done')