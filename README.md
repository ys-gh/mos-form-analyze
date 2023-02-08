# mos-form集計プログラム

## 環境構築
```
$ pip install -r requirements.txt
```

## Firebase設定

1. 実験の立ち上げに使っているプロジェクトより認証ファイルをローカルにダウンロードし、適当な場所に配置する

2. 環境変数を設定する
```
$ export GOOGLE_APPLICATION_CREDENTIALS={path/to/serviceAccountKey.json}
```

## 実験スクリプトを微修正する

8行目付近のmethodsをcollectionに対応するように修正する

ex. (ついでに95%信頼区間も出力される)

```
$ python main.py
> 
method: m1 MOS: 3.4761904761904763 +- 0.6288755397091259
method: m2 MOS: 3.3333333333333335 +- 0.6533333333333334
method: m3 MOS: 3.4285714285714284 +- 0.5669567884768645
number of subjects: 4
```