import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext

def crawl_and_display():
    url = entry.get()  # 从输入框获取用户输入的网址
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = soup.find_all('a')
    for link in links:
        output_area.insert(tk.END, link.get('href') + '\n')

# 创建主窗口
root = tk.Tk()
root.title('Simple Web Crawler')

# 创建输入框和按钮
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
entry = tk.Entry(root)
entry.pack()
crawl_button = tk.Button(root, text="Crawl", command=crawl_and_display)
crawl_button.pack()

# 创建文本域来显示爬取的链接
output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
output_area.pack()

# 运行主循环
root.mainloop()