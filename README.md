# Analyzer-GPT_with_AutoGen

An intelligent data analysis assistant that transforms natural language questions into executable Python code, delivering insights from your CSV data in seconds.

---

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776ab.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-ff4b4b.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-00a97f.svg)](https://platform.openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🎯 Overview

Analyzer-GPT is an AI-powered data analysis platform that bridges the gap between business questions and technical implementation. Simply upload your CSV dataset and ask questions in plain English—the system automatically generates, executes, and explains Python-based analyses.

### Key Features

- **Natural Language Interface**: Ask questions like "What drives customer churn?" or "Predict sales for next month"
- **Intelligent Code Generation**: Automatically writes optimized Python code using pandas, scikit-learn, and statistical libraries
- **Sandboxed Execution**: Secure code execution environment with safety guardrails
- **Visual Insights**: Generates publication-ready plots and visualizations
- **Narrative Explanations**: Provides context-aware interpretations of analytical results
- **Multiple Analysis Types**: Supports EDA, regression, clustering, forecasting, and more

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

```bash
# Clone the repository
git clone https://github.com/deshmukh-viraj/Analyzer_GPT_with_AutoGen.git
cd Analyzer_GPT

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### Launch Application

**Streamlit Web Interface** (Recommended):
```bash
streamlit run streamlit.py
```
Access at [http://localhost:8501](http://localhost:8501)

**CLI Interface**:
```bash
python main.py
```

---

## 📁 Project Structure

```
Analyzer_GPT/
├── agents/
│   ├── prompts/
│   │   └── DataAnalyzerPrompt.py   # System prompts and templates
│   ├── code_executor.py            # Secure code execution engine
│   └── data_analyzer.py            # LLM-powered analysis orchestrator
├── config/
│   ├── constants.py                # Configuration constants
│   ├── docker_utils.py             # Docker integration utilities
│   └── model_client.py             # OpenAI API client wrapper
├── models/
│   ├── analyzer.py                 # Core analysis models
│   └── team/
│       └── analyzer.py             # Team-based analysis components
├── temp/                           # Temporary execution files (auto-cleaned)
├── venv/                           # Virtual environment (git-ignored)
├── .env                            # Environment variables (git-ignored)
├── .gitignore
├── main.py                         # CLI entry point
├── streamlit.py                    # Web UI entry point
├── requirements.txt                # Python dependencies
└── README.md
```

---

## 💡 How It Works

### Analysis Pipeline

1. **Data Ingestion**: Upload CSV → automatic data profiling and type inference
2. **Question Processing**: NLP parsing to understand analytical intent
3. **Code Generation**: LLM generates context-aware Python analysis code
4. **Secure Execution**: Sandboxed environment runs code with resource limits
5. **Result Synthesis**: Combines outputs (plots, tables, statistics) with narrative insights
6. **Presentation**: Streamlit interface displays interactive results

### Architecture Components

- **Data Analyzer Agent**: Orchestrates the analysis workflow and manages LLM interactions
- **Code Executor**: Provides isolated execution environment with safety constraints
- **Model Client**: Handles Gemini API communication with retry logic and error handling
- **Prompt Templates**: Few-shot learning examples for consistent code generation

---

## 🔬 Example Use Cases

### Business Analytics
```
Question: "Identify top 3 factors influencing customer lifetime value"
→ Correlation analysis + feature importance visualization + predictive insights
```

### Time Series Forecasting
```
Question: "Forecast monthly revenue for next quarter"
→ Prophet/ARIMA model + confidence intervals + seasonality breakdown
```

### Exploratory Data Analysis
```
Question: "Show distribution of sales across regions with outliers highlighted"
→ Box plots + statistical summary + anomaly detection
```

### Machine Learning
```
Question: "Build a churn prediction model and show performance metrics"
→ Train/test split + model training + ROC curves + feature importance
```

---

### Data Privacy

- All data processing occurs locally
- Uploaded files are never persisted beyond session lifetime
- Only data summaries (not raw data) are sent to LLM APIs

---

## 🛠️ Configuration

### Model Settings

Edit `config/model_client.py` to customize:
- Model selection (GPT-3.5-turbo, GPT-4, etc.)
- Temperature and token limits
- Timeout and retry parameters

### Execution Parameters

Modify `config/constants.py` for:
- Temporary file locations
- Execution timeout values
- Supported file formats

---

## 📊 Supported Analysis Types

- **Descriptive Statistics**: Summary statistics, distributions, correlations
- **Visualization**: Histograms, scatter plots, heatmaps, time series plots
- **Statistical Testing**: Hypothesis tests, A/B testing, significance tests
- **Machine Learning**: Classification, regression, clustering
- **Time Series**: Forecasting, trend analysis, seasonality decomposition
- **Data Quality**: Missing value analysis, outlier detection, data profiling

---

## 🐛 Troubleshooting

### Common Issues

**API Key Error**:
- Verify `.env` file exists and contains valid OpenAI API key
- Ensure no extra spaces in key value

**Module Import Errors**:
- Confirm virtual environment is activated
- Run `pip install -r requirements.txt` again

**Streamlit Port Conflict**:
- Specify different port: `streamlit run streamlit.py --server.port 8502`

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Viraj Deshmukh**
---

## 🙏 Acknowledgments

- OpenAI for GPT models
- Streamlit for the web framework
- The open-source Python data science community

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ and Python

</div> 
