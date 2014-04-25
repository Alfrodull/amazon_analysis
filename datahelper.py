import urllib
import simplejson as json

def get_product_data(asin):
	'''根据输入的asin获取商品信息'''
	target_url = 'http://112.124.1.3:8004/api/commodity/' + asin
	return json.loads(urllib.urlopen(target_url).read())

def get_star_list(product_data):
	'''从获取的数据中提取评分'''
	star_list = [float(single_review['star'].split()[0]) \
                 for single_review in product_data['review']]
    return star_list


