


def perform_operation(num1, num2, operation):
    match operation :
        case "add" :
            return (num1 + num2)
        case "subtract" :
            return (num1 - num2)
        case "multiply" :
            return (num1 * num2)
        case "divide" :
            if num2 == 0:
                return (f"Division by zero is not allowed !")
            elif num2 == 1:
                return (num1)
            else :
                return (num1 / num2)
        case _ :
            return(f"Error: Operation selected is not exist")