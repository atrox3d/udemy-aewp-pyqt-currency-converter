from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox
)


from currency_scraper import get_currency


def show_currency():
    input_text = text.text()
    from_currency = from_combo.currentText()
    to_currency = to_combo.currentText()
    rate = get_currency(from_currency, to_currency)
    value = round(float(input_text) * rate, 2)
    print(f'{value=}')
    message = f'{input_text} {from_currency} is {value} {to_currency}'
    output.setText(message)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()

currencies = ['USD', 'EUR', 'INR']
from_combo = QComboBox()
from_combo.addItems(currencies)
layout.addWidget(from_combo)

to_combo = QComboBox()
to_combo.addItems(currencies)
layout.addWidget(to_combo)

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currency)

output = QLabel('')
layout.addWidget(output)

window.setLayout(layout)
window.show()
app.exec()

