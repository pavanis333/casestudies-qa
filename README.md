# 🏛️ UPSC Ethics Hub

A localized, offline-first React application designed to help UPSC aspirants prepare for **GS Paper IV (Ethics)**. It features an interactive library of case studies, a practice mode with hidden model answers, and flashcards for rapid ethical reasoning.

## 🚀 Features

- **Case Study Library**: Browse real UPSC case studies from 2013-2025.
- **Practice Mode**: Test your ethical decision-making by hiding model answers until you're ready.
- **Flashcards**: Randomly generated dilemma scenarios for quick recall.
- **Progress Tracking**: Tracks "read" and "practiced" cases using LocalStorage.
- **Data Management**: Export and Import your progress to keep your data safe.
- **Favorites**: Bookmark difficult cases for later review.
- **Advanced Search & Filters**: Filter by Year and Category, with search term highlighting.
- **Responsive Design**: Modern, glassmorphism-inspired UI that works on all devices.

## 🛠️ Tech Stack

- **Framework**: React + Vite
- **Styling**: Vanilla CSS (Variables, HSL colors, Glassmorphism)
- **Data Processing**: Python (`pdfplumber` for extraction)

## 💻 Developer Guide

### Prerequisites

- **Node.js** (v16 or higher)
- **npm** (v7 or higher)
- **Python 3.10+** (only if you need to update case study data)
- **uv** (recommended for Python dependency management)

### 1. Installation

Clone the repository and install dependencies:

```bash
npm install
```

### 2. Running Locally

Start the development server:

```bash
npm run dev
```

Access the app at `http://localhost:5173`.

### 3. Updating Case Study Data

The application loads data from `src/data.json`. This JSON is populated by extracting text from the official `casestudies.pdf`.

If you have a new `casestudies.pdf` or want to refine the text extraction:

1.  **Set up Python environment**:
    ```bash
    uv venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    uv pip install pdfplumber
    ```

2.  **Run the Import Pipeline**:
    We have a comprehensive script that extracts text, parses cases, and updates the JSON database.
    ```bash
    python import_all_cases.py
    ```

### 4. Project Structure

- `src/App.jsx`: Main application component containing routing logic (tabs) and state management.
- `src/App.css`: Component-specific styles.
- `src/index.css`: Global design system (variables, reset, typography).
- `src/data.json`: The source of truth for all case studies.
- `import_all_cases.py`: The master script for PDF data extraction and JSON population.

### 5. Building for Production

To create a production-ready build:

```bash
npm run build
```

Preview the build locally:

```bash
npm run preview
```

## 📝 License

This project is for educational purposes. Case study content is derived from public UPSC questions.
