def get_response(user_input: str):
    lower_case = user_input.lower()

    if lower_case == '':
        return "well, you're awfully silet..."
    elif 'hello' in lower_case:
        return 'Hello there.'