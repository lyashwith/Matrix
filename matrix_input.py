import tkinter as tk
import array
import transpose
root = tk.Tk()
root.geometry("500x200")
entry=[]
for i in range(3):
    row_entry=[]
    for j in range(3):
        box1 = tk.Entry(root, width=15)
        box1.grid(row=j, column=i, padx=10, pady=15)
        row_entry.append(box1)
    entry.append(row_entry)

matrix=[]
def matrix_gen():
    global matrix
    row_no=0
    while row_no<3:
        col_no=0
        row=[]
        while col_no<3:
            row.append(int(entry[col_no][row_no].get()))
            col_no+=1
        matrix.append(row)
        row_no+=1
    print(matrix)
    return matrix
    
def transpose_call():
    global matrix
    a=transpose.transpose(matrix,3,3)
    print(a)

    
btn = tk.Button(root, text="submit", command=matrix_gen)
btn.grid(row=4, column=0, columnspan=3, pady=10)
btn = tk.Button(root, text="submit", command=transpose_call)
btn.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
