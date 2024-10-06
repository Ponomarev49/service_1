import json

from bot import Product, Bot


def load_products_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        product_list = data.get('products', [])
        for i in range(len(product_list)):
            bot.products[i+1] = Product(name = product_list[i]["name"], producer = product_list[i]["producer"], id = product_list[i]["id"])


def load_magazines_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        bot.addresses = data


def send_messages_to_magazines():
    for id in bot.products:
        print(f"Сообщите о наличии товара {bot.products[id].name} производителя {bot.products[id].producer} по адресу {bot.addresses[bot.products[id].id]}")


def get_messages_from_magazines(file_path):
    # в дальнейшем сообщения будут отправляться в админку
    with open(file_path, 'r') as file:
        data = json.load(file)
        answers_list = data.get('answers', [])

        for answer in answers_list:
            if answer['answer']=='True':
                print(f'Товар {bot.products[answer["id"]].name} найден')
            else:
                print(f'Товар {bot.products[answer["id"]].name} не найден')
            del bot.products[answer["id"]]


bot = Bot()
load_products_from_json('products.json')
load_magazines_from_json('magazines.json')
send_messages_to_magazines()
get_messages_from_magazines('answers.json')