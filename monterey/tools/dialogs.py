from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import input_dialog, yes_no_dialog, button_dialog, radiolist_dialog, checkboxlist_dialog

#==============================================================================

class Dialog:
    def __init__(self):
        """
        A lighweight for handling user inputs in the terminal.

        Attributes:
            ask: A method to prompt the user for input in the terminal.
            confirm: A method to prompt the user for a yes/no confirmation.
            asklist: A method to prompt the user to select from a list of choices.
            radio: A method to prompt the user to select from a list of choices using a radio list.
            checkbox: A method to prompt the user to select from a list of choices using a checkbox list.
            button: A method to prompt the user to select from a list of choices using buttons.
        """
        pass

    @staticmethod
    def ask(message: str = None, title: str = None):
        """
        Prompt for user input in the terminal.

        Example:
            ```python
            from yosemite.tools.dialogs import Dialog

            Dialog.ask("What is your name?")
            ```

        Args:
           message (str): Message to be displayed in the terminal.
           title (str): Title of the dialog box.
        """
        if not title:
            title = "Input"
        if message and title:
            value = input_dialog(title=title, text=message).run()
            return value
        else:
            print("'title' and 'message' are required for prompt_input()")

    @staticmethod
    def confirm(message: str = None):
        """
        Prompt for user input in the terminal.

        Example:
            ```python
            Dialog.confirm("Are you sure?")
            ```

        Args:
           message (str): Message to be displayed in the terminal.    
        """
        if not message:
            message = ""
        if message:
            value = yes_no_dialog(title="Confirmation", text=message).run()
            return value
        else:
            print("'message' is required for prompt_confirmation()")

    @staticmethod
    def asklist(choices: list = None, message: str = None):
        """
        Prompt for user input in the terminal.

        Example:
            ```python
            list = ["Red", "Green", "Blue"]
            Dialog.asklist("Choose a color:", list)
            ```

        Args:
           choices (list): A list of options for the user to choose from.
           message (str): Message to be displayed in the terminal.
        """
        if not message:
            message = ""
        if message and choices:
            value = input_dialog(title=message, text=message, completer=WordCompleter(words=choices)).run()
            return value
        else:
            print("'message' and 'choices' are required for asklist()")

    @staticmethod
    def radio(choices: str = None, message: str = None):
        """
        Display a dialog with choices offered as a radio list.

        Example:
            ```python
            list = ["Red", "Green", "Blue"]
            Dialog.radio("Choose a color:", list)
            ```

        Args:
           message (str): Message to be displayed in the terminal.
           choices (list): A list of tuples for the radio options.
        """
        if not message:
            message = ""
        if message and choices:
            value = radiolist_dialog(title="RadioList dialog", text=message, values=choices).run()
            return value
        else:
            print("'message' and 'choices' are required for radiolist()")

    @staticmethod
    def checkbox(choices: str = None, message: str = None):
        """
        Display a dialog with choices offered as a checkbox list.

        Example:
            ```python
            list = ["Red", "Green", "Blue"]
            Dialog.checkbox("Choose a color:", list)
            ```

        Args:
           message (str): Message to be displayed in the terminal.
           choices (list): A list of tuples for the checkbox options.
        """
        if not message:
            message = ""
        if message and choices:
            value = checkboxlist_dialog(title="CheckboxList dialog", text=message, values=choices).run()
            return value
        else:
            print("'message' and 'choices' are required for checkboxlist()")

    @staticmethod
    def button(choices: str = None, message: str = None):
        """
        Display a dialog with choices offered as buttons.

        Example:
            ```python
            list = ["Red", "Green", "Blue"]
            Dialog.button("Choose a color:", list)
            ```

        Args:
           message (str): Message to be displayed in the terminal.
           choices (list): A list of tuples for the button options.
        """
        if not message:
            message = ""
        if message and choices:
            value = button_dialog(title="Button dialog", text=message, buttons=choices).run()
            return value
        else:
            print("'message' and 'choices' are required for button()")

#==============================================================================

if __name__ == "__main__":
    Dialog.ask("What is your name?")
    Dialog.confirm("Are you sure?")
    Dialog.asklist("Choose a color:", list)
    Dialog.radio("Choose a color:", list)
    Dialog.checkbox("Choose a color:", list)
    Dialog.button("Choose a color:", list)