########################
# Calculator REPL       #
########################

from decimal import Decimal
import logging
from colorama import Fore, Style, init


from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError
from app.history import AutoSaveObserver, LoggingObserver
from app.operations import OperationFactory

init(autoreset=True)

def calculator_repl():
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """
    try:
        # Initialize the Calculator instance
        calc = Calculator()

        # Register observers for logging and auto-saving history
        calc.add_observer(LoggingObserver())
        calc.add_observer(AutoSaveObserver(calc))

        print("Calculator started. Type 'help' for commands.")

        while True:
            try:
                # Prompt the user for a command
                command = input("\nEnter command: ").lower().strip()

                if command == 'help':
                    # Display available commands
                    print(Fore.BLUE + "\nAvailable commands:")
                    print(Fore.BLUE +
                        "  add, subtract, multiply, divide, power, root, modulus, int_division, percent, abs_difference - Perform calculations"
                    )
                    print(Fore.MAGENTA + "  history - Show calculation history")
                    print(Fore.MAGENTA + "  clear - Clear calculation history")
                    print(Fore.MAGENTA + "  undo - Undo the last calculation")
                    print(Fore.MAGENTA + "  redo - Redo the last undone calculation")
                    print(Fore.MAGENTA + "  save - Save calculation history to file")
                    print(Fore.MAGENTA + "  load - Load calculation history from file")
                    print(Fore.MAGENTA + "  exit - Exit the calculator")
                    continue

                if command == 'exit':
                    # Attempt to save history before exiting
                    try:
                        calc.save_history()
                        print(Fore.GREEN + f"History saved successfully.")
                    except Exception as e: #pragma: no cover
                        print(Fore.RED + f"Warning: Could not save history: {e}")
                    print(Fore.BLUE + f"Goodbye!")
                    break

                if command == 'history':
                    # Display calculation history
                    history = calc.show_history() #pragma: no cover
                    if not history:
                        print("No calculations in history")
                    else: #pragma: no cover
                        print("\nCalculation History:")
                        for i, entry in enumerate(history, 1):
                            print(f"{i}. {entry}")
                    continue

                if command == 'clear':
                    # Clear calculation history
                    calc.clear_history() #pragma: no cover
                    print(Fore.GREEN + f"History cleared")
                    continue

                if command == 'undo':
                    # Undo the last calculation
                    if calc.undo(): #pragma: no cover
                        print(Fore.GREEN + f"Operation undone")
                    else: #pragma: no cover
                        print(Fore.RED + f"Nothing to undo")
                    continue #pragma: no cover

                if command == 'redo':
                    # Redo the last undone calculation
                    if calc.redo(): #pragma: no cover
                        print(Fore.GREEN + f"Operation redone")
                    else: #pragma: no cover
                        print(Fore.RED + f"Nothing to redo")
                    continue

                if command == 'save':
                    # Save calculation history to file
                    try: 
                        calc.save_history()
                        print(Fore.GREEN + f"History saved successfully.")
                    except Exception as e:
                        print(Fore.RED + f"Error saving history: {e}")
                    continue #pragma: no cover

                if command == 'load':
                    # Load calculation history from file
                    try:
                        calc.load_history()
                        print(Fore.GREEN + f"History loaded successfully.")
                    except Exception as e:
                        print(Fore.RED + f"Error loading history: {e}")
                    continue #pragma: no cover

                if command in [
                    'add', 'subtract', 'multiply', 'divide', 'power', 'root', 'modulus',
                    'int_division', 'percent', 'abs_difference'
                ]:
                    # Perform the specified arithmetic operation
                    try:
                        print("\nEnter numbers (or 'cancel' to abort):")
                        a = input("First number: ")
                        if a.lower() == 'cancel':
                            print(Fore.RED + f"Operation cancelled")
                            continue
                        b = input("Second number: ")
                        if b.lower() == 'cancel':
                            print(Fore.RED + f"Operation cancelled")
                            continue

                        # Create the appropriate operation instance using the Factory pattern
                        operation = OperationFactory.create_operation(command)
                        calc.set_operation(operation)

                        # Perform the calculation
                        result = calc.perform_operation(a, b)

                        # Normalize Decimal results without switching to scientific notation.
                        if isinstance(result, Decimal):
                            result = format(result.normalize(), "f")

                        print(Fore.YELLOW + f"\nResult: {result}")
                        
                    except (ValidationError, OperationError) as e: #pragma: no cover
                        # Handle known exceptions related to validation or operation errors
                        print(Fore.RED + f"Error: {e}")
                    except Exception as e:
                        # Handle any unexpected exceptions
                        print(Fore.RED + f"Unexpected error: {e}")
                    continue

                # Handle unknown commands
                print(Fore.RED + f"Unknown command: '{command}'. Type 'help' for available commands.")

            except KeyboardInterrupt:
                # Handle Ctrl+C interruption gracefully
                print(Fore.RED + "\nOperation cancelled")
                continue
            except EOFError:
                # Handle end-of-file (e.g., Ctrl+D) gracefully
                print(Fore.RED + "\nInput terminated. Exiting...")
                break
            except Exception as e:
                # Handle any other unexpected exceptions
                print(Fore.RED + f"Error: {e}")
                continue

    except Exception as e:
        # Handle fatal errors during initialization
        print(Fore.RED + f"Fatal error: {e}")
        logging.error(Fore.RED + f"Fatal error in calculator REPL: {e}")
        raise
