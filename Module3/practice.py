# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
pswd = 198964


guess = int(input('Input a number to guess\nHint: between 4 and 8 digits digits\n'))
if guess == pswd:
    print('Nice one!\nYou hit the point!')


while guess != pswd:
    if guess == pswd:
        print('Nice one!\nYou hit the point!')
        break
    elif guess > 10000000 or guess < 9999:
        print('Your input is a tad too large, please try again')
        guess = int(input('Input a number to guess\nHint: between 4 and 8 digits digits\n'))
    elif guess > pswd:
        print('Your input is a tad too large, please try again')
        guess = int(input('Input a number to guess\nHint: between 4 and 8 digits digits\n'))
        
    elif guess < pswd:
        print('Your input is a tad too small, please try again')
        guess = int(input('Input a number to guess\nHint: between 4 and 8 digits digits\n'))

        

# 1.告訴使用者需要輸入的數字範圍 input()


# 2.使用者猜對要回傳「恭喜中獎」，並結束迴圈的執行


# 3.超出範圍要顯示「超出範圍請重新輸入」


# 4.數字太大 要提示「請輸入更小的數字」


# 5.數字太小 要提示「請輸入更大的數字」


