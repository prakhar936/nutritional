import spacy

# Load a pre-trained SpaCy NER model
nlp = spacy.load("en_core_web_sm")

# Example text containing food items
text = "I had pizza and salad for lunch at the Italian restaurant."

# Process the text with SpaCy NER
doc = nlp(text)

# Extract food items (entities labeled as "FOOD")
food_items = [ent.text for ent in doc.ents if ent.label_ == "FOOD"]

# Print the extracted food items
print(food_items)
