from random import randint

while True:

    # 1. 유저의 입력을 받습니다.
    user_choice = input(f"""
{'=' * 51}

가위바위보 게임에 오신 것을 환영합니다.
해당하는 숫자를 입력하시고 [enter] 를 눌러주세요.
게임을 종료하기 위해서는 [ctrl + c] 를 눌러주세요.
1. 가위
2. 바위
3. 보

{'=' * 51}

당신의 선택(숫자로 입력해주세요): """)

    # 1-1. 유저가 잘못된 값을 입력하면 다시 입력을 받습니다.
    while user_choice not in ['1', '2', '3']:
        user_choice = input('오류! 올바른 값을 입력해주세요. 당신의 선택(숫자로 입력해주세요): ')

    if user_choice == '1':
        user_choice_name = '가위'
    elif user_choice == '2':
        user_choice_name = '바위'
    else:
        user_choice_name = '보'
    print(f'\n{"=" * 51}\n')
    print(f'{user_choice_name}를 내셨군요!')

    # 2. 컴퓨터의 값을 랜덤으로 받습니다.
    computer_choice = str(randint(1, 3))

    if computer_choice == '1':
        computer_choice_name = '가위'
    elif computer_choice == '2':
        computer_choice_name = '바위'
    else:
        computer_choice_name = '보'

    print(f'컴퓨터는 {computer_choice_name}를 냈습니다.')
    print(f'\n{"=" * 51}\n')

    # 3. 유저와 컴퓨터의 값을 비교합니다.
    if (user_choice == '1' and computer_choice == '3') or (user_choice == '2' and computer_choice == '1') or (user_choice == '1' and computer_choice == '2'):
        print('당신이 이겼습니다!', end=" ")
    elif (computer_choice == '1' and user_choice == '3') or (computer_choice == '2' and user_choice == '1') or (computer_choice == '1' and user_choice == '2'):
        print('컴퓨터가 이겼습니다!', end=" ")
    else:
        print('비겼습니다!', end=" ")

    game_over = input('한 판 더 할까요? (Y / N) : ')
    while game_over.upper() not in ['Y', 'N']:
        game_over = input('잘못된 값을 입력했습니다. 한 판 더 할까요? (Y / N) : ')
    if game_over.upper() == 'N':
        print('게임을 종료합니다……')
        break