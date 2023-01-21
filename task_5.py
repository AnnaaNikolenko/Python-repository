import random


steps = {}
test_case = {}


class TestCase:
    def __init__(self, id, name, result):
        self.id = id
        self.name = name
        self.result = result

    def set_step(self, step_number, step_text):
        steps[step_number] = step_text

    def delete_step(self, step_number):
        del steps[step_number]

    def get_steps(self):
        return steps

    def set_result(self):
        return self.result

    def get_test_case(self):
        test_case['id'] = self.id
        test_case['Название'] = self.name
        test_case['Шаги'] = self.get_steps()
        test_case['Ожидаемый результат'] = self.set_result()
        print(test_case)


testCase = TestCase(random.randint(100, 999), 'Добавление товара в корзину', 'Товар окажется в корзине')
testCase.set_step(1, 'Перейти на сайт')
testCase.set_step(2, 'Перейти в раздел Товары')
testCase.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
testCase.set_step(4, 'А этот шаг будет удален')
testCase.delete_step(4)
testCase.get_steps()
testCase.set_result()
testCase.get_test_case()