import urllib
import simplejson as json

def get_product_data(asin):
	'''use asin to get get_product_data '''
	target_url = 'http://112.124.1.3:8004/api/commodity/' + asin
	return json.loads(urllib.urlopen(target_url).read())

def get_star_list(product_data):
	'''get star infomation from product data'''
	return [float(single_review['star'].split()[0]) for single_review in product_data['review']]

def get_price_list(product_data):
	'''get first price infomation from product data'''
	price_date_li = []
	for offer in product_data['offer']:
		if offer['info']:
			price_date_li.append((offer['info'][0]['price'],offer['info'][0]['timestamp']))
	return price_date_li

if __name__ == '__main__':
	# product_data = get_product_data('B00D386JBA')
	product_data = get_product_data('B003FGWY1O')
	# sl = get_star_list(product_data)
	# print sl
	pdl = get_price_list(product_data)
	print pdl
