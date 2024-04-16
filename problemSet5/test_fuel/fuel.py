import sys
def main():
    user_input = input("Fraction: ")
    try:
        percent = convert(user_input)
    except ZeroDivisionError:
        sys.exit("Error: Zero Division error")
        
    except ValueError:
        sys.exit("Error: ValueError")
    
    output = gauge(percent)
    print(output)


def convert(fraction: str) -> int:
    """expects a string and return an int"""   
    while True:
        try:
            ls = fraction.split("/")
            assert len(ls) == 2
            numerator = int(ls[0])
            denominator = int(ls[1])
            percent_value = numerator / denominator
            if percent_value  > 1:
                raise(ValueError)
            percent_value = percent_value * 100
        except ZeroDivisionError:
            raise(ZeroDivisionError)
        except:
            raise(ValueError)
        return int(percent_value)
 
        
def gauge(percentage: int) -> str:
        """expects int and return str"""
        if isinstance(percentage, int):
            if percentage <= 1:
                return "E"
            elif percentage >= 99 and percentage <= 100:
                return "F"
            else:
                return f"{percentage}%"
        else:
            raise(TypeError)


if __name__ == "__main__":
    main()