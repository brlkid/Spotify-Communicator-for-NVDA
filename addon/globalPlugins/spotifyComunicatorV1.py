import globalPluginHandler
from scriptHandler import script
import ui
from api import getDesktopObject

spotify = None 

if spotify==None:
    for child in getDesktopObject().children:
        if "spotify" in str(child.appModule).lower():
            spotify = child

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    @script(gesture="kb:NVDA+shift+t", description = "Reports the title of the currently playing Spotify song if the Spotify app is running")
    def script_getSongTitle(self, gesture):
        if spotify==None or spotify.name==None: 
            ui.message("Spotify linking failed. Either start the Spotify app, or press ctrl+NVDA+f3 to reload linking.")
        else: 
            ui.message(spotify.name)

