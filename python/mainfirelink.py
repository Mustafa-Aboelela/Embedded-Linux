
import webbrowser      
import firelink          #it's a file at the same dir

x= firelink.firefox()

webbrowser.open(f'{x}', new=2)