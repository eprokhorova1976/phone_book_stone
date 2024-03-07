import view
import model
import text

def find_contacts(message):
    search_word = view.input_data (message)
    result = model.find_contacts (search_word)
    view.show_contacts (result, text.find_contact_no_result(search_word))
    return True if result else False

def start_app():
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1