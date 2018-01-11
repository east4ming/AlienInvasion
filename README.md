# AlienInvasion
A Python Game Project. To study how to use python doing a game project.

开发一个游戏. 使用Python的一组功能强大而有趣的模块, 可用于管理图形/动画/声音, 让你能够更轻松地开发复杂的游戏. 

## 武装飞船

在本章, 创建一艘能根据用户输入而左右移动和射击的飞船. 
在本章, 还学习管理包含多个文件的项目. 会重构很多代码, 以提高代码的效率, 并管理文件的内容, 以确保项目组织有序.

### 规划项目

先做好规划, 确保不偏离轨道, 从而提高项目成功的可能性.
编写关于**外星人入侵**的描述, 让你清楚地知道该如何动手开发它.

> 游戏简介:
> 在游戏**外星人入侵**中, 玩家控制一艘最初出现在屏幕底部中央的飞船. 玩家可以使用箭头键左右移动飞船, 还可以使用空格键进行射击. 游戏开始时, 一群外星人出现在天空中, 他们在屏幕中向下移动. 玩家的任务时射杀这些外星人. 玩家将所有外星人都消灭干净后, 将出现一群新的外星人, 他们移动的速度更快. 只要有外星人撞到了玩家的飞船或到达了屏幕底部, 玩家就损失一艘飞船. 玩家损失三艘飞船后, 游戏结束.

### 安装 Pygame

### 开始游戏项目

首先创建一个空的Pygame窗口, 供后面用来绘制游戏元素, 如飞船和外星人.
我们还将让这个游戏响应用户输入, 设置背景色以及加载飞船图像.

#### 创建Pygame窗口以及响应用户输入

> 详细解释见`alien_invasion.py`的`run_game()`函数.
#### 设置背景色

