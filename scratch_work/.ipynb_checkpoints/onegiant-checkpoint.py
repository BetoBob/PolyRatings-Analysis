import os
import pickle
import pandas as pd
import sys

teacher_df = []

for teacher in os.listdir('/data301/share/robert_h/polyratings_profiles/'):
    path = "/data301/share/robert_h/polyratings_profiles/" + teacher
    if(path.endswith(".pkl")):
        teacher_df.append(pickle.load(open(path, "rb")))

reviews = pd.concat(teacher_df)
reviews["student_gpa"] = reviews.student_gpa.astype("float")

sys.setrecursionlimit(1000000000)
pickle.dump(reviews, open("polyratings_reviews.pkl", "wb"))
