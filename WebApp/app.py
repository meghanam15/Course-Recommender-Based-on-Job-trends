from flask import Flask, render_template, request
import webbrowser
import threading
import pandas as pd
import numpy as np
from courserec import hybrid_filtering  # Ensure hybrid_filtering function is correctly implemented

# Initialize Flask app
app = Flask(__name__)

# Load the DataFrame from a CSV file for job clustering
csv_file = 'C:\\Users\\Meghana\\Desktop\\MCA Final Demo\\LinkedIn\\company_cluster.csv'  # Replace with the actual CSV file path
try:
    company_cluster_df = pd.read_csv(csv_file)
    print(f"DataFrame loaded successfully with {len(company_cluster_df)} rows.")
except Exception as e:
    print(f"Error loading DataFrame: {e}")
    company_cluster_df = pd.DataFrame()  # Fallback to an empty DataFrame if loading fails

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    search_result = None
    error_message = None
    recommended_courses = []
    skill_input = None

    if request.method == "POST":
        skill_input = request.form.get("search_query", "").strip()

        if not skill_input:
            error_message = "Please enter a skill to search for."
        else:
            # Search logic for matching job skills in the DataFrame
            if not company_cluster_df.empty:
                matched_rows = company_cluster_df[company_cluster_df['job_skills'].str.contains(skill_input, case=False, na=False)]

                if not matched_rows.empty:
                    # Get top result and include company, cluster name, and job level
                    search_result = matched_rows[['company', 'cluster_name', 'job level']].head(1).to_dict(orient='records')
                else:
                    error_message = f"No matches found for '{skill_input}'."
            else:
                error_message = "Error with the dataset."

            # Course recommendation (using hybrid filtering)
            if skill_input:
                # Create a user-item matrix (dummy data for now, replace with actual ratings)
                user_item_matrix = np.random.rand(100, 5)  # Random data for testing

                # Get hybrid recommendations (content + collaborative)
                recommended_courses = hybrid_filtering(skill_input, user_item_matrix)

                # Limit to 5 recommended courses
                recommended_courses = recommended_courses[:5]

                if not recommended_courses:
                    error_message = f"No recommendations found for '{skill_input}'."

    return render_template("search.html", 
                           search_result=search_result, 
                           error_message=error_message,
                           skill_input=skill_input,
                           recommended_courses=recommended_courses)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Function to automatically open the browser
def open_browser():
    webbrowser.open_new('http://localhost:5000')

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
