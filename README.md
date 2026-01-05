# 日本の営業日カレンダー

日本の「営業日」を定義したiCalendar形式（.ics）のカレンダーデータです。
Googleカレンダー、Outlook、Appleカレンダーなどにインポートまたは購読して利用できます。

## 📅 定義・条件

* **期間:** 2026年1月 ～ 2030年12月
* **営業日:** 平日（月～金）
* **休業日（除外日）:**
    * 土曜日・日曜日
    * 日本の国民の祝日
    * 年末年始休業（12月31日、1月1日～1月3日）

## 🔗 カレンダーの一覧

| カレンダーの内容 | iCalファイル |
| :--- | :--- |
| **全営業日** | [all.ics](https://shiro46mt.github.io/biz-calendar-jp/data/all.ics) |
| **月初・月末営業日** | [first_and_last.ics](https://shiro46mt.github.io/biz-calendar-jp/data/first_and_last.ics) |
| **5の倍数営業日** | [days_of_5.ics](https://shiro46mt.github.io/biz-calendar-jp/data/days_of_5.ics) |
| 第1営業日 | [day_01.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_01.ics) |
| 第2営業日 | [day_02.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_02.ics) |
| 第3営業日 | [day_03.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_03.ics) |
| 第4営業日 | [day_04.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_04.ics) |
| 第5営業日 | [day_05.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_05.ics) |
| 第6営業日 | [day_06.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_06.ics) |
| 第7営業日 | [day_07.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_07.ics) |
| 第8営業日 | [day_08.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_08.ics) |
| 第9営業日 | [day_09.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_09.ics) |
| 第10営業日 | [day_10.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_10.ics) |
| 第11営業日 | [day_11.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_11.ics) |
| 第12営業日 | [day_12.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_12.ics) |
| 第13営業日 | [day_13.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_13.ics) |
| 第14営業日 | [day_14.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_14.ics) |
| 第15営業日 | [day_15.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_15.ics) |
| 第16営業日 | [day_16.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_16.ics) |
| 第17営業日 | [day_17.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_17.ics) |
| 第18営業日 | [day_18.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_18.ics) |
| 第19営業日 | [day_19.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_19.ics) |
| 第20営業日 | [day_20.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_20.ics) |
| 第21営業日 | [day_21.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_21.ics) |
| 第22営業日 | [day_22.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_22.ics) |
| 第23営業日 | [day_23.ics](https://shiro46mt.github.io/biz-calendar-jp/data/day_23.ics) |

## 使い方

### 🗓 Googleカレンダー
1. **「iCalファイル」** のリンクを右クリックし、**「リンクのアドレスをコピー」** を選択します。
2. Googleカレンダーを開きます。
3. 左サイドバーの「他のカレンダー」の横にある「＋」をクリックし、「URLで追加」を選択します。
4. コピーしたURLを貼り付けて「カレンダーを追加」をクリックします。

### 🍎 Apple iCloudカレンダー (iPhone / iPad / Mac)
[こちらのページ](https://shiro46mt.github.io/biz-calendar-jp/)の **「📅 購読する」** リンクをクリック（タップ）してください。
自動的にカレンダーアプリが起動し、追加画面が表示されます。

### 💾 ファイルとして保存したい場合
**「iCalファイル」** のリンクをクリックすると、ソースコード（テキスト）が表示されます。ブラウザの「名前をつけて保存」などで `.ics` ファイルとして保存し、Outlookなどに手動でインポートすることも可能です。

## 生成方法

Python (`icalendar`, `jpholiday`) を使用して生成しています。
