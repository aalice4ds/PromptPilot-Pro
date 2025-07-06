# PromptPilot-Pro
✨ A Prompt Engineering lab built with Gemini Pro that compares Zero-Shot, Few-Shot &amp; Chain-of-Thought prompting techniques with semantic scoring and beautiful visualizations.
# 🤖 PromptPilot Pro – A Prompt Engineering Lab Using Gemini AI

PromptPilot Pro is a unique and insightful project that compares **Zero-Shot**, **Few-Shot**, and **Chain-of-Thought** (CoT) prompt strategies using **Gemini Pro (Google Generative AI)**.

This lab helps you analyze, compare, and visualize how different prompts impact model responses, with an intuitive scoring system and beautiful charts. Ideal for **AI interns**, **prompt engineers**, and **LLM researchers**.

---

## 🎯 Project Goals

✔️ Evaluate different prompting techniques  
✔️ Score responses using **semantic similarity** 
✔️ Present results with elegant visualizations  
✔️ Ready for deployment as a **Streamlit app**  

---

## 📊 Prompt Strategies Compared

| Type                   | Description                                                                 |
|----------------------- |-----------------------------------------------------------------------------|
| **Zero-Shot**          | Model responds with no examples or context                                  |
| **Few-Shot**           | A few examples are given to guide the model                                 |
| **Chain-of-Thought**   | The model is encouraged to "think step-by-step"                             |

---

## 📈 Visual Insights

The following visualizations are generated to compare prompt outputs:

### 🕸 Radar Chart
Traits like Fluency, Relevance, Accuracy, Creativity  
![Radar Chart](images/radar_chart.png)

### 🍩 Donut Chart
Accuracy percentage comparison  
![Donut Chart](images/donut_chart.png)

### 📍 Lollipop Chart
Cosine similarity scores (semantic evaluation)  
![Lollipop Chart](images/lollipop_chart.png)

---

## 🧠 How We Score Prompts

- Uses `sentence-transformers` to generate embeddings
- Compares with a reference answer using **cosine similarity**
- Rating:
  - ✅ Above 0.85 → Excellent
  - 👍 0.60–0.85 → Good
  - ⚠️ Below 0.60 → Needs improvement

---

## 🔧 Tech Stack

| Tool/Library          | Purpose                          |
|-----------------------|----------------------------------|
| `google-generativeai` | Gemini Pro API integration       |
| `sentence-transformers` | Semantic similarity evaluation |
| `matplotlib`, `seaborn` | Visualizations                 |
| `streamlit` (optional)  | Interactive Web UI             |

---

## 📂 Project Structure

PromptPilot-Pro/
├── PromptPilotPro.ipynb # Main project notebook
├── requirements.txt # Python dependencies
├── README.md # This file
├── streamlit_app.py # Optional web version
└── images/
├── radar_chart.png
├── donut_chart.png
└── lollipop_chart.png


---

## 💻 How to Run

### ✅ Jupyter Notebook

```bash
git clone https://github.com/your-username/PromptPilot-Pro.git
cd PromptPilot-Pro
pip install -r requirements.txt
jupyter notebook
streamlit run streamlit_app.py
