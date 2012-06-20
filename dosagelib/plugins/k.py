from re import compile, IGNORECASE

from ..helpers import _BasicScraper



class KernelPanic(_BasicScraper):
    latestUrl = 'http://www.ubersoft.net/kpanic/'
    imageUrl = 'http://www.ubersoft.net/kpanic/d/%s'
    imageSearch = compile(r'src="(.+?/kp/kp.+?)" ')
    prevSearch = compile(r'<li class="previous"><a href="(.+?)">')
    help = 'Index format: yyyymmdd.html'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.split('/')[-1].split('.')[0]



class Key(_BasicScraper):
    latestUrl = 'http://key.shadilyn.com/latestpage.html'
    imageUrl = 'http://key.shadilyn.com/pages/%s.html'
    imageSearch = compile(r'"((?:images/.+?)|(?:pages/images/.+?))"')
    prevSearch = compile(r'</a><a href="(.+?html)".+?prev')
    help = 'Index format: nnn'



class Krakow(_BasicScraper):
    latestUrl = 'http://www.krakowstudios.com/'
    imageUrl = 'http://www.krakowstudios.com/archive.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class Kukuburi(_BasicScraper):
    latestUrl = 'http://www.kukuburi.com/current/'
    imageUrl = 'http://thaumic.net/%s'
    imageSearch = compile(r'img src="(http://www.kukuburi.com/../comics/.+?)"')
    prevSearch = compile(r'nav-previous.+?"(http.+?)"')
    help = 'Index format: non'


class KevinAndKell(_BasicScraper):
    latestUrl = 'http://www.kevinandkell.com/'
    imageUrl = 'http://www.kevinandkell.com/%s/kk%s%s.html'
    imageSearch = compile(r'<img.+?src="(/?(\d+/)?strips/kk\d+.gif)"', IGNORECASE)
    prevSearch = compile(r'<a.+?href="(/?(\.\./)?\d+/kk\d+\.html)"[^>]*><span>Previous Strip', IGNORECASE)
    help = 'Index format: yyyy-mm-dd'

    def setStrip(self, index):
        self.currentUrl = self.imageUrl % tuple(map(int, index.split('-')))



class KillerKomics(_BasicScraper):
    latestUrl = 'http://www.killerkomics.com/web-comics/index_ang.cfm'
    imageUrl = 'http://www.killerkomics.com/web-comics/%s.cfm'
    imageSearch = compile(r'<img src="(http://www.killerkomics.com/FichiersUpload/Comics/.+?)"')
    prevSearch = compile(r'<div id="precedent"><a href="(.+?)"')
    help = 'Index format: strip-name'
