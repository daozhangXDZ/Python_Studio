import logging

from grab import Grab

logging.basicConfig(level=logging.DEBUG)

g = Grab()

g.go('https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn')
g.doc.set_input('username', '1485418053@qq.com')
g.doc.set_input('password', 'dao9412hujingbo')
g.doc.submit()

g.doc.save('/tmp/x.html')

g.doc('//ul[@id="user-links"]//button[contains(@class, "signout")]').assert_exists()

home_url = g.doc('//a[contains(@class, "header-nav-link name")]/@href').text()
repo_url = home_url + '?tab=repositories'

g.go(repo_url)

for elem in g.doc.select('//h3[@class="repo-list-name"]/a'):
    print('%s: %s' % (elem.text(),
                      g.make_url_absolute(elem.attr('href'))))