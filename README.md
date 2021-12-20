# robosys_ros


# 2021年ロボットシステム学課題２


# プログラム


ROSの機能を用いて計算を行うプログラム


1から順に＋1されるプログラムに計24倍された数を24で割るプログラム


ex.)3 * 2 * 3 * 4 / 24 = 3 ＜ー　これを出力


______


#動作環境


| OS | ROS |  
|:---|----:|
| Ubuntu20.04 | ROS1-noetic |


# ノード連携


 - count.py 


   ー＞１から順に＋１されるノード


 - twice.py


  ー＞count.pyからSubscribeした数を2倍してPublishする


 - third.py


  ー＞twice.pyからSubscribeした数を3倍してPublishする


 - quadruple.py


  ー＞third.pyからSubscribeした数を4倍してPublishする


 - devid.py


  ー＞quadruple.pyからSubscribeした数を24で割算してPublishする


______


#実行方法


1. roscore

   (ROSを立ち上げる)


1. 各ノードを立ち上げる
 

  1.rosrun mypkg count.py


  1.rosrun mypkg twice.py

 
  1.rosrun mypkg third.py


  1.rosrun mypkg quadruple.py


  1.rosrun mypkg devid.py


＊また、今後一回のrosrunで各ノードが立ち上げられるroslaunchファイルを作成予定

1.各ノードが正常に立ち上がっているか確認


 - rostopic list


  この際に立ち上げたノード名がすべて表示されていれば正常に立ち上がっている


1.出力


 - rostopic echo /devid


____


#実行結果


以下のリンクからyoutubeの動画がご覧出来ます


