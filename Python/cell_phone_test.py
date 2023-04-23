import cellphone as cp

def main():
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail= float(input('Enter the retail price: '))

    # creating an instance of the Cellphone class
    phone = cp.CellPhone(man, mod, retail)

    # displaying the data that was entered 
    print('Here is the data you entered and the information we have now')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model Number: {phone.get_model()}')
    print(f'Retail Price: {phone.get_retail_price():,.2f}')

# calling the main function
if __name__ == '__main__':
    main()


