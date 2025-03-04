<div align="center">

# 📝️ `QRToSheet` <!-- omit in toc -->

</div>

## 📖 `Table Of Contents` <!-- omit in toc -->


- [🚗 `Features`](#-features)
- [📋 `Dependencies`](#-dependencies)
- [📥 `Istallation`](#-istallation)
  - [Using Pip](#using-pip)
- [⚙️ `Usage`](#️-usage)
  - [1. Create A Google Form](#1-create-a-google-form)
  - [2. Get The Pre-Filled Link](#2-get-the-pre-filled-link)
  - [3. Extract Required Values](#3-extract-required-values)
  - [4. Create And Configure The `.env` File](#4-create-and-configure-the-env-file)
  - [5. Link The Form To A Google Sheet](#5-link-the-form-to-a-google-sheet)
  - [6. Run The Script](#6-run-the-script)
  - [7. Verify QR Code Generation](#7-verify-qr-code-generation)
- [🔧 `Customization`](#-customization)

## 🚗 `Features`

- **No server or database required** – Generates QR codes locally without external dependencies.
- **Personalized QR codes** – Each generated QR code links to a Google Form with a pre-filled user name.
- **Automated pre-filling** – Users scanning the QR code will see their name already entered in the form field.

## 📋 `Dependencies`

Ensure you have Python installed on your system. Then, install the required dependencies:

- [Pillow (PIL)](https://pypi.org/project/pillow/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [qrcode](https://pypi.org/project/qrcode/)

## 📥 `Istallation`

### Using Pip

If you're not using NixOS, you can install all dependencies with:

```bash
pip install -r requirements.txt
```

## ⚙️ `Usage`

### 1. Create A Google Form

- Add a field that will store user names.
- The script currently supports only one field for names.

### 2. Get The Pre-Filled Link

- Click the three-dot menu (top-right of the form editor).
- Select **"Get pre-filled link"**.
- Enter any placeholder value in the name field.
- Click **"Get link"** and copy the generated URL.

### 3. Extract Required Values

From the copied URL:

```
https://docs.google.com/forms/d/e/{your_form_id}/viewform?usp=pp_url&entry.{your_form_field_id}={your_value}
```

Identify:

- `your_form_id` → The unique Google Form ID.
- `your_form_field_id` → The field entry number.
- `your_value` → Can be ignored since we only need it to get the entry number.

### 4. Create And Configure The `.env` File

Create a `.env` file in the project folder and add:

```
FORM_ID=your_form_id
USERS=John Doe,Jane Smith,Bob Johnson
ENTRY=your_entry_here
```

### 5. Link The Form To A Google Sheet

- Open the Google Form.
- Go to the **Responses** tab.
- Click **"Link to Sheets"** to save responses automatically.

### 6. Run The Script

Execute:

```bash
python main.py
```

### 7. Verify QR Code Generation

- A folder named `qr_codes` will be created.
- It will contain personalized QR codes for each user in the `.env` file.
- These QR codes will direct users to the Google Form with their name pre-filled.

## 🔧 `Customization`

The script currently supports only a single name field, but it can be modified to handle additional fields if needed.

- [⬆ Back To Top](%EF%B8%8F-qrtosheet-)