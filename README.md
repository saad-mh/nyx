# ZYNTH Labs – Project Nyx

Nyx is a hybrid, autonomous personal assistant being developed under **ZYNTH Labs**. The long‑term vision is to build a Jarvis‑style background agent that silently manages calendar, memory, tasks, and multimodal inputs while only interrupting when necessary.

This repository currently contains the **Phase 1 foundation**:

* Modular agent loop
* Google Calendar integration
* Safety‑gated execution
* Swappable LLM backend
* Cost tracking scaffolding

---

##  Core Philosophy

* **Silent by default**: Nyx executes low‑risk tasks without notifying.
* **Plan before act**: Explicit analysis -> planning -> execution.
* **Human in the loop** for medium/high‑risk actions.
* **Local‑first mindset** with optional cloud fallback.
* **Strict modularity** so every component can be swapped later.

---

## 📁 Project Structure

```
project_root/
│
├── main.py                # Scheduler + main Nyx loop
├── config.py              # Secrets & pricing (gitignored)
│
├── agent/
│   ├── __init__.py
│   ├── collector.py       # Pulls calendar/context
│   ├── reasoning.py       # Analysis + planning (LLM)
│   ├── executor.py        # Executes safe actions
│   └── logger.py          # Central logging
│
├── llm/
│   ├── __init__.py
│   └── query.py           # LLM abstraction layer (OpenAI for now)
│
├── integrations/
│   ├── __init__.py
│   └── calendar_client.py # Google Calendar integration
│
├── credentials.json       # Google OAuth (local only, gitignored)
├── token.json             # Google OAuth token (auto‑generated, gitignored)
└── requirements.txt
```

---

## ⚙️ Current Capabilities (Phase 1)

* Authenticated Google Calendar access (read/write)
* Periodic background scheduler (APScheduler)
* LLM‑driven situation analysis
* LLM‑driven action planning in strict JSON
* Safety‑gated execution (auto‑run only low‑risk actions)
* Console logging of all actions
* Cost estimation scaffolding (INR‑aware)

---

## 🚧 Current Status

⚠️ **Paused due to API credit requirement.**

The OpenAI API now requires **prepaid credits even for testing**. Until credits are added or a local LLM backend is wired in, Nyx’s reasoning loop is paused.

All non‑LLM components (calendar, scheduler, executor) are already in place and ready.

---

## 🔐 Security Rules

* `config.py`, `credentials.json`, and `token.json` are **never committed**.
* OpenAI key is restricted to **Responses API only**.
* Google OAuth app is in **testing mode with whitelisted users only**.
* All actions require explicit **risk classification** before execution.

---

## ▶️ How Nyx Runs (When Credits Are Available)

```bash
python main.py
```

* Nyx wakes up every `AGENT_INTERVAL_MINUTES`.
* Pulls calendar context.
* Runs **analysis → planning → execution**.
* Executes only low‑risk actions silently.
* Logs everything to the console.

---

## 🧪 Development Mode

For offline testing without spending money:

* Replace `llm/query.py` with an **Ollama‑based local LLM client**.
* Keep the rest of the architecture unchanged.

---

## 🧩 Long‑Term Vision

* Multimodal perception (image, video, audio)
* Long‑term memory with embeddings
* Local inference via GPT‑OSS / LLaMA / Qwen
* Voice wake‑word + speech I/O
* Hardware hub (edge device)

---

## 📝 TODO (Live Roadmap)

### Phase 1 – Stabilization

* [ ] Add terminal‑based confirmation flow for medium‑risk actions
* [ ] Add persistent action logs in a database
* [ ] Add monthly cost aggregation + budget alerts
* [ ] Add robust JSON schema validation for planner outputs
* [ ] Graceful fallback when LLM API is unavailable

### Phase 2 – Memory

* [ ] Design long‑term memory schema (preferences, facts, habits)
* [ ] Add vector database for semantic memory
* [ ] Add explicit user confirmation for memory writes

### Phase 3 – Multimodal

* [ ] Image parsing pipeline (OCR + vision model)
* [ ] Screenshot/UI understanding
* [ ] Whisper‑based speech‑to‑text
* [ ] Audio output (TTS)

### Phase 4 – Local‑First Inference

* [ ] Swap OpenAI backend with Ollama
* [ ] Test GPT‑OSS / Qwen / LLaMA models
* [ ] Add routing between local brain and cloud fallback

### Phase 5 – Autonomy & UX

* [ ] Attention / interruption scoring
* [ ] Focus‑mode awareness
* [ ] Daily silent summaries
* [ ] Minimal UI dashboard

---

## 🏷️ Naming

* Organization: **ZYNTH Labs**
* Assistant: **Nyx**
* Current Version: `Nyx v0.x (Foundation Phase)`

Name changes only occur on **major version shifts**.

---

## 📌 Resume Point

When credits are available, the next action is:

1. Reactivate OpenAI calls
2. Run first live autonomous calendar cycle
3. Enable confirmation flow for medium‑risk actions

---

*ZYNTH Labs - Building silent systems that think first and speak only when necessary.*
