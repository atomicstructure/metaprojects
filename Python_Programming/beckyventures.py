while True:

    print('Welcome to Becky ventures')
    schoolName = str(input('Please Enter School Name: '))
    print('Hello {}'.format(schoolName))

    className = str(input('Please enter class: '))
    print('Thank You {}, you are registering for {}'.format(schoolName,className))

    totalPagesPrinted = int(input('Please enter total number of pages printed: '))
    print('Total number of pages printed is {}'.format(totalPagesPrinted))
    totalPhotocopies = int(input('Please enter total number of Photocopies made: '))
    print('Total number of Photocopies made is: {}'.format(totalPhotocopies))
    printedPagesAmount = totalPagesPrinted * 20
    totalPhotcopyAmount = totalPhotocopies * 4
    totalPayable = printedPagesAmount + totalPhotocopies
    print("Amount Payable is: ₦{}".format(totalPayable))
    toPay = int(input('How much do you want to pay?: ₦ '))
    balance = totalPayable - toPay
    print('Your Balance is:  ₦{}'.format(balance) )
    print('Thank you, Please call again {}'.format(schoolName))

    choice = input("Do you want to register other classes?: Y/N?: ")
    match choice:
        case 'N':
            break
        case 'Y':
            continue