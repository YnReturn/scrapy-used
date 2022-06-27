import scrapy
from beauty.items import BeautyItem

class SexualSpider(scrapy.Spider):
    name = 'sexual'
    allowed_domains = ['mm131.net']
    start_urls = ['https://www.mm131.net/xinggan/']

    #next_page_url = ''
    #next_page_image_url = ''
    
    def parse(self, response):
        #item = BeautyItem()
        # i = self.i_parse(response)
        # while True:
        #for url in self.i_parse(response):
        # img = self.ii_parse(response)
        # print(img)
        # item["<<<<<<<<<<<<<<"+'imgesrc'] = img
        # yield item
        #parse_all = self.i_parse(response)
        # print(parse_all)
        # for url in parse_all:
        # print(next(parse_all))
        
        #while True:
            # 处理第一页的所有的子页面的图像
            #for url in parse_all:
                #print(url)
                # print(parse_all)
                #yield scrapy.Request(url=url, callback=self.ii_parse, dont_filter=True, priority=1, flags=["zhe shi 5"])
                #<<< question！ 我试验了很多次，当我在类中调用另外的函数后，self.next_page_image_url是有进行修改的,
                # 但是经过scrapy.Request的callback调用另外的函数后，self.next_page_image_url竟然并没有修改值。
                # 还有scrapy.Request 似乎不用yield就不会调用callback。会不会有这种可能，这时的变量值已然是空，并没有执行
                # ii_parse，根据输出的结果的确是先输出了5，而不是3,4
                #print("5____________" + self.next_page_image_url )
                #while True:

                    #yield scrapy.Request(url=self.next_page_image_url, callback=self.ii_parse, dont_filter=True, flags=['aaaaaaz'])
                    #if self.next_page_image_url == None:
                        #break
                    
            #parse_all = scrapy.Request(url=self.next_page_url, callback=self.i_parse,dont_filter=True, flags="qqqqqqqqqqd")
            #if self.next_page_url == None:
                #break


    #def i_parse(self, response):
        #>>> 性感美女页面的一级页面中第一页的封面图片链接数据类似['https://www.mm131.net/xinggan/5749.html','https://www.mm131.net/xinggan/5748.html']
        page_url = response.xpath('//dl[@class="list-left public-box"]//a[contains(@target,"_blank")]/@href').getall()
        #while True：
            #>>> 进入性感美女页面的一级页面中第二页此时的返回值类似格式'li
        #if response.xpath('//span[@class="page-ch"]'):
        #    return
        # next_page_url = self.start_urls[0] + response.xpath('//a[@class="page-en"]/@href').get()
        # 这里有个智障玩意，我最开始selector之后，便一直在修改语法逻辑问题，从来没有想过我的selector会是错的。结果当我的程序没有
        #问题后，便是发现最终还是一直在爬取这固定页面，我又以为是我的yield出现了问题，以为yield scrapy.request的调用顺序有问题
        # 以为callback有问题，资料查的漫天飞起，直到看到别人的一段代码和我的基本逻辑一模一样，但是确实成功的，这时我才意识到，会不会
        # 是我的selector出现了错误，于是重新F12，结果发现我的selector的确是如此的在固定页面回转。
            # page_url.append(next_page_url)
        # print(page_url)
        #print(next_page_url)
        for url in page_url:
            #if response.xpath('//span[@class="page-ch"]') == []:
            yield scrapy.Request(url=url, callback=self.ii_parse, dont_filter=True)
        next_page_url = response.css('.page_now+a::attr(href)').get()
        #response.urljoin(next_page_url)
        if next_page_url:
            yield scrapy.Request(url=response.urljoin(next_page_url), callback=self.parse, dont_filter=True)
        #if response.xpath('//span[@class="page-ch"]') == []:
       #     yield from  page_url
        #else:
        #    self.next_page_url = None
        #yield scrapy.Request(url=next_page_url, callback=self.i_parse, dont_filter=True)
        #yield  next_page_url

    def ii_parse(self, response):

        #>>> 进入性感美女页面的二级页面中的第一页的图像链接
        page_image_url = response.xpath('//div[@class="content-pic"]//@src').get()
        #print("3____________" + page_image_url)
        #while True:
        #>>> 进入性感美女页面的二级页面中的第二页的图像链
        #if response.xpath('//span[@class="page-ch"]') == []:
        #    return
        # next_page_image_url = self.start_urls[0] + response.xpath('//a[@class="page-en"]/@href').get()
        #print("4____________" + self.next_page_image_url)
        # page_image_rl.append(next_page_image_url)
        #if response.xpath('//span[@class="page-ch"]') == []:
        #response.css('.page_now+a::attr(href)').get()
        item = BeautyItem()
        item['image'] = page_image_url
        item['dirname'] = response.xpath('//div[@class="content"]/h5/text()').get()
        yield item
        next_page_image_url = response.css('.page_now+a::attr(href)').get()
        #print("4____________" + next_page_image_url)
        if next_page_image_url:
            yield scrapy.Request(url=response.urljoin(next_page_image_url), callback=self.ii_parse, dont_filter=True)
        #else:
        #    self.next_page_image_url = None
        #self.ii_parse(scrapy.Request(next_page_image_url))
        #yield next_page_image_url            
        
    
    '''
    start_urls = ['https://www.mm131.net/xinggan/5740.html']
    
    def parse(self, response):
        item = BeautyItem()
        item['image_url'] = response.xpath('//div[@class="content-pic"]//@src').get()
        yield item

        print("wo yao print le !!!!!!")
        print(item['image_url'])
    '''