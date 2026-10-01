# batube

添加 PATH 环境变量（推荐）

Win+R 打开运行框，输入 sysdm.cpl 回车

点击"高级" → "环境变量"

在"用户变量"中找到 Path，点"编辑"

点击"新建"，添加Scripts 目录：

   C:\Users\93450.DESKTOP-SA01561\AppData\Local\Python\pythoncore-3.14-64\Scripts
	
同时把 Python 主目录也加上：

   C:\Users\93450.DESKTOP-SA01561\AppData\Local\Python\pythoncore-3.14-64


寻找目录：

python -c "import sys; print(sys.executable)"

运行后，终端会输出一串路径，例如：

C:\Users\93450\AppData\Local\Python\pythoncore-3.14-64\python.exe

如何配置环境变量：

Python 主目录：将上面输出的路径中最后的 \python.exe 删掉。（即 C:\Users\93450\AppData\Local\Python\pythoncore-3.14-64）

Scripts 目录：在主目录后面加上 \Scripts。（即 C:\Users\93450\AppData\Local\Python\pythoncore-3.14-64\Scripts）



检查 pip 是否可用

python -m pip --version

自动修复

python -m ensurepip --upgrade

修复方法2

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py







安装 pytubefix

pip install pytubefix

更新 pytubefix
pip install --upgrade pytubefix


安装 ffmpeg

winget install ffmpeg

