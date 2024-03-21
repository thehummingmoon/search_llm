import csv
import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

# Load data from CSV
data = []
with open('scraped_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(row[0])  # Assuming the text is in the first column

# Tokenize the data
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
encoded_data = [tokenizer.encode(text, return_tensors="tf") for text in data]

# Define and initialize the model
model = TFGPT2LMHeadModel.from_pretrained("gpt2")

# Define training parameters
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# Train the model (simplified example)
num_epochs = 3
for epoch in range(num_epochs):
    for batch in encoded_data:
        with tf.GradientTape() as tape:
            outputs = model(batch)
            logits = outputs.logits
            loss = loss_fn(batch, logits)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

# Save the trained model
model.save_pretrained(r"C:\Users\Smile\web-crawler\env")
