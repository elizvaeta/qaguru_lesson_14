from selene import browser, by, have


class CareerPage:
    def open(self):
        browser.open('/career')
        return self

    @property
    def titles(self):
        return browser.all('[data-test="htmlTag title"]')

    def open_vacancies(self):
        return browser.element(by.text('Работа в ИТ')).click()

    def open_blog(self):
        return browser.element('[data-item-name="Смотреть все статьи"]').click()

    def should_have_info_blocks(self):
        self.titles[0].should(have.text('Создаем то, что любят миллионы'))
        self.titles[1].should(have.text('Направления'))
        self.titles[2].should(have.text('Наши преимущества'))
        self.titles[3].should(have.text('Амбициозные задачи'))
        self.titles[4].should(have.text('Работа по всей России и не только'))
        self.titles[5].should(have.text('Карьерный рост'))
        self.titles[6].should(have.text('Развиваем ИТ-сообщество'))
        self.titles[7].should(have.text('Образование и преподавание'))
        self.titles[8].should(have.text('Блог о работе'))
        self.titles[9].should(have.text('Современный рабочий процесс'))

    def should_go_to_vacancies(self):
        self.open_vacancies()

        browser.should(have.url_containing("/it/about/"))

    def should_go_to_blog(self):
        self.open_blog()

        browser.switch_to_tab(1)

        browser.should(have.url_containing("/blog"))


career_page = CareerPage()
