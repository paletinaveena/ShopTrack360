# # app.py

# import streamlit as st
# import pandas as pd
# import os
# import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.set_page_config(page_title="ShopTrack360", layout="wide")

# st.title("ShopTrack360")
# st.markdown("Customer Retention and Engagement Optimization on an E-Commerce Platform")

# # === Load Data === #
# @st.cache_data
# def load_csv(file_path):
#     if os.path.exists(file_path):
#         return pd.read_csv(file_path)
#     else:
#         st.warning(f"⚠️ File not found: `{file_path}`")
#         return pd.DataFrame()

# # Load customer features and churn predictions
# customer_df = load_csv("/Users/naveenapaleti/Projects/ShopTrack360/data/customer_features.csv")
# churn_df = load_csv("/Users/naveenapaleti/Projects/ShopTrack360/data/churn_predictions.csv")

# # === Section: Churn Summary === #
# st.subheader("Churn Risk Overview")

# if not churn_df.empty:
#     total_users = churn_df.shape[0]
#     predicted_churn = churn_df['churn_pred'].sum()
#     avg_churn_prob = churn_df['churn_prob'].mean()

#     col1, col2, col3 = st.columns(3)
#     col1.metric("Total Users", f"{total_users:,}")
#     col2.metric("Predicted to Churn", f"{predicted_churn:,}")
#     col3.metric("Avg Churn Probability", f"{avg_churn_prob:.2%}")

#     fig = px.histogram(churn_df, x='churn_prob', nbins=20,
#                        title="Churn Probability Distribution",
#                        color_discrete_sequence=['indianred'])
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.info("Upload or generate `churn_predictions.csv` to populate churn metrics.")

# # === Section: User Feature Explorer === #

# with st.expander("🔍 Explore User Features", expanded=False):
#     if not customer_df.empty:
#         st.subheader("Customer Data")
#         st.dataframe(customer_df, use_container_width=True)

#         with st.form("feature_plot_form"):
#             all_columns = customer_df.columns.tolist()
#             selected_columns = st.multiselect("Select columns to visualize", all_columns)
#             plot_submit = st.form_submit_button("📊 Plot Selected Features")

#         if plot_submit:
#             if selected_columns:
#                 for col in selected_columns:
#                     plt.figure(figsize=(6, 3))

#                     # Auto-detect column type
#                     if customer_df[col].nunique() <= 10:
#                         # Categorical / Binary Feature
#                         sns.countplot(x=col, data=customer_df)
#                         plt.title(f"Distribution of {col}")
#                     else:
#                         # Numeric Feature
#                         sns.histplot(customer_df[col], kde=True, bins=30)
#                         plt.title(f"Histogram of {col}")

#                     plt.tight_layout()
#                     st.pyplot(plt)
#                     plt.clf()
#             else:
#                 st.warning("Please select at least one column to visualize.")
#     else:
#         st.info("Upload or generate `customer_features.csv` to begin analysis.")

# # === Footer === #
# st.markdown("---")
# st.markdown("Author: Naveena Paleti")
# st.markdown(f"[LinkedIn]({"https://www.linkedin.com/in/naveena-paleti/"})  |  [GitHub]({"https://github.com/paletinaveena"})")



# app.py

import streamlit as st
import pandas as pd
import os
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="ShopTrack360", layout="wide")

# === Title & Header === #
st.title("📦 ShopTrack360 Dashboard")
st.markdown("**Customer Retention and Engagement Optimization for E-Commerce**")

# === Load Data Function === #
@st.cache_data
def load_csv(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        st.warning(f"⚠️ File not found: `{file_path}`")
        return pd.DataFrame()

# === Load Datasets === #
customer_df = load_csv("data/customer_features.csv")
churn_df = load_csv("data/churn_predictions.csv")

# === Section 1: Churn Risk Overview === #
st.markdown("## 📉 Churn Risk Summary")

if not churn_df.empty:
    total_users = churn_df.shape[0]
    predicted_churn = churn_df['churn_pred'].sum()
    avg_churn_prob = churn_df['churn_prob'].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Users", f"{total_users:,}")
    col2.metric("Predicted to Churn", f"{predicted_churn:,}")
    col3.metric("Avg Churn Probability", f"{avg_churn_prob:.2%}")

    fig = px.histogram(
        churn_df,
        x='churn_prob',
        nbins=20,
        title="Distribution of Churn Probabilities",
        color_discrete_sequence=['indianred']
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("🔍 Upload or generate `churn_predictions.csv` to view churn insights.")

# === Section 2: User Feature Explorer === #
st.markdown("## 📊 Explore Customer Features")

if not customer_df.empty:
    with st.expander("Click to view raw data and plot feature distributions"):
        st.dataframe(customer_df.head(50), use_container_width=True)

        with st.form("feature_plot_form"):
            selected_columns = st.multiselect("Select columns to visualize", customer_df.columns.tolist())
            plot_submit = st.form_submit_button("Plot Selected Features")

        if plot_submit and selected_columns:
            for col in selected_columns:
                fig, ax = plt.subplots(figsize=(6, 3))

                if customer_df[col].nunique() <= 10:
                    sns.countplot(x=col, data=customer_df, ax=ax)
                    ax.set_title(f"Count of {col}")
                else:
                    sns.histplot(customer_df[col], kde=True, bins=30, ax=ax)
                    ax.set_title(f"Distribution of {col}")

                st.pyplot(fig)
        elif plot_submit:
            st.warning("⚠️ Please select at least one column to visualize.")
else:
    st.info("📁 Upload or generate `customer_features.csv` to explore features.")

# === Footer === #
st.markdown("---")
st.markdown("Created by **Naveena Paleti**  |  [LinkedIn](https://www.linkedin.com/in/naveena-paleti/) | [GitHub](https://github.com/paletinaveena)")
