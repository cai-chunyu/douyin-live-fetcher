import logging
import sys
from config import LIVE_ROOM_URL
from src import dy_live
from src.utils.common import init_global
from src.utils.http_send import send_start


if __name__ == '__main__':
    # 日志配置
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.ERROR)
    print("记得修改config.py里面的直播地址啊，不然获取不到数据的！")
    # 初始化要做的事情：比如初始化全局变量
    init_global()
    # 推送直播点赞等数据
    send_start()
    # 在config.py配置中修改直播地址: LIVE_ROOM_URL
    url = LIVE_ROOM_URL
    args = sys.argv[1:]
    if len(args) > 0:
        url = 'https://live.douyin.com/' + args[0]
    dy_live.parseLiveRoomUrl(url)
