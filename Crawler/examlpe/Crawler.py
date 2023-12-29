import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from DelKeyWord import remove_keyword, remove_multi
 
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'
}
 
webdriver = webdriver.Chrome()
 
# 首先我们写好抓取网页的函数
def get_html(url):
    try:
        r = requests.get(
            url,
            headers=headers
        )
        r.raise_for_status()
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "
 
 
def get_content(url, cli_type, cli_class):
    try:
        comments = []
        webdriver.get(url)
        html = webdriver.page_source
        soup = BeautifulSoup(html, 'lxml')
        # liTags = soup.find_all('div', attrs={'class': 'd_post_content j_d_post_content'})
        liTags = soup.find_all('div', attrs={cli_type: cli_class})
    except:
        return " ERROR "
 
    # 通过循环找到每个帖子里的我们需要的信息：
    for li in liTags:
        comment = {}
        if li.text.strip():
            comment['content'] = li.text.strip()+"\n"
        comments.append(comment)
    return comments
 
 
def Out2File(dicts):
    with open(file_name, 'a+', encoding='utf-8') as f:
        for comment in dicts:
            if (not comment) or (('点击展开，查看完整图片' or '该楼层疑似违规已被系统折叠，隐藏此楼查看此楼') in dicts):
                continue
            f.write('{}'.format(comment['content']))
        print('当前页面爬取完成')
 
 
def main(base_url, deep, cli_type, cli_class):
    # 将所有需要爬去的url存入列表
    if deep:
        url_list = []
        for i in range(1, int(deep)):
           url_list.append(base_url + '?pn=' + str(i))
        print('所有的网页已经下载到本地！ 开始筛选信息...')
    else:
        url_list = [base_url]
        print('所有的网页已经下载到本地！ 开始筛选信息...')
    # 循环写入所有的数据
    for url in url_list:
        content = get_content(url, cli_type, cli_class)
        Out2File(content)
    print('所有的信息都已经保存完毕！正在进行数据集规范化...')
 
 
if __name__ == '__main__':
    while True:
        base_url = input('请输入需要爬取的贴吧链接：')
        deep = input('请输入需要爬取的页数：（输入0则仅爬取单页）\n目前多页数爬取仅支持百度贴吧！')
        cli_type = input('请输入需要爬取的类（class、id等）：\n若填0则爬取页面所有内容.')
        cli_class = input('请输入需要爬取的标识（若无填0）：')
        r_m = input('是否需要删除重复行（需要填1，反之填0）：')
        r_k = input('填写需要删除的关键字（没有请填0）：')
        idx = 1
        while True:
            if not os.path.exists('Output_' + str(idx) + '.txt'):
                file_name = 'Output_' + str(idx) + '.txt'
                break
            idx += 1
        main(base_url, deep, cli_type, cli_class)
        if r_m:
            remove_multi(file_name)
        if not r_k:
            remove_keyword(file_name, r_k)
        print('已将输出规范为数据集格式.')
        if not int(input('是否继续爬取？（输入0结束）')):
            break
