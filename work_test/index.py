# Call lib
# import Ensemble
# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from sklearn.metrics import accuracy_score
import Ensemble
from PIL import Image, ImageTk
from tkinter import PhotoImage

# Create a Tkinter window
window = tk.Tk()
window.title('milknew.csv')

# Get data from Ensemble.py
data = Ensemble.Voting.data

left_frame = tk.Frame(window, bg='#FAEBD7')  # Set background color for the left frame
left_frame.pack(side=tk.RIGHT, padx=10, pady=20)

# Create labels and entry widgets for user input
input_labels = ['pH', 'Temprature', 'Taste', 'Odor', 'Turbidity', 'Colour']
entry_boxes = []

# ... (โค้ดก่อนหน้านี้)

for label_text in input_labels:
    if label_text == 'pH':
        label_color = '#FAEBD7'  # 
        label_fg_color = '#03a9f4'  # รหัสสีของข้อความ
    elif label_text == 'Temprature':
        label_color = '#FAEBD7'  # 
        label_fg_color = '#ff8f00'  # รหัสสีของข้อความ
    elif label_text == 'Taste':
        label_color = '#FAEBD7'  # 
        label_fg_color = '#bf360c'  # รหัสสีของข้อความ
    elif label_text == 'Odor':
        label_color = '#FAEBD7'  # 
        label_fg_color = '#3949ab'  # รหัสสีของข้อความ
    elif label_text == 'Turbidity':
        label_color = '#FAEBD7'  # 
        label_fg_color = '#cddc39'  # รหัสสีของข้อความ
    elif label_text == 'Colour':
        label_color = '#FAEBD7'  # 
        label_fg_color = '#7571ff'  # รหัสสีของข้อความ
    else:
        label_color = '#FAEBD7'  # สีพื้นหลังปกติ

    

    label = tk.Label(left_frame, text=label_text, font=("Arial", 18), bg=label_color, fg=label_fg_color)  # ใช้ fg เพื่อกำหนดสีของข้อความ
    label.grid(row=input_labels.index(label_text), column=0, pady=5, sticky='e')  # Use 'e' for right alignment

    entry_var = tk.DoubleVar()  # Use DoubleVar for numeric input
    entry = tk.Entry(left_frame, textvariable=entry_var, font=("Arial", 20))  # ปรับ font ในนี้
    entry.grid(row=input_labels.index(label_text), column=1, pady=5)

    entry_boxes.append(entry_var)

# ... (โค้ดที่เหลือ)


# # Create a button to trigger predictions
# predict_button = tk.Button(left_frame, text="Predict Quality", command=lambda: predict_quality(entry_boxes))
# predict_button.grid(row=len(input_labels), column=0, columnspan=2, pady=10)

# Load the image for the button
button_image = PhotoImage(file="ipmgwork\IMG_2393.PNG")  # แทน path/to/your/image.png ด้วยตำแหน่งของไฟล์รูปภาพของคุณ
# Create a button with the image
predict_button = tk.Button(left_frame, image=button_image, command=lambda: predict_quality(entry_boxes), bd=0)  # bd=0 ทำให้ไม่มีกรอบรอบปุ่ม
predict_button.grid(row=len(input_labels), column=0, columnspan=2, pady=10)

# Function to predict quality based on user input
def predict_quality(entry_boxes):
    # Get user input from entry boxes
    user_input = [entry.get() for entry in entry_boxes]

    # Make predictions using the Voting Classifier
    predictions = Ensemble.Voting.voting_clf.predict([user_input])

    # Map numeric predictions
    predicted_label = 'Low' if predictions[0] == 1 else 'High'

    # Display the predicted quality
    result_label["text"] = f"Predicted Quality = {predicted_label}"
    result_label["bg"] = "#FAEBD7"
    result_label["font"] = ("Arial", 15, "bold")

    # Display accuracy information for each classifier
    accuracy_labels["text"] = ""
    for model, model_instance in zip(
        ['Bagging', 'Boosting', 'Random Forest', 'Logistic', 'Naive Bayes', 'SVM', 'Decision Tree', 'MLP', 'AdaBoost'],
        [Ensemble.Voting.bagging_clf, Ensemble.Voting.boosting_clf, Ensemble.Voting.random_forest_model,
        Ensemble.Voting.logistic_model,
        Ensemble.Voting.naive_bayes_model, Ensemble.Voting.svm_model, Ensemble.Voting.decision_tree_model,
        Ensemble.Voting.mlp_model, Ensemble.Voting.adaboost_model]):
        predictions = model_instance.predict(Ensemble.Voting.X)
        accuracy = accuracy_score(Ensemble.Voting.y, predictions) * 100
        
        # เปลี่ยนเป็น Low หรือ High ตามค่าความแม่นยำ
        accuracy_text = "High" if accuracy >= 80 else "Low"
        
        accuracy_labels["text"] += f"{model} Accuracy : {accuracy_text}\n"
        accuracy_labels["fg"] = "green" if accuracy >= 80 else "red"  # Color the text based on accuracy
        accuracy_labels["bg"] = '#FAEBD7'
        accuracy_labels["justify"] = "left"

# Create a label to display the predicted quality
result_label = tk.Label(left_frame, text="", font=("Arial", 18))
result_label.grid(row=len(input_labels) + 1, column=0, columnspan=2, pady=10)

# Create a label to display accuracy information
accuracy_labels = tk.Label(left_frame, text="", font=("Arial", 13))
accuracy_labels.grid(row=len(input_labels) + 2, column=0, columnspan=2, pady=10)

# Pack the Treeview to the window at the BOTTOM
tree = ttk.Treeview(window)
tree["columns"] = tuple(data.columns)

# Add columns to Treeview
for col in data.columns:
    tree.column(col, anchor="center", width=100)
    tree.heading(col, text=col, anchor="center")

# Insert data into Treeview with alternating row colors
for index, row in data.iterrows():
    if index % 2 == 0:
        tree.insert("", index, values=tuple(row), tags=('even',))
    else:
        tree.insert("", index, values=tuple(row), tags=('odd',))

# Configure tag colors
tree.tag_configure('even', background='#b3e0ff')
tree.tag_configure('odd', background='#ffffff')

# Insert data into Treeview
for index, row in data.iterrows():
    tree.insert("", index, values=tuple(row))

# Pack the Treeview to the window at the BOTTOM
tree.pack(expand=tk.YES, fill=tk.BOTH, pady=10, side=tk.LEFT)

# table = ImageTk.PhotoImage(Image.open("ipmgwork\IMG_2396.PNG"))
# canvas = tk.Canvas(window, width=table.width(), height=table.height())
# canvas.create_image(20, 10, anchor="nw", image=table)
# canvas.pack(side=tk.RIGHT)

# Run the Tkinter event loop
window.mainloop()
