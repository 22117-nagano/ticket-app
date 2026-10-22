import streamlit as st

st.set_page_config(
    page_title="イベント前売り券 販売所", page_icon="🎫", layout="centered"
)

st.title("🎫 イベント前売り券 購入ページ")
st.write("ご希望の商品を選んで決済画面へ進んでください。")

st.markdown("---")

# 商品1：1本 150円
st.subheader("🍢 1本")
st.write("価格: **150円**")
if st.button("1本を購入する"):
  st.success("以下のリンクからお支払いをお願いします！")
  st.markdown("[👉 PayPay送金ページを開く](https://qr.paypay.ne.jp/p2p01_c2MZuCGoCeyv9mLB)")
  st.info("※お支払い完了画面のスクショをスタッフにお見せください。")

st.markdown("---")

# 商品2：もも3本 250円
st.subheader("🍢 もも3本")
st.write("価格: **250円**")
if st.button("もも3本を購入する"):
  st.success("以下のリンクからお支払いをお願いします！")
  st.markdown("[👉 PayPay送金ページを開く](https://qr.paypay.ne.jp/p2p01_pRBtYbjovwVz6Cpt)")
  st.info("※お支払い完了画面のスクショをスタッフにお見せください。")

st.markdown("---")

# 商品3：三種3本 300円
st.subheader("🍢 三種3本")
st.write("価格: **300円**")
if st.button("三種3本を購入する"):
  st.success("以下のリンクからお支払いをお願いします！")
  st.markdown("[👉 PayPay送金ページを開く](https://qr.paypay.ne.jp/p2p01_duKTj45nemf7gA64)")
  st.info("※お支払い完了画面のスクショをスタッフにお見せください。")

# 購入ボタンが押された後の「完了画面（証明・スクショ用）」
else:
  st.success("🎉 決済手続きに進みます！")
  st.markdown(
      f"### 選択商品: **{st.session_state.item_name} ({st.session_state.price}円)**"
  )

  st.warning(
      "⚠️ **手順**\n"
      "1. 下のボタンからお支払いをお願いします。\n"
      "2. **お支払いが完了したら、この画面をスクリーンショット保存してください。**\n"
      "3. 当日の受付でこの画面のスクショをご提示ください。"
  )

  # PayPayのリンク（店舗用や指定金額リンクに変更可能）
  st.markdown(
      f"[👉 PayPay送金画面を開く (¥{st.session_state.price})](https://paypay.me/your_id)"
  )

  st.markdown("---")

  if st.button("← 商品選びに戻る"):
    st.session_state.purchased = False
    st.rerun()
