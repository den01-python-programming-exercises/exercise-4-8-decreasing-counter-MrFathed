from decreasing_counter import DecreasingCounter

def main():
    #write your code below this line
    counter = DecreasingCounter(100)

    counter.print_value()

    counter.reset()
    counter.print_value()

    counter.decrement()
    counter.print_value()

if __name__ == '__main__':
    main()
