#!/usr/bin/env python
# coding: utf-8
import src.modules.data_scrape as data_scrape

# In[ ]:

# Scraped website data in the document data type
data_in_document_type = data_scrape.Scrape_Data('data/urls.txt')

# The same scraped data in a txt file
data_in_txt = '/data/training/input.txt'

from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import random
from fuzzywuzzy import fuzz
import qrcode
from io import BytesIO

# Define patterns and corresponding responses
patterns_responses = {
    r"hello.*": ["Hello! How are you?", "Hi there!", "Hey! What can I do for you?"],
    r"how are you.*": ["I'm okay thank you, how are you?", "Doing well, thanks for asking!", "I'm good, how about you?"],
    r"what is your name.*": ["Hey, my name is Cecil the Chatbot, and I'm here to assist you!"],
    r"what is the university of gloucestershire.*": ["The University of Gloucestershire is a public university based in Gloucestershire, England. It is located over three campuses, two in Cheltenham and one in Gloucester. The university can trace its earliest civic history to the Cheltenham Training College, which was established in 1847 by the Reverend Francis Close."],
    r"when was the business school opened.*": ["The business school was opened in 2018."],
    r"how much did the business school cost.*": ["The business school cost £18 million."],
    r"give me a brief description of the business school.*": ["Opened in 2018, this new £18 million development features an impressive atrium, boardroom, state-of-the-art lecture rooms along with the following specialist spaces: Thomas Reuters trading room, Consumer behaviour lab, Moot court room, Growth Hub."],
}

# Function to match patterns and return corresponding response with fuzzy matching
def process_input(user_input):
    max_ratio = 0
    best_pattern = None
    for pattern, responses in patterns_responses.items():
        ratio = fuzz.partial_ratio(user_input.lower(), pattern.lower())
        if ratio > max_ratio:
            max_ratio = ratio
            best_pattern = pattern
    if max_ratio >= 80:  # Adjust the threshold as needed
        return random.choice(patterns_responses[best_pattern])
    else:
        return "Bot: I'm sorry, I didn't understand that."

# Function to handle user submission
def handle_submission():
    handle_input()

# Function to handle user input
def handle_input():
    user_input = user_entry.get()
    conversation_text.insert(tk.END, "User: " + user_input + "\n")
    bot_response = process_input(user_input)
    conversation_text.insert(tk.END, bot_response + "\n")
    conversation_text.see(tk.END)  # Scroll to the bottom
    user_entry.delete(0, tk.END)

# Generate QR code for the chatbot URL and display it in a new window
def generate_qr_code():
    qr_data = "https://your-chatbot-url.com"  # Replace with your chatbot URL
    qr = qrcode.make(qr_data)
    qr.show()




# Create a submit button
submit_button = tk.Button(root, text="Submit", command=handle_submission)


# Load and display the image
image = Image.open("3.jpeg")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

# Create a scrolled text widget to display conversation
conversation_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, font=("Arial", 12))


# In[ ]:




