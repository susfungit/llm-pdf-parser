# 🧠 Ingesto Assistant – AI-Powered Data Ingestion Framework

Welcome to **Ingesto Assistant**, a modular, agent-driven platform for automating the ingestion of vendor data files (primarily Excel/CSV), mapping them to your internal schema, transforming and validating the data, and exporting clean output for use.

---

## 🚀 Features

- ✅ Auto-detects incoming files and vendor
- ✅ LLM/AI-ready schema mapping engine
- ✅ Transformation agent with custom rules per vendor
- ✅ Validation agent with schema definitions
- ✅ Retry & feedback loop for human-in-the-loop corrections
- ✅ Dash-based visual UI for mapping approval
- ✅ Log viewer UI for audit trail of processed files
- ✅ Orchestrator that combines auto/manual flows
- ✅ Ready for Docker deployment

---

## 📁 Folder Structure

```
ingesto_assistant/
├── app/                    # Core ingestion logic
│   ├── controller.py
│   ├── auto_processor.py
│   ├── ingestion_orchestrator.py
│   ├── schema_mapper.py
│   ├── feedback_agent.py
│   ├── transformation_agent.py
│   ├── validator_agent.py
│   ├── notifier.py
│   ├── vendor_identifier.py
│   └── monitor_agent.py

├── config/
│   ├── mappings/           # {vendor}_mapping.json
│   └── transformations/    # {vendor}_transformations.json

├── data/
│   ├── incoming/           # Upload new vendor files here
│   ├── output/             # Final transformed CSVs
│   └── auto_output/        # Auto-processed files (no manual review)

├── approval_ui/
│   └── layout.py           # Dash layout for approval screen

├── dashboard_ui/
│   └── log_viewer.py       # Dash layout for logs

├── dashboard.py            # Log viewer webapp entry point
├── logs/
│   └── processed_files.txt

├── main.py                 # Starts schema mapping UI
└── Dockerfile              # Docker build instructions
```

---

## ⚙️ How to Use

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run approval UI for new vendor mappings
```bash
python main.py
```

### 3. Run log viewer dashboard
```bash
python dashboard.py
```

### 4. Start orchestrator (auto/manual flow)
```bash
python app/ingestion_orchestrator.py
```

Files placed in `data/incoming/` will be auto-processed if vendor is known, or routed to UI otherwise.

---

## 🧪 Adding a New Vendor

1. Upload their raw `.csv` file to `data/incoming/`
2. If vendor is new, UI will ask for mapping approval
3. Optionally define transformation rules under `config/transformations/{vendor}_transformations.json`

---

## ✍️ Feedback Buttons
- 👍 Approve mapping → Logs and saves mapping
- 👎 Reject → Triggers new AI-suggested mapping (if connected) or refreshes the match

---

## 📦 Docker Deployment
```bash
docker build -t ingesto-assistant .
docker run -p 8501:8501 ingesto-assistant
```

---

## 🧠 LLM Integration (Optional)
You can plug in OpenAI/GPT/Claude to:
- Suggest header-to-schema mappings
- Auto-generate transformation formulas
- Propose validation rules

---

## 📧 Coming Soon

- Email notifications for approval
- Role-based access control
- Metrics dashboard (processed files, failure rate, vendor stats)

---

## 👨‍💻 Authors
Built with ❤️ using Dash, Python, Pandas, and modular agents.