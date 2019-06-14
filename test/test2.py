if __name__ == '__main__':
    card_list = [1, 2, 3, 4, 5, 65, 6, 7, 7, 8, 98, 9, 9, 0, 0, 0, 23, 3]

    # 初始化页面
    step = 2
    pages = [card_list[i:i + step] for i in range(0, len(card_list), step)]

    print(pages)
