import urllib2, json
from random import randrange
from os.path import basename, realpath, dirname

class ImgurNSFW:
    def __init__(self):
        self.script_path = dirname(realpath(__file__))
        self.__key       = None
        self.__gallery   = None
        self.__type      = None

    def getScriptPath(self):
        return self.script_path

    def setKey(self, key):
        self.__key = key

    def getKey(self):
        return self.__key

    def setGallery(self, gallery):
        self.__gallery = gallery

    def getGallery(self):
        return self.__gallery

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def getWallpaper(self):
        req = urllib2.Request('https://api.imgur.com/3/gallery/'+ self.getGallery() + '/' + self.getType())
        req.add_header('Authorization', 'Client-ID ' + self.getKey())

        try:
            result = urllib2.urlopen(req)
            data   = json.loads(result.read())
        except urllib2.HTTPError:
            data = None

        if data == None:
            return False

        return data['data'][randrange(0, len(data['data']))]['link']

    def saveWallpaper(self, image):
        filename = basename(image)

        with open(self.script_path + '/wallpapers/' + filename, 'w') as f:
            req    = urllib2.Request(image)
            result = urllib2.urlopen(req).read()

            f.write(result)

        return self.script_path + '/wallpapers/' + filename
