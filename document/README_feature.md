# タスクブランチ

<details>
<summary><h2>add question-table</h2></summary>

priority: high<br>
***branch-name: feature/edit-question-table***

正解したかのフラグをつける。<br>
column_name: is_correct
column_name: category_id

</details>

<details>
<summary><h2>pagination</h2></summary>

priority: high<br>
***branch-name: feature/pagination***

カテゴリをページネーションで表示する。7件。

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
***branch-name: feature/ask-question-by-category***  ← feature/ask-questionブランチから派生

where category_id = 

でとってくる。


#### ランダムに問題を出題する
***branch-name: feature/ask-question-random***  ← feature/ask-questionブランチから派生

questionsテーブルから50問をとってくる。

＝＝＝＝＝＝＝＝＝＝＝




