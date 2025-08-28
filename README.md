# 📊 Feedback Analyzer (Sentiment Analysis using AI)

## 🔹 Overview

This project analyzes user feedback using **AI (NLP - Natural Language Processing)**. It performs **Sentiment Analysis** on customer reviews/feedback and generates comprehensive results with:

- **Sentiment Classification** (Positive / Negative / Neutral)
- **Confidence Score** for each prediction

### Future Improvements
- **Text Similarity Analysis** to group similar feedback
- **Topic Clustering** to identify major issues & praise areas
- **Sentiment Trends** over time analysis

## 🔹 Features

- ✨ Reads customer feedback from CSV files
- 🤖 Uses **Hugging Face Transformers** (`pipeline("sentiment-analysis")`)
- 📊 Saves results with **sentiment + confidence score** into a new CSV
- 🔧 Easy to extend with additional NLP tasks
- ⚡ Fast processing with pre-trained AI models

## 🔹 Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.9+ |
| **Data Processing** | Pandas |
| **AI/ML Framework** | Hugging Face Transformers |
| **Model Backend** | PyTorch / TensorFlow |
| **File Format** | CSV |

## 🔹 Installation

### Prerequisites
- Python 3.9 or higher
- Git

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/feedback-analyzer.git
   cd feedback-analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   # Linux/Mac
   python -m venv env
   source env/bin/activate
   
   # Windows
   python -m venv env
   env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🔹 Usage

### Input Format

1. **Prepare your input file** as `feedback.csv` in the project folder:
   ```csv
   feedback
   The app is very user-friendly!
   I love how simple the interface is.
   The app crashes often when I try to upload files.
   Average experience, nothing special.
   ```

### Running the Analyzer

2. **Execute the analyzer:**
   ```bash
   python feedback_analyzer.py
   ```

### Output Format

3. **Results will be saved** in `results.csv`:
   ```csv
   feedback,sentiment,confidence
   The app is very user-friendly!,POSITIVE,0.99
   I love how simple the interface is.,POSITIVE,0.99
   The app crashes often when I try to upload files.,NEGATIVE,0.98
   Average experience, nothing special.,NEUTRAL,0.85
   ```

## 🔹 Example Results

| Feedback | Sentiment | Confidence |
|----------|-----------|------------|
| The app is very user-friendly! | POSITIVE | 0.99 |
| I love how simple the interface is. | POSITIVE | 0.99 |
| The app crashes often when I try to upload files. | NEGATIVE | 0.98 |
| Average experience, nothing special. | NEUTRAL | 0.85 |

## 📁 Project Structure

```
feedback-analyzer/
├── feedback_analyzer.py      # Main analysis script
├── requirements.txt          # Python dependencies
├── feedback.csv             # Input file (user-provided)
├── results.csv              # Output file (generated)
├── README.md                # Project documentation
```

## 🔹 Dependencies

Create a `requirements.txt` file with:
```txt
pandas>=1.5.0
transformers>=4.21.0
torch>=1.12.0
```

## 🔹 Future Scope

- ✅ **Similarity Analysis**: Group related feedback using text similarity
- ✅ **Sentiment Summary**: Generate overall customer sentiment reports
- ✅ **Web Application**: Deploy as a web app using Flask/Django + React
- ✅ **Real-time Analysis**: Process feedback in real-time via API
- ✅ **Multi-language Support**: Analyze feedback in multiple languages
- ✅ **Advanced Visualizations**: Create charts and graphs for sentiment trends

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔹 Author

👨‍💻 **Developed by [Dulkar]**
