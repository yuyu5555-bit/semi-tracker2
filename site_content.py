# -*- coding: utf-8 -*-
"""
半導体テーマトラッカー — 手動コンテンツ(ここだけ編集すればいい)
=================================================================
編集 → GitHubにcommit → Actionsで update-data を Run するだけで反映。index.html は触らない。

■ どこを書き換えるか
  - WEEKLY : mode="auto" なら「今週の解説」を自動生成(何もしなくていい)。
             自分で書きたい週だけ mode="manual" にして title/body/start/end を書く。
  - EVENTS : 終わった行を消して新しい行を足す(date は "YYYY-MM-DD")。
             kind = earnings(決算) / macro(統計) / industry(業界) / regulation(規制)
  - NEWS   : 気になったニュースを1ブロック足す(古いのは消してOK)。
             sentiment -2〜+2、tags は themes.py のマクロkey、stocks の dir は "up"/"down"
  - MACRO  : WSTSはSIA月次発表の数字を1行追加。CapExは各社発表時に更新。

■ 自動で動くもの(手を触れなくていい)
  - 今日の要注目 / 今週のハイライト / 最新ヘッドライン(RSS) / 見出しの銘柄ハイライト
  - 今週の解説(WEEKLY mode="auto" のとき)

※ 2026-07-11 時点の実データ入り
"""

WEEKLY = {
    "mode": "auto",
    "title": "SKハイニクス米上場が号砲、メモリ主導サイクル最高潮",
    "body": "WSTS 5月の世界半導体売上は1,206億ドル(前年比+104.1%)で単月過去最高を更新、前月比プラスは15ヶ月連続。SKハイニクスが米ADR上場で約265億ドルを調達しHBM増産へ——メモリテスタ・後工程・材料の裾野に波及する。\nCapExはTSMC 520〜560億ドル、Samsung 110兆ウォンと史上最大の投資合戦で、日本の装置・材料の受注環境は追い風継続。一方、対中規制(MATCH法案)の審議と、2027年の米IT設備投資の持続性には引き続き注意。",
    "start": "2026-07-06",
    "end": "2026-07-10"
}

EVENTS = [
    {
        "date": "2026-07-16",
        "kind": "industry",
        "title": "TSMC 2Q決算・ガイダンス(見込)"
    },
    {
        "date": "2026-07-23",
        "kind": "earnings",
        "title": "ディスコ 1Q決算"
    },
    {
        "date": "2026-07-29",
        "kind": "earnings",
        "title": "アドバンテスト 1Q決算(15:30)"
    },
    {
        "date": "2026-07-31",
        "kind": "earnings",
        "title": "ルネサス 2Q決算(見込)"
    },
    {
        "date": "2026-08-04",
        "kind": "macro",
        "title": "SIA/WSTS 6月分 月次統計(見込)"
    },
    {
        "date": "2026-08-06",
        "kind": "earnings",
        "title": "東京エレクトロン 1Q決算(見込)"
    },
    {
        "date": "2026-08-28",
        "kind": "earnings",
        "title": "レーザーテック 本決算(見込)"
    }
]

NEWS = [
    {
        "date": "2026-07-08",
        "sentiment": 2,
        "title": "SKハイニクス、米ADR上場で約265億ドル調達——HBM増産を加速",
        "summary": "米国預託証券のNasdaq上場で史上級の調達。初値は公開価格を大きく上回り$170で寄付き。調達資金はHBM製造能力の大幅拡張に充当。",
        "tags": [
            "memory",
            "spe_test"
        ],
        "chain": [
            "HBM設備投資の加速",
            "メモリテスタ・後工程装置の受注拡大",
            "日本の検査・実装装置に波及"
        ],
        "stocks": [
            {
                "code": "6857",
                "name": "アドバンテスト",
                "dir": "up"
            },
            {
                "code": "6146",
                "name": "ディスコ",
                "dir": "up"
            },
            {
                "code": "6871",
                "name": "日本マイクロニクス",
                "dir": "up"
            }
        ]
    },
    {
        "date": "2026-07-06",
        "sentiment": 2,
        "title": "WSTS 5月売上1,206億ドル・前年比+104%——単月最高を更新",
        "summary": "SIA発表。前月比+9.2%で15ヶ月連続プラス。米州+132%、アジア太平洋+119%、中国+89%と全地域で大幅成長。AI特需がロジックとメモリを牽引。",
        "tags": [
            "memory",
            "compute"
        ],
        "chain": [
            "市況の拡大継続",
            "装置・材料の受注環境が強含み"
        ],
        "stocks": [
            {
                "code": "8035",
                "name": "東京エレクトロン",
                "dir": "up"
            },
            {
                "code": "285A",
                "name": "キオクシア",
                "dir": "up"
            }
        ]
    },
    {
        "date": "2026-06-29",
        "sentiment": 1,
        "title": "韓国、4,800兆ウォンのAI投資構想——Samsung/SKがDRAM能力倍増へ",
        "summary": "政財界が合同発表。新ファブ4棟(約5,200億ドル)＋先端パッケージング棟。Yongin/Cheongjuの前倒しも。装置・材料需要には追い風だが、中期の供給過剰リスクも意識される。",
        "tags": [
            "spe_front",
            "materials"
        ],
        "chain": [
            "韓国メモリの大増産",
            "前工程装置・材料の需要増",
            "中期は供給過剰リスクに注意"
        ],
        "stocks": [
            {
                "code": "8035",
                "name": "東京エレクトロン",
                "dir": "up"
            },
            {
                "code": "4063",
                "name": "信越化学",
                "dir": "up"
            },
            {
                "code": "3436",
                "name": "SUMCO",
                "dir": "up"
            }
        ]
    },
    {
        "date": "2026-07-09",
        "sentiment": 1,
        "title": "ラピダス、2nmウェハーをTSMC比低価格で提供へ——2027年量産時$20,000/枚",
        "summary": "価格戦略で受注獲得を狙う報道。国策ファウンドリの立ち上がりは国内の装置・材料・検査の投資継続に直結。",
        "tags": [
            "facility",
            "spe_front"
        ],
        "chain": [
            "国策2nmの受注拡大期待",
            "国内ファブ投資の継続",
            "装置・検査・材料に裾野"
        ],
        "stocks": [
            {
                "code": "8035",
                "name": "東京エレクトロン",
                "dir": "up"
            },
            {
                "code": "6920",
                "name": "レーザーテック",
                "dir": "up"
            }
        ]
    },
    {
        "date": "2026-07-07",
        "sentiment": -1,
        "title": "米MATCH法案の審議継続——対中DUV規制拡大なら装置に逆風",
        "summary": "旧世代露光装置まで規制対象を広げ、同盟国にも同水準を求める法案。成立すれば中国売上比率の高い日本装置株の業績予想に下押し。",
        "tags": [
            "spe_front",
            "materials"
        ],
        "chain": [
            "対中規制の拡大懸念",
            "中国向け売上の下振れリスク",
            "装置株のセンチメント悪化"
        ],
        "stocks": [
            {
                "code": "8035",
                "name": "東京エレクトロン",
                "dir": "down"
            },
            {
                "code": "7735",
                "name": "SCREEN",
                "dir": "down"
            }
        ]
    }
]

MACRO = {
    "wsts": {
        "label": "WSTS 世界半導体売上(月次)",
        "unit": "十億ドル",
        "series": [
            {
                "month": "2025-11",
                "value": 75.3,
                "yoy_pct": 29.8
            },
            {
                "month": "2025-12",
                "value": 79.6,
                "yoy_pct": 34.0
            },
            {
                "month": "2026-01",
                "value": 82.5,
                "yoy_pct": 46.1
            },
            {
                "month": "2026-02",
                "value": 88.8,
                "yoy_pct": 61.8
            },
            {
                "month": "2026-03",
                "value": 99.5,
                "yoy_pct": 79.2
            },
            {
                "month": "2026-04",
                "value": 110.5,
                "yoy_pct": 93.9
            },
            {
                "month": "2026-05",
                "value": 120.6,
                "yoy_pct": 104.1
            }
        ]
    },
    "capex": {
        "label": "主要ファブ CapEx ガイダンス(2026年)",
        "as_of": "2026-07時点",
        "items": [
            {
                "company": "TSMC",
                "value": 54,
                "yoy_pct": 32,
                "note": "計画520〜560億ドル(前年409億ドル)。2nm・CoWoS増産"
            },
            {
                "company": "Samsung",
                "value": 74,
                "yoy_pct": 128,
                "note": "110兆ウォン(半導体CapEx+R&D)。HBM4・先端ファウンドリ"
            },
            {
                "company": "SK hynix",
                "value": 20,
                "yoy_pct": 40,
                "note": "前年比4割増(SC-IQ推計)。HBM4集中・Yongin前倒し"
            },
            {
                "company": "Micron",
                "value": 25,
                "yoy_pct": 81,
                "note": "広島含む増産。HBM専用ファブ増設"
            },
            {
                "company": "Intel",
                "value": 17,
                "yoy_pct": -4,
                "note": "横ばい〜微減。18A立ち上げ優先・投資選別"
            }
        ]
    },
    "cycle": "2026年市場はWSTS予測で前年比90%増の1兆5,112億ドル——初の1兆ドル超え。AIデータセンター向けのメモリ・ロジックが牽引する拡大フェーズ。業界CapExも約2,000億ドル(+20%)と過去最高で、装置・材料の受注環境は強い。リスクは2027年の米IT投資の持続性、対中規制、韓国大増産による中期の供給過剰。"
}
