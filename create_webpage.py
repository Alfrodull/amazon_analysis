import os
import sys
import datahelper


index = 'index.html'
star_hist = 'star_hist.js'
price_line = 'price_line.js'
webdir = 'webpages'

def page_template(target):
	return 'webpage_template/%s' % target

def init(asin):
	'''init homepage'''

	pwebdir = os.path.join(webdir,asin)
	if not os.path.exists(pwebdir):
		os.makedirs(pwebdir)
	homepage = os.path.join(pwebdir,index)
	if os.path.isfile(homepage):
		os.remove(homepage)
	try:
		open(homepage, 'wb').write(open(page_template(index),'rb').read())
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



if __name__ == '__main__':
	if len(sys.argv) <= 1:
		sys.argv.append('B003FGWY1O')
	product_data = datahelper.get_product_data(sys.argv[1])
	if product_data:
		init(sys.argv[1])
		draw_star_hist(product_data)
		draw_price_line(product_data)
	else:
		print 'no any data'