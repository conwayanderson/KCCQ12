import streamlit as st

def main():
    st.title("Kansas City Cardiomyopathy Questionnaire (KCCQ-12)")

    st.write("Please answer the following questions:")

    q1 = st.selectbox("Q1. In the past 2 weeks, how much has your heart failure limited your enjoyment of life?", 
                      ['', 'Extremely', 'Quite a bit', 'Moderately', 'Slightly', 'Not at all'])

    q2 = st.selectbox("Q2. In the past 2 weeks, how many times did you visit the emergency room or urgent care center because of your heart failure?", 
                      ['', '0', '1', '2', '3', '4 or more'])

    q3 = st.selectbox("Q3. In the past 2 weeks, on average, how many times has swelling in your feet, ankles, or legs bothered you?", 
                      ['', 'All of the time', 'Several times a day', 'At least once a day', '3 or more times per week', '1 or 2 times per week', 'Less than once a week', 'Never'])

    q4 = st.selectbox("Q4. In the past 2 weeks, on average, how many times has shortness of breath bothered you?", 
                      ['', 'All of the time', 'Several times a day', 'At least once a day', '3 or more times per week', '1 or 2 times per week', 'Less than once a week', 'Never'])

    q5 = st.selectbox("Q5. In the past 2 weeks, on average, how many times has fatigue, low energy, or tiredness bothered you?", 
                      ['', 'All of the time', 'Several times a day', 'At least once a day', '3 or more times per week', '1 or 2 times per week', 'Less than once a week', 'Never'])

    q6 = st.selectbox("Q6. In the past 2 weeks, on average, how many times has chest pain, chest tightness, or angina bothered you?", 
                      ['', 'All of the time', 'Several times a day', 'At least once a day', '3 or more times per week', '1 or 2 times per week', 'Less than once a week', 'Never'])

    q7 = st.selectbox("Q7. In the past 2 weeks, how many nights did you have trouble sleeping because of your heart failure?", 
                      ['', 'Every night', '5 or 6 nights per week', '3 or 4 nights per week', '1 or 2 nights per week', 'Less than once a week', 'Never'])

    q8 = st.selectbox("Q8. In the past 2 weeks, how much has your heart failure limited your ability to do your usual activities (work, hobbies, and chores)?", 
                      ['', 'Extremely', 'Quite a bit', 'Moderately', 'Slightly', 'Not at all'])

    q9 = st.selectbox("Q9. In the past 2 weeks, how often have you felt short of breath?", 
                      ['', 'At rest', 'With minimal activity', 'With moderate activity', 'With strenuous activity'])

    q10 = st.selectbox("Q10. In the past 2 weeks, how much has your heart failure limited your ability to walk?", 
                       ['', 'Unable to walk', 'Very limited', 'Moderately limited', 'Slightly limited', 'Not at all limited'])

    q11 = st.selectbox("Q11. In the past 2 weeks, how often have you had swelling in your feet, ankles, or legs?", 
                       ['', 'At rest', 'With minimal activity', 'With moderate activity', 'With strenuous activity'])

    q12 = st.selectbox("Q12. In the past 2 weeks, how much has your heart failure limited your ability to climb a flight of stairs?", 
                       ['', 'Unable to climb', 'Very limited', 'Moderately limited', 'Slightly limited', 'Not at all limited'])

    if st.button("Submit"):
        kccq_score = calculate_kccq_score(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12)
        st.write(f"Your KCCQ-12 score is: {kccq_score}")

def calculate_kccq_score(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12):
    response_mapping = {
        '': None,
        'Extremely': 0,
        'Quite a bit': 25,
        'Moderately': 50,
        'Slightly': 75,
        'Not at all': 100,
        '0': 100,
        '1': 75,
        '2': 50,
        '3': 25,
        '4 or more': 0,
        'All of the time': 0,
        'Several times a day': 20,
        'At least once a day': 40,
        '3 or more times per week': 60,
        '1 or 2 times per week': 80,
        'Less than once a week': 100,
        'Never': 100,
        'Every night': 0,
        '5 or 6 nights per week': 25,
        '3 or 4 nights per week': 50,
        '1 or 2 nights per week': 75,
        'At rest': 0,
        'With minimal activity': 33,
        'With moderate activity': 67,
        'With strenuous activity': 100,
        'Unable to walk': 0,
        'Very limited': 25,
        'Moderately limited': 50,
        'Slightly limited': 75,
        'Not at all limited': 100,
        'Unable to climb': 0
    }

    scores = [response_mapping[q] for q in [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]]
    if None in scores:
        st.warning("Please answer all questions.")
        return

    # Calculate domain scores
    kccq_overall = (sum(scores[:2]) / 2)
    kccq_symptom_frequency = (sum(scores[2:7]) / 5)
    kccq_physical_limitation = (sum(scores[7:12]) / 5)

    # Calculate the average of the domain scores
    kccq_score = (kccq_overall + kccq_symptom_frequency + kccq_physical_limitation) / 3

    return round(kccq_score, 2)

if __name__ == "__main__":
    main()

