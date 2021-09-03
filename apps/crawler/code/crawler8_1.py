import requests

api_url = f'http://anipython.com/crawler/8/api'

response = requests.get(api_url)
data_dict = response.json()
"""
输出: 
{
    'data': [
        {
            'desc': '如果只选一门编程语言来学习, 就学 Python 吧',
            'id': 1,
            'title': 'Python入门视频',
            'url': 'https://study.163.com/course/introduction/1211262812.htm?share=2&shareId=480000002210461'
        },
        {
            'desc': '用python 的pandas 库进行数据分析, 来操作excel表格, 实现办公自动化。',
            'id': 2,
            'title': 'Python Pandas Excel 办公自动化',
            'url': 'https://study.163.com/course/introduction/1209966922.htm?share=2&shareId=480000002210461'
        },
        {
            'desc': '学习使用 flask 进行 python web 开发',
            'id': 3,
            'title': 'Python Web 接单实战',
            'url': 'https://study.163.com/course/introduction/1211591811.htm?share=2&shareId=480000002210461'
        },
        ...
    ]
}
"""