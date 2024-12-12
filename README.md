Course Recommender System

A Course Recommender System built using job trends analysis to recommend courses that align with the skills in demand. This project combines data preprocessing, K-Means clustering, hybrid recommendation techniques, and Singular Value Decomposition (SVD) to provide personalized course recommendations for users based on current market trends.

Table of Contents

Overview

Features

Technologies Used

Dataset

Architecture

Usage

Future Work

Contributing

License

Overview

The Course Recommender System analyzes job descriptions and trends from platforms like LinkedIn to extract the most in-demand skills. These skills are matched with an educational dataset to suggest the highest-rated courses that help users acquire the skills needed for trending jobs.

Key methods include:

Job trend analysis: Extracting key skills using data preprocessing and clustering.

Course recommendations: Leveraging hybrid filtering techniques, including Content-Based Filtering and Collaborative Filtering with SVD.

Similarity measurement: Matching extracted job skills with course skills using Cosine Similarity and TF-IDF.

Features

Skill Extraction: Uses K-Means clustering to identify job-related skills.

Hybrid Filtering: Combines Content-Based and Collaborative Filtering for accurate recommendations.

Job-Course Matching: Matches job market skills to relevant courses based on skill sets.

Interactive Interface: A web-based platform for users to search for courses based on job roles or skills.

Technologies Used

Programming Languages: Python, HTML, CSS

Framework: Flask

Data Analysis Libraries: Pandas, NumPy, Scikit-learn

Recommendation Techniques:

K-Means Clustering

KNN (K-Nearest Neighbors)

SVD (Singular Value Decomposition)

Content-Based Filtering

Collaborative Filtering

Web Technologies: html css for UI design

Dataset

The project uses two primary datasets:

LinkedIn Job Dataset: Contains job descriptions, skills, and titles.
                      url: https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024

Course Dataset (courses_with_skills.csv): Includes the following fields:

id, title, url, is_paid, instructor_names, category, headline, num_subscribers, rating, num_reviews, instructional_level, objectives, curriculum, and Skills.
url:https://www.kaggle.com/datasets/emrebayirr/udemy-course-dataset-categories-ratings-and-trends

Note: The dataset includes columns for num_subscribers and num_reviews that are used for ranking courses.

Architecture

Data Preprocessing:

Text cleaning and tokenization using Python's re module.

Vectorization of skills using TF-IDF.

Job Analysis:

Skills extracted using K-Means clustering.

Course Recommendation:

Hybrid filtering with SVD for collaborative filtering.

Matching job skills to courses using Cosine Similarity.

Web Application:

Flask backend connects the recommendation system with an interactive front end.

Allows users to search for jobs or skills and receive recommendations.

Usage

Search Job Trends: Enter job titles to analyze skills in demand.

Get Recommendations: Based on the job trend analysis, receive course recommendations tailored to the extracted skills.

Browse Courses: View detailed course information, including ratings, reviews, and instructor details.

Future Work

Integration with real-time job feeds from platforms like LinkedIn or Indeed.

Adding a user authentication system for personalized recommendations.

Incorporating advanced NLP techniques such as BERT or GPT for skill extraction.

Expanding the dataset with additional courses and categories.

Contributing

Contributions are welcome! Please fork the repository and create a pull request to suggest improvements.

License

This project is licensed under the MIT License. See the LICENSE file for details.
