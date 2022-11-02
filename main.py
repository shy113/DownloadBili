# *-* encoding:utf8 *_*
# Author       : GZH
# Date         : 2022年11月01日
# Description  : 下载哔哩哔哩视频

# _*_ coding:utf-8 _*_
import time
import win32con, win32gui, pyautogui, pyperclip
from bs4 import BeautifulSoup
from win32api import GetAsyncKeyState

# 退出键F2
switch_exit = win32con.VK_F2


# 返回按键状态
def key_pressed(key):
    return GetAsyncKeyState(key) & 1 == 1


# 获取窗口左上顶点的坐标
def getHwnd_lt(title):
    hwnd = win32gui.FindWindow(None, title)
    l, t, r, b = win32gui.GetWindowRect(hwnd)  # 返回左上顶点 和 右下顶点的 坐标
    if (win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) & win32con.WS_CAPTION):  # 窗口具有标题栏（包含 WS_BODER)
        l += 8
        t += 30
    return l, t


# 获得各个控件的坐标
def getwidgetXY():
    left, top = getHwnd_lt('哔哩下载姬')
    # print(left, top)
    # screenWidth, screenHeight = pyautogui.size()  # 获取屏幕的尺寸
    # mouse_x, mouse_y = pyautogui.position()  # 返回鼠标的坐标
    # print(f'mousex  {mouse_x} mousey  {mouse_y}')
    inputbox_x, inputbox_y = left + 301, top + 34  # 输入框所在位置
    checkallBtn_x, checkallBtn_y = left + 22, top + 687  # 全选框所在位置
    downBtn_x, downBtn_y = left + 1171, top + 684  # 下载按钮所在位置
    dict = {
        'inputbox': {
            'x': inputbox_x,
            'y': inputbox_y
        },
        'checkallBtn': {
            'x': checkallBtn_x,
            'y': checkallBtn_y
        },
        'downBtn': {
            'x': downBtn_x,
            'y': downBtn_y
        }
    }
    return dict


# 从html中获取下载链接
def get_download_href(filename):
    hreflist = []
    with open(filename, 'r', encoding='UTF-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")
    lis = soup.find_all('li', class_='list-item')
    for li in lis:
        href = 'https:' + li.find('a').get('href')
        hreflist.append(href)
    return hreflist


# 逻辑
def main(filename):
    # 倒计时
    print('请回到哔哩哔哩下载姬')
    for i in range(6, 0, -1):
        if (key_pressed(switch_exit)):
            return
        print("\r倒计时{}秒！\n".format(i), end="")
        time.sleep(1)
    # link_list = []  # 存放链接的列表
    # with open(f'{filename}', 'r') as f:
    #     for line in f.readlines():
    #         link_list.append(line.strip())
    #         # print(line.strip())  # 把末尾的'\n'删掉
    link_list = get_download_href(filename)
    i = 0
    for link in link_list:
        if (key_pressed(switch_exit)):
            return
        # 拿到输入框 全选按钮 下载按钮的坐标
        dict = getwidgetXY()
        if i == 0:
            # 2.粘贴链接
            pyperclip.copy(link)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(['enter'], 0.3)  # 间隔0.3
            time.sleep(4)

            # 3.按下全选键
            pyautogui.click(dict['checkallBtn']['x'], dict['checkallBtn']['y'], duration=0.3)
            # time.sleep(0.3)
            # 4.按下下载键
            pyautogui.click(dict['downBtn']['x'], dict['downBtn']['y'], duration=0.3)
            # time.sleep(0.3)
        else:
            # 1.清空文本输入框
            pyautogui.click(dict['inputbox']['x'], dict['inputbox']['y'], duration=0.3)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press(['space'], interval=0.1)

            # 2.粘贴链接
            pyperclip.copy(link)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(['enter'], 0.3)  # 间隔0.3
            time.sleep(4)

            # 3.按下全选键
            pyautogui.click(dict['checkallBtn']['x'], dict['checkallBtn']['y'], duration=0.3)
            # time.sleep(0.5)
            # 4.按下下载键
            pyautogui.click(dict['downBtn']['x'], dict['downBtn']['y'], duration=0.3)
            # time.sleep(0.5)
        i += 1  # 让i不等于0

    print('下载完成')


if __name__ == '__main__':
    main('index.html')

# '''
# 1.鼠标移动到输入框 单机左键
# 2.Ctral + A 全选 输入框内容
# 3.按'space'(空格)删除
# 4.Ctrl V粘贴新链接
# 5.按Enter
# 6. 等待 3秒后 鼠标移动到全选框 单机左键
# 7. 等待一秒后 鼠标移动到 '下载选中项' 单机左键  pyautogui.click(sizex/2,sizey/2, duration=0.5)
# '''

# while True:
#     left, top = getHwnd_lt('哔哩下载姬')
#     print(left, top)
#     screenWidth, screenHeight = pyautogui.size()  # 获取屏幕的尺寸
#     mouse_x, mouse_y = pyautogui.position()  # 返回鼠标的坐标
#
#     print(f'mousex  {mouse_x} mousey  {mouse_y}')
#     time.sleep(0.1)

# inputbox_x, inputbox_y = left + 301, top + 34  # 输入框所在位置
# checkallBtn_x, checkallBtn_y = left + 22, top + 687  # 全选框所在位置
# downBtn_x, downBtn_y = left + 1171, top + 684  # 下载按钮所在位置
#
# dict = {
#     'inputbox': {
#         'x': inputbox_x,
#         'y': inputbox_y
#     },
#     'checkallBtn': {
#         'x': checkallBtn_x,
#         'y': checkallBtn_y
#     },
#     'downBtn': {
#         'x': downBtn_x,
#         'y': downBtn_y
#     }
# }
