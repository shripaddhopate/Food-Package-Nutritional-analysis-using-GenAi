import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk
import google.generativeai as genai
from tkinter import Text, Scrollbar
#enter your Gemini API Key here
genai.configure(api_key = "AzaSyA78u1MehLi5Ymfy30c9wZALUgZEkGC")
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    generation_config={"temperature": 0, "top_p": 0.5}
)
app = tk.Tk()
app.title("Eat Healthy") 
app.geometry("600x500") 
app.configure(bg="#f0f0f0")  

frame_image = tk.Frame(app, bg="white", bd=2, relief="groove")
frame_image.pack(pady=10)
label = tk.Label(frame_image, text="Upload an Image", font=("Arial", 12), bg="white")
label.pack(padx=20, pady=20)

frame_output = tk.Frame(app, bg="white", bd=2, relief="groove")
frame_output.pack(pady=10, fill="both", expand=True)

output_label = tk.Label(frame_output, text="Food For Health Analysis:", font=("Arial", 12, "bold"), bg="white")
output_label.pack(pady=5)

output_text = Text(frame_output, wrap="word", height=8, width=60, font=("Arial", 10), bg="#f9f9f9", fg="black")
output_text.pack(pady=5, padx=10)

scrollbar = Scrollbar(frame_output, command=output_text.yview)
scrollbar.pack(side="right", fill="y")
output_text.config(yscrollcommand=scrollbar.set)

def imageUploader():
    file_types = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=file_types)

    if path:
        img = Image.open(path)
        img = img.resize((200, 200))
        pic = ImageTk.PhotoImage(img)

        label.config(image=pic, text="")
        label.image = pic

        processImage(path)
    else:
        output_text.insert("1.0", "⚠️ No file selected! Please choose an image.\n")

def processImage(image_path):
    img = Image.open(image_path)

    text_prompt = """Read the nutritional elements and ingredients from the image.
    Provide a list of items with their weights and state whether it is good for health or not."""

    response = model.generate_content([text_prompt, img])

    output_text.delete("1.0", "end") 
    output_text.insert("1.0", response.text) 

btn_upload = tk.Button(app, text="📂 Upload Image", command=imageUploader, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, relief="raised")
btn_upload.pack(pady=10)

app.mainloop()
