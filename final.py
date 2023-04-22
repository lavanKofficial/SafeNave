from algo import places 

initial = "https://www.google.com/maps/dir"  
places.insert(0, initial) 

joined_string = "/".join(places)
string_with_space =  joined_string


string_with_plus = "+".join(string_with_space.split()) if " " in string_with_space else string_with_space  



import webbrowser
from tkinter import *
   
root = Tk() 
root.title("WebBrowsers") 
root.geometry("660x660") 
webbrowser.open(string_with_plus)