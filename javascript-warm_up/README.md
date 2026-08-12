# JavaScript - Warm up

## 📋 Description
This repository introduces core **JavaScript** fundamentals executed on the backend using **Node.js (v14.x)**. The project covers foundational concepts such as variable declarations (`const`, `let`), primitive and reference data types, conditional branching, loops, functions, objects, and modular scripting, while maintaining compliance with the **semistandard** code formatting rules.

---

## 🛠️ Requirements & Environment
- **Operating System:** Ubuntu 20.04 LTS
- **Runtime Environment:** Node.js v14.x
- **Style Guide / Linter:** `semistandard` (Standard JS rules with mandatory semicolons)
- **Allowed Editors:** `vi`, `vim`, `emacs`
- **Shebang Header:** `#!/usr/bin/node` (first line of every script)
- **File Permissions:** All script files must be executable (`chmod +x`)
- **Formatting:** Files must end with a single new line

---

## 💻 Environment Setup

### 1. Install Node.js 14 & NPM
```bash
curl -sL [https://deb.nodesource.com/setup_14.x](https://deb.nodesource.com/setup_14.x) | sudo -E bash -
sudo apt-get install -y nodejs
```

2. Install Semistandard Linter

```bash
sudo npm install semistandard --global
```
## 📂 Project Tasks

| Task | File | Description |
| :--- | :--- | :--- |
| **0. First constant, first print** | `0-javascript_is_amazing.js` | Script that prints `"JavaScript is amazing"` using a `const` variable `myVar` and `console.log()`. |
| **1. 3 languages** | `1-multi_languages.js` | Script that prints 3 specific lines (`C is fun`, `Python is cool`, `JavaScript is amazing`) using `console.log()` without `var`. |
| **2. Arguments** | `2-arguments.js` | Script that checks command-line arguments using `process.argv` and prints messages depending on whether 0, 1, or multiple arguments are passed. |
| **3. Value of my argument** | `3-value_argument.js` | Script that prints the first command-line argument passed to it, or prints `"No argument"` if none are provided, without using `length` or `var.`|
| **4. Create a sentence** | `4-concat.js` | Script that prints two passed command-line arguments in the format `"<arg1> is <arg2>"` using `console.log()` and template literals. |
| **5. An Integer** | `5-to_integer.js` | Script that prints `"My number: <integer>"` if the first argument can be converted to an integer; otherwise, prints `"Not a number"`. |
| **6. Loop to languages** | `6-multi_languages_loop.js` | Script that prints 3 lines using an array of strings and a loop, without using `if/else` statements, with only one `console.log`, and without `var`. |

## 🚀 Usage & Testing

To run the script and verify code style compliance:

```Bash
# Grant executable permissions
chmod +x 0-javascript_is_amazing.js

# Execute the script
./0-javascript_is_amazing.js
# Output: JavaScript is amazing

# Validate code compliance with semistandard
semistandard ./0-javascript_is_amazing.js
```

```Bash
# Grant executable permissions
chmod +x 1-multi_languages.js

# Execute the script
./1-multi_languages.js
# Output:
# C is fun
# Python is cool
# JavaScript is amazing

# Validate code compliance with semistandard
semistandard ./1-multi_languages.js
```

```Bash
# Grant executable permissions
chmod +x 2-arguments.js

# Execute the script with arguments
./2-arguments.js Holberton School
# Output: Arguments found

# Validate code compliance with semistandard
semistandard ./2-arguments.js
```

```Bash
# Grant executable permissions
chmod +x 3-value_argument.js

# Execute the script with an argument
./3-value_argument.js School
# Output: School

# Validate code compliance with semistandard
semistandard ./3-value_argument.js
```

```Bash
# Grant executable permissions
chmod +x 4-concat.js

# Execute the script with two arguments
./4-concat.js c cool
# Output: c is cool

# Validate code compliance with semistandard
semistandard ./4-concat.js
```

```Bash
# Grant executable permissions
chmod +x 5-to_integer.js

# Execute the script with a number
./5-to_integer.js 89
# Output: My number: 89

# Validate code compliance with semistandard
semistandard ./5-to_integer.js
```

```Bash
# Grant executable permissions
chmod +x 6-multi_languages_loop.js

# Execute the script
./6-multi_languages_loop.js
# Output:
# C is fun
# Python is cool
# JavaScript is amazing

# Validate code compliance with semistandard
semistandard ./6-multi_languages_loop.js
```
