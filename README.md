# ドキュメント

| path | 説明 |
|-----------|-----------|
|[./document/setup.md](./document/setup.md)|セットアップ方法|
|[./document/deploy.md](./document/deploy.md)|デプロイ方法|
|[./document/deploy.md](./document/table_definition.md)|テーブル定義書|
|[./document/README_feature.md](./document/README_feature.md)|開発予定機能別ブランチ|




## routers directory vs cruds directory

### crudsフォルダのファイル
このファイル内の関数は、主にデータベースに対する直接の操作を行います。SQLAlchemyセッションを使用してデータベースとやり取りし、データの作成、読み取り、更新、削除（CRUD）を実装しています。

### routersフォルダのファイル

routers/item.py
このファイルは、APIエンドポイントを定義し、HTTPリクエストを処理するためのルートハンドラーを提供します。具体的には、以下の操作が含まれます：

create: POSTリクエストを処理し、新しいアイテムを作成するエンドポイントを提供する。
update: PUTリクエストを処理し、指定されたIDのアイテムを更新するエンドポイントを提供する。
delete: DELETEリクエストを処理し、指定されたIDのアイテムを削除するエンドポイントを提供する。
find_by_id: GETリクエストを処理し、指定されたIDのアイテムを取得するエンドポイントを提供する。
find_by_name: GETリクエストを処理し、指定された名前を含むアイテムを検索するエンドポイントを提供する。
このファイルは、HTTPリクエストを受け取り、それを適切なCRUD操作にルーティングします。HTTPステータスコードの設定やエラーハンドリングもここで行われます。APIRouterを使ってエンドポイントを定義し、依存性注入（Depends）を使用してデータベースセッションを管理しています。


====================

schemas.py ファイルの目的は、Pydantic を使用してデータバリデーションとデータ構造の定義を行うことです（静的型付け言語のようにするためのもの（
models.py は　modelの定義


====================

https://jwt.io/




# 機能
fastapi pagination
7件づつcategoryを出す。

