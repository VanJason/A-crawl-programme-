#-*- coding:utf-8 -*-

"""
广州公共资源交易网
"""

import re
import urllib
from urllib import request
from bs4 import BeautifulSoup
import xlwt
from selenium import webdriver
from bs4 import BeautifulSoup

# def get_content(url):
# 	driver = webdriver.PhantomJS()
# 	driver.set_window_size(800,600)

# 	driver.get(url)
# 	driver.find_element_by_link_text(u"政府采购").click()
# 	# driver.find_element_by_css_selector("span > dd").click()
# 	driver.find_element_by_xpath("/x:html/x:body/x:div[2]/x:div[3]/x:div[1]/x:div[2]/x:div[1]/x:div[5]/x:a").click()
# 	driver.find_element_by_id("searchvalue").clear()
# 	driver.find_element_by_id("searchvalue").send_keys(u"医院")
# 	driver.find_element_by_id("img1").click()

# 	return driver
class Programme_gzcw():
	
	def get_content2_gzcw(self,url,keyword):
		"""
		打开网址
		搜索关键词
		"""
		driver = webdriver.PhantomJS()
		driver.set_window_size(800,600)

		driver.get(url)
		driver.find_element_by_id("searchvalue").clear()
		driver.find_element_by_id("searchvalue").send_keys(keyword)
		driver.find_element_by_id("img1").click()

		return driver


	def get_web_gzcw(self,info):
		"""
		获取项目网址
		实现翻页
		"""
		weblist=[]
		corrt_weblist = []

		i = 2
		soup = BeautifulSoup(info.page_source)

		website = soup.find_all(href=re.compile("layout3"))

		for web in website:
			gotoweb = web['href']

			weblist.append(gotoweb)
		while i < len(weblist):
			corrt_weblist.append(weblist[i])

			i += 1

		return corrt_weblist

	def get_title_gzcw(self,soup):
		"""
		获取项目标题
		"""
		title_all = soup.find('h1', style=re.compile("text"))
		try:
			title = title_all.get_text()
		except:
			title = None

		return title


	def get_beginningtime_gzcw(self,list_table):
		"""
		获取公布时间
		"""
		i = 0
		j = 0
		site = 0
		for message in list_table:
			try:
				message.index(u"发布时")
				site = i
			except:
				i +=1
		if site !=0:
			if len(list_table[site]) < 4:
				return list_table[site +2]
			else:
				return list_table[site + 1]
		else:
			for message2 in list_table:
				try:
					message2.index(u"交易中心位置图")
					site = j
				except:
					j +=1
			if site !=0:
				return list_table[site-1]
			else:
				return None


	def get_agentcompany_gzcw(self,list_table):
		return "测试，返回代理机构"
	# 	i = 0
	# 	site = 0
	# 	for message in list_table:
	# 		try:
	# 			message.index(u"采购代理机构")
	# 			site = i
	# 		except:
	# 			i +=1
	# 	# if site !=0:
	# 	# 	return list_table[site]
	# 	# else:
	# 	# 	return None
	# 	return i


	def get_buyer_gzcw(self,list_table):
		"""
		获取采购人
		"""
		i = 0
		site = 0
		for message in list_table:
			try:
				message.index(u"采购人名称")
				site = i
			except:
				i +=1
		if site !=0:
			buyer = list_table[site]
			return buyer[6:]
		else:
			return None

	def get_showtime_gzcw(self,list_table):
		"""
		获取开标时间
		"""
		i = 0
		site = 0
		j = 0
		for message in list_table:
			try:
				message.index(u"和开标时间")
				site = i
			except:
				i +=1

		if site !=0:
			if len(list_table[site+1]) < 2:
				return list_table[site +2]
			else:
				return list_table[site+1]
		else:
			for message2 in list_table:
				try:
					message2.index(u"及开标时间")
					site = j
				except:
					j +=1
			if site !=0:
				if len(list_table[site+1]) <2:
					return list_table[site+2]
				else:
					return list_table[site+1]
			else:
				return None

	def get_account_gzcw(self,list_table):
		"""
		获取项目预算
		"""
		i = 0
		site = 0
		for message in list_table:
			try:
				message.index(u"预算")
				site = i
			except:
				i +=1

		if site !=0:
			if len(list_table[site+1]) <2:
				return list_table[site+2]
			else:
				return list_table[site+1]
		else:
			return None

	def get_money_gzcw(self,list_table):
		return "测试，返回中标金额"

	def get_programme_destinate_gzcw(self,list_table):
		"""
		获取采购内容
		"""
		i = 0
		site = 0
		for message in list_table:
			try:
				message.index(u"采购内容：")
				site = i
			except:
				i +=1

		if site !=0:
			return list_table[site+1]
		else:
			return None

	def get_detail_gzcw(self,WBall,filename,state1,state2,state3,state4,state5,state6,state7,state8):
		"""
		总调用方法
		写入EXCEL
		"""
		
		wbk = xlwt.Workbook()
		sheet = wbk.add_sheet('sheet 1',cell_overwrite_ok=True)

		sheet.write(0,0,"招标公告日期")
		sheet.write(0,1,"链接")
		sheet.write(0,2,"地区")
		sheet.write(0,3,"招标机构")
		sheet.write(0,4,"采购单位")
		sheet.write(0,5,"项目名称")
		sheet.write(0,6,"采购内容")
		sheet.write(0,7,"开标日期")
		sheet.write(0,8,"中标公告时间")
		sheet.write(0,9,"中标公司")
		sheet.write(0,10,"总金额")
		sheet.write(0,11,"中标金额")
		sheet.write(0,12,"预算（元）")
		sheet.write(0,13,"中标公告链接")

		excel_count = 1

		for web in WBall:
			html = urllib.request.urlopen('http://www.gzggzy.cn' + web)
			content = html.read()
			html.close()
			"""打开项目网址"""
			message = []

			soup = BeautifulSoup(content)

			message_all = soup.find_all('div', class_="xx-text")
			for message_part in message_all:
				for message_unit in message_part.stripped_strings:
					message.append(message_unit)

			# print(get_title(soup),get_beginningtime(message),get_buyer(message),get_showtime(message),get_account(message),get_programme_destinate(message))

			if state1 is True:
				sheet.write(excel_count,5,self.get_title_gzcw(soup))
			else:
				None
			if state2 is True:	
				sheet.write(excel_count,12,self.get_account_gzcw(soup))
			else:
				None
			if state3 is True:
				sheet.write(excel_count,0,self.get_beginningtime_gzcw(soup))
			else:
				None
			if state4 is True:	
				sheet.write(excel_count,3,self.get_agentcompany_gzcw(soup))
			else:
				None
			if state5 is True:
				sheet.write(excel_count,1,"http://www.gdgpo.gov.cn" + web)
			else:
				None
			if state6 is True:
				sheet.write(excel_count,11,self.get_money_gzcw(soup))
			else:
				None
			if state7 is True:
				sheet.write(excel_count,7,self.get_showtime_gzcw(soup))
			else:
				None
			if state8 is True:
				sheet.write(excel_count,6,self.get_buyer_gzcw(soup))
			else:
				None

			excel_count +=1

		wbk.save(filename)

	# info = get_content('http://www.gzggzy.cn')
	# info = get_content2('http://www.gzggzy.cn/cms/wz/view/index/layout2/zfcglist.jsp?siteId=1&channelId=456')
	# WBall = get_web(info)
	# print(get_detail(WBall))


