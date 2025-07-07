{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9d11db2a-4713-4dc4-b7e7-37fb83947c6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-08 02:53:18.145 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-07-08 02:53:18.147 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# ----------------------------\n",
    "# 1️⃣ App Title\n",
    "# ----------------------------\n",
    "st.title(\"📊 Codeforces User Analytics (Demo)\")\n",
    "st.write(\n",
    "    \"This is a demo. Enter a handle to see how it will look.\"\n",
    ")\n",
    "\n",
    "# ----------------------------\n",
    "# 2️⃣ Input box\n",
    "# ----------------------------\n",
    "handle = st.text_input(\"🔎 Enter Codeforces handle:\", value=\"demo_user\")\n",
    "\n",
    "if handle:\n",
    "    st.success(f\"Pretending to fetch data for: **{handle}** ...\")\n",
    "\n",
    "    # ----------------------------\n",
    "    # 3️⃣ Fake rating data\n",
    "    # ----------------------------\n",
    "    dummy_rating_data = {\n",
    "        'contestName': ['Contest A', 'Contest B', 'Contest C'],\n",
    "        'oldRating': [1200, 1250, 1300],\n",
    "        'newRating': [1250, 1300, 1350],\n",
    "        'rank': [500, 400, 350]\n",
    "    }\n",
    "    rating_df = pd.DataFrame(dummy_rating_data)\n",
    "\n",
    "    st.subheader(\"📈 Rating Changes\")\n",
    "    st.dataframe(rating_df)\n",
    "    st.line_chart(rating_df['newRating'])\n",
    "\n",
    "    # ----------------------------\n",
    "    # 4️⃣ Fake submissions data\n",
    "    # ----------------------------\n",
    "    dummy_problems = {\n",
    "        'Problem': ['Two Sum', 'Binary Search', 'Graph Paths'],\n",
    "        'Verdicts': [['OK', 'WRONG_ANSWER'], ['OK'], ['TIME_LIMIT_EXCEEDED']],\n",
    "        'Tags': [['math'], ['binary search'], ['graphs']]\n",
    "    }\n",
    "    problem_df = pd.DataFrame(dummy_problems)\n",
    "\n",
    "    st.subheader(\"🗂️ Problems Attempted\")\n",
    "    st.dataframe(problem_df)\n",
    "\n",
    "    # ----------------------------\n",
    "    # ✅ Placeholder chart\n",
    "    # ----------------------------\n",
    "    st.subheader(\"✅ Coming Soon: More Stats!\")\n",
    "\n",
    "    st.write(\"Here you can add pie charts, bar charts, and more analysis.\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
