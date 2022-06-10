# -*- coding: utf-8 -*-

import time


def generate(
    generator,
    text: str,
    max_len: int = 512,
    nums: int = 3,
    mode: str = "topp",
    step_callback=None,
):
    start = time.time()
    result = generator.writer(
        [text.replace("\n", "氼")],  # 文本数据就是上面的data
        nums=nums,  # 一个开头要生成几个文本
        k=0.8 if mode=='topp' else 10,  # 搜索窗口
        batch_size=32,
        max_len=max_len,  # 最大长度
        iter_data_num=400,  # 一次处理多少个开头
        mode=mode,  # 别动
        iter_max_num=0,
        step_callback=step_callback,
    )  # 检查重复解码的句子的次数，越大就越慢同时重复句子越少)
    outputs = [result[i].replace("氼", "\n") for i in range(nums)]
    end = time.time()
    return outputs, end - start
