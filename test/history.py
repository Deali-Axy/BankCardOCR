import os

if __name__ == '__main__':
    print(os.path.abspath(os.curdir))
    cur_path = os.path.abspath(os.curdir)
    temp_path = os.path.abspath(os.path.join(cur_path, '..', 'images', 'temp'))
    for raw_name in os.listdir(temp_path):
        print(raw_name)
        file_name = raw_name[0:raw_name.index('.')]
        card_file = os.path.join(temp_path, raw_name)
        card_id = file_name.split('@')[0]
        card_num = file_name.split('@')[1]
        card_create_time=os.path.getctime(card_file)
        print(card_id)
        print(card_num)
