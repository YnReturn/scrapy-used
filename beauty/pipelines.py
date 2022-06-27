# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re

class BeautyPipeline(ImagesPipeline):
    # print(item['image_url'])    
    # def process_item(self, item, spider):
    def get_media_requests(self, item, info):
        # for url in item['image_url']:
        yield Request(url = item['image'], headers={'referer':'https://www.mm131.net/xinggan/'}, meta = {'name':item['dirname']})

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        name = request.meta['name']
        #print("!!!!!!!!!!!!!!" + name)
        #name = re.sub(r'[？\\*|“<>:/]', '', name)
        '''
        这个是重写了scrapy的 file_path函数，默认的保存位置时full。为了分类，将file_path进行改写
        但是出现了差错，我item了标题，但是却出现了文件反复保存在多个同名文件夹，也就是name，name(2)，name（3）
        最开始我以为是，itme保存name时，如果是重复的相同数据，会进行name(2),也就是像我们系统保存同名文件时，如果不覆盖，
        会自动生成同名文件后面加上(2)。最开始的思路是将spider文件进行修改，达到，同一页面中的请求只保存一个name。但是我没有解决方法
        于是，我还是将思路转到了file_path上，最开始我是并不知道file_path运行规则，后来经过几次的验证，发现，file_path就是将get_media_
        request函数保存的位置，然后查询这些语句的运行的value是什么？经过几个print，我得出了fiel_path是可以保存在同名文件夹中的。
        也就是说，item在保存name时，并不会向系统那样，相同name不会生成(2)(3)什么的。也就是说，和之前一样，就是我selector出现了错误
        经过f12，确认后的确，进入第三级页面后的标题，自己就带有（2）（3），于是我最开始的思路，是寻找网页上有没有其他的元素，没有这种（2）（3）
        元素，但是没有找到，于是，只能将得到的字符串数据进行删除，修改。也就是将Name中的(2)(3)这种数据删掉。于是我在网上搜到了一个最简单的方法
        直接保留字符串中的中文字符，其他字符删掉，于是乎，便是得到了re正则表达式中的re.sub('[^\u4e00-\u9fa5]+','',name)。
        运行符合预期。
        '''
        name = re.sub('[^\u4e00-\u9fa5]+','',name)
        #print("$$$$$$$$$$$$" + name)
        filename = u'{0}/{1}'.format(name, image_guid)
        return filename
'''
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        folder_name = item['folder_name']
        # img_name = item['img_name']  #图片没有名字不启用这个语句
        # 因为图片没有名字就用url截取最后的字符串作为名字
        image_guid = request.url.split('/')[-1]
        img_name = image_guid
        # name = img_name + image_guid
        # name = name + '.jpg'
        # 0 代表文件夹，1 代表文件
        filename = u'{0}/{1}'.format(folder_name, img_name)
        return filename

    # 固定改写的函数，不需要修改
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item
'''