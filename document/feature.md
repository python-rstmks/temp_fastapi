# タスクブランチ

<details>
<summary><h2>deleting subcategory</h2></summary>

priority: high<br>
***branch-name: feature/delete-subcategory***

サブカテゴリ画面にてサブカテゴリを削除（論理削除）

</details>

<details>
<summary><h2>問題個別ページ</h2></summary>

priority: high<br>
***branch-name: feature/delete-subcategory***

questionレコードのedit, deleteを行う。

</details>



<details>
<summary><h2>edit question</h2></summary>

priority: high<br>
***branch-name: feature/edit-question***

questionのタイトルとanswerを編集。

</details>



## 問題出題画面

問題作成初期画面において<br>
[1]ランダムで出題するか、<br>
[2]カテゴリ、サブカテゴリに絞って出題するか選択できるようにする。


出題される問題の数をinputタグnumberで選べるようにする。
<br>


フロント側で問題を一問解いて次の問題に移ると同時に、正解か不正解のフラグをサーバに送信する。
<br>
20問解ききる前にやめてしまう可能性があるため、まとめて正解不正解のフラグを送信しない。

「問題を出題する」ボタンをクリックすると同時にサーバにフラグ1（ランダムかカテゴリ選択式）とフラグ2（不正解の問題からのみ出題する or 正解不正解の問題に関係なく出題する）とカテゴリidのarray（カテゴリ選択式の場合は）を含んだリクエストを送信して、questionsデータのレスポンスをもらう。

#### カテゴリで絞って問題を出題する
***branch-name: feat/ask-question-by-category***  ← feature/ask-questionブランチから派生

where category_id = 

でとってくる。


#### ランダムに問題を出題する
***branch-name: feat/ask-question-random***  ← feature/ask-questionブランチから派生

max_question_idより小さい乱数を50個作成して、それを配列に格納。
questionsテーブルから50問をとってくる。

＝＝＝＝＝＝＝＝＝＝＝

あるquestionに対して、カテゴリとサブカテゴリを割り当てることができる。

カテゴリ内にクエスチョンがあるという認識よりは、

クエスチョンに対して、カテゴリ（いくつでも可）、や　サブカテゴリを割り当てることができる。

もしくは

化学＞熱化学　というタグを割り当てる。無機化かがく＞錯体　というタグを割り当てる。



questionに対してのタグ付けについて

→ カテゴリのみでタグをつける場合は　赤色。

→ カテゴリ名＞サブカテゴリ名　でタグをつける場合は　緑色とする。






