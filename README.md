```
source fleamarket_venv/bin/activate
pip install -r requirements.txt
```

[step1]
uvicorn main:app --reload

[step2]
localhost:8000/docs
にアクセス

[step3]
alembic revision --autogenerate -m "Create user tables"

[step4]
alembic revision --autogenerate -m "Add foreign key"

[step5]
alembic upgrade head

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


# Item テーブル定義書

| 列名          | データ型          | NULL許容 | デフォルト値     | 説明/制約                                      |
|---------------|------------------|----------|-----------------|------------------------------------------------|
| name          | String           | No       |                 | 商品名                                          |
| price         | Integer          | No       |                 | 価格                                            |
| description   | String           | Yes      |                 | 商品説明                                        |
| status        | Enum(ItemStatus) | No       | ItemStatus.ON_SALE | 商品状態（例: ON_SALE）                        |
| created_at    | DateTime         | No       | datetime.now()  | 作成日時                                        |
| updated_at    | DateTime         | No       | datetime.now()  | 更新日時（onupdateで更新時に現在時刻に変更）    |
| user_id       | Integer          | No       |                 | ユーザーID（`users.id`への外部キー、削除時にCASCADE） |

### Category テーブル定義書

| 列名          | データ型      | NULL許容 | デフォルト値     | 説明/制約                                      |
|---------------|--------------|----------|-----------------|------------------------------------------------|
| id            | Integer       | No       |                 | 主キー                                          |
| name          | String        | No       |                 | カテゴリ名                                      |
| created_at    | DateTime      | No       | datetime.now()  | 作成日時                                        |
| updated_at    | DateTime      | No       | datetime.now()  | 更新日時（onupdateで更新時に現在時刻に変更）    |
| user_id       | Integer       | No       |                 | ユーザーID（`users.id`への外部キー、削除時にCASCADE） |

### SubCategory テーブル定義書

| 列名          | データ型      | NULL許容 | デフォルト値 | 説明/制約                                      |
|---------------|--------------|----------|-------------|------------------------------------------------|
| id            | Integer       | No       |             | 主キー                                          |

### SubCategoryQuestion Table

| Column Name     | Data Type | Constraints                  | Description |
|-----------------|-----------|------------------------------|-------------|
| subcategory_id  | Integer   | Primary Key, Foreign Key     | Identifies the subcategory associated with a question. References `subcategories.id`. |
| question_id     | Integer   | Primary Key, Foreign Key     | Identifies the question associated with a subcategory. References `questions.id`. |

# 機能
fastapi pagination
7件づつcategoryを出す。

