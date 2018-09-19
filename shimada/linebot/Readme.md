## Ngrokを利用した起動方法
とりあえずローカルで実行する際のメモ
### アプリケーションの起動
必要なモジュールのインストール
~~~
pip install -r requirements.txt
~~~

環境変数の読み込み
~~~
export LINE_CHANNEL_SECRET=***********
export LINE_CHANNEL_ACCESS_TOKEN=***********
~~~

アプリケーションの起動
~~~
python app.py
~~~

### ngrokの起動
app.pyで起動した際のポートを指定する
~~~
ngrok http 8000
~~~

### LINE Developer Consoleで設定
Ngrokを起動した際のアドレスを設定する