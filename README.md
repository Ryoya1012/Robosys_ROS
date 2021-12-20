# robosys_ros


# 2021年ロボットシステム学課題２


# プログラム


ROSの機能を用いて計算を行うプログラム


1から順に＋1されるプログラムに計24倍された数を24で割るプログラム


ex.)3 * 2 * 3 * 4 / 24 = 3 ＜ー　これを出力


______

# ノード連携


 # count.py 


   ー＞１から順に＋１されるノード


 # twice.py


  ー＞count.pyからSubscribeした数を2倍してPublishする


 # third.py


  ー＞twice.pyからSubscribeした数を3倍してPublishする


 # quadruple.py


  ー＞third.pyからSubscribeした数を4倍してPublishする


 # devid.py


  ー＞quadruple.pyからSubscribeした数を24で割算してPublishする


______


#実行方法




