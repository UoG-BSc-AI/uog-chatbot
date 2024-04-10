#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Open source model  - Hugging transformers library

import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import re
import random
import qrcode
from io import BytesIO
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define patterns and corresponding responses
patterns_responses = {
    r"hello.*": ["Hello! How are you?", "Hi there!", "Hey! What can I do for you?"],
    r"how are you.*": ["I'm okay thank you, how are you?", "Doing well, thanks for asking!", "I'm good, how about you?"],
    r"what is your name.*": ["Hey, my name is Cecil the Chatbot, and I'm here to assist you!"],
    r"what is the university of gloucestershire.*": ["The University of Gloucestershire is a public university based in Gloucestershire, England. It is located over three campuses, two in Cheltenham and one in Gloucester. The university can trace its earliest civic history to the Cheltenham Training College, which was established in 1847 by the Reverend Francis Close."],
    r"when was the business school opened.*": ["The business school was opened in 2018."],
    r"how much did the business school cost.*": ["The business school cost £18 million."],
    r"give me a brief description of the business school.*": ["Opened in 2018, this new £18 million development features an impressive atrium, boardroom, state-of-the-art lecture rooms along with the following specialist spaces: Thomas Reuters trading room, Consumer behaviour lab, Moot court room, Growth Hub."],
    r"Give me information about the performing arts centre .*": ["This £2million facility is purpose-built with transformative studios to accommodate any performance."],
    r"Give me information about the health social care facilities .*": ["Our new dedicated facilities and equipment allow students to prepare for the frontline of healthcare and learn the very cutting-edge techniques."],
    r"Give me information about the sports facilities.*": ["You’ll be challenged and supported by experienced coaches, therapists and scientists to develop the practical and theoretical skills you need to succeed after graduating. Our sports facilities have recently been expanded to include a brand-new stadium, pitches and sports hall."],
    r"What is oxstalls campus .*": ["This is a high-energy campus of forward-thinking and competitive students. Here, our students train for the frontline of healthcare, perform and produce shows, work alongside elite athletes and make connections with global businesses. Located 15 mins’ walk from Gloucester city centre and Kingsholm rugby stadium, you’ll have easy access to clubs, bars, shops, theatres and cafes."],
    r"Are there green spaces at oxstalls campus .*": ["The campus is surrounded by ponds and green spaces, or nearby is the new area and surrounding pitches where our students can be found competing or just playing for fun."],
    r"Is there food drink at oxstalls campus .*": ["The campus’ refectory offers hot meals, snacks, fresh sandwiches, a salad bar and freshly baked cakes and pastries. There are vegan and vegetarian options available as well as vending machines and free water stations, so you can top up your bottle."],
    r"Are there illustration architecture studios .*": ["These open-plan studios offer a bespoke space for each student to develop their individual style. We’re expanding the studios for the launch of our brand-new Architecture, Construction & Environment subject community."],
    r"Tell me about the hardwick centre fine art photography .*": ["Just a few minutes’ walk from the main campus is a thriving hub of creativity for our fine art and photography students. It offers year-round exhibitions in the gallery, including our own third-year Degree Show, where students showcase their work to visiting artists and the public."],
    r"Tell me about the education humanities facilities .*": ["Whether you’re the next generation of teachers and carers, campaigning for social change or putting your passion into words – these historic grounds offer modern facilities for our students to debate, research and train."],
    r"What is the natural social sciences facilities .*": ["From understanding the mind and investigating crime, to supporting animal conservation and researching disease, students can explore their curiosity for the world around them in top-spec labs and facilities."],
    r"What is francis close hall .*": ["Referred to as the ‘Hogwarts campus’, the ivy-clad, gothic grounds sit alongside modern structures and facilities. The buildings are Grade II listed and made of Cotswold stone which gives the campus a bright glow all year round. Close to the town centre and nearby parks, you’ll get the best of both country and city living – this is a rare and inspiring space to study and learn."],
    r"Are there green spaces at francis close hall .*": ["Students can be found hanging out on the campuses’ central green space or nearby is the beautiful Pittville Park which has a boating lake, tennis courts, aviary and ornamental garden. The campus’ best-kept secret is the edible gardens and pond which attract birds, frogs and wildlife. This oasis for staff, students and the local community has a woodfired oven and LED lights for pizza parties all year-round. Surrounding Cheltenham are the stunning Cotswold Hills. The Cotswolds are the largest Area of Outstanding Natural Beauty (AONB) in the UK."],
    r"Is there food and drink at campus .*": ["The campus’ refectory offers hot meals, snacks, fresh sandwiches, a salad bar and freshly baked cakes and pastries. There are vegan and vegetarian options available as well as vending machines and free water stations, so you can top up your bottle. The Student Union bar provides evening entertainment and drinks or, 5 mins’ walk from campus you’ll find the buzzing Brewery Quarter. This has a Nando’s, Five Guys, cocktail bars, a cinema, bowling alley and Tesco Express."],
    r"Tell me about the computing engineering centre .*": ["These state-of-the-art facilities offer the very latest hardware and software for our students to experiment and innovate."],
    r"What is the design centre .*": ["Our brand-new centre offers bespoke professional spaces for our design students to develop their creative talent. Each studio is unique and you’ll find student designs painted on some of the walls."],
    r"What is the media centre .*": ["With top-spec facilities, this interdisciplinary hub provides a professional space where students can commission, collaborate and create together."],
    r"What is park campus .*": ["These beautiful grounds offer a creative hub for our art, media and technology students to collaborate and inspire each other. Set in the Montpellier district of the town, the campus has a real buzz, surrounded by Georgian villas, botanical gardens, bars and boutiques."],
    r"Are there green spaces at park campus .*": ["Originally laid out as a zoological garden, with its own lake and elephant walkway, Park Campus is surrounded by picturesque parklands. It has MUGA pitches and acres of green for students to hang out. In view from the campus are the stunning Cotswold Hills. The Cotswolds are the largest Area of Outstanding Natural Beauty (AONB) in the UK."],
    r"What food and drink does park campus offer .*": ["The campus’ refectory offers hot meals, snacks, fresh sandwiches, a salad bar and freshly baked cakes and pastries. There are vegan and vegetarian options available, as well as vending machines and free water stations, so you can top up your bottle. The Student Union bar provides evening entertainment and drinks or nearby you’ll find the buzzing district of Montpellier which has bars, restaurants, late-night cafes and supermarkets. Cheltenham’s best hot chocolate is just a 10 minute walk away on Bath Road, as well as The Natural Grocery Store, selling organic and all-natural products."],
}

# Function to check for pattern matches and get a response
def get_pattern_response(user_input):
    for pattern, responses in patterns_responses.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return None

# Function to generate response using GPT-2
def generate_response(user_input):
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    output = model.generate(input_ids, max_length=200, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Function to handle user submission
def handle_submission():
    user_input = user_entry.get()
    conversation_text.insert(tk.END, "User: " + user_input + "\n")

    # First, check for predefined pattern responses
    pattern_response = get_pattern_response(user_input)
    if pattern_response:
        bot_response = pattern_response
    else:
        # If no pattern matches, use GPT-2, possibly with a focused prompt
        focused_prompt = "University of Gloucestershire Information: " + user_input
        bot_response = generate_response(focused_prompt)

    conversation_text.insert(tk.END, "Bot: " + bot_response + "\n")
    conversation_text.see(tk.END)  # Scroll to the bottom
    user_entry.delete(0, tk.END)

# Generate QR code for the chatbot URL and display it in a new window
def generate_qr_code():
    qr_data = "https://your-chatbot-url.com"  # Replace with your chatbot URL
    qr = qrcode.make(qr_data)
    qr.show()

# Create a Tkinter window
root = tk.Tk()
root.title("University of Gloucestershire - AI Chat Bot")  # Update window title
root.geometry("750x600")  # Set window size

# Create a user entry box
user_entry = tk.Entry(root)
user_entry.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=handle_submission)
submit_button.pack(side=tk.TOP, padx=5, pady=5)

# Create a button to generate and display the QR code
qr_button = tk.Button(root, text="Show QR Code", command=generate_qr_code)
qr_button.pack(side=tk.TOP, padx=5, pady=5)

# Load and display the image
image = Image.open("3.jpeg")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

# Create a scrolled text widget to display conversation
conversation_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, font=("Arial", 12))
conversation_text.pack(expand=True, fill=tk.BOTH)

# Run the Tkinter event loop
root.mainloop()


# In[ ]:




