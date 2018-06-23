
# coding: utf-8

# In[13]:


import re
import string

pyuic_file_path = "calc_full_template.py"
f = open(pyuic_file_path)
lines = f.readlines()


# In[14]:


lines = [i for i in lines if i != "\n"]
lines = [i for i in lines if i[0] != "#"]


# In[15]:


spaces = ["\n"] * 3
written_files = []
written_files.append(lines[0])
import_line = ["import sys\n"]
written_files += import_line
written_files += spaces
written_files += lines[1:6]


# In[16]:


ind = 0
for line in lines:
    if line[0:5] == "class":
        ind = lines.index(line) + 1
lines = lines[ind::]


# In[17]:


for line in lines:
    if line[4:7] == "def":
        print(line)
        lines.remove(line)


# In[18]:


for j in range(3):
    for i in range(len(lines)):
        lines[i] = lines[i].replace("MainWindow", "self", 10)


# In[19]:


for i in range(len(lines)):
    lines[i] = lines[i].replace("_translate(\"self\", ", "", 10)


# In[20]:


for i in range(len(lines)):
    lines[i] = lines[i].replace(", None)", "", 10)


# In[21]:


main_class = ["class Window(QtGui.QMainWindow):\n",
             "    def set_layout(self):\n",
             "        \"\"\"Creates the layout and initializes all objects\"\"\" \n",
             "        self.setWindowTitle(\"Title Goes Here\") \n"]
written_files += spaces
written_files += main_class


# In[22]:


ind_if = 0
for i in range(len(lines)):
    if lines[i][0:2] == "if":
        ind_if = i


# In[23]:


written_files += lines[:ind_if]


# In[24]:


written_files += spaces
init_lines = ["    def __init__(self):\n",
              "        \"\"\"The initialization method, which intializes the actions of each button and shows the GUI\"\"\" \n",
              "        super(Window, self).__init__()\n",
              "        self.set_layout()\n",
              "        self.show()\n"]
written_files = written_files + init_lines + spaces
main_lines = ["if __name__ == \"__main__\":\n",
              "    app = QtGui.QApplication(sys.argv)\n",
              "    MainWindow = Window()\n",
              "    sys.exit(app.exec_())\n"]
written_files += main_lines

for i in range(len(written_files)):
    written_files[i] = written_files[i].replace("self.retranslateUi(self)", "\n")
    written_files[i] = written_files[i].replace("QtCore.QMetaObject.connectSlotsByName(self)", "\n")
with open("converted.py", "w") as w:
    w.writelines(written_files)
    w.flush()
f.close()

