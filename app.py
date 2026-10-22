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
