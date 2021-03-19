import os
import subprocess
import shutil
import random
import fontTools
from fontTools.ttLib import TTFont
import tempfile
import uuid

pathToFontToolsMutator = os.path.join(os.path.split(fontTools.__file__)[0], 'varLib/mutator.py')

class VFInstance:
    
    def __init__(self, sourcePath, location, DEBUG=False):
        self.instancePath = tempfile.mkstemp()[1]
        tempPath = sourcePath.replace('.ttf', '-instance.ttf')
        
        cmds = ['python', pathToFontToolsMutator, sourcePath]
        for k, v in location.items():
            cmds.append('%s=%s' %(k, v))
        proc = subprocess.Popen(cmds, stdout=subprocess.PIPE)
        out = proc.communicate()[0]

        if DEBUG:
            print ('---')
            print (' '.join(cmds))
            print ('---')
            print (out)

        myUUID = str(uuid.uuid4()).replace('-', '')
        f = TTFont(tempPath)
        self.fontName = 'VF'+str(myUUID)
        
        f['name'].setName(self.fontName, 6, 1, 0, 0) # Macintosh
        f['name'].setName(self.fontName, 6, 3, 1, 0x409) # Windows
        
        os.remove(tempPath)
        
        f.save(self.instancePath)
        
    def getName(self):
	    return self.fontName

    def getPath(self):
        return self.instancePath

    def remove(self):
        try:
            os.remove(self.instancePath)
        except:
            pass
