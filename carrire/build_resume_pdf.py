#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

FONT_PATH = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
pdfmetrics.registerFont(TTFont("IPAGothic", FONT_PATH))

OUT = "toshiyuki-hioki_職務経歴書_20260803.pdf"

doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    leftMargin=18 * mm, rightMargin=18 * mm,
    topMargin=16 * mm, bottomMargin=16 * mm,
    title="職務経歴書",
)

title_style = ParagraphStyle("title", fontName="IPAGothic", wordWrap="CJK", fontSize=20, leading=26, alignment=TA_CENTER, spaceAfter=6)
meta_style = ParagraphStyle("meta", fontName="IPAGothic", wordWrap="CJK", fontSize=10.5, leading=15, alignment=TA_CENTER, spaceAfter=2)
h2_style = ParagraphStyle("h2", fontName="IPAGothic", wordWrap="CJK", fontSize=13, leading=18, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor("#1f3d5c"))
company_style = ParagraphStyle("company", fontName="IPAGothic", wordWrap="CJK", fontSize=11.5, leading=16, spaceBefore=8, spaceAfter=2, textColor=colors.HexColor("#1f3d5c"))
biz_style = ParagraphStyle("biz", fontName="IPAGothic", wordWrap="CJK", fontSize=9.5, leading=13, spaceAfter=4, textColor=colors.HexColor("#555555"))
body_style = ParagraphStyle("body", fontName="IPAGothic", wordWrap="CJK", fontSize=9.5, leading=15, spaceAfter=5)
label_style = ParagraphStyle("label", fontName="IPAGothic", wordWrap="CJK", fontSize=9.5, leading=15, spaceAfter=5, textColor=colors.HexColor("#1f3d5c"))
period_style = ParagraphStyle("period", fontName="IPAGothic", wordWrap="CJK", fontSize=9.5, leading=13)
th_style = ParagraphStyle("th", fontName="IPAGothic", wordWrap="CJK", fontSize=9.5, leading=13, textColor=colors.white)

story = []

story.append(Paragraph("職　務　経　歴　書", title_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1f3d5c"), spaceAfter=8))
story.append(Paragraph("2026年8月3日現在", meta_style))
story.append(Paragraph("氏名　日置　俊行", meta_style))
story.append(Spacer(1, 6))

def h2(text):
    story.append(Paragraph(text, h2_style))

def body(lines):
    for l in lines:
        story.append(Paragraph(l, body_style))

h2("■職務要約")
body([
    "プロジェクトマネジメント歴11年。大手自動車メーカーや通信キャリア企業において、要件定義～基本設計、DX推進プロジェクトなど幅広い業務に携わり、タスク管理やベンダーコントロールのスキルを磨いてきました。メンバーの後進育成やチーム全体の効率化に強みを持ち、国内外での折衝や資料作成・プレゼンの経験も豊富です。",
    "近年は、総合建設業においてDX・AI推進顧問として、経営層と現場双方の認識差を構造化し、業務自動化・制度整備・インフラ改善までを一気通貫で推進。AWSやPythonを活用した業務効率化や、新規事業構想のコンサルティング業務にも従事し、プロジェクトの成功に貢献しています。IT技術の知識とマネジメントスキルを活かし、課題解決と成果創出に注力しています。",
])

h2("■活かせる知識・経験")
body([
    "・チームマネジメント: メンバー育成、後進教育、チームの生産性向上。",
    "・組織DX推進: 経営層・現場・バックオフィス間の認識差を構造化し、業務自動化/制度整備/インフラ改善を一気通貫で推進。",
    "・AI活用によるナレッジマネジメント: Claude Codeを用い、プロジェクトの意思決定背景・課題・解決経緯をドキュメント化。属人化防止と引き継ぎ性の向上に貢献。",
    "・DX推進: AWSやPythonを活用した業務効率化プロジェクトの実施。",
    "・プロジェクト管理: 要件定義、タスク管理、進捗管理、ベンダーコントロール。",
    "・プレゼン・資料作成: 国内外の役員やプロジェクトメンバー向けの資料作成とプレゼンテーション。",
    "・業務プロセス改善: 設計変更情報一元管理プロジェクトにて160h/月の工数削減に貢献。",
    "・技術的知識: Python、AWS、Figma、Copilot、M365、マーケティング戦略。",
])

h2("【職務経歴】")

def entry_table(period, summary_lines, body_lines, knowledge):
    period_p = Paragraph(period.replace("\n", "<br/>"), period_style)
    content_flow = []
    for l in summary_lines:
        content_flow.append(Paragraph(l, label_style))
    content_flow.append(Paragraph("【業務内容】", label_style))
    for l in body_lines:
        content_flow.append(Paragraph(l, body_style))
    content_flow.append(Paragraph("【関連知識】" + knowledge, body_style))

    header = [Paragraph("期間", th_style), Paragraph("業務内容", th_style)]
    data = [header, [period_p, content_flow]]
    t = Table(data, colWidths=[24 * mm, 149 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3d5c")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t

entries = []

entries.append({
    "company": "■森信建設株式会社（DX・AI推進顧問）",
    "biz": "事業内容：総合建設業（元請け工事のほか、介護事業等の関連事業を展開）",
    "period": "2025年10月\n～現在",
    "summary": [
        "概要：経営課題整理・現場実装伴走を担うDX・AI推進顧問",
        "役割：PM・DX推進（経営・現場・バックオフィス横断）",
        "規模：マネージャー",
    ],
    "body": [
        "・社長、現場、総務経理、外部業者、社労士の間にある認識差を整理し、意思決定に必要な論点・比較表・実行手順へ落とし込み",
        "・ANDPAD、KING OF TIME、LINE WORKS、Google Workspace、Excel、Pythonを活用し、紙・Excel・チャット・SaaSが分断された業務フローを再設計",
        "・タスク一覧、意思決定ログ、業務マニュアル、経営層向け説明資料を整備し、属人的な判断・対応を再現可能な業務プロセスへ変換",
        "・ANDPADエクスポートExcelを工事管理表へ自動転記し、NASコピーとメール通知まで行うWindows自動化をPythonで設計・構築",
        "・KING OF TIMEデータを社労士提出用Excelへ変換し、Chatwork確認・手集計の二重運用を解消（Python）",
        "・LINE WORKSを入口とした購入申請、休暇・遅刻連絡、設備予約、経費申請、社内通知のモック作成・運用設計を実施（GAS）",
        "・2016年以降未改定だった就業規則について、最新法令を反映した本文を作成し、新旧変更点を添えて社労士へ提出",
        "・ONU/OG交換、HPE製スイッチ・ハブ・APを導入し、社内Wi-Fi環境を外部から監視・制御できる体制を業者と連携し構築",
        "・Claude Codeを活用し、各DX推進プロジェクトの背景(なぜ着手したか)・課題・解決に至った経緯を`CLAUDE.md`形式でドキュメント化。属人化しがちな意思決定の根拠を言語化し、自分以外の担当者でも経緯を理解できる状態を整備",
        "　→DX施策を“検討状態”から“実装・運用検証フェーズ”へ移行",
        "　→工事管理表、勤怠、LINE WORKS、就業規則、ネットワーク対応など複数テーマを、経営判断可能な粒度まで構造化",
        "　→現場・管理側の二重入力、個別確認、属人対応を減らす自動化・標準化施策を複数実装",
        "　→ドキュメント化により、保守・引き継ぎや他プロジェクトへの考え方の横展開が容易な状態を実現",
    ],
    "knowledge": "ANDPAD、KING OF TIME、LINE WORKS、Google Workspace、Chatwork、Zapier、GAS、Python、Claude Code、ネットワーク機器（HPE）",
})

entries.append({
    "company": "■モビルス株式会社（業務委託）",
    "biz": "事業内容：生成AIやノンボイス型SaaSなどのCX支援ソリューションを開発・提供",
    "period": "2025年4月\n～2025年7月",
    "summary": ["概要：生成AIを用いたSaaS製品の導入PM", "役割：プロジェクト管理、顧客折衝、プレゼン対応", "規模：5名"],
    "body": [
        "・SaaS導入プロジェクトにおいて、タスク・スケジュール管理、顧客折衝、ニーズ把握を通じたソリューション提案および導入支援を担当。",
        "　→顧客のニーズを喚起するため、提案型かつ選択肢を持たせて意向を確認。",
        "　→常に先を読んで新しい情報を提供し、更なるニーズを喚起。",
        "　→３ヶ月で２社のソリューション導入を実現。",
    ],
    "knowledge": "Anthropic、ChatGPT、Gemini、AWS、M365、Backlog",
})

entries.append({
    "company": "■NTTファイナンス株式会社（業務委託）",
    "biz": "事業内容：金融系システム プロジェクト推進PM",
    "period": "2024年11月\n～2025年3月",
    "summary": ["概要：金融系システム基盤更改プロジェクト推進PM", "役割：プロジェクトタスク管理、プレゼン対応、ドキュメント作成、要件定義書レビュー", "規模：30名"],
    "body": [
        "・チームが抱えるタスク、および打ち合わせで発生したタスクの整理、管理。",
        "　→100前後のタスクを6名に割り当て。進捗管理、日程管理の対応。",
        "・事業所長、部長、課長、他拠点所長向けの報告資料のシナリオ整理、資料作成。ベンダー向けの打合せシナリオ整理、資料作成。",
        "　→２つの開発プロジェクトに対し、メンバーと事前に意識合わせ対応。",
        "　→タスク進捗確認、宿題フォロー等のベンダーコントロール。",
        "　→事業所長、部長、課長、他拠点所長向けのプレゼン対応。",
        "　→ベンダーや他部署との打ち合わせファシリテーション。",
    ],
    "knowledge": "Figma、AWS、Java、M365、VDI、redmine、Backlog",
})

entries.append({
    "company": "■株式会社NTTドコモ（業務委託）",
    "biz": "事業内容：DXプロジェクト推進業務",
    "period": "2024年4月\n～2024年9月",
    "summary": ["概要：経営企画部のDXプロジェクト推進業務（PM）", "役割：業務効率化課題の整理および推進。業務効率化ツールの要件定義〜詳細設計", "規模：10名"],
    "body": [
        "・所属課長、プロパーと連携し、LLMを用いた要件定義のブレスト。",
        "　→DXプロジェクトの方向性を業務開始１ヶ月目で確定。",
        "　→抽出された課題の本質を追求する手法を、プロパーと共有。",
        "・所属課長、プロパーへ基本設計を提案し、保守・運用まで対応。",
        "　→月20個の定例議事録タスクの効率化（1h/人）に貢献。",
        "　→プロパーへツール設計方法、LLMの使い方の教育に尽力。",
    ],
    "knowledge": "Python、power automate、power automate desktop、M365、Copilot、VS CODE、ChatGPT 4o、Splashtop",
})

entries.append({
    "company": "■トヨタ自動車株式会社（パート勤務）",
    "biz": "事業内容：次世代燃料電池の材料探索業務",
    "period": "2023年7月\n～現在",
    "summary": ["概要：サステナブルな次世代燃料電池の材料探索業務", "役割：小型電池の試作、データ検証、Pythonを用いたデータ整理", "規模：7名"],
    "body": [
        "・プロパーと連携し、データ自動管理ツールの開発(要件定義～詳細設計)。小型電池の設計/テスト。",
        "　→フォルダ管理工数（1h/人）の削減に貢献。",
    ],
    "knowledge": "化学系知識、燃料電池業界知識、LCAに関する知識、CFPに関する知識、Python構築、メンテ、運用知識",
})

entries.append({
    "company": "■トヨタ自動車株式会社（パート勤務）",
    "biz": "事業内容：新規事業立ち上げ業務",
    "period": "2023年7月\n～現在",
    "summary": ["概要：新規事業に対するコンサルティング（社内有志活動の一環）", "役割：事業構想に対するコンサルティング業務", "規模：２名"],
    "body": [
        "・プロパーの太陽光発電を活用した新規事業に対し、要件定義、顧客折衝、マーケティング。",
        "　→事業目的、手段、ガントチャート見直しにより、最終選考まで進出。",
        "　→事業計画に必要なエッセンス（なぜやるか、何をするか、どうやるか）を主担当者と共に考え、プレゼン資料への落とし込みまでサポート。",
    ],
    "knowledge": "SNSマーケティング、自然農の栽培方法、自然栽培の栽培方法、耕作放棄地に関する法律、マーケティング知識、総合コンサルティング知識",
})

entries.append({
    "company": "■株式会社ドゥシステム（業務委託）",
    "biz": "事業内容：函南町の町おこし（新規事業検討段階）",
    "period": "2023年6月\n～2023年8月",
    "summary": ["概要：食×温泉×アスリートをベースとした町おこし事業の構想", "役割：事業構想に対するコンサルティング業務（2か月）", "規模：5名"],
    "body": [
        "・社外部長、社外課長と共に、要件定義、課題整理、ロードマップ見直し。",
        "　→３候補から新規事業として選抜に貢献。",
        "　→食、流通、販促、農薬、肥料などの現実問題ノウハウを顧客へ伝授。",
        "使用ツール：リーンキャンバス、企画書",
    ],
    "knowledge": "SNSマーケティング、自然農の栽培方法、自然栽培の栽培方法、耕作放棄地に関する法律、マーケティング知識、総合コンサルティング知識",
})

entries.append({
    "company": "■株式会社アッチェ",
    "biz": "事業内容：素材メーカー営業・マネジメント・人材育成（業務委託）",
    "period": "2021年2月\n～2023年5月",
    "summary": ["概要：人材育成、営業マネジメント業務の企画、担当（PM)", "役割：営業・マネジメント・人材育成", "規模：20名"],
    "body": [
        "・人事採用担当、後進教育、部内マネジメント、教育資料作成/プレゼン、SNSマーケティングの実施。",
        "　→11名の部下育成。120名の後進教育リーダーを担当。",
        "　→13名の自立に貢献。",
    ],
    "knowledge": "セールス、マーケティングに関する知識、AIDMA、コーチングスキル、脳科学知識、心理学知識",
})

entries.append({
    "company": "■株式会社メイテック",
    "biz": "事業内容：人材派遣事業（資本金：50億円／売上高：1071億40百万円／従業員数：8,080名 ※2022年3月31日現在）",
    "period": "2013年10月\n～2022年5月",
    "summary": ["派遣先：ジヤトコ株式会社", "概要：自動車部品（トランスミッション）の設計、開発実務", "役割：PM・DX推進・自動車部品（トランスミッション）の設計、開発", "規模：10名"],
    "body": [
        "・部品設計チーム間での仕様変更情報を一元管理するシステム構築プロジェクトを推進。",
        "・プロジェクトの推進、設計チームへの啓蒙活動の実施。あるべき業務プロセスのヒアリングを実施。要件定義。",
        "・Pythonを用いて開発プロセスを効率化するツールを設計・開発。",
        "　→設計手戻り削減により、約160時間/月の工数削減を達成。",
        "　→部品設計チーム間での情報共有がスムーズになり、チーム間の連携強化に貢献。",
        "　→仕様変更情報を一元管理するシステムを導入。業務プロセスの透明性と設計精度の向上に貢献。",
        "・国内外ベンダー、部署内外部長・課長へプレゼン、ガントチャート作成＆フォロー。",
        "　→仕様策定/トラブル対応。対メキシコ２案件、対ドイツ１案件を完遂。",
        "　→メキシコ人プロパー2名に対し、会議のファシリテーションを教育。",
    ],
    "knowledge": "システムズエンジニアリング、マネジメントスキル（仮説思考、MECEの考え方要因分析、KT法、KJ法）、PMBOK、流体力学、材料力学、熱力学、3Dモデリング、アセンブリ",
})

entries.append({
    "company": "■スリープロウィズテック株式会社",
    "biz": "事業内容：人材派遣",
    "period": "2011年10月\n～2013年9月",
    "summary": ["派遣先：東芝キャリア株式会社", "概要：輸送機械用エアコン性能試験実務", "役割：列車用空調機器の性能試験、信頼性試験の実務主担当（計２年）", "規模：３～４名で製品毎に担当分け"],
    "body": [
        "・プロパーと連携し、報告書の作成、海外顧客先にてメンテ対応、性能試験・環境試験用台車の基本設計。",
        "　→鉄道会社３社の列車空調機の設計に貢献。",
        "使用ツール：振動計、騒音計、ストロボ回転計、ＦＦＴアナライザ、サーマルレコーダー、ハイブリッドレコーダー、パワーメーター、クランプメーター、風速計、冷暖房試験用設備、絶縁抵抗試験器、耐電圧試験機、熱電対、ひずみゲージ、スリップリング、圧力センサ",
    ],
    "knowledge": "圧縮機、送風機、モータ、冷凍サイクル、筐体、板金、機構、配管、治具、振動、流体、圧力、冷媒、熱交換器",
})

entries.append({
    "company": "■日清紡ペーパープロダクツ株式会社",
    "biz": "",
    "period": "2010年4月\n～2011年3月",
    "summary": ["概要：高級紙の製造および抄紙機のメンテナンス", "役割：製造担当として高級紙の製造およびメンテナンス担当（１年）", "規模：２５名"],
    "body": [
        "１．パルプと原料を混ぜ合わせ、様々な高級紙の製造。",
        "２．抄紙機のメンテナンスおよび清掃。",
        "使用ツール：ＷｉｎｄｏｗｓＸＰ",
    ],
    "knowledge": "抄紙工学",
})

entries.append({
    "company": "■日清紡メカトロニクス株式会社",
    "biz": "",
    "period": "2008年4月\n～2010年3月",
    "summary": ["概要：太陽電池製造設備の設計", "役割：機械設計の実務主担当（２年）", "規模：１００名"],
    "body": [
        "1. 検査装置の設計：機構設計を元に、基本レイアウトの設計、組立図、部品図の設計。",
        "使用ツール：ＭＩＣＲＯ－ＣＡＤＡＭ、ＷｉｎｄｏｗｓＸＰ",
    ],
    "knowledge": "部品設計、詳細設計、筐体、生産設備、製図、機構、板金、材料、加工、光学、表面処理、締結・接合・接着",
})

for e in entries:
    block = [Paragraph(e["company"], company_style)]
    if e["biz"]:
        block.append(Paragraph(e["biz"], biz_style))
    block.append(entry_table(e["period"], e["summary"], e["body"], e["knowledge"]))
    story.append(KeepTogether(block))
    story.append(Spacer(1, 10))

h2("■語学")
body(["英語: ビジネスレベル。海外ベンダーとの会議ファシリテーションや資料作成の経験あり。"])

h2("■実績")
story.append(Paragraph("DX推進プロジェクト:", label_style))
body(["AWSやPythonを活用し、業務効率化を実現（例：定例議事録作成の自動化で1時間/人の削減）。総合建設業では、工事管理・勤怠・社内通知の自動化と就業規則改定を並行推進。"])
story.append(Paragraph("業務プロセス改善:", label_style))
body(["自動変速機設計部門にて、仕様変更情報を一元管理するシステムを構築。設計手戻り削減により、月160時間の工数削減を達成。"])
story.append(Paragraph("後進教育の推進:", label_style))
body(["部下11名の育成を通じて、チーム全体のスキルアップを実現。さらに、120名以上の若手育成リーダーとして、教育プログラムの構築と運用を担当。後進の13名を自立へ導く成果を上げる。"])

h2("■自己PR")
body([
    "私の強みは、経営層と現場の間にある認識差を構造化し、意思決定可能な資料・運用ルール・自動化ツールへ落とし込む力です。総合建設業でのDX・AI推進顧問としては、紙・Excel・チャット・SaaSが分断された業務を、ANDPAD・LINE WORKS・Google Workspace・Pythonなどを組み合わせて再設計し、就業規則改定やネットワーク整備まで一気通貫で推進してきました。",
    "都市と自然、テクノロジーと人との間を行き来しながら、栽培から事業企画、タスク管理まで一貫して推進できる点も強みです。週末は果樹園と畑を運営し、自然栽培・不耕起・無農薬の実践や、大豆・果樹の挿し木・保存食づくりなどを軸とした地域参加型イベントも企画・実施しています。畑の立ち上げ期には、1区画・1人から始めた運営を、現在は約20名超のメンバーが関わる共同運用体制へと拡大しました。",
    "プロジェクトマネージャーとして培った「全体像から逆算して段取りを組む力」と、現場・農園運営での「実地で人を巻き込む力」を掛け合わせ、企画から日常オペレーション、現地での作業支援までを包括的にカバーできます。加えて、要件定義力・タスク設計・資料作成・メンバー教育・SNS発信など、事業部全体をマネジメントするうえでの基盤スキルも備えています。",
    "幅広い経験と知識を元に、御社の抱える問題を解決するご提案ができると考えております。",
    "以上",
])

doc.build(story)
print("wrote", OUT)
