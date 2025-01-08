import allure
from Pages.progress_bar_page import ProgressBar
from Pages.load_delays_page import LoadDelays
from Pages.text_input_page import TextInput
from Pages.dynamic_table_page import DynamicTable
from Pages.non_breaking_space_page import NonBreakingSpace


@allure.suite('Тесты')
class Tests:
    @allure.title('Проверить работоспособность заполняемой шкалы')
    def test_progress_bar(self, driver):
        progress = ProgressBar(driver)

        progress.open_target_page()
        progress.click_start_btn()
        progress.wait_till_75()
        progress.is_result_less_5()
        progress.is_duration_less_17k()

    @allure.title('Проверить работу теста с учётом задержек')
    def test_delays(self, driver):
        delay = LoadDelays(driver)

        delay.open_target_page()
        delay.click_delay_page()
        delay.check_delayed_btn()

    @allure.title('Проверить автоматический ввод текста')
    def test_input_text(self, driver):
        input_page = TextInput(driver)

        input_page.open_target_page()
        old_name = input_page.get_btn_name()
        input_page.insert_new_value('New button name')
        input_page.click_named_btn()
        new_name = input_page.get_btn_name()
        with allure.step('Проверить, что название кнопки изменилось'):
            assert old_name != new_name, (
                '[FAILED] Button name stays the same'
            )

    @allure.title('Проверить работу с динамически генерируемыми таблицами')
    def test_dynamic_tables(self, driver):
        tables = DynamicTable(driver)

        tables.open_target_page()
        tables.check_cpu_loading()

    @allure.title('Проверить поиск с неразрывными пробелами')
    def test_unbreakable_spaces(self, driver):
        spaces = NonBreakingSpace(driver)

        spaces.open_target_page()
        spaces.check_nbsp_btn()