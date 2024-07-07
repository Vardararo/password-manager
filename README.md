# Password Manager

A simple and secure password manager built using Python and Tkinter. This application helps you generate strong passwords and store them securely.

## Features

-   **Password Generation**: Generate strong, random passwords with a mix of letters, numbers, and symbols.
-   **Save Passwords**: Save website credentials (website, email/username, password) to a JSON file.
-   **Find Password**: Enter the website and click "Search" to find the stored password.
-   **Display All Stored Data**: Go to the "Vault" tab and click "Refresh Data" to display all stored credentials.
-   **Clipboard Copy**: Automatically copy generated passwords to the clipboard.

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

    ![Image Alt text](images\Password Manager.png "Password App")
    ![Image Alt text](images\Password Manager.png "Saved Data")


## File Structure

-   `password_manager.py`: The main application script.
-   `data.json`: The JSON file where credentials are stored.
-   `logo.png`: The logo image displayed in the application.

## Dependencies

-   `tkinter`: Standard Python interface to the Tk GUI toolkit.
-   `pyperclip`: A cross-platform Python module for clipboard operations.
-   `json`: Built-in Python module for JSON file operations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

-   The Tkinter library for providing the GUI framework.
-   The pyperclip library for clipboard functionalities.
