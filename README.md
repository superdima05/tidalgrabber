# Tidal Grabber

If you have a lossless subscription, and you want to get .flac files, you can use this python script. ONLY PYTHONISTA 3

Requirements: 
  - tidalapi
  - transliterate 
  - mutagen
  - Apple Shortcuts
  - Pythonista 3
  
To use this script install this shortcut: https://www.icloud.com/shortcuts/68cd544de6ca432a9bb1afb0e277ebbc or from "Tidal Grabber.shortcut", then from TIDAL application share a track, playlist, album to this shortcut.

Shortcut algoritm = Get text from TIDAL -> Parse text to get a link -> Get a type of content (e.g track, playlist, album) -> Copy to clipboard a text with special format "type|id" (e.g "track|000") -> Run Pythonista 3.

Pythonista algoritm = Get text from clipboard -> Parse it to get a type, and id -> Run ported tidal.py with parameters from step 2 
  
Script has 4 modes:
  - Playlist step 
  - Track grabber
  - Album grabber
  - Search
  
Features:
 - Automatically set ID3 tags
 - Automatically sets album artworks
 - No need get token manually to use this script
