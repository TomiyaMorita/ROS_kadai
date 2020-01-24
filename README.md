# ROS_kadai

ロボットシステム学2019の課題2 ROSを利用してLEDをブラウザから点灯させるプログラム

##　作成したプログラムについて

###　使用方法　

sudo apt install ros-kinetic-rosbridge-suite

chmod +x led_ros.py

chmod +x input_ros.py

chmod +x listener.py

cd catkin_ws/

catkin_make

roscore

rosrun mypkg led_ros.py

rosrun mypkg input_ros.py

###　操作について

rosrun mypkg input_ros.pyを実行し、以下のコマンドにより操作する

a : LED1点灯

b : LED1消灯

c : LED2点灯

d : LED2消灯

e : LED3点灯

f : LED3消灯

##　動画URL

###　作成したプログラムの実行結果の動画

https://youtu.be/jq4qKkAaTYM

