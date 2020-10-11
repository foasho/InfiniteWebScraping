#無限スクロールサイトのスクレイピングをやってみよう
こんにちは！
今日も元気にブログを更新していきます。
今日は前回話していた無限スクロールサイトのスクレイピングをやっていきたいと思います。
AIを作成するには大量の画像が必要になる時がありますよね。
そんなときに無限スクロールサイトのスクレイピングは効果的だと思います。

##環境
・Windows10
・Chromeバージョン：86.0.4240.75
・ChromeDriver：86.0.4240.75
・Selenium：3.141.0

##事前調査
今回フォーカスするサイトは、前回おなじみの500pxという写真投稿サービスサイトです。
まずは、スクレイピングするサイトのURLとそのURLのスクロールを行う要素のID名またはクラス名、そして取得したい画像の親要素のクラス名をメモしておきます。
今回もテストとして空の画像を取得します。
調査結果
・取得するURL：https://500px.com/search?q=%E7%A9%BA&type=photos
・スクロールするクラス名：justified-gallery
・画像の親要素のクラス名またはID名：photo_link

##事前調査をもとに、コードを記述する
観るのが面倒な方は以下の3行で、できます。
```commandline
git clone 
pip install -r requirements.txt
```

```python

```