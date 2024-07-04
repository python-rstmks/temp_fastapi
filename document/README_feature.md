# タスクブランチ

<!-- ## edit-question-table -->



<details>
<summary>edit-question-table</summary>

priority: high<br>
***branch-name: feature/edit-question-table***


</details>





正解したかのフラグをつける。
column_name:

## subcategoryCreate 
***branch-name: feature/subcategory-create***
<hr/>

HOMEのカテゴリの下にプラスボタンを置いてそれをクリックするとinputボックスが出現して入力できる仕組みにする。


## subcategory page
***branch-name: feature/subcategory-page***

紐づいた問題を表示する。<br>
問題は全件取得する。

<hr/>

## category search
***branch-name: feature/search-category***

部分一致検索

一旦表示されているページネーションのカテゴリをすべてcategoryListから削除して、
部分検索に一致するカテゴリのみを表示する。

検索ボックスを空にすると再びページネーションに基づくcategoryが表示される。

<hr/>

## subcategory search
***branch-name: feature/search-subcategory***

## 問題出題画面
***branch-name: feature/ask-question***

問題作成初期画面において<br>
[1]ランダムで出題するか、<br>
[2]カテゴリ、サブカテゴリに絞って出題するか選択できるようにする。


出題される問題の数をinputタグnumberで選べるようにする。
<br>
「問題を出題する」ボタンをクリックすると同時にサーバにフラグ付きのリクエストを送信して、問題をデータのレスポンスをもらう。

問題を一問解いて次の問題に移ると同時に、正解か不正解のフラグをサーバに送信する。
<br>
50問解ききる前にやめてしまう可能性があるため、まとめて正解不正解のフラグを送信しない。

#### カテゴリで絞って問題を出題する
***branch-name: feature/ask-question-by-category***  ← feature/ask-questionブランチから派生

問題作成はバックエンドが行うのでapi叩くだけ。


#### ランダムに問題を出題する
***branch-name: feature/ask-question-random***  ← feature/ask-questionブランチから派生

問題作成はバックエンドが行うのでapi叩くだけ。



