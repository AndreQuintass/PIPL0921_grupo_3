import random
class Post:
    def __init__(self, title: str, body: str, userId: int):
        self.title = title
        self.body = body
        self.userId = userId

titles = [
    "Branca de neve",
    "Joao pe de feijao",
    "Anzel e greta",
    "Os 3 porquinhos",
    "Cinderela",
    "Bela adormecida"
]

bodys = [
    "sahkjdsahkjdhsa kjdh sakjdhsakjd hsajk",
    "dsa hdjklsahdkjashdjksa asdkjsahdas",
    "kashdjkashjkdasjk dsahdasj dsa",
    "dajhdskdhasjkdhs dsah djksaasdasdasa",
    "sadasdasdajhdkashkjjasjkd adsad hsa",
    "kshd adksahdjkasdjkash dsahkiuashdkj as"
]

postList = [Post(random.choice(titles), random.choice(bodys), int(idd/3)+1) for idd in range(20)]
