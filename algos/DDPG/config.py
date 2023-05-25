#!/usr/bin/env python
# coding=utf-8
'''
Author: JiangJi
Email: johnjim0816@gmail.com
Date: 2023-02-21 20:32:11
LastEditor: JiangJi
LastEditTime: 2023-05-25 23:39:27
Discription: 
'''
import numpy as np
class AlgoConfig:
    def __init__(self):
        self.gamma = 0.99  # 贴现因子，值越大，表示未来的收益占更大的比重
        self.critic_lr = 1e-3  # critic 模型的学习率
        self.actor_lr = 1e-4  # actor 模型的学习率
        self.buffer_size = 8000  # 经验回放池的大小
        self.batch_size = 128  # 训练 actor 及 critic 模型的 batch 大小
        self.tau = 0.001  # 软更新参数，值越小，表示在更新目标网络参数时，参数变化越小
        self.critic_hidden_dim = 256  # critic 网络的隐含层数
        self.actor_hidden_dim = 256  # actor 网络的隐含参数
        self.value_min = -np.inf  # clip min critic value
        self.value_max = np.inf  # clip max critic value