# Import simple GUI 
import PySimpleGUI as sg

# Create a Hangman class
class Hangman:
    def __init__(self) -> None:
        # Create a PySimpleGUI window with the title "Hangman"
        self._window = sg.Window(
            title="Hangman", layout=[[]], finalize=True, margins=(100, 100)
        )

    def read_event(self):
        # Read events from the PySimpleGUI window
        return self._window.read()

    def close(self):
        # Close the PySimpleGUI window
        self._window.close()


if __name__ == "__main__":
    # Create an instance of the Hangman class
    game = Hangman()
    
    # Event loop
    while True:
        # Read the event and values from the PySimpleGUI window
        event, values = game.read_event()
        
        # Check if the event is the window being closed
        if event in {sg.WIN_CLOSED}:
            break
    
    # Close the PySimpleGUI window
    game.close()
