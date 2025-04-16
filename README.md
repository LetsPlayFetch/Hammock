# Hammock 🏕️  
### **Handles setup and cleanup for running a Python script in a temp virtual environment**

---

## 🧑‍💻 **Author / Contact**  
Made by [@LetsPlayFetch](https://github.com/LetsPlayFetch)  
Open an issue or reach out through GitHub if you’ve got questions or ideas.

---

## 🐛 **Bug Tracker**  
Report bugs here: [https://github.com/LetsPlayFetch/Hammock/issues](https://github.com/LetsPlayFetch/Hammock/issues)

---

## *Known Issues*
- Will fail if the Python script requires a truly non-existent or private module  
- Not optimized for Windows 
- Cant crawl to find additional libraries 
- Only allows a single programs execution

---

##  **Build Instructions**  
No build needed — just make sure you have Python 3 installed, then clone and go.

```bash
git clone git@github.com:LetsPlayFetch/Hammock.git
cd Hammock
```

---

### 🚀 **How to Run**  
Make sure you’re in the folder with `hammock.py`, then:

```bash
python3 hammock.py your_script.py
```

That’s it — it sets up a virtualenv, installs what you need, runs the script, and cleans it all up.
