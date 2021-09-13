"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def normlevel(value1, feature, parent):
    if value1 == "SFC":
        return 0
    elif value1.startswith("FL"):
        return int(value1[2:]) * 100
    elif value1.endswith("ALT"):
        return int(value1[0:-3])
    else:
        return 0

@qgsfunction(args='auto', group='Custom')
def astype(feature, parent):
	if feature['class']:
		return feature['class']
	elif feature['type'] in ["D", "DANGER"]:
		return "DANGER"
	elif feature['type'] in ["P", "PROHIBITED"]:
		return "PROHIBITED"
	elif feature['type'] in ["R", "RESTRICTED"]:
		return "RESTRICTED"
	elif feature['name'].startswith("NSGA") or feature['name'].startswith("TRAG"):
		return "WAVE"
	else:
		return "OTHER"
	
@qgsfunction(args='auto', group='Custom')
def tnptype(feature, parent):
	if feature['class']:
		return feature['class']
	elif feature['type'] in ["D", "DANGER"]:
		return "DANGER"
	elif feature['type'] in ["P", "PROHIBITED"]:
		return "PROHIBITED"
	elif feature['type'] == ["R", "RESTRICTED"]:
		return "RESTRICTED"
	elif feature['title'].startswith("NSGA") or feature['title'].startswith("TRAG"):
		return "WAVE"
	else:
		return "OTHER"
