from re import compile

from ..helpers import _BasicScraper



class NineteenNinetySeven(_BasicScraper):
    name = '1997'
    latestUrl = 'http://www.1977thecomic.com/'
    imageUrl = 'http://www.1977thecomic.com/%s'
    imageSearch = compile(r'<img src="(http://www.1977thecomic.com/comics-1977/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><span class="prev">')
    help = 'Index format: yyyy/mm/dd/strip-name'



class EightHalfByEleven(_BasicScraper):
    name = '8HalfByEleven'
    latestUrl = 'http://www.lucastds.com/webcomic/'
    imageUrl = 'http://www.lucastds.com/webcomic/index.php?strip_id=%s'
    imageSearch = compile(r'<img src="(istrip_files/strips/.+?)"')
    prevSearch = compile(r'</a><a href="(/webcomic/.+?)"><img[^>]+?src="themes/tedzsee/images/previous_a.png">')
    help = 'Index format: nnn'
