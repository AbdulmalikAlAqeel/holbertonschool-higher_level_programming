# JavaScript - DOM Manipulation

## 📋 Description
This project introduces the fundamentals of **DOM (Document Object Model) Manipulation** using vanilla **JavaScript**. It covers how to select HTML elements, modify their styles and contents, bind events to user interactions, and make asynchronous network requests (`XMLHttpRequest` and `Fetch API`) directly within the browser environment.

---

## 🛠️ Requirements & Environment
- **Browser:** Google Chrome (version 57.0 or later)
- **Style Guide / Linter:** `semistandard` (Standard JS rules with mandatory semicolons)
- **Allowed Editors:** `vi`, `vim`, `emacs`
- **File Formatting:** All files must end with a single new line
- **Constraint:** HTML pages must not reload for each action (DOM updates, data fetching, etc.)

---

## 📂 Project Tasks

| Task | File | Description |
| :--- | :--- | :--- |
| **0. Color Me** | `0-script.js` | Updates the text color of the HTML `header` element to red (`#FF0000`) using `document.querySelector`. |
| **1. Click and turn red** | `1-script.js` | Updates the text color of the HTML `header` element to red (`#FF0000`) when the user clicks on the tag with id `red_header`. |
| **2. Add .red class** | `2-script.js` | Adds the class `red` to the `header` element when the user clicks on the tag with id `red_header`. |
| **3. Toggle classes** | `3-script.js` | Toggles the class of the `header` element between `red` and `green` when the user clicks on the tag with id `toggle_header`. |
| **4. List of elements** | `4-script.js` | Adds a new `<li>Item</li>` element to the `ul` with class `my_list` when the user clicks on the tag with id `add_item`. |
| **5. Change the text** | `5-script.js` | Updates the text of the `header` element to `New Header!!!` when the user clicks on the tag with id `update_header`. |

---

## 🚀 Usage & Testing

To test the scripts:
1. Open the respective HTML file (e.g., `0-main.html`) in **Google Chrome**.
2. Ensure the JavaScript file (e.g., `0-script.js`) is in the same directory and correctly referenced in the HTML.
3. Validate code compliance with `semistandard`:

```bash
semistandard --fix 0-script.js
semistandard 0-script.js


semistandard --fix 1-script.js
semistandard 1-script.js


semistandard --fix 2-script.js
semistandard 2-script.js


semistandard --fix 3-script.js
semistandard 3-script.js


semistandard --fix 4-script.js
semistandard 4-script.js


semistandard --fix 5-script.js
semistandard 5-script.js
