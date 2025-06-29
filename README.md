# Apexon--SCARF

## 🧠 Project Name: **SCARF**

**S**upermarket **C**hain **A**gent for **R**eplenishment & **F**orecasting

---

## ✅ What You’re Building

A smart autonomous agent that:

* Analyzes supermarket sales and inventory daily
* Identifies shortages
* Uses prompt-based intelligence to recommend replenishment strategies
* Avoids spoilage and delays
* Optionally automates data input/output (via Google Sheets or APIs)

---

## 👥 Team Plan: 3 Members

| Member      | Role                          | Responsibility                                             |
| ----------- | ----------------------------- | ---------------------------------------------------------- |
| 🧑‍💻 Dev 1 | **AI + Prompt Engineer**      | Design prompt flows, connect GPT to planning steps         |
| 📊 Dev 2    | **Data/Logic Engineer**       | Code the inventory/sales analysis, format data for prompts |
| 🧑‍🎨 Dev 3 | **UI/Integrator + Presenter** | Optional Streamlit UI, slide deck, final demo packaging    |

---

## 🪜 Project Timeline – 3-Day Plan (Adjustable)

| Day   | Goals                                                       | Owner     |
| ----- | ----------------------------------------------------------- | --------- |
| | Setup repo, write problem statement, create sample datasets | All       |
|       | Build Python logic: sales vs. inventory shortage calculator | Dev 2     |
|       | Write Prompt 1: Inventory Planning                          | Dev 1     |
|  | Connect Python output → LLM input                           | Dev 1 + 2 |
|       | Add Prompt 2: Risk + Spoilage Analyzer                      | Dev 1     |
|       | Design sample slides and demo UI (optional)                 | Dev 3     |
| | Final prompt chain, integrate results into UI or terminal   | All       |
|       | Add bonus features (Sheets/API/alerts)                      | Dev 3     |
|       | Rehearse pitch, finalize slides                             | All       |

---

## 💥 Real-World Extension Ideas (For Extra Edge)

| Feature                        | Tool/Method                  | What It Adds                                              |
| ------------------------------ | ---------------------------- | --------------------------------------------------------- |
| 📄 Google Sheets Input         | `gspread`, `pandas`          | Pull live sales/inventory data from shared sheets         |
| 📧 Auto Email Alerts           | `smtplib`, `Twilio`, Zapier  | Send reorder alerts to suppliers                          |
| 📈 Demand Forecasting          | `Prophet`, `sklearn`, or LLM | Predict future sales instead of using just today's        |
| 📊 Streamlit App               | `streamlit`, `plotly`        | Live dashboard for store manager to review & approve plan |
| 📦 RAG-style Supplier Matching | LangChain + embeddings       | Match best supplier based on previous success rate        |
| 🔄 Auto-agent Loop             | LangChain / CrewAI           | Continuous monitor, auto-run daily without trigger        |

---

## 📂 Deliverables for Submission

| Item                    | Description                                   |
| ----------------------- | --------------------------------------------- |
| ✅ Notebook/Code         | Python code to calculate shortages & call LLM |
| ✅ Prompt Scripts        | Clear documentation of prompt chain           |
| ✅ Sample Inputs/Outputs | Simulated inventory, sales, and GPT plan      |
| ✅ Slide Deck (5 slides) | Intro, problem, agent design, results, future |
| ✅ (Optional) Demo UI    | Streamlit interface to input & view results   |

---

## 🧱 Tech Stack Suggestion

| Area                            | Tool                                                      |
| ------------------------------- | --------------------------------------------------------- |
| Code + Logic                    | Python (pandas, matplotlib)                               |
| LLM Interface                   | OpenAI GPT-4 (via `openai` API or ChatGPT)                |
| Sheets/API                      | `gspread`, `requests`, or Zapier                          |
| UI (optional)                   | Streamlit                                                 |
| Prompt Orchestration (optional) | LangChain or CrewAI (if you want advanced agent chaining) |




