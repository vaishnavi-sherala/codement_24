# Required Libraries
import tkinter as tk
import nltk
import numpy as np
import random
import string
import speech_recognition as sr
import pyttsx3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Text-to-Speech Engine
def fun1():
    engine = pyttsx3.init()

    # Sample Health Data
    corpus = [
        'I have a headache.',
        'My stomach hurts.',
        'I feel nauseous.',
        'I have a fever.',
        'I have a cough.',
        'I feel tired all the time.',
        'I experience shortness of breath.',
        'I have chest pain.',
        'I have a sore throat.',
        'I have diarrhea.',
        'I have constipation.',
        'I have back pain.',
        'I feel dizzy.',
        'I have a skin rash.',
        'I have a runny nose.',
        'I feel anxious.',
        'I have difficulty sleeping.',
        'I have blurred vision.',
        'I feel depressed.',
        'I have joint pain.',
        'I have muscle cramps.',
        'I have high blood pressure.',
        'I have diabetes.',
        'I have asthma.',
        'I have allergies.',
        'I have arthritis.',
        'I have migraines.',
        'I have eczema.',
        'I have acne.',
        'I have a urinary tract infection.',
        'I have a yeast infection.',
        'I have a toothache.',
        'I have a cold.',
        'I have a stomach virus.',
        'I have a sinus infection.',
        'I have a sprained ankle.',
        'I have a broken bone.',
        'I have a cut.',
        'I have a bruise.',
        'I have a concussion.',
        'I have a sore back.',
        'I have a sore neck.',
        'I have a sore shoulder.',
        'I have a sore knee.',
        'I have a sore hip.',
        'I have a sore elbow.',
        'I have a sore wrist.',
        'I have a sore ankle.',
        'I have a sore foot.',
        'I have a sore toe.',
        'I have a rash on my arm.',
        'I have a rash on my leg.',
        'I have a rash on my face.',
        'I have a rash on my chest.',
        'I have a rash on my back.',
        'I have a rash on my stomach.',
    ]

    # Sample Health Rules
    rules = {
        'headache': 'Drink plenty of water and try to relax in a quiet, dark room.',
        'stomach pain': 'Avoid spicy or greasy foods and try drinking ginger tea.',
        'nausea': 'Avoid heavy or greasy foods, and try drinking ginger tea or ginger ale to settle your stomach.',
        'fever': 'Rest, drink Water, and take over-the-counter fever reducers like acetaminophen or ibuprofen.',
        'cough': 'Stay hydrated and try over-the-counter cough medicines,Drink warm water. If cough persists, see a doctor.',
        'fatigue': 'Ensure you are getting enough sleep and maintaining a healthy diet. Consider reducing stress through relaxation techniques.',
        'shortness of breath': 'Sit upright and try to remain calm. If symptoms persist, seek medical attention immediately.',
        'chest pain': 'Seek immediate medical attention. Do not ignore chest pain as it could be a sign of a heart attack or other serious condition.',
        'sore throat': 'Gargle with warm salt water and drink plenty of Water. Over-the-counter throat lozenges may also provide relief.',
        'diarrhea': 'Stay hydrated with clear And clear Water and consume bland, easy-to-digest foods like bananas, rice, and toast.',
        'constipation': 'Increase your fiber intake with fruits, vegetables, and whole grains. Drink plenty of water and try gentle exercise.',
        'back pain': 'Apply heat or cold packs to the affected area and try gentle stretches. Over-the-counter pain relievers may also help.',
        'dizziness': 'Sit or lie down and rest until the dizziness subsides. Avoid sudden movements. If dizziness persists, see a doctor.',
        'skin rash': 'Keep the affected area clean and dry. Avoid scratching the rash. Over-the-counter hydrocortisone cream may help reduce itching.',
        'runny nose': 'Use saline nasal spray to relieve congestion and keep the nasal passages moist. Over-the-counter decongestants may also provide relief.',
        'anxiety': 'Practice deep breathing exercises, meditation, or yoga to help manage anxiety. Consider seeking professional help if anxiety is interfering with daily life.',
        'difficulty sleeping': 'Establish a regular sleep schedule and create a relaxing bedtime routine. Avoid caffeine and electronics before bedtime.',
        'blurred vision': 'Rest your eyes and ensure proper lighting when reading or using electronic devices. If vision changes persist, see an eye doctor.',
        'depression': 'Reach out to friends, family, or a mental health professional for support. Practice self-care activities and consider therapy or medication if needed.',
        'joint pain': 'Apply ice or heat packs to the affected joint and try gentle stretches or exercises. Over-the-counter pain relievers may also help.',
        'muscle cramps': 'Stretch and massage the affected muscle. Drink plenty of Water and ensure you are getting enough electrolytes like potassium and magnesium.',
        'high blood pressure': 'Follow a healthy diet low in sodium and high in fruits, vegetables, and whole grains. Exercise regularly and avoid smoking and excessive alcohol.',
        'diabetes': 'Monitor blood sugar levels regularly and follow a balanced diet. Take medication as prescribed and incorporate regular exercise into your routine.',
        'asthma': 'Use prescribed inhalers as directed and avoid triggers like smoke, pollen, and pet dander. Follow an asthma action plan provided by your doctor.',
        'allergies': 'Avoid triggers like pollen, dust, and pet dander. Use over-the-counter antihistamines or nasal sprays for symptom relief.',
        'arthritis': 'Engage in regular low-impact exercise like swimming or walking to maintain joint flexibility. Apply heat or cold packs to reduce pain and inflammation.',
        'migraines': 'Identify and avoid triggers like certain foods, stress, or lack of sleep. Take prescribed migraine medications as directed.',
        'eczema': 'Keep skin moisturized and avoid triggers like harsh soaps or detergents. Use over-the-counter hydrocortisone cream for itching and inflammation.',
        'acne': 'Cleanse skin regularly with a gentle cleanser and avoid picking or squeezing pimples. Use over-the-counter acne treatments containing benzoyl peroxide or salicylic acid.',
        'urinary tract infection': 'Drink plenty of water and urinate frequently to flush out bacteria. Avoid irritants like caffeine and alcohol. Take prescribed antibiotics as directed.',
        'yeast infection': 'Keep the affected area clean and dry. Avoid tight-fitting clothing and use over-the-counter antifungal creams or suppositories.',
        'toothache': 'Rinse your mouth with warm salt water and apply a cold compress to the outside of your cheek if there is swelling. Take over-the-counter pain relievers as needed.',
        'cold': 'Get plenty of rest, drink warm water, and use over-the-counter cold remedies to relieve symptoms.',
        'stomach virus': 'Stay hydrated with clear and clean Water and eat bland foods. Rest and avoid contact with others to prevent spreading the virus.',
        'sinus infection': 'Use saline nasal spray, warm compresses, and over-the-counter decongestants to relieve symptoms. If symptoms persist, see a doctor.',
        'sprained ankle': 'Rest, ice, compress, and elevate the ankle (RICE method). Use over-the-counter pain relievers and avoid putting weight on the affected ankle.',
        'broken bone': 'Seek immediate medical attention. Immobilize the affected area and apply ice to reduce swelling. Follow medical advice for treatment and recovery.',
        'cut': 'Clean the cut with soap and water, apply an antibiotic ointment, and cover with a sterile bandage. Seek medical attention if the cut is deep or won\'t stop bleeding.',
        'bruise': 'Apply a cold compress to reduce swelling and pain. Elevate the affected area if possible. If the bruise is severe or accompanied by other symptoms, see a doctor.',
        'concussion': 'Rest and avoid activities that could worsen symptoms. Monitor for signs of concussion such as headache, dizziness, nausea, or confusion. Seek medical attention if symptoms worsen.',
        'sore back': 'Apply heat or ice packs to the affected area and try gentle stretches or exercises. Over-the-counter pain relievers may also help.',
        'sore neck': 'Apply heat or ice packs to the affected area and try gentle neck stretches. Ensure proper posture and avoid activities that strain the neck.',
        'sore shoulder': 'Rest the affected shoulder and avoid activities that a+ggravate pain. Apply heat or ice packs and try gentle shoulder stretches.',
        'sore knee': 'Rest the affected knee and avoid activities that aggravate pain. Apply ice packs and elevate the knee. Consider using a knee brace for support.',
        'sore hip': 'Rest the affected hip and avoid activities that aggravate pain. Apply heat or ice packs and try gentle hip stretches.',
        'sore elbow': 'Rest the affected elbow and avoid activities that aggravate pain. Apply ice packs and elevate the elbow. Consider using an elbow brace for support.',
        'sore wrist': 'Rest the affected wrist and avoid activities that aggravate pain. Apply ice packs and elevate the wrist. Consider using a wrist brace for support.',
        'sore ankle': 'Rest the affected ankle and avoid activities that aggravate pain. Apply ice packs and elevate the ankle. Consider using an ankle brace for support.',
        'sore foot': 'Rest the affected foot and avoid activities that aggravate pain. Apply ice packs and elevate the foot. Consider using supportive footwear.',
        'sore toe': 'Rest the affected toe and avoid activities that aggravate pain. Apply ice packs and elevate the toe. Consider using wider or more comfortable shoes.',
        'rash on arm': 'Keep the affected area clean and dry. Apply a gentle moisturizer or calamine lotion to soothe itching. Avoid scratching the rash.',
        'rash on leg': 'Keep the affected area clean and dry. Apply a gentle moisturizer or calamine lotion to soothe itching. Wear loose, breathable clothing.',
        'rash on face': 'Keep the affected area clean and avoid harsh skincare products. Apply a gentle moisturizer and avoid scratching or picking at the rash.',
        'rash on chest': 'Keep the affected area clean and dry. Avoid tight-fitting clothing and irritating fabrics. Use over-the-counter hydrocortisone cream for itching and inflammation.',
        'rash on back': 'Keep the affected area clean and dry. Wear loose, breathable clothing. Use over-the-counter antihistamines or hydrocortisone cream for itching and inflammation.',
        'rash on stomach': 'Keep the affected area clean and dry. Avoid irritating fabrics and harsh skincare products. Use over-the-counter hydrocortisone cream for itching and inflammation.',
    }

    # Sample Medicine Suggestions
    # Sample Medicine Suggestions
    medicines = {
        'headache': {
            'medicine': ['Aspirin (₹10)', 'Acetaminophen (₹15)', 'Ibuprofen (₹20)'],
            'when_to_take': 'As needed, with a full glass of water.',
            'quantity': '1-2 tablets (follow dosage instructions on the packaging).'
        },
        'stomach hurts': {
            'medicine': ['Antacids (₹12)', 'Pepto-Bismol (₹25)', 'Simethicone (₹18)'],
            'when_to_take': 'After meals and before bedtime, or as directed by your doctor.',
            'quantity': '1-2 tablets as needed.'
        },
        'nauseous': {
            'medicine': ['Ginger capsules (₹30)', 'Emetrol (₹22)', 'Bismuth subsalicylate (₹28)'],
            'when_to_take': '30 minutes before meals or as needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'fever': {
            'medicine': ['Acetaminophen (₹15)', 'Ibuprofen (₹20)', 'Aspirin (₹10)'],
            'when_to_take': 'Every 4-6 hours as needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'cough': {
            'medicine': ['Dextromethorphan (₹25)', 'Guaifenesin (₹18)', 'Codeine (₹35)'],
            'when_to_take': 'Every 4-6 hours as needed, with plenty of Water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'shortness of breath': {
            'medicine': ['Albuterol (₹40)', 'Corticosteroids (₹30)', 'Oxygen therapy (₹100)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'chest pain': {
            'medicine': ['Nitroglycerin (₹50)', 'Aspirin (₹10)', 'Beta-blockers (₹35)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'sore throat': {
            'medicine': ['Throat lozenges (₹15)', 'Acetaminophen (₹15)', 'Ibuprofen (₹20)'],
            'when_to_take': 'As needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'diarrhea': {
            'medicine': ['Loperamide (₹25)', 'Bismuth subsalicylate (₹28)', 'Probiotics (₹30)'],
            'when_to_take': 'After each loose stool, or as directed by your doctor.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'constipation': {
            'medicine': ['Fiber supplements (₹20)', 'Stool softeners (₹25)', 'Laxatives (₹18)'],
            'when_to_take': 'Before bedtime or as directed by your doctor.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'back pain': {
            'medicine': ['Acetaminophen (₹15)', 'Ibuprofen (₹20)', 'Naproxen (₹30)'],
            'when_to_take': 'Every 4-6 hours as needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'dizzy': {
            'medicine': ['Meclizine (₹35)', 'Antihistamines (₹18)', 'Scopolamine patches (₹50)'],
            'when_to_take': 'As needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'skin rash': {
            'medicine': ['Hydrocortisone cream (₹40)', 'Antihistamines (₹18)', 'Calamine lotion (₹25)'],
            'when_to_take': 'Apply to affected area as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'runny nose': {
            'medicine': ['Antihistamines (₹18)', 'Decongestants (₹20)', 'Nasal corticosteroids (₹30)'],
            'when_to_take': 'As needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'difficulty sleeping': {
            'medicine': ['Melatonin (₹25)', 'Diphenhydramine (₹20)', 'Trazodone (₹35)'],
            'when_to_take': '30 minutes before bedtime, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'blurred vision': {
            'medicine': ['Prescription glasses (₹200)', 'Contact lenses (₹150)', 'Eye drops (₹30)'],
            'when_to_take': 'As needed or as directed by your eye doctor.',
            'quantity': 'Follow usage instructions or doctor\'s advice.'
        },
        'joint pain': {
            'medicine': ['Acetaminophen (₹15)', 'Ibuprofen (₹20)', 'Naproxen (₹30)'],
            'when_to_take': 'Every 4-6 hours as needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'muscle cramps': {
            'medicine': ['Hydration (₹0)', 'Magnesium supplements (₹25)', 'Quinine (₹35)'],
            'when_to_take': 'As needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'high blood pressure': {
            'medicine': ['Antihypertensive medications (₹45)', 'Diuretics (₹30)', 'Beta-blockers (₹35)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'diabetes': {
            'medicine': ['Insulin (₹200)', 'Oral medications (₹100)', 'Blood sugar monitoring (₹50)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'asthma': {
            'medicine': ['Inhaled corticosteroids (₹80)', 'Bronchodilators (₹60)', 'Leukotriene modifiers (₹70)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'allergies': {
            'medicine': ['Antihistamines (₹18)', 'Decongestants (₹20)', 'Corticosteroids (₹30)'],
            'when_to_take': 'As needed or as directed by your doctor.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'arthritis': {
            'medicine': ['NSAIDs (₹25)', 'Corticosteroids (₹30)', 'DMARDs (₹50)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'migraines': {
            'medicine': ['Triptans (₹50)', 'Ergotamine (₹45)', 'Acetaminophen with caffeine (₹25)'],
            'when_to_take': 'At the onset of migraine symptoms, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'eczema': {
            'medicine': ['Topical corticosteroids (₹40)', 'Antihistamines (₹18)', 'Emollients (₹30)'],
            'when_to_take': 'Apply to affected skin as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'acne': {
            'medicine': ['Benzoyl peroxide (₹30)', 'Salicylic acid (₹25)', 'Topical retinoids (₹40)'],
            'when_to_take': 'Apply to affected skin as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'urinary tract infection': {
            'medicine': ['Antibiotics (₹50)', 'Pain relievers (₹20)', 'Urinary analgesics (₹30)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'yeast infection': {
            'medicine': ['Antifungal medications (₹45)', 'Topical creams (₹35)', 'Oral tablets (₹50)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'toothache': {
            'medicine': ['Acetaminophen (₹15)', 'Ibuprofen (₹20)', 'Benzocaine gel (₹30)'],
            'when_to_take': 'As needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'cold': {
            'medicine': ['Acetaminophen (₹15)', 'Ibuprofen (₹20)', 'Decongestants (₹25)'],
            'when_to_take': 'Every 4-6 hours as needed, with a full glass of water.',
            'quantity': 'Follow dosage instructions on the packaging.'
        },
        'stomach virus': {
            'medicine': ['Oral rehydration solutions (₹40)', 'Antiemetics (₹30)', 'Antidiarrheal medications (₹35)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'sinus infection': {
            'medicine': ['Antibiotics (₹50)', 'Decongestants (₹25)', 'Saline nasal spray (₹20)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'sprained ankle': {
            'medicine': ['RICE therapy (₹0)', 'NSAIDs (₹25)', 'Ankle brace (₹50)'],
            'when_to_take': 'As needed or as directed by your doctor.',
            'quantity': 'Follow usage instructions or doctor\'s advice.'
        },
        'broken bone': {
            'medicine': ['Immobilization (₹0)', 'Pain relievers (₹20)', 'Bone stimulators (₹40)'],
            'when_to_take': 'As directed by your doctor.',
            'quantity': 'Follow dosage instructions or doctor\'s advice.'
        },
        'cut': {
            'medicine': ['Antiseptic solution (₹20)', 'Antibiotic ointment (₹30)', 'Sterile bandage (₹15)'],
            'when_to_take': 'Apply to the wound as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'bruise': {
            'medicine': ['Cold compress (₹10)', 'Arnica gel (₹35)', 'Pain relievers (₹20)'],
            'when_to_take': 'Apply to the bruised area as needed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'concussion': {
            'medicine': ['Rest (₹0)', 'Pain relievers (₹20)', 'Brain rest (₹0)'],
            'when_to_take': 'As needed or as directed by your doctor.',
            'quantity': 'Follow usage instructions or doctor\'s advice.'
        },
        'rash on my arm': {
            'medicine': ['Topical corticosteroids (₹40)', 'Antihistamines (₹18)', 'Calamine lotion (₹25)'],
            'when_to_take': 'Apply to affected area as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'rash on my leg': {
            'medicine': ['Topical corticosteroids (₹40)', 'Antihistamines (₹18)', 'Calamine lotion (₹25)'],
            'when_to_take': 'Apply to affected area as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'rash on my face': {
            'medicine': ['Topical corticosteroids (₹40)', 'Antihistamines (₹18)', 'Calamine lotion (₹25)'],
            'when_to_take': 'Apply to affected area as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'rash on my chest': {
            'medicine': ['Topical corticosteroids (₹40)', 'Antihistamines (₹18)', 'Calamine lotion (₹25)'],
            'when_to_take': 'Apply to affected area as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'rash on my back': {
            'medicine': ['Topical corticosteroids (₹40)', 'Antihistamines (₹18)', 'Calamine lotion (₹25)'],
            'when_to_take': 'Apply to affected area as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
        'rash on my stomach': {
            'medicine': ['Topical corticosteroids (₹40)', 'Antihistamines (₹18)', 'Calamine lotion (₹25)'],
            'when_to_take': 'Apply to affected area as directed.',
            'quantity': 'Follow usage instructions on the packaging.'
        },
    }

        # Add more medicine suggestions for other conditions


    # Sample Diet Recommendations
    diet_recommendations = {
        'headache': 'Ensure you stay hydrated and try to consume foods rich in magnesium like almonds, spinach, and bananas. Avoid caffeinated and alcoholic beverages.',
        'stomach pain': 'Stick to easily digestible foods like bananas, rice, applesauce, and toast (BRAT diet). Avoid spicy, greasy, or heavy foods.',
        'fever': 'Focus on staying hydrated with water, clear broth, and electrolyte-rich drinks. Eat light, nourishing foods like soups, broths, and steamed vegetables.',
        'cough': 'Stay hydrated by drinking plenty of fluids like water, herbal teas, and clear broths. Consume foods that are soothing to the throat such as warm liquids, honey, and ginger.',
        # Add more diet recommendations for other conditions
    }

    # Preprocessing
    def preprocess_text(text):
        text = text.lower()
        text = ''.join([char for char in text if char not in string.punctuation])
        return text

    # TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english', token_pattern=None)
    tfidf_matrix = tfidf_vectorizer.fit_transform([preprocess_text(sentence) for sentence in corpus])

    # Function to generate bot response
    def get_bot_response(user_input):
        user_input = preprocess_text(user_input)
        user_tfidf = tfidf_vectorizer.transform([user_input])

        # Calculate similarity between user input and corpus
        similarities = cosine_similarity(user_tfidf, tfidf_matrix)
        idx = np.argmax(similarities)
        
        # Check if the input matches a rule
        for condition, rule in rules.items():
            if condition in user_input:
                if condition in medicines:
                    medicine_info = medicines[condition]
                    medicine_suggestion = random.choice(medicine_info['medicine'])
                    response = f"{rule}\nTake care of your {condition} by taking {medicine_suggestion} {medicine_info['when_to_take']}. Quantity: {medicine_info['quantity']}."
                    if condition in diet_recommendations:
                        response += f"\nAdditionally, for your {condition}, {diet_recommendations[condition]}"
                    return response
                else:
                    response = rule
                    if condition in diet_recommendations:
                        response += f"\nAdditionally, for your {condition}, {diet_recommendations[condition]}"
                    return response
        
        # If no match found, return "Please try again"
        return "Please try again."

    # Function to handle speech recognition
    def recognize_speech():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        try:
            user_input = recognizer.recognize_google(audio)
            entry.delete(0, tk.END)
            entry.insert(tk.END, user_input)
        except sr.UnknownValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Could not understand audio. Please speak clearly or type your message.")
        except sr.RequestError as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, f"Error: {e}")

    # Function to handle user input and display bot response
    def send():
        user_input = entry.get()
        if user_input.strip() != "":
            if user_input.lower() in ['hi','help me','hii','hiii', 'hello', 'hay', 'namaskar', 'i have some problem']:
                bot_response = "Welcome to Sehat Sathi chat bot. Please tell me your problem."
            elif user_input.lower() in ['bye', 'good bye']:
                bot_response = "Thank you! Have a nice day. Take care of your health."
            else:
                bot_response = get_bot_response(user_input)
            
            chat_log.config(state=tk.NORMAL)
            chat_log.insert(tk.END, "You: " + user_input + "\n\n", "user")
            chat_log.insert(tk.END, "Sehat Sathi: " + bot_response + "\n\n", "bot")
            chat_log.config(state=tk.DISABLED)
            
            # Scroll to the bottom
            chat_log.see(tk.END)
            
            engine.say(bot_response)
            engine.runAndWait()
            
            entry.delete(0, tk.END)

    # GUI Setup
    root = tk.Tk()
    root.title("Sehat Sathi")
    root.configure(bg="#FDFEFE")  # Set background color

    frame = tk.Frame(root, bg="#FDFEFE")  # Set background color
    scrollbar = tk.Scrollbar(frame)
    chat_log = tk.Text(frame, height=25, width=50, yscrollcommand=scrollbar.set, bg="#FDFEFE", wrap="word")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_log.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
    frame.pack()

    entry_frame = tk.Frame(root, bg="#FDFEFE")  # Set background color
    entry = tk.Entry(entry_frame, width=50, bg="#E5E7E9")
    entry.pack(pady=10, side=tk.LEFT)
    send_button = tk.Button(entry_frame, text="Send", command=send, bg="#4CAF50", fg="white")  # Set button color
    send_button.pack(side=tk.LEFT)
    mic_button = tk.Button(entry_frame, text="🎤", command=recognize_speech, bg="#4CAF50", fg="white")  # Set button color
    mic_button.pack(side=tk.LEFT)
    entry_frame.pack()

    # Configure chat log text style
    chat_log.tag_configure("user", foreground="blue")  # Set color for user messages
    chat_log.tag_configure("bot", foreground="red")  # Set color for bot messages

 