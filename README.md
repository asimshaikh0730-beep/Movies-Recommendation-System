#Application Link:- https://movies-recommendation-system-tv8n.onrender.com
# 🎬 Movies Recommendation System

A content-based movie recommender built with **NLP** and **Streamlit**. Pick a movie you like, and the app suggests **5 similar movies** instantly.

---

## 📌 Overview

Ever finished a great movie and wondered *"what should I watch next?"* This project answers that question.

The system reads the **content** of each movie (its tags), converts the text into numbers, and finds the movies that are most similar to your choice using **cosine similarity**.

---

## ✨ Features

- Content-based recommendations (no user data needed)
- Clean and simple **Streamlit** web interface
- Dropdown with thousands of movies to choose from
- Top **5 similar movies** in one click
- Fast results, because the similarity matrix is pre-computed

---

## 🧠 How It Works

1. **Data:** TMDB 5000 Movies dataset (movies + credits)
2. **Merge and clean:** Both files are merged on the movie title and the useful columns are kept
3. **Create tags:** Movie information is combined into a single `tags` column, and each list is joined into one text string
4. **Vectorization:** `CountVectorizer` (Bag of Words) turns every movie's tags into a vector
5. **Similarity:** `cosine_similarity` measures how close every movie is to every other movie
6. **Recommend:** For the selected movie, the 5 most similar movies are returned

```
Tags text  →  CountVectorizer  →  Vectors  →  Cosine Similarity  →  Top 5 Movies
```

### Simple example

If you pick a space adventure movie, its tags (genre, keywords, cast, etc.) will look very close to other space and sci-fi movies. Their vectors point in a similar direction, so their cosine similarity score is high, and they show up as recommendations.

---

## 🛠️ Tech Stack

| Tool | Use |
|---|---|
| Python | Main language |
| Pandas, NumPy | Data cleaning and processing |
| Scikit-learn | CountVectorizer and cosine similarity |
| Streamlit | Web app |
| Pickle, Joblib | Saving processed data and similarity matrix |

---

## 📂 Project Structure

```
Movies-Recommendation-System/
│
├── app.py                 # Streamlit app
├── movies.pickle          # Processed movies data
├── similarity.joblib      # Pre-computed similarity matrix
├── notebook.ipynb         # Data cleaning + model building
├── requirements.txt       # Dependencies
└── README.md
```

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/asimshaikh0730-beep/Movies-Recommendation-System.git
cd Movies-Recommendation-System
```

**2. Install the requirements**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 💻 Core Code

```python
def recommend(name_movie):
    movie_index = data[data["title"] == name_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]
    return [data.iloc[i[0]].title for i in movies_list]
```

It finds the selected movie, sorts all movies by similarity score, skips the movie itself, and returns the next 5.

---

## 📦 requirements.txt

```
pandas
numpy
scikit-learn
streamlit
joblib
```

---

## 🔮 Future Improvements

- Show movie **posters** using the TMDB API
- Try **TF-IDF** or **sentence embeddings** for better accuracy
- Add filters by genre, year, or rating
- Deploy the app on **Streamlit Community Cloud**

---

## 🙌 Acknowledgements

- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) on Kaggle
- Learned and built while following the TuteDude Gen AI course

---

## 👤 Author

**Asim**
GitHub: [asimshaikh0730-beep](https://github.com/asimshaikh0730-beep)

⭐ If you liked this project, please give it a star!
