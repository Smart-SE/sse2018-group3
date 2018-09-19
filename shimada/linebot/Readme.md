## Ngrokを利用した起動方法
とりあえずローカルで実行する際のメモ
### ラズパイに準備しておくもの
python3.x
~~~
python3 -V
~~~

ngrokのインストール
~~~
pip3 install ngrok 
~~~

必要なモジュールのインストール
~~~
pip3 install -r requirements.txt
~~~

## デモ手順
今回はデモなのでngrokを使用する.

### LINE BOTを友だちに追加
別途共有します

### ngrokの起動
app.pyで起動する際のポートを指定する
~~~
ngrok http 8000
~~~

### 環境変数の設定
公開NGなので別途共有します
~~~
export LINE_CHANNEL_SECRET=***********
export LINE_CHANNEL_ACCESS_TOKEN=***********
~~~

### ngrokのアドレスを指定する
ngrokは起動するたびにアドレスが変わるので以下を変更する
- variable.py
- LINEデベロッパーコンソール内のWebhook URL(ブラウザから操作)

### アプリケーションの実行
アプリケーションの起動
~~~
python3 app.py
~~~

### ボットへメッセージを送信