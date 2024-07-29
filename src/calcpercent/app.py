import toga
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN, LEFT


class CalcPercent(toga.App):
    def startup(self):
        """Construct and show the Toga application."""
        main_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                padding=20,
                alignment=CENTER,
                background_color='#f0f0f0',
            )
        )

        header_label = toga.Label(
            "Calculadora de Desconto",
            style=Pack(
                padding_bottom=20,
                font_size=24,
                font_weight="bold",
                text_align=CENTER,
                color='#333333'
            )
        )

        price_cash_label = toga.Label(
            "Preço no caixa:",
            style=Pack(
                padding=(0, 5),
                font_size=14,
                font_weight="bold",
                text_align=LEFT,
                color='#333333'
            )
        )
        self.price_cash_input = toga.NumberInput(
            style=Pack(
                flex=1,
                padding=(10, 10),
                background_color='#ffffff',
                color='#333333',
            ),
            step=0.01
        )

        price_shelf_label = toga.Label(
            "Preço da gôndola:",
            style=Pack(
                padding=(0, 5),
                font_size=14,
                font_weight="bold",
                text_align=LEFT,
                color='#333333'
            )
        )
        self.price_shelf_input = toga.NumberInput(
            style=Pack(
                flex=1,
                padding=(10, 10),
                background_color='#ffffff',
                color='#333333',
            ),
            step=0.01,
        )

        cash_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        cash_box.add(price_cash_label)
        cash_box.add(self.price_cash_input)
        cash_box.add(price_shelf_label)
        cash_box.add(self.price_shelf_input)

        self.result_label = toga.Label(
            "",
            style=Pack(
                padding=10,
                color="green",
                font_size=18,
                font_weight="bold",
                text_align=CENTER,
            )
        )

        result_box = toga.Box(style=Pack(
            direction=COLUMN,
            padding=10,
            background_color='#ffffff',
            color='#cccccc',
            )
        )
        result_box.add(self.result_label)

        calculate_button = toga.Button(
            "Calcular",
            on_press=self.calculate_discount,
            style=Pack(
                padding=(12, 30),
                background_color="#007BFF",
                color="#FFFFFF",
                font_size=16,
                font_weight="bold",
                text_align=CENTER,
            )
        )
        button_box = toga.Box(style=Pack(
            direction=COLUMN,
            alignment=CENTER,
            padding=10
            )
        )
        button_box.add(calculate_button)

        main_box.add(header_label)
        main_box.add(result_box)
        main_box.add(cash_box)
        main_box.add(button_box)

        self.main_window = toga.MainWindow(
            title=self.formal_name
        )
        self.main_window.content = main_box
        self.main_window.show()

    def calculate_discount(self, widget):
        price_cash = self.price_cash_input.value
        price_shelf = self.price_shelf_input.value

        if not price_cash:
            self.result_label.text = "O campo 'Preço no caixa' obrigatório"
            return

        if not price_shelf:
            self.result_label.text = "O campo 'Preço da gôndola' obrigatório"
            return

        try:
            if price_cash <= 0 or price_shelf <= 0:
                self.result_label.text = " Zero error."
                return

            price_difference = price_cash - price_shelf
            discount_percent = (price_difference / price_cash) * 100

            self.result_label.text = f'O percentual de desconto é de {discount_percent:.2f}%'
        except ValueError:
            self.result_label.text = "Por favor, insira valores numéricos válidos."


def main():
    return CalcPercent()
