#coding = gbk
'''
#爬虫的一般步骤:
1.确定url地址（网页分析） -- 完成一半
2.发送网络请求requests（js，html，css）
3.数据解析（筛选数据）
4.保存数据（本地文件/数据库）
'''

import requests
import parsel
import csv
import os
import pandas as pd

# 1.确定url地址（网页分析）（静态网页/动态网页）
url = 'https://nba.hupu.com/stats/players'

# 2.发送网络需求
response = requests.get(url=url)
html_data = response.text
# print(html_data)

# 3.数据解析
# 3.1 转换数据类型
selector = parsel.Selector(html_data)
trs = selector.xpath('//tbody//tr[not(@class="color_font1 bg_a")]')

col = ['Rank', 'Player', 'Team', 'Score', 'shots_made', 'shooting_percentage', 'threes_made',
    'threepoint_percentage', 'freeshows_made', 'freeshow_rate', 'games', 'playing_time']
dt = pd.DataFrame(columns=col)

data_list = []
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
    # print(rank, player, team, score, shots_made, shooting_percentage, threes_made,
    #     threepoint_percentage, freeshows_made, freeshow_rate, games, playing_time)
    dt = dt.append(dic, ignore_index=True)

dt.to_csv("NBA_Data.csv", index=0)


#     data_dict = {
#                 '排名': rank, '球员': player, '球队': team, '得分': score,
#                 '命中-出手': shots_made, '命中率': shooting_percentage, '命中-三分': threes_made, '三分命中率': threepoint_percentage,
#                 '命中-罚球': freeshows_made, '罚球命中率': freeshow_rate, '场次': games, '上场时间': playing_time}
