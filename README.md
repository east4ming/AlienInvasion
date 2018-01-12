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

#### 创建设置类

每次给游戏添加新功能时, 通常也将引入一些新设置. 
下面来编写一个名为`settings`的模块, 其中包含一个名为`Settings`的类, 用于将所有设置存储在一个地方, 以免在代码中到处添加设置. 这样, 我们就能传递一个设置对象, 而不是众多不同的设置. 
另外, 这让函数调用更简单, 且在项目增大时修改游戏的外观更容易: 
要修改游戏, 只需修改`settings.py`的一些值, 而无需查找散布在文件中的不同设置.

在主程序文件中, 导入`Settings`类, 调用`pygame.init()`, 再创建一个`Settings`实例, 并将其存储在变量`ai_settings`中.

#### 添加飞船图像

为了在屏幕上绘制飞船, 我们将加载一幅图像, 再使用Pygame方法`blit()`绘制.
选择素材时, 务必注意**许可**.

> http://pixabay.com/

在游戏中几乎可以使用任何类型的图像文件, 但使用位图(.bmp)文件最为简单, 因为Pygame默认加载位图.
选择图像时, 特别注意**背景色**. 尽可能选择**背景透明**的图像.
在主项目文件夹中创建一个文件夹*images*, 用来保存图像文件.

#### 创建 Ship 类

创建一个`ship`模块, 其中包含`Ship`类, 负责管理飞船的大部分行为.

加载图像后, 我们使用`get_rect()`获取相应surface的属性rect. Pygame之所以效率高, 一个原因是它让你能够像处理矩形(rect对象)一样处理游戏元素, 即便他们的形状并非矩形.
像矩形一样处理游戏元素之所以高效, 是因为矩形是简单的几何形状. 而玩家不会注意到我们处理的不是游戏元素的实际形状.

处理rect对象, 可使用矩形四角和中心的x和y坐标. 可通过设置这些值来指定矩形位置.

要将游戏元素居中, 可设置相应rect对象的属性center/centerx/centery. 要让游戏元素与屏幕边缘对齐, 可使用属性top/bottom/left/right; 要调整游戏元素的水平或垂直位置, 可使用属性x和y, 分别对应矩形左上角的x和y坐标.

> 在pygame中, 原点(0, 0)位于屏幕左上角, 向右下方移动时, 坐标值将增大. 在1200×800的屏幕上, 原点位于左上角, 右下角为(1200, 800)

#### 在屏幕上绘制飞船


