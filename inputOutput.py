import collections
import io
import math
import tkinter as tk
from tkinter import Canvas, ttk
from PIL import ImageTk, Image
from Text import prepared_textForRLE,prepared_textForLZW,prepared_textForHuffmanEncoding,prepared_textForGolomb,prepared_textForArithmetic,prepared_beforeCopression,RLEBest,LZWBest,ArithmeticBest,GolombBest,HuffmanBest,BestOftheWestNumbers,BestOftheWestVars
from RLEEncoding import compress_message
from LZWEncoding import Ord_lzw_compress, calculate_metrics as lzCalc
from HuffmanEncoding import huffman_compress, calculate_metrics as huCalc
from GolombEncoding import Golomb_Encoding_Text,calculate_metrics as GoCalc
from ArthmitcEncoding import arithmetic_coding,calculate_character_probability,calculate_metrics as ArCalc
from bitsForArithmetic import decimal_to_binary
from HuffmanTree import visualize_huffman_tree
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np  
import time






def on_closing():
    root.destroy()
    root.quit()
root = tk.Tk()
root.title("Compression Application")
notebook = ttk.Notebook(root)
notebook.place(relx=0, rely=0, relwidth=1, relheight=1)

def switch_tab(tab_index):
    notebook.select(tab_index)
def switch_button_color(button_index):
    # Reset background color of all buttons
    for i, button in enumerate(buttons):
        if i == button_index:
            button.config(bg="blue")
        else:
            button.config(bg="SystemButtonFace")
# Create tabs and add them to the notebook
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.add(tab1)
notebook.add(tab2)
notebook.add(tab3)
# Create a frame for the buttons
button_frame = ttk.Frame(root)
button_frame.place(relx=0.92, rely=0.39, anchor="n")

# Create buttons to switch between tabs
button1 = tk.Button(button_frame, text="Switch to Tab 1", command=lambda: [switch_tab(0),switch_button_color(0)])
button1.pack(side="top")

button2 = tk.Button(button_frame, text="Switch to Tab 2", command=lambda: [switch_tab(1),switch_button_color(1)])
button2.pack(side="top")

button3 = tk.Button(button_frame, text="Switch to Tab 3", command=lambda: [switch_tab(2),switch_button_color(2)])
button3.pack(side="top")
buttons = [button1,button2,button3]

window_width = 950
window_height = 650
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))
##########################################################################################
#Tab11
##########################################################################################
#############################
#Interface Tier
#############################

selected_button = None

input_frame = tk.Frame(tab1, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
input_frame.place(relx=0.23, rely=0.02, anchor="n", width=400, height=100)

instructions_label = tk.Label(input_frame, text="Enter text below:")
instructions_label.place(relx=0.1, rely=0.1, anchor="w")

text_entry = tk.Entry(input_frame, width=50)
text_entry.place(relx=0.1, rely=0.3, anchor="w")

small_instructions_label = tk.Label(input_frame, text="M for Golomb Encoding:")
small_instructions_label.place(relx=0.1, rely=0.6, anchor="w")

small_text_entry = tk.Entry(input_frame, width=10)
small_text_entry.place(relx=0.1, rely=0.8, anchor="w")

initial_outputFrame = tk.Frame(tab1, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
initial_outputFrame.place(relx=0.72, rely=0.02, anchor="n", width=500, height=100)

display_preProccessod_Text = tk.Label(initial_outputFrame,text="",anchor="nw",justify="left",wraplength=300)
display_preProccessod_Text.place(relx=0.01, rely=0.02, anchor="nw", relheight=0.98)

display_initial_metrics = tk.Label(initial_outputFrame,text="",anchor="nw",justify="left",wraplength=150)
display_initial_metrics.place(relx=0.7, rely=0.02, anchor="nw", relheight=0.98)

display_frame1 = tk.Frame(tab1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
display_frame1.place(relx=0.162, rely=0.2, anchor="n", width=270, height=80)

text_display1 = tk.Label(display_frame1, text="", anchor="nw", justify="left")
text_display1.place(relx=0.01, rely=0.02, anchor="nw", relwidth=0.98, relheight=0.98)

display_frame2 = tk.Frame(tab1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
display_frame2.place(relx=0.16, rely=0.35, anchor="n", width=270, height=150)

text_display2 = tk.Label(display_frame2, text="", anchor="nw", justify="left")
text_display2.place(relx=0.01, rely=0.02, anchor="nw", relwidth=0.98, relheight=0.98)

display_frame3 = tk.Frame(tab1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
display_frame3.place(relx=0.50, rely=0.70, anchor="n", width=930, height=160)

text_display3 = tk.Label(display_frame3, text="", anchor="nw", justify="left")
text_display3.place(relx=0.01, rely=0.02, anchor="nw", relwidth=0.98, relheight=0.9)  

display_frame4 = tk.Frame(tab1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
display_frame4.place(relx=0.6, rely=0.2, anchor="n", width=500, height=160)

text_display4 = tk.Label(display_frame4, text="", anchor="nw", justify="left")
text_display4.place(relx=0.01, rely=0.02, anchor="nw", relwidth=0.98, relheight=0.9) 

display_frame5 = tk.Frame(tab1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
display_frame5.place(relx=0.6, rely=0.47, anchor="n", width=500, height=140)

text_display5 = tk.Label(display_frame5, text="", anchor="nw", justify="left")
text_display5.place(relx=0.01, rely=0.02, anchor="nw", relwidth=0.98, relheight=0.9)  

def on_submit_enter(event):
    submit_button.config(bg="yellow")

def on_submit_leave(event):
    submit_button.config(bg="SystemButtonFace")

def run():
    global RLETime
    global LZWTime 
    global GolombTime 
    global HuffmanTime 
    global ArithmeticTime
    submit_button.config(bg="red")
    root.update()  # Update the GUI to show the red color
    try:
        showTextWithCalculatedMetrics()
        startTime = time.time()
        display_text1ForRLEEncdoing()
        RLETime = time.time()-startTime
        display_text2ForDoctorASCIILZWEncdoing()
        LZWTime = time.time()-startTime
        display_text3ForHuffmanEncoding()
        HuffmanTime = time.time()-startTime
        display_text4ForGolombEncoding()
        GolombTime = time.time()-startTime
        display_text5ForArithmeticEncoding()
        ArithmeticTime = time.time()-startTime
        runPlot()
        runTree()
    except Exception as e:
        print(f"{e} :::> You may be leave entry empty")
        text_entry.delete(0, tk.END)  # Clear the current text
        text_entry.insert(0, "Please, Enter text for compression")  # Insert the new text

    submit_button.config(bg="green")


submit_button = tk.Button(input_frame, text="Compress", command=run)
submit_button.place(relx=0.75, rely=0.8, anchor="w")
submit_button.bind("<Enter>", on_submit_enter)
submit_button.bind("<Leave>", on_submit_leave)

# Golomb choice button 
golomb_button_User = tk.Button(input_frame,text="UserChoice", command=lambda: select_button(golomb_button_User))
golomb_button_User.place(relx=0.35, rely=0.82, anchor="w")

golomb_button_Default = tk.Button(input_frame,text="DefaultValue", command=lambda: select_button(golomb_button_Default))
golomb_button_Default.place(relx=0.53, rely=0.82, anchor="w")

def choosen_text(index):
    if index == 0:
        text_entry.delete(0, tk.END)  # Clear the current text
        text_entry.insert(0, RLEBest)  # Insert the new text
    elif index == 1:
        text_entry.delete(0, tk.END)  # Clear the current text
        text_entry.insert(0, LZWBest)  # Insert the new text
    elif index == 2:
        text_entry.delete(0, tk.END)  # Clear the current text
        text_entry.insert(0, HuffmanBest)  # Insert the new text
    elif index == 3:
        text_entry.delete(0, tk.END)  # Clear the current text
        text_entry.insert(0, GolombBest)  # Insert the new text
    elif index == 4:
        text_entry.delete(0, tk.END)  # Clear the current text
        text_entry.insert(0, ArithmeticBest)  # Insert the new text
global selected_button2
selected_button2 = None
def select_buttonForBest(button):
    
    selected_button2 = button
    if selected_button2:
        selected_button2.config(relief=tk.RAISED, bg="SystemButtonFace")
    selected_button2.config(relief=tk.SUNKEN, bg="light green")

    # Reset the background color of all buttons
    for btn in buttons2:
        btn.config(bg="SystemButtonFace")

    # Set the background color of the selected button to light green
    button.config(bg="light green")
def button_click_action(button):
    if button["bg"] != "light green":
        select_buttonForBest(button)
    else:
        button.config(relief=tk.RAISED, bg="SystemButtonFace")
        for btn in buttons2:
            btn.config(relief=tk.RAISED)
        text_entry.delete(0, tk.END)
        

            

best_button_frame = tk.Frame(tab1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
best_button_frame.place(relx=0.160, rely=0.6, anchor="n", width=270, height=50)
RLEBestTextButton = tk.Button(best_button_frame, text="RLE", command=lambda: [choosen_text(0),button_click_action(RLEBestTextButton)])
RLEBestTextButton.place(relx=0.01, rely=0.5, anchor="w")
LZWBestTextButton = tk.Button(best_button_frame, text="LZW", command=lambda: [choosen_text(1),button_click_action(LZWBestTextButton)])
LZWBestTextButton.place(relx=0.13, rely=0.5, anchor="w")
HuffmanBestTextButton = tk.Button(best_button_frame, text="Huffman", command=lambda: [choosen_text(2),button_click_action(HuffmanBestTextButton)])
HuffmanBestTextButton.place(relx=0.27, rely=0.5, anchor="w")
ArithmeticBestButton = tk.Button(best_button_frame, text="Arithmetic", command=lambda: [choosen_text(3),button_click_action(ArithmeticBestButton)])
ArithmeticBestButton.place(relx=0.495, rely=0.5, anchor="w")
GolombBestTextButton = tk.Button(best_button_frame, text="Golomb", command=lambda: [choosen_text(4),button_click_action(GolombBestTextButton)])
GolombBestTextButton.place(relx=0.755, rely=0.5, anchor="w")
buttons2=[RLEBestTextButton, LZWBestTextButton, HuffmanBestTextButton, ArithmeticBestButton, GolombBestTextButton]

        
alternate_color_id = None

def alternate_color():
    if golomb_button_User["bg"] == "light green":
        golomb_button_User.config(bg="SystemButtonFace")
        golomb_button_Default.config(bg="light green")
    else:
        golomb_button_User.config(bg="light green")
        golomb_button_Default.config(bg="SystemButtonFace")

def start_alternating():
    global alternate_color_id
    alternate_color()
    alternate_color_id = root.after(100, start_alternating)

# Call start_alternating to initialize the alternating color effect
start_alternating()

def select_button(button):
    global selected_button
    if selected_button:
        selected_button.config(relief=tk.RAISED, bg="SystemButtonFace")
    selected_button = button
    selected_button.config(relief=tk.SUNKEN, bg="green")
    # Enable or disable small_text_entry based on the selected button
    if selected_button == golomb_button_User :
        small_text_entry.config(state=tk.NORMAL)
    else:
        small_text_entry.delete(0, tk.END)
        small_text_entry.config(state=tk.DISABLED)
    
    # Stop the alternating color effect when a button is pressed
    root.after_cancel(alternate_color_id)

########################################################################################################
##########################################################################################
#Tab2
##########################################################################################
#############################
#Interface & Logic Tier
#############################
Grand_frame = tk.Frame(tab2, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
Grand_frame.place(relx=0.06,rely=.01,width=730,height=575)
def get_max_CR_name():
    # Mapping of variable names to descriptions
    list_MappingCR = {
        "Run Length Encoding":RLEcR,
        "LZW Encoding":LZWcR,
        "Golomb Encoding":GolombcR,
        "Huffman Encoding":HuffmancR,
        "Arithmetic Encoding":ArithmeticcR
    }
    best_cr = max(list_MappingCR, key=list_MappingCR.get)
    return best_cr
def get_max_E_name():
    # Mapping of variable names to descriptions
    list_Mappinge = {
        "Run Length Encoding":RLEe,
        "LZW Encoding":LZWe,
        "Golomb Encoding":Golombe,
        "Huffman Encoding":Huffmane,
        "Arithmetic Encoding":Arithmetice
    }
    best_e = max(list_Mappinge, key=list_Mappinge.get)
    return best_e
def get_max_T_name():
    # Mapping of variable names to descriptions
    list_Mappingt = {
        "Run Length Encoding":RLETime,
        "LZW Encoding":LZWTime,
        "Golomb Encoding":GolombTime,
        "Huffman Encoding":HuffmanTime,
        "Arithmetic Encoding":ArithmeticTime
    }
    best_t = max(list_Mappingt, key=list_Mappingt.get)
    return best_t
    

def runPlot():
    # Clear previous plot if it exists
    for widget in Grand_frame.winfo_children():
        widget.destroy()

    # Create a frame to hold the plot
    plot_frame = tk.Frame(Grand_frame)
    plot_frame.place(relx=0.06,rely=0.01)
    BestAlgoFrame = tk.Frame(Grand_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
    BestAlgoFrame.place(relx=0.055,rely=0.85,width=650,height=75)
    # Data for the bar chart
    categories = ['Run Length', 'LZW', 'Golomb', 'Huffman', 'Arithmetic']
    # If we want fair compareance we equal compression ratio for Arithmetic Encoding to zero
    ArithmeticcR = 0 
    CRvalues = [RLEcR, LZWcR, GolombcR, HuffmancR, ArithmeticcR]
    best_cr = get_max_CR_name()
    # print(best_cr)
    Evalues = [RLEe,LZWe,Golombe,Huffmane,Arithmetice]
    best_e = get_max_E_name()
    # print(best_e)
    Times = [RLETime,LZWTime,GolombTime,HuffmanTime,ArithmeticTime]
    best_t = get_max_T_name()
    # print(best_t)
    best_val_var = BestOftheWestVars.format(best_cr,best_e,best_t)
    best_vals_num = BestOftheWestNumbers.format(round(max(CRvalues),5),round(max(Evalues),5),round(min(Times),6)) 
    text_Display_bestAlgoLabel = tk.Label(BestAlgoFrame,text="Best Compression based on:",anchor="nw",justify="center")
    text_Display_bestAlgoLabel.place(relx=0.1,rely=0.1)
    text_Display_bestAlgo = tk.Label(BestAlgoFrame,text="",anchor="nw",justify="left")
    text_Display_bestAlgo.place(relx=0.1,rely=0.4)
    text_Display_bestAlgo.config(text=best_vals_num)
    text_Display_bestName = tk.Label(BestAlgoFrame,text="",anchor="nw",justify="left")
    text_Display_bestName.place(relx=0.1,rely=0.7)
    text_Display_bestName.config(text=best_val_var)
    
    # Create a Matplotlib figure and axis

# Create a NumPy array of indices for the x-coordinates
    indices = np.arange(len(categories))
    fig, ax = plt.subplots()

    # Create bar chart
    # Create bar chart for the first set of values
    ax.bar([x - 0.2 for x in range(len(categories))], CRvalues, width=0.2, label='Compression Ratio')
    ax.bar([x for x in range(len(categories))], Evalues, width=0.2, label='Efficiency')
    ax.bar([x + 0.2 for x in range(len(categories))], Times, width=0.2, label='Time')
    # Add labels and title
    ax.set_xlabel('Compression Algorithms')
    ax.set_title('Best Algorithm')
    ax.set_xticks(indices)
    ax.set_xticklabels(categories)
    ax.legend()
    # Embed the Matplotlib plot in the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(anchor="center")
########################################################################################################
##########################################################################################
#Tab3
##########################################################################################
#############################
#Interface & Logic Tier
#############################
Grand_Tree_frame = tk.Frame(tab3, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
Grand_Tree_frame.place(relx=0.06,rely=.01,width=700,height=560)
HuffmanLabel = tk.Label(tab3,text="Huffman Tree",font=("Helvetica", 16),highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
HuffmanLabel.place(relx=0.83,rely=0.05)
magnification = 1.0  # Initialize magnification factor

def runTree():
    # Clear previous plot if it exists
    for widget in Grand_Tree_frame.winfo_children():
        widget.destroy()
        
    plot_frame = tk.Frame(Grand_Tree_frame)
    plot_frame.pack(fill=tk.BOTH, expand=True)
    
    entered_text = text_entry.get()
    huffman_tree = huffman_compress(entered_text)[2]
    graph = visualize_huffman_tree(huffman_tree)
    image_bytes = graph.pipe(format='png')
    image = Image.open(io.BytesIO(image_bytes))
    photo = ImageTk.PhotoImage(image)  # Keep a reference to prevent garbage collection

    global canvas
    canvas = tk.Canvas(plot_frame, width=image.width, height=image.height)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo  # Keep a reference to the image object
    canvas.pack(fill=tk.BOTH, expand=True)

    # Create buttons
    buttons_frame = tk.Frame(tab3)
    buttons_frame.place(relx=0.06,rely=.92)

    move_left_button = tk.Button(buttons_frame, text="Move Left", command=move_left)
    move_left_button.pack(side=tk.LEFT, padx=5, pady=5)

    move_right_button = tk.Button(buttons_frame, text="Move Right", command=move_right)
    move_right_button.pack(side=tk.LEFT, padx=5, pady=5)
    
    move_up_button = tk.Button(buttons_frame, text="Move Up", command=move_up)
    move_up_button.pack(side=tk.LEFT, padx=5, pady=5)

    move_down_button = tk.Button(buttons_frame, text="Move Down", command=move_down)
    move_down_button.pack(side=tk.LEFT, padx=5, pady=5)

def update_canvas():
    global magnification
    current_width = canvas.winfo_width()
    current_height = canvas.winfo_height()

    # Calculate new dimensions based on magnification
    new_width = int(current_width * magnification)
    new_height = int(current_height * magnification)

    # Get the current scroll region
    x0, y0, x1, y1 = canvas.bbox("all")

    # Adjust the scroll region based on the new dimensions
    canvas.config(scrollregion=(0, 0, new_width, new_height))

    # Rescale the canvas contents
    canvas.scale("all", 0, 0, magnification, magnification)

def move_left():
    # Move canvas view to the left
    canvas.xview_scroll(-1, "units")

def move_right():
    # Move canvas view to the right
    canvas.xview_scroll(1, "units")
def move_up():
    # Move canvas view upwards
    canvas.yview_scroll(-1, "units")

def move_down():
    # Move canvas view downwards
    canvas.yview_scroll(1, "units")

#############################
#Logic Tier
#############################
########################################################################################################
# Call alternate_color to initialize the initial state

def showTextWithCalculatedMetrics():
    entered_text = text_entry.get()
    text1 = entered_text.format()
    bits_before_encoding = len(entered_text)*8
    char_freq = collections.Counter(entered_text)
    entropy = calculate_entropy(char_freq)
    text2 = prepared_beforeCopression.format(bits_before_encoding,round(entropy,4))
    display_preProccessod_Text.config(text=text1)
    display_initial_metrics.config(text=text2)

def calculate_entropy(char_freq):
    total_chars = sum(char_freq.values())
    entropy = -sum((freq / total_chars) * math.log2(freq / total_chars) for freq in char_freq.values())
    return entropy

def display_text1ForRLEEncdoing():
    global RLEcR  
    global RLEe
    entered_text = text_entry.get()
    bits_after_encoding, compression_ratio = compress_message(entered_text)
    updated_prepared_text = prepared_textForRLE.format(bits_after_encoding,
                                                       round(compression_ratio, 4))
    RLEcR = compression_ratio
    RLEe = 0
    text_display1.config(text=updated_prepared_text)

def display_text2ForDoctorASCIILZWEncdoing():
    global LZWcR
    global LZWe
    entered_text = text_entry.get()
    compressed_data = Ord_lzw_compress(entered_text)
    calculated_Data = lzCalc(entered_text, compressed_data)
    bits_after_encoding = round(calculated_Data[1], 4)
    average_length = round(calculated_Data[4], 4)
    compression_ratio = round(calculated_Data[2], 4)
    efficiency = round(calculated_Data[5], 4)
    updated_prepared_text = prepared_textForLZW.format(compressed_data,
                                                       bits_after_encoding,
                                                       average_length,
                                                       compression_ratio,
                                                       efficiency)
    
    text_display2.config(text=updated_prepared_text)
    LZWcR = compression_ratio
    LZWe = efficiency
    
def display_text3ForHuffmanEncoding():
    global HuffmancR
    global Huffmane
    entered_text = text_entry.get()
    compressed_data,code_map,huffman_tree = huffman_compress(entered_text)
    calculated_Data = huCalc(entered_text)
    bits_after_encoding = round(calculated_Data[1], 4)
    compression_ratio = round(calculated_Data[2], 4)
    probablities = calculated_Data[3]
    average_length = round(calculated_Data[5], 4)
    efficiency = round(calculated_Data[6], 4)
    updated_prepared_text = prepared_textForHuffmanEncoding.format(
        compressed_data,
        code_map,
        huffman_tree,
        bits_after_encoding,
        probablities,
        average_length,
        compression_ratio,
        efficiency)
    HuffmancR = compression_ratio
    Huffmane = efficiency
    text_display3.config(text=updated_prepared_text)
    
def display_text4ForGolombEncoding():
    global GolombcR
    global Golombe
    entered_text = text_entry.get()
    try:
        if selected_button == golomb_button_User:
            # print("You Entered first step")
            M = int(small_text_entry.get())
        elif selected_button == golomb_button_Default:
            # Calculate M as the square root of the length of entered_text
            M = int(math.sqrt(len(entered_text)))
        else:
            text_display4.config(text="You left text compression empty")

    except Exception as e:
        print(f"You Choose default mode for golomb or Enter numrical")
            
    compressed_data,RLE = Golomb_Encoding_Text(entered_text,M)
    calculated_Data = GoCalc(entered_text,compressed_data,RLE,M)
    bits_after_encoding = calculated_Data[1]
    compression_ratio = calculated_Data[2]
    average_length = calculated_Data[3]
    efficiency = calculated_Data[5]
    updated_prepared_text = prepared_textForGolomb.format(
        compressed_data,
        RLE,
        bits_after_encoding,
        average_length,
        compression_ratio,
        efficiency)
    GolombcR = compression_ratio
    Golombe = efficiency
    text_display4.config(text=updated_prepared_text)

def display_text5ForArithmeticEncoding():
    global ArithmeticcR
    global Arithmetice
    entered_text = text_entry.get()
    probabilities = calculate_character_probability(entered_text)
    ranges, last_range, original_size, compressed_value = arithmetic_coding(entered_text
                                                                              ,probabilities)
    calculated_Data = ArCalc(original_size,compressed_value,probabilities)
    bits_after_encoding = decimal_to_binary(compressed_value)[3]
    average_length = calculated_Data[1]
    compression_ratio = calculated_Data[2]
    efficiency = calculated_Data[3]

    updated_prepared_text = prepared_textForArithmetic.format(
        compressed_value,
        ranges,
        last_range,
        bits_after_encoding,
        average_length,
        compression_ratio,
        efficiency
    )
    ArithmeticcR = compression_ratio
    Arithmetice = efficiency
    text_display5.config(text=updated_prepared_text)

########################################################################################################
    
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()



 
