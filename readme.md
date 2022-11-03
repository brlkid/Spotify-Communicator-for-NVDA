# Spotify Communicator

This package contains a basic integration for the Windows Spotify application.

At current, it can read the title of the currently playing track however functionality to copy metadata to the clipboard is coming.

This package is distributed under the terms of the GNU General Public License, version 2 or later. Please see the file COPYING.txt for further details.

## commands:

- NVDA+shift+t: This will announce the name of the currently playing Spotify track.

## Notes:

- Note: the addon will inform the user if the Spotify app is not detected. If this is the case, one must start the Spotify app, then either press NVDA+CTRL+f3 or restart NVDA to allow the addon to reload the detection of Spotify.

- Note: If linking is successful, but there is no song playing, either Spotify or Spotify premium (according to your subscription level) will be announced. In future versions, this should be fixed, however for now that indicates that no song or media is playing.