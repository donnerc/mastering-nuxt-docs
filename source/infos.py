from datetime import datetime

today = datetime.now()

month_names = {
    "en": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
    "fr": [
        "Janvier",
        "Février",
        "Mars",
        "Avril",
        "Mai",
        "Juin",
        "Juillet",
        "Août",
        "Septembre",
        "Octobre",
        "Novembre",
        "Décembre",
    ],
}


def get_current_month_name(locale='en'):
    return month_names[locale][today.month - 1]


class DocumentInfos:

    language = "en"
    title = "Mastering Nuxt"
    first_name = "Cédric"
    last_name = "Donner"
    author = f"{first_name} {last_name}"
    year = today.year
    month = get_current_month_name()
    day = today.day
    seminary_title = "Personal notes"
    tutor = ""
    release = "0.1"
    repository_url = "https://github.com/donnerc/mastering-nuxt-notes"

    @classmethod
    def date(cls):
        return f"{cls.day} {cls.month} {cls.year}"


infos = DocumentInfos()

print(f"Date: {infos.day, infos.year, infos.month}")
