##说明  
本程序使用python编写，功能是根据输入的商品类别或者ASIN从trendata.cn的API获取数据并解析，生成显示统计图表的网页。  
若需要生成某个商品的统计图表，使用脚本create_webpage.py，需要一个参数指定ASIN。例如:   

	$ python create_webpage.py B004PWLR06

若需要生成某类商品的图表，使用脚本create_catepage.py。
需要两个参数，分别指定商品类别和获取条数。第一参数为trenddata的API中规定的商品类名，第二参数为从API获取的信息的页数（从第一页开始），每页有20个商品的数据。  
如果不输入第二参数，则默认获取一页，即二十条数据。例：  

	$ python create_catepage.py "Kitchen>Furniture>Home Office Furniture" 3
	# 第二参数是可选的

程序会在当前文件夹下建立一个名为“webpages”的文件夹，生成的网页存在以AISN和商品分类的名字命名的子文件夹里  
网页中图表的生成使用了以javascript编写的[highcharts](www.highcharts.com)图表库，在网页中以在线链接的方式引入了该库，所以请在能正常连接到网络时查看图表。  


----------------------------------
click [here](./wiki) for more details