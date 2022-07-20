# bakuhatsu_supportweb

## データベースの作成

mysqlにログインして以下のコマンドを実行する

```
create database bakuhatsu_support_web
```

## テーブルを作成

ルートディレクトリで以下のコマンドを実行する

```
python manage.py migrate
```

## 初期データを登録

ルートディレクトリで以下のコマンドを実行する

```
python manage.py loaddata contents/fixtures/posts-data.json
python manage.py loaddata faq/fixtures/posts-data.json
python manage.py loaddata contant/fixtures/posts-data.json
python manage.py loaddata information/fixtures/posts-data.json
```

## パッケージのインストール

ルートディレクトリで以下のコマンドを実行する

```
pip install -r requirements.txt
```
