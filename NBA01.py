'''
#爬虫的一般步骤:
1.确定url地址（网页分析） -- 完成一半
2.发送网络请求requests（js，html，css）
3.数据解析（筛选数据）
4.保存数据（本地文件/数据库）
'''

import requests
import parsel
import pandas as pd

a = True    # 对应to_csv中的header参数,第一遍爬取之后设成false, 不需要再加入header了

for i in range(1,4):   #通过查看pagelist得知一共有3页数据，唯一的变化即url末尾的1，2，3
    print("爬取第" + str(i) + "页的数据:")
    
    col = ['Rank', 'Player', 'Team', 'Score', 'shots_made', 'shooting_percentage', 'threes_made',  #标题
        'threepoint_percentage', 'freeshows_made', 'freeshow_rate', 'games', 'playing_time']
    dt = pd.DataFrame(columns=col)

# 1.确定url地址（网页分析）（静态网页/动态网页）, 每次加一
    url = 'https://nba.hupu.com/stats/players/pts/' + str(i)

    # 2.发送网络需求
    response = requests.get(url=url)
    html_data = response.text
    # print(html_data)

    # 3.数据解析
    # 3.1 转换数据类型
    selector = parsel.Selector(html_data)
    trs = selector.xpath('//tbody//tr[not(@class="color_font1 bg_a")]')

    dic = {}

    for tr in trs:
        rank = tr.xpath('./td[1]/text()').get()
        dic['Rank'] = rank
        player = tr.xpath('./td[2]/a/text()').get()  # 球员
        dic['Player'] = player
        team = tr.xpath('./td[3]/a/text()').get()  # 球队
        dic['Team'] = team
        score = tr.xpath('./td[4]/text()').get()  # 得分
        dic['Score'] = score
        shots_made = tr.xpath('./td[5]/text()').get()  # 命中-出手
        dic['shots_made'] = shots_made
        shooting_percentage = tr.xpath('./td[6]/text()').get()  # 命中率
        dic['shooting_percentage'] = shooting_percentage
        threes_made = tr.xpath('./td[7]/text()').get()  # 命中-三分
        dic['threes_made'] = threes_made
        threepoint_percentage = tr.xpath('./td[8]/text()').get()  # 三分命中率
        dic['threepoint_percentage'] = threepoint_percentage
        freeshows_made = tr.xpath('./td[9]/text()').get()  # 命中-罚球
        dic['freeshows_made'] = freeshows_made
        freeshow_rate = tr.xpath('./td[10]/text()').get()  # 罚球命中率
        dic['freeshow_rate'] = freeshow_rate
        games = tr.xpath('./td[11]/text()').get()  # 场次
        dic['games'] = games
        playing_time = tr.xpath('./td[12]/text()').get()  # 上场时间
        dic['playing_time'] = playing_time
        dt = dt.append(dic, ignore_index=True)

    print(dt)
    print()
    dt.to_csv("NBA_Data.csv", mode='a', index=0,encoding='utf_8_sig',header=a)
    a = False   

print("爬取结束,已生成csv文件")  