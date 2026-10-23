import streamlit as st

st.set_page_config(
    page_title="イベント前売り券 販売所", page_icon="🐓", layout="centered"
)

# セッション状態を使って購入完了状態を管理
if "purchased" not in st.session_state:
  st.session_state.purchased = False
  st.session_state.item_name = ""
  st.session_state.price = 0

st.title("🎫 イベント前売り券 購入ページ")

# まだ購入手続きをしていない場合
if not st.session_state.purchased:
  st.write("ご希望の商品を選んで決済へ進んでください。\n""デジタル前売り券のお支払い方法はPayPayのみです。\n""現金で前売り券をご購入される方は、16:00までに1Fのパワエレ実験室へご訪問ください。\n""三種はもも・鶏皮・ねぎまのセットです")
  st.markdown("---")

  # 1本 150円
  st.subheader("🐓 1本（150円）")
  if st.button("1本を購入する"):
    st.session_state.purchased = True
    st.session_state.item_name = "1本"
    st.session_state.price = 150
    st.rerun()

  # もも3本 250円
  st.subheader("🐓 もも3本（250円）")
  if st.button("もも3本を購入する"):
    st.session_state.purchased = True
    st.session_state.item_name = "もも3本"
    st.session_state.price = 250
    st.rerun()

  # 三種3本 300円
  st.subheader("🐓 三種1セット（300円）")
  if st.button("三種1セットを購入する"):
    st.session_state.purchased = True
    st.session_state.item_name = "三種1セット"
    st.session_state.price = 300
    st.rerun()

# 購入ボタンが押された後の「完了画面（証明・スクショ用）」
else:
  st.success("🎉 決済手続きに進みます！")
  st.markdown(
      f"### 選択商品: **{st.session_state.item_name} ({st.session_state.price}円)**"
  )

  st.warning(
      "⚠️ **手順**\n"
      "1. 下のボタンからお支払いをお願いします。\n"
      "2. お支払いが完了したら、PayPayの返信機能からデジタル前売り券URLを送信します。\n"
      "(前売り券の画面はリロードしても更新されません。)\n"
      "3. 当日の受付で前売り券をご提示ください。\n"
  )

  # ▼▼▼ ここで金額ごとにURLを切り替えています ▼▼▼
  if st.session_state.price == 150:
    paypay_url = "https://qr.paypay.ne.jp/p2p01_c2MZuCGoCeyv9mLB"  # ←150円用のURLに変更
  elif st.session_state.price == 250:
    paypay_url = "https://qr.paypay.ne.jp/p2p01_pRBtYbjovwVz6Cpt"  # ←250円用のURLに変更
  else:
    paypay_url = "https://qr.paypay.ne.jp/p2p01_duKTj45nemf7gA64"  # ←300円用のURLに変更
  # ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

  st.markdown(
      f"[👉 PayPay送金画面を開く (¥{st.session_state.price})]({paypay_url})"
  )

  st.markdown("---")

  if st.button("← 商品選びに戻る"):
    st.session_state.purchased = False
    st.rerun()
