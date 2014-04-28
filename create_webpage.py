import os
import sys
import datahelper


com_page = 'commodity.html'
star_hist = 'star_hist.js'
price_line = 'price_line.js'
review_t_line = 'review_time_line.js'
webdir = 'webpages'
com_info = 'com_info.js'

def page_template(target):
	return 'webpage_template/%s' % target

def init(product_data):
	'''init homepage'''
	asin = product_data['ASIN']
	com_name = product_data['productInfo'][0]['name']
	img_link = product_data['productInfo'][0]['img']
	zlink = 'http://www.amazon.com/dp/'+asin

	pwebdir = os.path.join(webdir,asin)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)

	homepage = os.path.join(pwebdir,com_page)
	pcom_info = os.path.join(pwebdir,com_info)
	if os.path.isfile(homepage):
		os.remove(homepage)
	if os.path.isfile(pcom_info):
		os.remove(pcom_info)
	try:
		open(homepage, 'wb').write(open(page_template(com_page),'rb').read())
		infofile = open(pcom_info,'wb')
		infofile.write('var com_name = \"%s\"\n\
						var zlink = \"%s\"\n' % \
						(com_name,zlink))
		infofile.write(open(page_template(com_info),'rb').read())
		infofile.close()
	except IOError:
		raise

def draw_star_hist(product_data):
	'''input data to star hist template'''
	asin = product_data['ASIN']
	star_list = datahelper.get_star_list(product_data)
	star_sum = [0,0,0,0,0]
	for star in star_list:
		if star == 5: star_sum[0]+=1
		elif star == 4: star_sum[1]+=1
		elif star == 3: star_sum[2]+=1
		elif star == 2: star_sum[3]+=1
		elif star == 1: star_sum[4]+=1
		else: pass
	pwebdir = os.path.join(webdir,asin)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	pstar_hist = os.path.join(pwebdir,star_hist)
	if os.path.isfile(pstar_hist):
		os.remove(pstar_hist)
	try:
		histfile = open(pstar_hist,'wb')
		histfile.write('var star_list = %s \n' % str(star_sum))
		histfile.write(open(page_template(star_hist),'rb').read())
		histfile.close()
	except IOError:
		raise


def draw_price_line(product_data):
	'''input data to price line template'''
	asin = product_data['ASIN']
	price_date_li = datahelper.get_price_list(product_data)
	price_list = []
	date_list = []
	for price_date in price_date_li:
		price_list.append(price_date[0]);
		date_list.append(str(price_date[1].split()[0]))

	pwebdir = os.path.join(webdir,asin)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	pprice_line = os.path.join(pwebdir,price_line)
	if os.path.isfile(pprice_line):
		os.remove(pprice_line)
	try:
		linefile = open(pprice_line,'wb')
		linefile.write('var price_list = %s \n' % str(price_list))
		linefile.write('var date_list = %s \n' % str(date_list))
		linefile.write(open(page_template(price_line),'rb').read())
		linefile.close()
	except IOError:
		raise

def draw_review_t_line(product_data):
	'''input data to review-time line template'''
	asin = product_data['ASIN']
	review_time = datahelper.get_review_time_list(product_data)
	count_list = review_time[0]
	date_list = review_time[1]

	pwebdir = os.path.join(webdir,asin)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	preview_t_line = os.path.join(pwebdir,review_t_line)
	if os.path.isfile(preview_t_line):
		os.remove(preview_t_line)
	try:
		linefile = open(preview_t_line,'wb')
		linefile.write('var count_list = %s \n' % str(count_list))
		linefile.write('var date_list = %s \n' % str(date_list))
		linefile.write(open(page_template(review_t_line),'rb').read())
		linefile.close()
	except IOError:
		raise


if __name__ == '__main__':
	if len(sys.argv) <= 1:
		default_asin = 'B003FGWY1O'
		sys.argv.append(default_asin)
	product_data = datahelper.get_product_data(sys.argv[1])
	if product_data:
		init(product_data)
		draw_star_hist(product_data)
		draw_price_line(product_data)
		draw_review_t_line(product_data)
	else:
		print 'no any data'