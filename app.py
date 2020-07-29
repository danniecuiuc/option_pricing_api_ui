import call

bar_value = call.barrier_bs(30, 12, 0.1, 0.05, 0.02, 0.1, 1)

def main():
    print(bar_value)
    print("Hello Main")

if __name__ == "__main__":
    main()
