import tkinter as tk
from tkinter import messagebox
import rdflib

# Load the OWL file using rdflib
g = rdflib.Graph()
g.parse("mathsITS.owl")

# Define a function to get area formula from the OWL file
def get_area_formula(shape):
    # Query to get the area formula for the selected shape
    query = f"""
        SELECT ?formula WHERE {{
            ?shape rdf:type <http://www.semanticweb.org/mathsITS#Shape> .
            ?shape rdfs:label "{shape}" .
            ?shape <http://www.semanticweb.org/mathsITS#hasAreaFormula> ?formula .
        }}
    """
    results = g.query(query)
    for row in results:
        return row[0].split('#')[-1]  # Extracting formula part
    
    return None

# Function to calculate area
def calculate_area():
    shape = shape_var.get()
    if shape == "Triangle":
        base = float(base_entry.get())
        height = float(height_entry.get())
        formula = "0.5 * base * height"
        area = 0.5 * base * height
    elif shape == "Square":
        side = float(side_entry.get())
        formula = "side * side"
        area = side * side
    else:
        formula = None
        area = None
    
    result_label.config(text=f"Formula: {formula}\nArea: {area}")

# Create the main window
root = tk.Tk()
root.title("Maths ITS - Shape Area Calculation")

# Create a label for instructions
instruction_label = tk.Label(root, text="Select a Shape and Provide Dimensions", font=("Arial", 14))
instruction_label.pack()

# Create a dropdown menu to select a shape
shape_var = tk.StringVar(root)
shape_var.set("Triangle")  # default value
shape_menu = tk.OptionMenu(root, shape_var, "Triangle", "Square")
shape_menu.pack()

# Entry fields for dimensions
base_label = tk.Label(root, text="Base:")
base_label.pack()
base_entry = tk.Entry(root)
base_entry.pack()

height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

side_label = tk.Label(root, text="Side:")
side_label.pack()
side_entry = tk.Entry(root)
side_entry.pack()

# Button to calculate area
calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.pack()

# Label to display the result
result_label = tk.Label(root, text="Formula: \nArea: ", font=("Arial", 12))
result_label.pack()

# Start the main event loop
root.mainloop()
