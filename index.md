# IKeJIがレツプリ祭りに出したキーボード

## 入手方法

何らかの方法でIKeJIに住所を教えてくれたら送るかもしれないし、送らないかもしれない。

[GitHub](https://github.com/ikeji/ikejisplit/tree/main)にもアップロードしたので、自分でPCBを発注する事もできる。

## 組み立てに必要なもの。

### PCB 2枚

キーボードに使うには左右に1枚ずつ必要。

左右とも同じ基板なので、どちらをどっちにしてもいい。

JLCPCBに発注した。送料込みで1枚250円ぐらい。

### RaspberryPiPico 2つ

左右に1つずつ必要。

IKeJIはUSB Type-CにしたいのでWebActのだいたい互換品を使っている。
[Aliexpressで購入](https://ja.aliexpress.com/item/1005003708090298.html)。1つ3ドルぐらいで買った。

だいたいピンヘッダがついてると思うけど、なかったら別途買う必要があるかもしれない。

### 4極ミニジャック PJ-320E

左右に1つずつ必要。

[Aliexpressで購入](https://ja.aliexpress.com/item/1711810776.html)すると、10個入りで2ドルぐらいで買った。


### 1N4148 48本

キーの数だけ必要。

[秋月電子](https://akizukidenshi.com/catalog/g/g100941/)で、50個150円で売ってる。

### MX互換キースイッチ 48個

キー本体。
MX互換のものを選ばないといけない。
足が5ピンのものを使う。

[遊舎工房](https://shop.yushakobo.jp/collections/all-switches)でいろいろ売ってる。
Aliexpressで1つ25セントで買った。

### キーキャップ

指にふれる所。

1セット買って必要なところだけ使ってもいいし、
無刻印のを必要なだけ買ってもいい。

写真のは20個5ドルで買ったのを使った。

### ゴム足

ケースをちゃんと作ってもいいけど、
とりあえず使うなら基板の裏の4隅にゴム足をつけるといいと思う。

たぶんダイソーで売ってる。

### ミニジャックケーブル

実は3極しか使ってないから3極のケーブルでも使える。

最悪ダイソーで100円で買えるはず。

### USBケーブル

うっかり充電用を使わないように注意。

## 組み立て

背が低い順に、
ダイオード -> ジャック -> RaspberryPiPico -> キースイッチ
の順番ではんだづけするといいと思う。

ダイオードは向きがあるので注意すべき。
基板の印刷をみてダイオードに入ってる線にあわせる。

スイッチは最後まで押し込まずに半田付けしてしまうミスがありがちなので注意する事。

## ソフトウエアのセットアップ

ミニジャックケーブルは、電源が入ってる時に抜き差しするとショートするので注意。
USBケーブルを抜いてから抜き差しする。

### CircuitPythonの準備

RP2040をファームウエア書き込みモードにする。
Picoの場合はBOOTSELを押しながらリセット。

`RPI-RP2`という名前のドライブが見える。

[公式サイト](https://circuitpython.org/board/raspberry_pi_pico/)から
`adafruit-circuitpython-raspberry_pi_pico-*.uf2`をダウンロード

今回は`adafruit-circuitpython-raspberry_pi_pico-ja-9.2.1.uf2`をダウンロードした。

`RPI-RP2`ドライブにこのファイルをコピー

キーボードが自動で再起動して、`CIRCUITPY`ドライブが見えるようになる。

### KMK Firmwareの準備

[KMK Firmwareのレポジトリ](https://github.com/KMKfw/kmk_firmware)をダウンロードしてくる。
`kmk`ディレクトリを`CIRCUITPY`ドライブ直下に置く。

### code.pyの準備

[GitHub上に設定サンプル](https://raw.githubusercontent.com/ikeji/ikejisplit/refs/heads/main/firmware/code.py)を置いたので、
この`code.py`をダウンロードして、これを`CIRCUITPY`に置く。

### 左右の設定

ここまでの手順を両方の基板に対してそれぞれおこなう。

左側の基板にUSBを差した時のドライブ名を`CIRCUITPYL`に、
右側の基板にUSBを差した時のドライブ名を`CIRCUITPYR`に変える。

## テスト

キーには左上から右に番号を振ってある。

デフォルトのファームウエアは、それぞれのキー番号を入力するように設定してある。
全部のキーが効くかを試す。

## キーマップの変更

キーマップを変更するには`code.py`を編集する。

キーボードドライブ内の`code.py`を直接エディタで編集すると、
エラーになる事があるので、
PC内で`code.py`を編集してから、キーボードにコピーするとよい。

まず、`code.py`の
```
    keyid_layer,  # <- Comment out after test
```
と書かれている行を消すとIKeJIが使ってる設定になる。

これを元に使いながらキーマップを育てていくといいと思う。

## おわりに

質問があればIKeJIまで聞いてほしい。

## おまけ: KiCadのキャプチャなど。

- 回路 ![](https://uploader.apps.ikeji.ma/file/a07eab9031fea238aeac856a8b44b49b/20250108194348.png)
- 配線 ![](https://uploader.apps.ikeji.ma/file/ac21bd73bdc5f890098420a21f32ddca/20250108194409.png)
- レンダリング(表) ![](https://uploader.apps.ikeji.ma/file/d8eff8ab132c8f1feff5efa4f6e674ff/20250108194425.png)
- レンダリング(裏) ![](https://uploader.apps.ikeji.ma/file/aefda3265f61962098edbf6da03b80c4/20250108194813.png)
