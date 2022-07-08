import pygame
import sys
import random

charpool = [
    "ァ",
    "ア",
    "ィ",
    "イ",
    "ゥ",
    "ウ",
    "ェ",
    "エ",
    "ォ",
    "オ",
    "カ",
    "ガ",
    "キ",
    "ギ",
    "ク",
    "グ",
    "ケ",
    "ゲ",
    "コ",
    "ゴ",
    "サ",
    "ザ",
    "シ",
    "ジ",
    "ス",
    "ズ",
    "セ",
    "ゼ",
    "ソ",
    "ゾ",
    "タ",
    "ダ",
    "チ",
    "ヂ",
    "ッ",
    "ツ",
    "ヅ",
    "テ",
    "デ",
    "ト",
    "ド",
    "ナ",
    "ニ",
    "ヌ",
    "ネ",
    "ノ",
    "ハ",
    "バ",
    "パ",
    "ヒ",
    "ビ",
    "ピ",
    "フ",
    "ブ",
    "プ",
    "ヘ",
    "ベ",
    "ペ",
    "ホ",
    "ボ",
    "ポ",
    "マ",
    "ミ",
    "ム",
    "メ",
    "モ",
    "ャ",
    "ヤ",
    "ュ",
    "ユ",
    "ョ",
    "ヨ",
    "ラ",
    "リ",
    "ル",
    "レ",
    "ロ",
    "ヮ",
    "ワ",
    "ヰ",
    "ヱ",
    "ヲ",
    "ン",
    "ヴ",
    "ヵ",
    "ヶ",
    "ヷ",
    "ヸ",
    "ヹ",
    "ヺ",
    "ぁ",
    "あ",
    "ぃ",
    "い",
    "ぅ",
    "う",
    "ぇ",
    "え",
    "ぉ",
    "お",
    "か",
    "が",
    "き",
    "ぎ",
    "く",
    "ぐ",
    "け",
    "げ",
    "こ",
    "ご",
    "さ",
    "ざ",
    "し",
    "じ",
    "す",
    "ず",
    "せ",
    "ぜ",
    "そ",
    "ぞ",
    "た",
    "だ",
    "ち",
    "ぢ",
    "っ",
    "つ",
    "づ",
    "て",
    "で",
    "と",
    "ど",
    "な",
    "に",
    "ぬ",
    "ね",
    "の",
    "は",
    "ば",
    "ぱ",
    "ひ",
    "び",
    "ぴ",
    "ふ",
    "ぶ",
    "ぷ",
    "へ",
    "べ",
    "ぺ",
    "ほ",
    "ぼ",
    "ぽ",
    "ま",
    "み",
    "む",
    "め",
    "も",
    "ゃ",
    "や",
    "ゅ",
    "ゆ",
    "ょ",
    "よ",
    "ら",
    "り",
    "る",
    "れ",
    "ろ",
    "ゎ",
    "わ",
    "ゐ",
    "ゑ",
    "を",
    "ん",
    "ゔ",
]

WIDTH = 1920
HEIGHT = 1080
CHAR_SIZE = 8


class Symbol:
    def __init__(self, x, y, color):
        self.char = self.generate_random_char()
        self.x = x
        self.y = y
        self.color = color

    def generate_random_char(self):
        return charpool[random.randint(0, len(charpool) - 1)]


class Stream:
    def __init__(self, x):
        self.x = x
        self.pool = []
        self.speed = random.randint(10, 15)

    def populate_pool(self):
        self.pool.clear()
        starting_point = random.randint(-800, -100)
        for i in range(random.randint(10, 100)):
            self.pool.append(
                Symbol(
                    self.x,
                    starting_point - (CHAR_SIZE * i),
                    (243, 243, 243) if i == 0 else (0, 197, 0),
                )
            )

    def move(self):
        for s in self.pool:
            s.y += self.speed
            s.char = s.generate_random_char()

        if self.pool[len(self.pool) - 1].y + CHAR_SIZE >= HEIGHT:
            self.populate_pool()


def exit_game():
    pygame.quit()
    sys.exit()


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_game()


def main():
    pygame.init()
    pygame.display.set_caption("matrix rain")

    # screen size
    # screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    font = pygame.font.Font("fonts/NotoSansJP-Regular.otf", CHAR_SIZE)
    clock = pygame.time.Clock()
    stream_arr = [Stream(CHAR_SIZE * i) for i in range(WIDTH // CHAR_SIZE)]
    for stream in stream_arr:
        stream.populate_pool()

    while True:
        screen.fill((0, 0, 0))
        for stream in stream_arr:
            for symbol in stream.pool:
                font_surf = font.render(
                    symbol.char,
                    True,
                    pygame.Color(symbol.color[0], symbol.color[1], symbol.color[2]),
                )
                screen.blit(font_surf, (symbol.x, symbol.y))
            stream.move()

        check_for_exit()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
