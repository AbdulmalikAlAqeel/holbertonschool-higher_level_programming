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
| **3. Value of my argument** | `3-value_argument.js` | Script that prints the first command-line argument passed to it, or prints `"No argument"` if none are provided, without using `length` or `var`. |
| **4. Create a sentence** | `4-concat.js` | Script that prints two passed command-line arguments in the format `"<arg1> is <arg2>"` using `console.log()` and template literals. |
| **5. An Integer** | `5-to_integer.js` | Script that prints `"My number: <integer>"` if the first argument can be converted to an integer; otherwise, prints `"Not a number"`. |
| **6. Loop to languages** | `6-multi_languages_loop.js` | Script that prints 3 lines using an array of strings and a loop, without using `if/else` statements, with only one `console.log`, and without `var`. |
| **7. I love C** | `7-multi_c.js` | Script that prints `"C is fun"` x times based on the first argument, or prints `"Missing number of occurrences"` if the argument is missing or invalid. |
| **8. Square** | `8-square.js` | Script that prints a square of size `x` using the character `X`, or prints `"Missing size"` if the argument is missing or invalid. |
| **9. Add** | `9-add.js` | Script that prints the addition of 2 integers using a defined function `add(a, b)`, without using `var`. |
| **10. Factorial** | `10-factorial.js` | Script that computes and prints a factorial recursively using a function, returning `1` for `NaN`, without using `var`. |
| **11. Second biggest!** | `11-second_biggest.js` | Searches for the second biggest integer in the list of arguments. |
| **12. Object** | `12-object.js` | Updates the value of a property inside a constant object. |
| **13. Add file** | `13-add.js` | A module that exports a function for addition. |

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

```Bash
# Grant executable permissions
chmod +x 7-multi_c.js

# Execute the script with a number
./7-multi_c.js 3
# Output:
# C is fun
# C is fun
# C is fun

# Validate code compliance with semistandard
semistandard ./7-multi_c.js
```

```Bash
# Grant executable permissions
chmod +x 8-square.js

# Execute the script with a size
./8-square.js 3
# Output:
# XXX
# XXX
# XXX

# Validate code compliance with semistandard
semistandard ./8-square.js
```

```Bash
# Grant executable permissions
chmod +x 9-add.js

# Execute the script with two numbers
./9-add.js 1 78
# Output: 79

# Validate code compliance with semistandard
semistandard ./9-add.js
```

```Bash
# Grant executable permissions
chmod +x 10-factorial.js

# Execute the script with a number
./10-factorial.js 5
# Output: 120

# Validate code compliance with semistandard
semistandard ./10-factorial.js
```

```Bash
# Example: Running the 11th task
chmod +x 11-second_biggest.js
./11-second_biggest.js 4 2 5 3 0 -34
# Output: 4

# Validate code compliance with semistandard
semistandard ./11-second_biggest.js
```

```Bash
# Example: Running the 12th task
chmod +x 12-object.js
./12-object.js
# Output:
# { type: 'object', value: 12 }
# { type: 'object', value: 89 }

# Validate code compliance with semistandard
semistandard ./12-object.js
```

```Bash
# Example: Running the 13th task via main file
chmod +x 13-main.js
./13-main.js
# Output: 8

# Validate code compliance with semistandard
semistandard ./13-add.js ./13-main.js
```
