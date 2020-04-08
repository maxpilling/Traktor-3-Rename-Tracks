# Using an XML, and a regex library to make things easier
import xml.etree.ElementTree as ET
import re

# Traktor saves the metadata in an xml file with their own file ending 'nml'.
path = "/Users/MaxPilling/Documents/Native Instruments/Traktor 3.1.1/collection.nml"

tree = ET.parse(path)
root = tree.getroot()

# The tracks info is in <COLLECTION ENTRIES=* > then within this there is info for each track
# Each one is in the form:          <ENTRY ...... TITLE="songname - artist">            ....... </ENTRY>
# I want to change it to the form:  <ENTRY ...... TITLE="songname" ARTIST="artist" >    ....... </ENTRY>

collection = root.find('COLLECTION')

pattern = re.compile('.+ - .+')
for entry in collection.iter('ENTRY'):
    # I only want to edit ones where there is no artist and the format is as I need it to be
    if (not entry.get('ARTIST') and pattern.match(entry.get('TITLE'))):
        oldTitle = entry.get('TITLE')
        artist, songname = oldTitle.split(' - ')
        entry.set('TITLE', songname)
        entry.set('ARTIST', artist)

# Save the XML
tree.write(path)
