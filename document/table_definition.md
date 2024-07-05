## Item テーブル定義書

| 列名          | データ型          | NULL許容 | デフォルト値     | 説明/制約                                      |
|---------------|------------------|----------|-----------------|------------------------------------------------|
| name          | String           | No       |                 | 商品名                                          |
| price         | Integer          | No       |                 | 価格                                            |
| description   | String           | Yes      |                 | 商品説明                                        |
| status        | Enum(ItemStatus) | No       | ItemStatus.ON_SALE | 商品状態（例: ON_SALE）                        |
| created_at    | DateTime         | No       | datetime.now()  | 作成日時                                        |
| updated_at    | DateTime         | No       | datetime.now()  | 更新日時（onupdateで更新時に現在時刻に変更）    |
| user_id       | Integer          | No       |                 | ユーザーID（`users.id`への外部キー、削除時にCASCADE） |

## Category テーブル定義書

| 列名          | データ型      | NULL許容 | デフォルト値     | 説明/制約                                      |
|---------------|--------------|----------|-----------------|------------------------------------------------|
| id            | Integer       | No       |                 | 主キー                                          |
| name          | String        | No       |                 | カテゴリ名                                      |
| created_at    | DateTime      | No       | datetime.now()  | 作成日時                                        |
| updated_at    | DateTime      | No       | datetime.now()  | 更新日時（onupdateで更新時に現在時刻に変更）    |
| user_id       | Integer       | No       |                 | ユーザーID（`users.id`への外部キー、削除時にCASCADE） |

## SubCategory テーブル定義書

| 列名          | データ型      | NULL許容 | デフォルト値 | 説明/制約                                      |
|---------------|--------------|----------|-------------|------------------------------------------------|
| id            | Integer       | No       |             | 主キー                                          |

## SubCategoryQuestion Table

| Column Name     | Data Type | Constraints                  | Description |
|-----------------|-----------|------------------------------|-------------|
| subcategory_id  | Integer   | Primary Key, Foreign Key     | Identifies the subcategory associated with a question. References `subcategories.id`. |
| question_id     | Integer   | Primary Key, Foreign Key     | Identifies the question associated with a subcategory. References `questions.id`. |