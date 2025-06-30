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


## 📘  ER Diagram Entities with Real-World Data Fields

---

### 🧾 **Customer Sales Data**

| Field                | Description                                            |
| -------------------- | ------------------------------------------------------ |
| `SaleID` (PK)        | Unique sale transaction ID                             |
| `CustomerID` (FK)    | Linked to customer master table                        |
| `ItemID` (FK)        | Purchased product ID                                   |
| `QuantitySold`       | Number of units sold                                   |
| `SaleDate`           | Timestamp of sale                                      |
| `Channel`            | POS / Online / App                                     |
| `Returned`           | Boolean: was it returned?                              |
| `Preordered`         | Boolean: if item was preordered (out-of-stock at sale) |
| `PurchaseFrequency`  | Derived: daily/weekly/monthly                          |
| `CustomerTotalSpend` | Aggregate of customer's past purchases                 |

---

### 👤 **Customer Data** (New table)

| Field             | Description                           |
| ----------------- | ------------------------------------- |
| `CustomerID` (PK) | Unique customer ID                    |
| `Name`            | Full name                             |
| `PhoneNumber`     | Contact                               |
| `FrequentItems`   | List of frequently purchased item IDs |
| `LifetimeValue`   | Total amount spent                    |
| `ReturnsCount`    | Number of returns made                |

---

### 🛒 **Inventory Data**

| Field                         | Description                                     |
| ----------------------------- | ----------------------------------------------- |
| `ItemID` (PK)                 | Product SKU / ID                                |
| `ItemName`                    | Display name                                    |
| `StockQty`                    | Total quantity in stock                         |
| `Location`                    | Store or warehouse                              |
| `VendorID` (FK)               | Linked to vendor                                |
| `CategoryID` / `CategoryName` | Product grouping                                |
| `ProductRating`               | Average customer rating                         |
| `ShelfLifeDays`               | Days until expiry (average)                     |
| `ExpiryDateBatch`             | Specific expiry per batch                       |
| `BatchID`                     | If multiple expiry dates for same product exist |
| `ReturnedQty`                 | Total quantity returned by customers            |

---

### 🚚 **Vendor Orders Data**

| Field           | Description                          |
| --------------- | ------------------------------------ |
| `OrderID` (PK)  | Vendor order ID                      |
| `VendorID` (FK) | Supplier                             |
| `ItemID` (FK)   | Item ordered                         |
| `OrderDate`     | Date ordered                         |
| `QtyOrdered`    | Quantity                             |
| `LeadTimeDays`  | Time to fulfill order                |
| `IsFulfilled`   | Boolean                              |
| `DeliveryDate`  | Actual delivery                      |
| `ReturnRate`    | % of items returned from this vendor |

---

### 🏢 **Vendor Master Data** (New Table)

| Field               | Description                                      |
| ------------------- | ------------------------------------------------ |
| `VendorID` (PK)     | Unique supplier ID                               |
| `VendorName`        | Display name                                     |
| `SuppliedItemIDs`   | List of item IDs supplied                        |
| `VendorRating`      | Derived from return rate, lead time, reliability |
| `PreferredCategory` | Optional: specialize in dairy, grains, etc.      |

---

## 🧠 Notes for Beginners

* You can **simulate batch expiry** using the same `ItemID` with different `BatchIDs` and `ExpiryDate`s.
* To track **product return rates**, link customer sales (returned items) back to `ItemID` and `VendorID`.
* Use **groupby + aggregate in pandas** to simulate `CustomerTotalSpend`, `FrequentItems`, or `VendorRating`.



CORE LOGIC
---

## 🎯 Objective Recap for Logic Layer

> Build the logic to **analyze supermarket data** (Inventory, Sales, Vendor) and produce:

* 🛒 Shortage alerts
* 📦 Reorder quantity suggestions
* 🧪 Spoilage/expiry risks
* 🔁 Vendor reliability insights
* 🧠 Preprocessed data for GPT prompt input

---

## ✅ Step-by-Step Logic Plan (Beginner-Friendly)

We'll divide the logic into **3 components**, each of which one team member can start with:

---

### 🔹 Step 1: Inventory Logic

👤 Owned by: Dev 1

| Goal                        | Action                                        |
| --------------------------- | --------------------------------------------- |
| 🛒 Identify low stock items | If `StockQty` < threshold (e.g. 20)           |
| 📆 Flag near-expiry batches | Filter `ExpiryDateBatch` within next 5–7 days |
| 🧾 Group by ProductID       | Aggregate batches, calculate total quantity   |
| 📌 Output                   | List of products needing reorder or disposal  |

---

### 🔸 Step 2: Sales + Customer Logic

👤 Owned by: Dev 2

| Goal                              | Action                                                |
| --------------------------------- | ----------------------------------------------------- |
| 📈 Find top-selling items         | `groupby(ItemID).sum(QuantitySold)` over last 30 days |
| 🔁 Find frequently returned items | Filter `Returned == True`, count by ItemID            |
| 🧍‍♀️ Track frequent customers    | Count purchases per `CustomerID`, show top 3 items    |
| 📌 Output                         | Popular items, customer insights, risky products      |

---

### 🔺 Step 3: Vendor Logic

👤 Owned by: Dev 3

| Goal                              | Action                                            |
| --------------------------------- | ------------------------------------------------- |
| 🚚 Calculate vendor lead time avg | `mean(LeadTimeDays)` per VendorID                 |
| 🔁 Track vendor return rates      | Average `ReturnRate` per vendor from VendorOrders |
| 🏆 Rate vendors                   | Score them based on fulfillment and return rates  |
| 📌 Output                         | Ranked vendor table, per product supplier mapping |

---

## 🧱 Folder & File Setup Suggestion

In your repo (PyCharm):

```
SCARF/
├── core/
│   ├── inventory_logic.py
│   ├── sales_logic.py
│   └── vendor_logic.py
```

Each file contains:

* `load_csv()` function
* `run_analysis()` function
* Optional: `to_prompt_format()` if preparing for GPT

---
