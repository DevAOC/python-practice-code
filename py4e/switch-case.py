# This function doesn't do anything
def switchCase(opened: str) -> bool:  # This function is an example of type definition
    match opened:  # Match is equivalent to the switch in JS
        case 'open':
            return True
        case 'closed':
            return False
        case _:
            return False
