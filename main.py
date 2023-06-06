import time
import cv2
import pyautogui

def get_xy(img_model_path,img_ss):

    # 将屏幕截图保存
    pyautogui.screenshot().save("screenshot.png")
    # 载入截图
    img = cv2.imread("screenshot.png")
    # 图像模板
    img_terminal = cv2.imread(img_ss)
    # 读取模板的宽度和高度
    height, width, channel= img_terminal.shape
    # 进行模板匹配
    result = cv2.matchTemplate(img, img_terminal,cv2.TM_SQDIFF_NORMED)
    # 解析出匹配区域的左上角坐标
    upper_left = cv2.minMaxLoc(result)[2]
    # 计算匹配区域右下角的坐标
    lower_right = (upper_left[0] + width, upper_left[1] + height)
    # 计算中心区域的坐标并且返回
    avg = (int((upper_left[0] + lower_right[0])/2), int((upper_left[1] + lower_right[1])/2))
    return avg


def auto_click(var_avg):

    pyautogui.click(var_avg[0], var_avg[1], button='left')
    time.sleep(1)
#
def routine(img_model_path,name,img_ss):
    avg = get_xy(img_model_path,img_ss)
    print(f'正在点击{name}')
    auto_click(avg)


#
#
# routine("a1.bmp",'测试')
# routine(img_name,'测试2')

routine('','测试',"a2.bmp")





