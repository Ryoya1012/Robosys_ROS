# 2021年ロボットシステム学課題２


## プログラム


ROSの機能を用いて計算を行うプログラム


1から順に＋1されるプログラムに計24倍された数を24で割るプログラム


ex.)3 * 2 * 3 * 4 / 24 = 3 


ROSのインストールは以下のURLから各自行ってください


[上田先生のレポジトリを参考](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop)

______


## 動作環境


| OS | ROS |  
|:----|------:|
| Ubuntu20.04 | ROS-noetic |


## ノード連携


 - count.py 


    １から順に＋１されるノード


 - twice.py

 
    count.pyからSubscribeした数を2倍してPublishする


 - third.py


    twice.pyからSubscribeした数を3倍してPublishする


 - quadruple.py


    third.pyからSubscribeした数を4倍してPublishする


 - devid.py


    quadruple.pyからSubscribeした数を24で割算してPublishする


______


## 実行方法


```
 $ roscore
```



     (ROSを立ち上げる)


1. 各ノードを立ち上げる
 

```
 $  rosrun mypkg count.py
```


```
 $  rosrun mypkg twice.py
```


``` 
 $  rosrun mypkg third.py
```


```
 $  rosrun mypkg quadruple.py
```


```
 $  rosrun mypkg devid.py
```



＊または、このレポジトリ内にlaunchfileを作成したため以下のように立ち上げることもできる


```
 $  roslaunch mypkg mypkg launch
```



 2. 各ノードが正常に立ち上がっているか確認


```
 $  rostopic list
```



  この際に立ち上げたノード名がすべて表示されていれば正常に立ち上がっている


 3. 出力


```
 $  rostopic echo /devid
```



____


## 実行結果


以下のリンクからyoutubeの動画がご覧出来ます

[YoutubeURL](https://youtu.be/Epd0Tx29t4s)
