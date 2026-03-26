# 📂 Bulk File Renamer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

A simple and efficient Python script to automatically rename multiple files in a directory using a custom prefix and sequential numbering.

---

## 🚀 Overview

This project was created to automate the process of renaming files in bulk, making it easier to organize folders and maintain a consistent naming pattern.

The script scans a directory, identifies files, and renames them while preserving their original extensions.

---

## ✨ Features

* 🔹 Bulk file renaming
* 🔹 Custom prefix support
* 🔹 Sequential numbering system
* 🔹 Preserves file extensions
* 🔹 Lightweight and fast

---

## 📁 Example

Before:

```
IMG_8392.jpg  
photo_final.png  
random123.jpeg  
```

After:

```
file_1.jpg  
file_2.png  
file_3.jpeg  
```

---

## 🛠️ Technologies

* Python 3
* Built-in library: `os`

---

## ▶️ How to Use

1. Clone this repository:

```bash
git clone https://github.com/your-username/bulk-file-renamer.git
```

2. Navigate to the project folder:

```bash
cd bulk-file-renamer
```

3. Edit the script and set your folder path:

```python
folder = r"C:\path\to\your\files"
```

4. Run the script:

```bash
python rename_files.py
```

---

## ⚠️ Important Notes

* Make sure to backup your files before running the script
* Avoid using folders with critical files
* The script does not prevent overwriting files (yet)

---

## 📈 Future Improvements

* [ ] Sort files before renaming
* [ ] Add user input for prefix
* [ ] Prevent overwriting existing files
* [ ] Create a GUI version
* [ ] Add logging system

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by Henrique Cunha
