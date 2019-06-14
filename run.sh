export VENV=/path/to/venv

export PYTHONUNBUFFERED=1
export QT_QPA_PLATFORM_PLUGIN_PATH=`echo $VENV`/lib/python3.6/site-packages/PyQt5/Qt/plugins/platforms
`echo $VENV`/bin/python `pwd`/GUI/main.py
