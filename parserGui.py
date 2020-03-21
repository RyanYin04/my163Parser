import tkinter as tk
import tkinter.filedialog, tkinter.messagebox
import pasrserTxtTidy as ptt

window = tk.Tk()
window.title('TXT 文本文件转换')
window.geometry('400x300')

infile_path = tk.StringVar()
def open_file():
    global infile_path
    path = tkinter.filedialog.askopenfilename()
    infile_path.set(path)
# 提示标签：
tk.Label(window, text = '文件路径', height = 1).pack()
# 创建按钮，选择文件：
tk.Button(window, text = '选择文件', width=15, height= 2, command = open_file).pack()
# 显示待操作文件路径：
tk.Label(window, textvariable = infile_path, width = 200, height = 2 ).pack()

# 创建按钮，选择导出位置：
direc_path = tk.StringVar()
def export_to():
    global direc_path
    path = tkinter.filedialog.askdirectory()
    direc_path.set(path)
tk.Label(window, text = '输出位置', height = 1).pack()
tk.Button(window, text = '选择路径', width = 15, height = 2, command = export_to).pack()
tk.Label(window, textvariable = direc_path, width = 200, height = 2 ).pack()


# 选择输出文件名：
tk.Label(window, text = '输出文件名', height = 1).pack()
output = tk.Entry(window)
output.pack()

# 创建按钮，执行程序：
def do():
    global infile_path, output, direc_path
    outFileName = output.get()
    ptt.run(infile_path.get(), outFileName, direc_path.get())
    tk.messagebox.showinfo(message= 'You are all set!')
tk.Button(window, text = '运行', width = 15, height = 2, command = do).pack()

window.mainloop()