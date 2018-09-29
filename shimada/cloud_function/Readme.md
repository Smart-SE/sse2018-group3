## Google Cloud Function + RasPi
デモの操作手順
1. 以下コマンドでFlaskのアプリケーションを起動する
~~~
python demo/himawari_linebot.py
~~~

1. NGROKを起動
~~~
ngrok http 8000
~~~

1. NGROKのアドレスをCloudFunctionの環境変数に設定する
ブラウザから手動でやる