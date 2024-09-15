import streamlit as st
from PIL import Image

# Настройка страниц
st.set_page_config(page_title="Поздравляю, любимая!", page_icon="🎉")

# Определение структуры страниц
def main():
    st.sidebar.title("Оглавление (хы-хы, как формально 😂)")
    page = st.sidebar.radio("Тыкай тыкай, там приколы!", ["Поздравление!", "Моя зайка в статике", "Моя зайка в динамике", "Немного песенок в студию", "Подарочек 🎁🎉"])

    if page == "Поздравление!":
        show_greeting()
    elif page == "Моя зайка в статике":
        create_photo_collage()
    elif page == "Моя зайка в динамике":
        upload_video_montage()
    elif page == "Немного песенок в студию":
        upload_audio()
    elif page == "Подарочек 🎁🎉":
        gift()

# Страница с поздравлением
def show_greeting():
    st.title("С Днем Рождения, мое солнышко! 🎉❤️️")
    st.write("Листай ниже! ↓")
    image = Image.open("media/i_duck.jpg")  # Локальный файл изображения
    st.image(image, caption="Напоминание как выгляжу (потерялся в Сарове...)", use_column_width=True)
    st.subheader("Поздравляю тебя с этим замечательным, невероятным, радостным днем!")
    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.write("Пусть в этот день тебя встречают улыбки и забота близких людей, пусть настроение будет на высоте и пусть никакие вонючие пары этому не помешают!")
    
    with col2:
        st.write("Оставайся такой же солнечной, доброй, искренней, нежной, красивой, заботливой, умной, веселой, милой и моей самой самой любимой на всем свете!")
    
    with col3:
        st.write("Я тебя очень сильно люблю, безумно счастлив и рад, что у меня есть такой замечательный человечек, как Ты!")

    col1, col2, col3 = st.columns((1,1,1))

    with col2:
        st.write("От твоего Данечки ❤️️")
    
    image = Image.open("media/happy_birthday_image.jpg")  # Локальный файл изображения
    st.image(image, caption="С Днем Рождения!", use_column_width=True)

# Страница для загрузки видео
def upload_video_montage():
    st.title("Посвящаю моему солнышку в ее День Рождения! 🎥")
    st.write("Видео получилось слишком большим, поэтому на страницу грузится не хочет :(")
    st.markdown("Поэтому вот [ссылка](https://drive.google.com/file/d/1bqZsC3aWpOOIPhHrhX4teDe0zESQr73m/view?usp=sharing) на гугл диск с видео!")
    st.write("Врубай на полную катушку!.. Ну, в смысле, на полный экран. Так лучше видно.")

# Страница для создания коллажа фото
def create_photo_collage():
    st.title("Твои фото слили (очень красивые) 📷")
    st.write("..или немного коллажей!")
    # Загрузка и отображение нескольких фото (локальные файлы изображений)
    images = ["media/collage1.png", "media/collage2.png"]  # Список локальных файлов
    cols = st.columns(len(images))
    
    for col, img_path in zip(cols, images):
        img = Image.open(img_path)
        col.image(img, use_column_width=True)

# Страница для загрузки аудио
def upload_audio():
    st.title("Готовлю тебя к подарку 😂😂😂🎵")
    st.write("Добавил немного песен, которые напоминают мне о тебе! Одну из них ты уже слышала ;)")
    st.write("Песни можно скачать к себе, а можно перейти на страничку в Яндекс.Музыке")
    st.divider()
    r"""##### Я - ненормальный, когда вижу тебя!"""
    st.write("Markul - Ненормальный")
    audio_file = open("media/Markul - 1.mp3", 'rb')  # Локальный файл аудио
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("[Ссылка на песню в Я.Музыке 😉](https://music.yandex.ru/album/28341204/track/119554464)")
    st.divider()
    r"""##### Хочу быть твоим последним пассажиром 😉"""
    st.write("Артем Кинг - Последний пассажир")
    audio_file = open("media/AK - 1.mp3", 'rb')  # Локальный файл аудио
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("[Ссылка на песню в Я.Музыке 😉](https://music.yandex.ru/album/10376936/track/64551561)")
    st.divider()
    r"""##### Ты наполняешь мою жизнь красками и смыслом!"""
    st.write("TumaniYO, Miyagi - Наполняй")
    audio_file = open("media/TumaniYO, Miyagi - Наполняй.mp3", 'rb')  # Локальный файл аудио
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("[Ссылка на песню в Я.Музыке 😉](https://music.yandex.ru/album/31348491/track/126278715)")
    st.divider()
    r"""##### Без тебя даже сахар - несладкий!"""
    st.write("КлоуКома - Несладкий сахар")
    audio_file = open("media/KK - 1.mp3", 'rb')  # Локальный файл аудио
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("[Ссылка на песню в Я.Музыке 😉](https://music.yandex.ru/album/8770958/track/58021693)")
    st.divider()
    r"""##### В ад - только перед тобой, в рай - только после тебя!"""
    st.write("pyrokinesis, BOOKER - в ад только перед тобой в рай только после тебя")
    audio_file = open("media/pyrokinesis, BOOKER - 1.mp3", 'rb')  # Локальный файл аудио
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("[Ссылка на песню в Я.Музыке 😉](https://music.yandex.ru/album/24135206/track/109050096)")
    st.divider()
    r"""##### Для других - у меня нет сердца!"""
    st.write("PHARAOH - Нет Сердца")
    audio_file = open("media/PHARAOH - 1.mp3", 'rb')  # Локальный файл аудио
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("[Ссылка на песню в Я.Музыке 😉](https://music.yandex.ru/album/14427354/track/79405420)")
    st.divider()
    r"""##### В этом мире скучно без тебя - задержись в нем на подольше, пожалуйста """
    st.write("Markul - Без тебя")
    audio_file = open("media/Markul - 2.mp3", 'rb')  # Локальный файл аудио
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.markdown("[Ссылка на песню в Я.Музыке 😉](https://music.yandex.ru/album/5905756/track/44121106)")
    st.divider()

# Страница для подарка!
def gift():
    st.title("Поздравляю тебя, любимая! Очень надеюсь, что тебе понравится 🎁🎉😊💝")
    st.markdown("[Нажми здесь, чтобы посмотреть сюрприз 😉✨🎁](https://ya.cc/t/jW0GlaDY5PWhdA)")
    image = Image.open("media/1.jpg")  # Локальный файл изображения
    st.image(image, caption="Мы с тобой только один бокальчик!", use_column_width=True)

# Запуск приложения
if __name__ == "__main__":
    main()