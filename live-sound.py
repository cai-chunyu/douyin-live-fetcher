import json
import requests
from pydub import AudioSegment

def merge_audio_files(file1, file2, output_file):
    # 读取两个音频文件
    audio1 = AudioSegment.from_file(file1)
    audio2 = AudioSegment.from_file(file2)
    # 拼接两个音频文件
    combined = audio1 + audio2
    # 导出合并后的音频文件
    combined.export(output_file, format="wav")

def chattts(text):
    res = requests.post('http://127.0.0.1:9966/tts', data={
        "text": text,
        "prompt": "",
        "voice": "4099",
        "temperature": 0.3,
        "top_p": 0.7,
        "top_k": 20,
        "skip_refine": 0,
        "custom_voice": 0
    })
    return res.json()

def read_and_process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # 过滤掉空行
    lines = [line.strip() for line in lines if line.strip()]
    # 每1行作为一个片段
    for line in lines:
        # 在每个句号后面添加换行符 
        formatted_text = line.replace('。', '。\n')
        # 将文本按句号分割成句子
        sentences = formatted_text.split('。\n')
        # 计算分割点，确保前一半和后一半都尽量平均
        mid_point = (len(sentences) + 1) // 2
        # 前一半文本
        first_half = '。\n'.join(sentences[:mid_point]) + ('。' if len(sentences) > mid_point else '')
        # 后一半文本
        second_half = '。\n'.join(sentences[mid_point:]) + '。'
        # 分别调用 chattts 函数
        response_first = chattts(first_half)
        response_second = chattts(second_half)
        # 解析返回的json并打印filename
        if response_first['code'] == 0 and response_second['code'] == 0:
            file1 = response_first['audio_files'][0]['filename']
            file2 = response_second['audio_files'][0]['filename']
            print('file1:' + file1)
            print('file2:' + file2)
            # 合并两个音频文件
            # output_file = 'D:/无人直播/地图/直播音频新/' + file1.replace('D:/BaiduNetdiskDownload/ChatTTS-ui-0.95/static/wavs/', '').replace('.wav', '_combined.wav')
            # merge_audio_files(file1, file2, output_file)
            # print(output_file)

# 调用函数处理文件
read_and_process_file('live-content2.txt')
