# Password Manager

A simple and secure password manager built using Python and Tkinter. This application helps you generate strong passwords and store them securely. The application uses `customtkinter` for an enhanced UI experience.

## Features

-   **Password Generation**: Generate strong, random passwords with a mix of letters, numbers, and symbols.
-   **Save Passwords**: Save website credentials (website, email/username, password) to a JSON file.
-   **Find Password**: Enter the website and click "Search" to find the stored password.
-   **Display All Stored Data**: Go to the "Vault" tab and click "Refresh Data" to display all stored credentials.
-   **Clipboard Copy**: Automatically copy generated passwords to the clipboard.
-   **Dark mode**: Uses dark mode with a custom color theme

## Code Overview

### Password Generation

The `generate_password` function creates a random password with a specified number of letters, symbols, and numbers. It then inserts the password into the password entry field and copies it to the clipboard using `pyperclip`.

### Save Password

The `save` function saves the entered website, email/username, and password to a JSON file (`data.json`). It checks for empty fields and confirms the details before saving.

### Find Password

The `find_password` function retrieves the stored password for a given website from the JSON file and displays it in a message box.

### Display Stored Data

The `display_stored_data` function reads all stored credentials from the JSON file and displays them in a text widget.


## Screenshots

![Password Manager](https://github.com/Vardararo/password-manager/assets/135714789/2f3cc2c0-c928-4f9f-b054-79ca36c5fe44)
![Vault](https://github.com/Vardararo/password-manager/assets/135714789/60c09811-83e2-4926-af84-d6538b1d81cd)


## File Structure

-   `password_manager.py`: The main application script.
-   `data.json`: The JSON file where credentials are stored.
-   `logo.png`: The logo image displayed in the application.

## Dependencies

-   `tkinter`: Standard Python interface to the Tk GUI toolkit.
-   `pyperclip`: A cross-platform Python module for clipboard operations.
-   `json`: Built-in Python module for JSON file operations.
-   `customtkinter`: Enhanced UI elements
-   `tkinterDnD`: Drag and drop support
-   `PIL (Pillow)`: For image handling

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

-   The Tkinter library for providing the GUI framework.
-   The pyperclip library for clipboard functionalities.
