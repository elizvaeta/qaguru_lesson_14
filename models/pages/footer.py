from selene import browser, be, have, command


class Footer:
    @property
    def footer(self):
        return browser.element('[data-module-type="advertFooter"]')

    @property
    def social_medias(self):
        self.footer.perform(command.js.scroll_into_view)

        return browser.element('[data-qa-type="uikit/footer.socMedia"]')

    def should_have_social_medias(self):
        self.footer.should(be.visible)

        self.social_medias.element('[title=VK]').should(have.attribute('href', 'https://vk.com/tinkoffbank'))
        self.social_medias.element('[title=Одноклассники]').should(have.attribute('href', 'http://ok.ru/tinkoffbank'))
        self.social_medias.element('[title=Twitter]').should(have.attribute('href', 'https://twitter.com/tinkoff_bank'))
        self.social_medias.element('[title=Telegram]').should(have.attribute('href', 'https://t.me/tinkoffbank'))


footer = Footer()
