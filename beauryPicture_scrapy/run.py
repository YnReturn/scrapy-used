from scrapy import cmdline


name = 'sexual'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
