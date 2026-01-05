from datetime import date, timedelta
from pathlib import Path

import jpholiday
from icalendar import Calendar, Event

# ==========================================
# 設定エリア
# ==========================================
START_DATE = date(2026, 1, 1)
END_DATE = date(2030, 12, 31)
OUTPUT_DIR = Path(__file__).parents[1] / 'docs/data'  # ファイルの保存先

# 年末年始の特別休業日（祝日以外で休みにする日）
# 1/1は祝日判定されるため、ここでは1/2, 1/3, 12/31を指定
SPECIAL_HOLIDAYS = [
    (1, 2), (1, 3), (12, 31)
]

# ==========================================
# ロジック部分
# ==========================================

def is_business_day(target_date):
    """営業日かどうかを判定する関数"""
    # 1. 土日チェック (月=0, ..., 土=5, 日=6)
    if target_date.weekday() >= 5:
        return False

    # 2. 日本の祝日チェック
    if jpholiday.is_holiday(target_date):
        return False

    # 3. 特別休業日チェック (1/2, 1/3, 12/31)
    if (target_date.month, target_date.day) in SPECIAL_HOLIDAYS:
        return False

    return True

def get_business_days_list(start, end):
    """期間内の全営業日を計算し、月ごとのメタデータを付与して返す"""
    current = start

    # 月ごとに営業日を一時保存する辞書
    month_cache = {} # key: (year, month), value: [date, date...]

    # まず全ての日付を走査して営業日を抽出
    while current <= end:
        if is_business_day(current):
            ym = (current.year, current.month)
            if ym not in month_cache:
                month_cache[ym] = []
            month_cache[ym].append(current)
        current += timedelta(days=1)

    # 営業日データに「第N営業日」「最終営業日フラグ」を付与してリスト化
    all_data = []
    for ym in sorted(month_cache.keys()):
        days_in_month = month_cache[ym]
        total_days = len(days_in_month)

        for idx, d in enumerate(days_in_month):
            nth = idx + 1  # 1始まりのインデックス
            is_last = (nth == total_days)

            all_data.append({
                'date': d,
                'nth': nth,          # 第N営業日
                'is_last': is_last,  # 月末営業日かどうか
                'total': total_days  # その月の総営業日数
            })

    return all_data

def create_ics_file(filename, events, calendar_name):
    """イベントリストからicsファイルを生成する"""
    cal = Calendar()
    cal.add('prodid', '-//Biz Calendar Generator//JP')
    cal.add('version', '2.0')
    cal.add('x-wr-calname', calendar_name) # カレンダー名（Googleカレンダー取り込み時に使われる）

    for e in events:
        event = Event()
        event.add('summary', e['title'])
        # 終日予定の場合、dtstart は date型、dtend は翌日の date型にするのが標準的
        event.add('dtstart', e['date'])
        event.add('dtend', e['date'] + timedelta(days=1))
        # ユニークID生成 (再生成しても同じIDになるように日付とタイトルで構成)
        uid = f"{e['date'].strftime('%Y%m%d')}-{e['type']}@bizcal"
        event.add('uid', uid)

        cal.add_component(event)

    # フォルダ作成と保存
    if not OUTPUT_DIR.is_dir():
        OUTPUT_DIR.mkdir()
    filepath = OUTPUT_DIR / filename
    filepath.write_bytes(cal.to_ical())
    print(f"作成完了: {filepath}")

# ==========================================
# メイン処理
# ==========================================
def main():
    print("営業日データを計算中...")
    biz_data = get_business_days_list(START_DATE, END_DATE)

    # --- パターン1: 営業日すべて ---
    events_p1 = []
    for d in biz_data:
        events_p1.append({
            'date': d['date'],
            'title': f"第{d['nth']}営業日",
            'type': 'all'
        })
    create_ics_file("all.ics", events_p1, "全営業日カレンダー")

    # --- パターン2: 各月の第N営業日 (例として第1〜第5を作成) ---
    # ※必要に応じて range(1, 6) を変更してください
    for n in range(1, 24):
        events_pn = []
        for d in biz_data:
            if d['nth'] == n:
                events_pn.append({
                    'date': d['date'],
                    'title': f"第{n}営業日",
                    'type': f'nth_{n}'
                })
        if events_pn:
            create_ics_file(f"day_{n:0>2d}.ics", events_pn, f"第{n}営業日カレンダー")

    # --- パターン3: 5の倍数営業日 (5, 10, 15, 20...) ---
    events_p3 = []
    for d in biz_data:
        if d['nth'] % 5 == 0:
            events_p3.append({
                'date': d['date'],
                'title': f"第{d['nth']}営業日",
                'type': 'multi_5'
            })
    create_ics_file("days_of_5.ics", events_p3, "5の倍数営業日")

    # --- パターン4: 月初営業日と月末営業日 ---
    events_p4 = []
    for d in biz_data:
        if d['nth'] == 1:
            events_p4.append({
                'date': d['date'],
                'title': "月初営業日",
                'type': 'first'
            })
        elif d['is_last']:
            events_p4.append({
                'date': d['date'],
                'title': "月末営業日",
                'type': 'last'
            })
    create_ics_file("first_and_last.ics", events_p4, "月初・月末営業日")

if __name__ == "__main__":
    main()