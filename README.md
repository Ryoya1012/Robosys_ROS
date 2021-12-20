# 2021年ロボットシステム学課題２


## プログラム


ROSの機能を用いて計算を行うプログラム


1から順に＋1されるプログラムに計24倍された数を24で割るプログラム


ex.)3 * 2 * 3 * 4 / 24 = 3 


______


## 動作環境


|      OS     |     ROS     |  
|:------------|------------:|
| Ubuntu20.04 | ROS1-noetic |


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


1. roscore

     (ROSを立ち上げる)


1. 各ノードを立ち上げる
 

    1.rosrun mypkg count.py


    2.rosrun mypkg twice.py

 
    3.rosrun mypkg third.py


    4.rosrun mypkg quadruple.py


    5.rosrun mypkg devid.py


＊また、今後一回のrosrunで各ノードが立ち上げられるroslaunchファイルを作成予定

 2. 各ノードが正常に立ち上がっているか確認


   - rostopic list


  この際に立ち上げたノード名がすべて表示されていれば正常に立ち上がっている


 3. 出力


   - rostopic echo /devid


____


#実行結果


以下のリンクからyoutubeの動画がご覧出来ます


