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
> 在游戏**外星人入侵**中, 玩家控制一艘最初出现在屏幕底部中央的飞船. 玩家可以使用箭头键左右移动飞船, 还可以使用
空格键进行射击. 游戏开始时, 一群外星人出现在天空中, 他们在屏幕中向下移动. 玩家的任务时射杀这些外星人. 
玩家将所有外星人都消灭干净后, 将出现一群新的外星人, 他们移动的速度更快. 只要有外星人撞到了玩家的飞船或到达了屏幕底部, 
玩家就损失一艘飞船. 玩家损失三艘飞船后, 游戏结束.

### 安装 Pygame

### 开始游戏项目

首先创建一个空的Pygame窗口, 供后面用来绘制游戏元素, 如飞船和外星人.
我们还将让这个游戏响应用户输入, 设置背景色以及加载飞船图像.

#### 创建Pygame窗口以及响应用户输入

> 详细解释见`alien_invasion.py`的`run_game()`函数.
#### 设置背景色

#### 创建设置类

每次给游戏添加新功能时, 通常也将引入一些新设置. 
下面来编写一个名为`settings`的模块, 其中包含一个名为`Settings`的类, 用于将所有设置存储在一个地方, 以免在代码中
到处添加设置. 这样, 我们就能传递一个设置对象, 而不是众多不同的设置. 
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

加载图像后, 我们使用`get_rect()`获取相应surface的属性rect. Pygame之所以效率高, 一个原因是它让你能够像处理
矩形(rect对象)一样处理游戏元素, 即便他们的形状并非矩形.
像矩形一样处理游戏元素之所以高效, 是因为矩形是简单的几何形状. 而玩家不会注意到我们处理的不是游戏元素的实际形状.

处理rect对象, 可使用矩形四角和中心的x和y坐标. 可通过设置这些值来指定矩形位置.

要将游戏元素居中, 可设置相应rect对象的属性center/centerx/centery. 要让游戏元素与屏幕边缘对齐, 
可使用属性top/bottom/left/right; 要调整游戏元素的水平或垂直位置, 可使用属性x和y, 分别对应矩形左上角的x和y坐标.

> 在pygame中, 原点(0, 0)位于屏幕左上角, 向右下方移动时, 坐标值将增大. 在1200×800的屏幕上, 原点位于左上角, 
右下角为(1200, 800)

#### 在屏幕上绘制飞船

### 重构: 模块 game_functions

在大型项目中, 经常需要在添加新代码前重构既有代码. 重构旨在简化既有代码的结构, 使其更容易扩展.
在本节中, 创建一个名为`game_functions`的新模块, 它将存储大量让游戏**外星人入侵**运行的函数.
通过创建模块`game_functions`, 可避免`alien_invasion.py`太长, 并使其逻辑更容易理解.

#### `check_events()`

首先把管理事件的代码移到名为`check_events()`的函数中, 以简化`run_game()`并隔离事件管理循环.
通过隔离事件循环, 可将事件管理与游戏的其他方面(如更新屏幕)分离.

#### `update_screen()`

为进一步简化`run_game()`, 将屏幕更新的代码移到一个名为`update_screen()`的函数中.

这两个函数让while循环更简单, 并让后续开发更容易: 在模块`game_functions`而不是`run_game()`中完成大部分工作.

鉴于一开始只想使用一个文件, 因此没有立刻引入模块`game_functions`. 这让我们能了解实际的开发过程: 一开始将代码
编写得尽可能**简单**, 并在项目越来越**复杂**时进行重构.

### 驾驶飞船

能左右移动飞船. 
先专注于向右移动, 再使用同样的原理来控制向左移动.

#### 响应按键

每当用户按键时, 都将在Pygame中注册一个事件. 事件都是通过方法 `pygame.event.get()` 获取的. 因此再函数 
`check_events()`中, 我们需要指定要检查哪些类型的事件. 每次按键都被注册为一个 `KEYDOWN`事件.
检测到`KEYDOWN`事件时, 需要检查按下的是否是特定的键. 例如, 按下的时右箭头键, 增大飞船的`rect.centerx` 值, 将飞船向右移动:

> 见 `game_functions.check_events()`

在函数`check_events()`中包含形参ship, 因为玩家按向右箭头时, 需要将飞船向右移动.
现在的效果是, 每按一次右箭头, 飞船向右移动1像素. 这并非控制飞船的高效形式. 下面来进行改进, 允许持续移动.

#### 允许不断移动

玩家按住右箭头不放时, 我们希望飞船不断地向右移动, 直到玩家松开为止. 我们让游戏检测`pygame.KEYUP`事件, 以便玩家松开
右箭头时我们能够知道这一点; 然后, 我们将结合使用`KEYDOWN`和`KEYUP`事件, 以及一个名为`moving_right`的标志来实现持续移动.
飞船不动时, 标志`moving_right`将为`False`. 玩家按下右箭头时, 我们将这个标志设置为`True`; 而玩家松开时, 我们将这个
标志重新设置为`False`.
飞船的属性都由`Ship`类控制, 因此我们将给这个类添加一个名为`moving_right`的属性和一个名为`update()`的方法. 
方法`update()`检查标志`moving_right`的状态, 如果这个标志为`True`, 就调整飞船的位置. 每当需要调整飞船的位置时, 
我们都调用这个方法.

> 见修改后的`ship.py`

在方法`__init__()`中, 添加了属性`self.moving_right`, 并将其初始值设置为`False`.
添加方法`update()`, 它在前述标志为`True`时向右移动飞船.

下面来修改`check_events()`, 使其在玩家按下右箭头时将`moving_right`设置为`True`, 
并在玩家松开时将`moving_right`设置为`False`.

> 见修改后的`game_functions.py`

- 修改了游戏在玩家按下右箭头时响应的方式; 不直接调整飞船的位置, 而只是将`moving_right`设置为`True`.
- 添加了一个新的`elif`块, 用于响应`KEYUP`事件: 玩家松开右箭头, 我们将`moving_right`设置为`False`

最后, 修改`alien_invasion.py`中的`while`循环, 以便每次执行循环时都调用飞船的方法`update()`.
飞船的位置将在检测到键盘事件后(但在更新屏幕前)更新. 这样, 玩家输入时, 飞船的位置将更新, 从而确保使用更新后的位置将
飞船绘制到屏幕上.

#### 左右移动

> 见代码

#### 调整飞船的速度

当前, 每次执行while循环时, 飞船最多移动1像素, 但我们可以在Settings类中添加属性`ship_speed_factor`, 用于控制飞船的速度. 

> 具体见`settings.py`

通过将速度设置指定为小数值, 可在后面加快游戏的节奏时更细致地控制飞船的速度. 然而, rect的centerx等属性只能存储整数值, 
因此需要对Ship类做修改.

> 见`ship.py`

- 在`__init__()`的形参列表中加入`ai_settings`, 让飞船能够获取其速度设置
- 将形参`ai_settings`的值存储在一个属性中, 以便能够在`update()`中使用它.
- `rect`只能存储整数部分, 定义一个可存储小数的新属性`self.center`. 使用`float()`将`self.rect.centerx`的值转换为小数, 
并存储到`self.center`中
- `update()`调整飞船位置时, 将`self.center`的值+或-`ai_settings.ship_speed_factor`的值. 更新`self.center`后, 
再根据它来更新飞船位置`self.rect.centerx`. (`self.rect.centerx`只保存整数部分, 但是显示飞船看起来效果差不多.)
- 在`alien_invasion.py`中创建Ship实例时, 需要传入实参`ai_settings`
    > 见`alien_invasion.py`

这样, 有助于让飞船反应速度足够快, 还能随着游戏进行加快游戏节奏.

#### 限制飞船活动范围

当前, 如果玩家一直按住箭头, 飞船会移动到屏幕外面, 消失. 下面来修复该问题, 让飞船到达边缘后停止移动.

> 见`ship.py`

- 在修改`self.center`的值之前检查飞船位置.
- `self.rect.right`返回飞船外接矩形的右边缘x坐标, 如果小于`self.screen_rect.right`值, 说明飞船未触及屏幕右边缘.
- 左边缘同理, 左边缘x坐标为0.

#### 重构 `check_events()`

随着游戏开发的进行, 函数`check_events()`将越来越长, 我们将其部分代码放在2个函数中: 一个处理KEYDOWN事件, 
另一个处理KEYUP事件.

> 见`game_functions.py`

创建了2个新函数, 包含形参event和ship. 将函数`check_events`中相应代码替换成对这两个函数的调用. 这样, 函数`check_events()`
更简单, 代码结构更清晰.

### 回顾

当前, 有4个文件.

#### `alien_invasion.py`

主文件. 创建一系列整个游戏都要用到的对象:

- 存储在`ai_settings`中的设置
- 存储在`screen`中的主显示surface
- 飞船实例
- 游戏主循环
    - 调用`check_events()`
    - `ship.update()`
    - `update_screen()`

要玩游戏, 只需要运行文件`alien_invasion.py`. 其他文件(settings.py game_functions.py ship.py)包含的代码被直接或间接地
导入到这个文件中.

#### `settings.py`

包含`Settings`类, 该类只包含`__init__()`方法, 初始化控制游戏外观和飞船速度的属性.

#### `game_functions.py`

包含一系列函数, 游戏的大部分工作都由它们完成.

- `check_events()`检测相关事件, 如按键和松开, 并使用辅助函数`check_keydown_events()`和`check_keyup_events()`来处理事件. 
目前, 这些函数管理飞船的移动.
- `update_screen()`, 用于在每次执行主循环时重绘屏幕

#### `ship.py`

包含Ship类. 

- `__init__()`
- 管理飞船位置的方法`update()`
- 在屏幕上绘制飞船的方法`blitme()`
- 飞船图像存储在文件夹images下的ship.bmp中.

### 射击

添加射击功能 - 玩家按空格键发射子弹(小矩形), 子弹在屏幕中向上穿行, 抵达屏幕边缘后消失.

#### 添加子弹设置

更新`settings.py`, 在`__init__()`存储新类`Bullet`所需的值:

> 具体见`settings.py`

#### 创建`Bullet`类

> 具体见`bullet.py`

继承了模块`pygame.sprite`中的`Sprite`类. 通过使用精灵, 可将游戏中相关元素**编组**, 进而同时操作编组中的所有元素.

- 创建子弹实例, 需要`ai_settings` `screen` `ship`实例, 还调用`super()`来继承`Sprite`
- 创建子弹属性rect. 子弹并非基于图像, 因此必须使用`pygame.Rect()`类从空白开始创建矩形. 创建这个类的实例时, 必须提供矩形
左上角的x y 坐标, 还有矩形的高度和宽度. 
- 在(0, 0)处创建, 并移动到正确的位置. 子弹初始位置取决于飞船的当前位置. 子弹宽度和高度从`ai_settings`中获取.
- 将子弹centerx设置为飞船的`rect.centerx`. 子弹应从飞船顶部射出, 因此子弹的rect的top设置为飞船的rect的top属性.
- 将子弹的y坐标存储为小数值, 以便能微调子弹速度.
- 将子弹的颜色/速度存储在`self.color`和`self.speed_factor`中.

下面是`bullet.py`的第二部分 -- 方法`update()`和`draw_bullet()`.

- 方法`update()`管理子弹的位置. 子弹发射出去向上移动, y坐标不断减小.
    - 属性`speed_factor`能随着游戏进行或根据需要提高速度
- 调用`draw_bullet()`绘制子弹. 函数`draw.rect()`使用存储在`self.color`中的颜色填充表示子弹rect占据的屏幕部分.

#### 将子弹存储到编组中

玩家每次按空格键时都发射一枚子弹.
在`alien_invasion.py`中创建一个编组(group), 用于存储所有有效的子弹, 以便能够管理发射出去的所有子弹.
这个编组是`pygame.sprite.Group`类的一个实例; `pygame.sprite.Group`类类似于列表, 但提供了有助于开发游戏的额外功能.
在主循环中, 将使用这个编组在屏幕上绘制子弹, 以及更新每颗子弹的位置:

> 具体见`alien_invasion.py`

创建了一个Group实例, 并将其命名为bullets. 这个编组是在while循环外面创建的.

> 如果在循环内部创建这样的编组, 游戏运行时将创建数千个子弹编组, 导致游戏慢的像蜗牛.

将bullets传递给`check_events()`和`update_screen()`.

- 在`check_events()`中, 需要在玩家按空格键时处理bullets
- 在`update_screen()`中, 需要更新要绘制到屏幕上的bullets

对编组调用`update()`时, 编组将自动对其中的每个精灵调用`update()`, 因此代码行`bullets.update()`将为编组
bullets中的每颗子弹调用`bullet.update()`

#### 开火

在`game_functions.py`中, 需要修改`check_keydown_events()`, 以便在玩家按空格键时发射子弹. 
无需修改`check_keyup_events()`, 因为玩家松开空格键时啥也不会发生.
还需要修改`update_screen()`, 确保在调用`flip()`前在屏幕上重绘每颗子弹.

> 具体见`game_functions.py`

编组bullets传递给`check_keydown_events()`. 玩家按下空格键时, 创建一颗新子弹(一个名为new_bullet的Bullet实例), 
并使用方法`add()`将其加入到编组bullets中; 代码`bullets.add(new_bullet)`将子弹存储到编组bullets中.

在`update_screen()`中, 方法`bullets.sprites()`返回一个列表, 包含编组bullets中的所有精灵. 为在屏幕上绘制发射的
所有子弹, 遍历编组bullets中的精灵, 并对每个精灵都调用`draw_bullet()`.
