# BankCard
## 环境
本项目的开发和测试环境为：
**系统：**
- Ubuntu 16.04
- Ubuntu 18.04
- Linux Mint 19.1

**Python：**
- Python 3.6

>在以上系统环境中可以正常运行本项目软件，若在其他系统环境下配置运行本项目，请自行解决依赖以及环境配置问题。

## 安装
### 安装依赖
```bash
pip install pyqt5 
pip install pyqt5-tools
pip install qtpy
pip install Pillow
```

## 配置

项目启动脚本`run.sh`内容如下：

```bash
export VENV=/path/to

export PYTHONUNBUFFERED=1
export QT_QPA_PLATFORM_PLUGIN_PATH=`echo $VENV`/lib/python3.6/site-packages/PyQt5/Qt/plugins/platforms
`echo $VENV`/bin/python `pwd`/GUI/main.py
```

修改`run.sh`中第一行，将`/path/to`修改为测试机上的python虚拟环境的绝对路径，并保存。

## 运行

使用项目压缩包中提供的`run.sh`文件来启动本软件：
```bash
# 切换到项目目录下
cd Bank_Card_OCR
# 使用前先为 run.sh 添加可执行权限
chmod +x run.sh
./run.sh
```

